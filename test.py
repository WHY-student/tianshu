# # tkinter复选框操作
#
# import tkinter as tk
#
# root = tk.Tk()
# root.title('问卷调查')
# root.geometry('220x80')  # 设置窗口大小
#
# flag_1 = False
# flag_2 = False
# flag_3 = False
# list_content = ['你的爱好是：']
# hobby_list = ['游泳', '唱歌', '旅游']
#
#
# def click_1():
#     global flag_1
#     flag_1 = not flag_1
#     if flag_1:
#         list_content.append(hobby_list[0])
#     else:
#         list_content.remove(hobby_list[0])
#     # print('你的爱好是：', list_content)
#     lab_msg['text'] = list_content
#
#
# def click_2():
#     global flag_2
#     flag_2 = not flag_2
#     if flag_2:
#         list_content.append(hobby_list[1])
#     else:
#         list_content.remove(hobby_list[1])
#     # print('你的爱好是：', list_content)
#     lab_msg['text'] = list_content
#
#
# def click_3():
#     global flag_3
#     flag_3 = not flag_3
#     if flag_3:
#         list_content.append(hobby_list[2])
#     else:
#         list_content.remove(hobby_list[2])
#     # print('你的爱好是：', list_content)
#     lab_msg['text'] = list_content
#
#
# '''窗体控件'''
# # 标题显示
# lab = tk.Label(root, text='请选择你的爱好：')
# lab.grid(row=0, columnspan=3, sticky=tk.W)
#
# # 多选框
# frm = tk.Frame(root)
# ck1 = tk.Checkbutton(frm, text='游泳', command=click_1)
# ck2 = tk.Checkbutton(frm, text='唱歌', command=click_2)
# ck3 = tk.Checkbutton(frm, text='旅游', command=click_3)
# ck1.grid(row=0)
# ck2.grid(row=0, column=1)
# ck3.grid(row=0, column=2)
# frm.grid(row=1)
#
# lab_msg = tk.Label(root, text='')
# lab_msg.grid(row=2, columnspan=3, sticky=tk.W)
#
# root.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox, filedialog
#
#
# # 点击勾选框触发
# def getselect(item):
#     print(item, 'selected')
#
#
# # 反选
# def unselectall():
#     for index, item in enumerate(list1):
#         v[index].set('')
#
#
# # 全选
# def selectall():
#     for index, item in enumerate(list1):
#         v[index].set(item)
#
#
# # 获取选择项
# def showselect():
#     selected = [i.get() for i in v if i.get()]
#     print(selected)
#
#
# # 建立一个数组保存 v=[](v.append(tk.StringVar()))
# window = tk.Tk()
# window.geometry('500x500')
# frame1 = tk.Frame(window, pady=10, padx=15)
# frame1.grid(row=0, column=0)
# # 全选反选
# opt = tk.IntVar()
# ttk.Radiobutton(frame1, text='全选', variable=opt, value=1, command=selectall).grid(row=0, column=0, sticky='w')
# ttk.Radiobutton(frame1, text='反选', variable=opt, value=0, command=unselectall).grid(row=0, column=1, sticky='w')
# list1 = ['阿尔及利亚', '澳大利亚', '博茨瓦纳', '巴西', '文莱', '加拿大', '智利', '中国', '哥伦比亚', '捷克', '丹麦', '美国', '印度']
# v = []
# # 设置勾选框，每四个换行
# for index, item in enumerate(list1):
#     v.append(tk.StringVar())
#     ttk.Checkbutton(frame1, text=item, variable=v[-1], onvalue=item, offvalue='',
#                     command=lambda item=item: getselect(item)).grid(row=index // 4 + 1, column=index % 4, sticky='w')
# ttk.Button(frame1, text="获取选择的国家", command=showselect).grid(row=index // 4 + 2, column=0)
# window.mainloop()


# name = "aaaaaabb"
# print(name[-2:])


# Makes all inactive windows transparent and keeps the active window opaque.
# This should be run in the background as a daemon like so:
# python2 inactive-window-transparent.py

# Range of values: 0 <= opacity <= 1
# where 1 is fully opaque and 0 is completely invisible
import sys
import os

import comtypes
import pywinauto
import six
from comtypes.gen._944DE083_8FB8_45CF_BCB7_C477ACB2F897_0_1_0 import IUIAutomationInvokePattern
from pywinauto import Application
from pywinauto.actionlogger import ActionLogger
from pywinauto.timings import Timings
from pywinauto.uia_defines import NoPatternInterfaceError

from main import *
from pywinauto.controls.hwndwrapper import HwndWrapper, _calc_flags_and_coords
from pywinauto import mouse


# IUIAutomationInvokePattern

def my_click(button):
    """Click the Button control by using Invoke or Select patterns"""
    try:
        """An interface to the Invoke method of the Invoke control pattern"""
        name = button.element_info.name
        control_type = button.element_info.control_type
        print(type(button.iface_invoke))
        print(button.iface_invoke.Invoke)
        elem = button.element_info.element
        print(elem)
        print(uia_defines.get_elem_interface(elem, "Invoke"))
        # print(elem.value)
        button.iface_invoke.Invoke()

        if name and control_type:
            button.actions.log("Invoked " + control_type.lower() + ' "' + name + '"')
        # Return itself to allow action chaining
    except NoPatternInterfaceError:
        button.select()

    # Return itself so that action can be chained
    return button


init_all_window()

for handle in play_title:
    init_one_window(handle, play_title[handle])
    app = Application(backend='uia').connect(handle=handle)
    dlg = app.top_window()
    play_all_window[0].get_yanlei()
    # dlg.print_control_identifiers()
    # dlg.minimize()
    # print(dlg.window_text())
    # menu = dlg.Menu
    # button = dlg.
    # my_click(dlg,zonghe_pos)
    # print(dlg.is_dialog)
    # dig.draw_outline(colour='red')
    # menu.click()
    # dlg.print_control_identifiers(depth=None, filename=None)
    # dlg_window = dlg.child_window(auto_id="270")
    # dlg_name = dlg.child_window(auto_id="270").Pane2
    # print(dlg_name.window_text())
    # dlg_window_2 = dlg.child_window(auto_id="120")
    # dlg_window_3 = dlg_window_2.child_window(auto_id="130")
    # # dlg_window_3.print_control_identifiers(depth=None, filename=None)
    # dlg_window_4 = dlg_window_3.child_window(auto_id="6590").child_window(auto_id="6740")
    # # dlg_window_4.print_control_identifiers()
    # test_button = dlg_window_4.Button
    # # print(type(test_button))
    # # print(dir(test_button))
    # my_click(test_button)
    # dlg_window.print_control_identifiers(depth=None, filename=None)
    # dlg.click(button='left', pressed='', coords=(477, 74), double=False, absolute=False)
    # try:
    #     print(dlg.child_window(auto_id="110").child_window(title="ID", auto_id="2650").window_text())
    #     print("在线")
    # except:
    #     print("不在线")
    # dlg.restore()
