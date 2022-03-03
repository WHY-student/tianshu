# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import time

import win32gui
import win32con
import uiautomation as auto
from pywinauto import Application

from click_pos import *
from id_automation import *

auto.uiautomation.SetGlobalSearchTimeout(3)
hwnd_title = {}
play_title = {}
play_all_window = []
npc_dict = {}


class play_window:
    handle = 0
    name = ''
    windowsControl = None
    windows_dlg = None
    # 当前状态
    is_play = False
    play_message = '未上线'
    play_name = '未上线'
    play_id = 0
    play_xian = 1

    def get_xian(self, handle_name):
        if handle_name[-2:] == "一线":
            self.play_xian = 1
        elif handle_name[-2:] == "二线":
            self.play_xian = 2
        elif handle_name[-2:] == "三线":
            self.play_xian = 3
        elif handle_name[-2:] == "四线":
            self.play_xian = 4

    def __init__(self, handle, handle_name):
        self.handle = handle
        self.windowsControl = auto.WindowControl(searchDepth=1, Name=handle_name)
        app = Application(backend='uia').connect(handle=handle)
        self.windows_dlg = app.top_window()
        self.name = self.windowsControl.Name
        self.get_xian(self.name)
        self.play_name = self.name.split('--幻影脱机')[0]

    def show(self):
        self.windows_dlg.restore()
        self.windowsControl.SetTopmost(True)

    def show_quit(self):
        self.windows_dlg.restore()

    def hide(self):
        self.windowsControl.SetTopmost(False)

    def hide_quit(self):
        self.windowsControl.SetTopmost(False)
        self.windows_dlg.minimize()

    # 点击事件，pos为click文件中提供的值
    def click(self, click_pos):
        self.windowsControl.Click(click_pos.x, click_pos.y)

    def update_message(self):
        self.name = self.windows_dlg.window_text()
        self.play_message = self.windows_dlg.child_window(auto_id="270").Pane2.window_text()
        self.get_xian(self.name)
        self.play_name = self.name.split('--幻影脱机')[0]
        # try:
        #     id_button = self.windows_dlg
        #     self.is_play = True
        # except:
        #     self.is_play = False

    def update_all_message(self):
        self.name = self.windows_dlg.window_text()
        self.play_message = self.windows_dlg.child_window(auto_id="270").Pane2.window_text()
        self.get_xian(self.name)
        self.play_name = self.name.split('--幻影脱机')[0]
        try:
            id_button = self.windows_dlg
            self.is_play = True
        except:
            self.is_play = False

    # 一键领奖
    def qiandao(self):
        self.click(zonghe_pos)
        self.click(main_pos)
        self.windowsControl.ButtonControl(Name='一键领奖').Click()
        self.windowsControl.ButtonControl(Name='活动奖励').Click()

    # 输出当前状态
    def logAll(self):
        if self.is_play:
            print("当前登录状态：" + self.play_message, "当前登录账号id：" + str(self.play_id), "当前登录账号名" + self.play_name)
        else:
            print("当前用户未登录")

    # 退出游戏
    def quit_game(self):
        if self.is_play == 1:
            self.windowsControl.ButtonControl(searchDepth=2, Name="退出").Click()
            self.is_play = 0

    # 登录游戏
    def enter_game(self, enter_xian):
        if self.is_play == 0:
            self.windowsControl.ComboBoxControl(searchDepth=3, AutomationId='460').Click()
            if enter_xian == 1:
                self.windowsControl.ListItemControl(searchDepth=4, Name="一线").Click()
            elif enter_xian == 2:
                self.windowsControl.ListItemControl(searchDepth=4, Name="二线").Click()
            elif enter_xian == 3:
                self.windowsControl.ListItemControl(searchDepth=4, Name="三线").Click()
            elif enter_xian == 4:
                self.windowsControl.ListItemControl(searchDepth=4, Name="四线").Click()
            else:
                return False
            self.windowsControl.ButtonControl(searchDepth=2, Name="登陆").Click()
            time.sleep(1)
            try:
                print(self.windows_dlg.child_window(auto_id="110").child_window(title="ID", auto_id="2650").window_text())
                self.is_play = 1
            except:
                self.windowsControl.ButtonControl(searchDepth=2, Name="进入").Click()
                time.sleep(1)
                try:
                    print(self.windows_dlg.child_window(auto_id="110").child_window(title="ID", auto_id="2650").window_text())
                    self.is_play = 1
                except:
                    self.windowsControl.ButtonControl(searchDepth=2, Name="退出").Click()
                    self.enter_game(enter_xian)

    def get_yanlei(self):
        if self.is_play:
            print("在玩")
            if self.play_xian != 1:
                self.quit_game()
                self.enter_game(1)
        else:
            print("不在玩")
            self.enter_game(1)
        print("开始领眼泪")
        self.click(zonghe_pos)
        self.click(main_pos)
        self.windowsControl.ButtonControl(Name='领眼泪').Click()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# 获取所有窗口
def init_all_window():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t != "" and "幻影脱机" in t:
            print(h, t)
            play_title[h] = t
    print(play_title)


# 对单一窗口进行初始化定义
def init_one_window(now_play, handle_name):
    now_play_window = play_window(now_play, handle_name)
    now_play_window.windowsControl.SetTopmost(True)
    now_play_window.show()
    auto.LogControl(now_play_window.windowsControl)
    # 判断是否有登录操作
    now_play_window.is_play = True
    try:
        if now_play_window.play_name in npc_dict:
            now_play_window.play_id = npc_dict[now_play_window.play_name]
        else:
            id_button = now_play_window.windowsControl.ButtonControl(Name='ID')
            id_button.Click()
            auto.SendKeys('{Enter}')
            # 将ID复制到聊天框内
            now_play_window.click(communication_pos)
            communication_liao_edit = now_play_window.windowsControl.EditControl(AutomationId=communication_liao_id)
            communication_liao_edit.Click()
            communication_liao_edit.SendKeys('{ctrl}a')
            communication_liao_edit.SendKeys('{ctrl}v')
            now_play_window.play_id = communication_liao_edit.GetValuePattern().Value
            communication_liao_edit.SendKeys('{ctrl}z')
            npc_dict[now_play_window.play_name] = now_play_window.play_id
            now_play_window.click(tip_pos)
        #     获取名字
        now_play_window.play_name = now_play_window.windowsControl.PaneControl(AutomationId=name_id).Name
        #     获取状态
        now_play_window.update_message()
    except:
        now_play_window.is_play = False
    now_play_window.windowsControl.SetTopmost(False)
    play_all_window.append(now_play_window)


def show_all_quit():
    for item in play_all_window:
        item.show_quit()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     init_all_window()
#     for handle in play_title:
#         init_one_window(handle, play_title[handle])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
