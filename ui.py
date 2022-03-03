import json
from tkinter import *  # 导入 Tkinter 库
from tkinter import ttk
from tkinter import messagebox
from main import *
import threading

xian_dict = {1: "一线", 2: "二线", 3: "三线", 4: "四线"}


def ui_qiandao():
    for row_update in choose_play_list:
        items = play_all_window[row_update]
        if items.is_play:
            items.show()
            items.qiandao()
            items.hide()
        else:
            pass


def ui_all_update():
    while 1:
        # print(len(play_all_window))
        for row_update in range(0, len(play_all_window)):
            play_all_window[row_update].update_message()
            if play_all_window[row_update].is_play:
                print('更新第' + str(row_update), '为' + play_all_window[row_update].play_message)
                text_list[row_update][0].set(play_all_window[row_update].play_name)
                text_list[row_update][1].set(play_all_window[row_update].play_id)
                text_list[row_update][2].set(play_all_window[row_update].play_message)
                text_list[row_update][3].set(xian_dict[play_all_window[row_update].play_xian])
            else:
                pass
        time.sleep(5)


def ui_all_yanlei():
    print(choose_play_list)
    for row_update in choose_play_list:
        print('领眼泪的第{}个'.format(row_update))
        items = play_all_window[row_update]
        items.show()
        items.get_yanlei()
        items.hide()


def ui_all_show():
    for row_update in choose_play_list:
        play_all_window[row_update].show_quit()


def ui_all_hide():
    for row_update in choose_play_list:
        print('隐藏的第{}个'.format(row_update))
        play_all_window[row_update].hide_quit()


def ui_top():
    auto.WindowControl(Name='tk').SetTopmost(True)


def fangan_1():
    fangan_index.set(1)
    choose_play_list.clear()
    for row_update in choose_list:
        row_update.set(0)
    for row_update in fangan_1_list:
        # print("方案1包含",row_update)
        choose_play_list.append(row_update)
        choose_list[row_update].set(1)
    print('当前方案编号为：' + str(fangan_index.get()))


def fangan_2():
    fangan_index.set(2)
    choose_play_list.clear()
    for row_update in choose_list:
        row_update.set(0)
    for row_update in fangan_2_list:
        choose_play_list.append(row_update)
        choose_list[row_update].set(1)
    print('当前方案编号为：' + str(fangan_index.get()))


def fangan_3():
    fangan_index.set(3)
    choose_play_list.clear()
    for row_update in choose_list:
        row_update.set(0)
    for row_update in fangan_3_list:
        choose_play_list.append(row_update)
        choose_list[row_update].set(1)
    print('当前方案编号为：' + str(fangan_index.get()))


def fangan_4():
    fangan_index.set(4)
    choose_play_list.clear()
    for row_update in choose_list:
        row_update.set(0)
    for row_update in fangan_4_list:
        choose_play_list.append(row_update)
        choose_list[row_update].set(1)
    print('当前方案编号为：' + str(fangan_index.get()))


def fangan_func_a():
    messagebox.askokcancel(title='错误', message='你还没选择方案')


def fangan_func_1():
    fangan_1_list.clear()
    index_choose = 0
    for row_update in choose_list:
        # print(row_update.get())
        if row_update.get() == 1:
            fangan_1_list.append(index_choose)
        index_choose += 1


def fangan_func_2():
    fangan_2_list.clear()
    index_choose = 0
    for row_update in choose_list:
        if row_update.get() == 1:
            fangan_2_list.append(index_choose)
        index_choose += 1


def fangan_func_3():
    fangan_3_list.clear()
    index_choose = 0
    for row_update in choose_list:
        if row_update.get() == 1:
            fangan_3_list.append(index_choose)
        index_choose += 1


def fangan_func_4():
    fangan_4_list.clear()
    index_choose = 0
    for row_update in choose_list:
        if row_update.get() == 1:
            fangan_4_list.append(index_choose)
        index_choose += 1


def fangan_keep():
    # print('当前方案编号为：' + str(fangan_index.get()))
    fangan_func_list = {0: fangan_func_a, 1: fangan_func_1, 2: fangan_func_2, 3: fangan_func_3, 4: fangan_func_4}
    fangan_function = fangan_func_list[fangan_index.get()]
    fangan_function()


def select_all():
    choose_play_list.clear()
    for row_update in range(0, len(choose_list)):
        choose_list[row_update].set(1)
        choose_play_list.append(row_update)


fangan_1_list = []
fangan_2_list = []
fangan_3_list = []
fangan_4_list = []
choose_play_list = []
choose_list = []
init_all_window()
with open('npc.txt') as f:
    all_data_json = json.loads(f.read())
for all_npc_name in all_data_json:
    npc_dict[all_npc_name] = all_data_json[all_npc_name]
for handle in play_title:
    init_one_window(handle, play_title[handle])
root = Tk()
frame_main = Frame(root)
frame_main.grid()
fangan_index = IntVar()
Button(frame_main, text="全选", command=select_all).grid(column=0, row=1)
Button(frame_main, text="方案1", command=fangan_1).grid(column=0, row=2)
Button(frame_main, text="方案2", command=fangan_2).grid(column=0, row=3)
Button(frame_main, text="方案3", command=fangan_3).grid(column=0, row=4)
Button(frame_main, text="方案4", command=fangan_4).grid(column=0, row=5)
Button(frame_main, text="保存", command=fangan_keep).grid(column=0, row=6)
top_column = 1
Button(frame_main, text="置顶", command=ui_top).grid(column=top_column, row=0)
top_column += 1
Label(frame_main, text="账号名").grid(column=top_column, row=0)
top_column += 1
Label(frame_main, text="id").grid(column=top_column, row=0)
top_column += 1
Label(frame_main, text="当前状态").grid(column=top_column, row=0)
top_column += 1
Label(frame_main, text="当前线路").grid(column=top_column, row=0)
top_column += 1
Label(frame_main, text="操作").grid(column=top_column, row=0)
top_column += 1
Button(frame_main, text="一键领奖+活动", command=ui_qiandao).grid(column=top_column, row=0)
top_column += 1
Button(frame_main, text="一键隐藏", command=ui_all_hide).grid(column=top_column, row=0)
top_column += 1
Button(frame_main, text="一键显示", command=ui_all_show).grid(column=top_column, row=0)
top_column += 1
Button(frame_main, text="一键领眼泪", command=ui_all_yanlei).grid(column=top_column, row=0)
top_column += 1
Button(frame_main, text="置顶", command=ui_all_show).grid(column=top_column, row=0)
a1 = StringVar()
a2 = StringVar()
a3 = StringVar()
a4 = StringVar()
a5 = StringVar()
a6 = StringVar()
a7 = StringVar()
a8 = StringVar()
a9 = StringVar()
a10 = StringVar()
a11 = StringVar()
a12 = StringVar()
a13 = StringVar()
a14 = StringVar()
a15 = StringVar()
a16 = StringVar()
a17 = StringVar()
a18 = StringVar()
a19 = StringVar()
a20 = StringVar()
a21 = StringVar()
a22 = StringVar()
a23 = StringVar()
a24 = StringVar()
a25 = StringVar()
a26 = StringVar()
a27 = StringVar()
a28 = StringVar()
a29 = StringVar()
a30 = StringVar()
a31 = StringVar()
a32 = StringVar()
a33 = StringVar()
a34 = StringVar()
a35 = StringVar()
a36 = StringVar()
a37 = StringVar()
a38 = StringVar()
a39 = StringVar()
a40 = StringVar()
a41 = StringVar()
a42 = StringVar()
a43 = StringVar()
a44 = StringVar()
a45 = StringVar()
text_list = [[a1, a2, a3], [a4, a5, a6], [a7, a8, a9], [a10, a11, a12], [a13, a14, a15], [a16, a17, a18],
             [a19, a20, a21], [a22, a23, a24], [a25, a26, a27], [a28, a29, a30], [a31, a32, a33], [a34, a35, a36],
             [a37, a38, a39], [a40, a41, a42], [a43, a44, a45]]


# 更新状态
def update(choose_row):
    play_all_window[choose_row].update_all_message()
    print('更新第' + str(choose_row), '为' + play_all_window[choose_row].play_message)
    text_list[choose_row][0].set(play_all_window[choose_row].play_name)
    text_list[choose_row][1].set(play_all_window[choose_row].play_id)
    text_list[choose_row][2].set(play_all_window[choose_row].play_message)
    text_list[choose_row][3].set(xian_dict[play_all_window[row - 1].play_xian])


# 选择
def choose_play(choose_row):
    choose_play_list.append(choose_row - 1)


for row in range(1, len(play_all_window) + 1):
    choose_list.append(IntVar())
    use_column = 0
    text_list[row - 1].append(StringVar())
    print('目前一共有' + str(len(play_all_window)), row)
    text_list[row - 1][0].set(play_all_window[row - 1].play_name)
    text_list[row - 1][1].set(play_all_window[row - 1].play_id)
    text_list[row - 1][2].set(play_all_window[row - 1].play_message)
    text_list[row - 1][3].set(xian_dict[play_all_window[row - 1].play_xian])
    use_column += 1
    ttk.Checkbutton(frame_main, text="", variable=choose_list[-1], onvalue=1, offvalue=0,
                    command=lambda row=row: choose_play(row)).grid(row=row, column=use_column, sticky='w')
    use_column += 1
    Label(frame_main, textvariable=text_list[row - 1][0]).grid(column=use_column, row=row)
    use_column += 1
    Label(frame_main, textvariable=text_list[row - 1][1]).grid(column=use_column, row=row)
    use_column += 1
    Label(frame_main, textvariable=text_list[row - 1][2]).grid(column=use_column, row=row)
    use_column += 1
    Label(frame_main, textvariable=text_list[row - 1][3]).grid(column=use_column, row=row)
    use_column += 1
    Button(frame_main, text="隐藏", command=play_all_window[row - 1].hide_quit).grid(column=use_column, row=row)
    use_column += 1
    Button(frame_main, text="显示", command=play_all_window[row - 1].show_quit).grid(column=use_column, row=row)
    use_column += 1
    Button(frame_main, text="置顶", command=play_all_window[row - 1].show).grid(column=use_column, row=row)
    use_column += 1
    Button(frame_main, text="取消置顶", command=play_all_window[row - 1].hide).grid(column=use_column, row=row)
    use_column += 1
    Button(frame_main, text="更新状态", command=lambda row=row: update(row - 1)).grid(column=use_column, row=row)


def ui_destroy():
    show_all_quit()
    npc_json = json.dumps(npc_dict)
    with open('npc.txt', 'w') as f1:
        f1.write(npc_json)
    root.destroy()


th = threading.Thread(target=ui_all_update)
th.setDaemon(True)  # 守护线程
th.start()
root.protocol('WM_DELETE_WINDOW', ui_destroy)
root.mainloop()
