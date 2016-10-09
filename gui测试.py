# -*- coding:utf-8 -*-
import Tkinter
from tkinter import ttk     # 在ttk模块中有一些高级的窗口小部件，让我们的界面看起来更好

#居中
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    root.geometry(size)


def testgui():
	# 初始化tk
	root = Tkinter.Tk()
	# 设置窗口的title
	root.title('Hello')

	# 指定master、标题
	Tkinter.Label(root, text='Hello').pack()

	center_window(root, 300, 240)
	root.maxsize(600, 400)
	root.minsize(300, 240)


	# 进入消息循环。其实就是显示
	root.mainloop()

win = Tkinter.Tk()
win.title("Python GUI")    # 添加标题
aLabel = ttk.Label(win, text="A Label")     # 创建一个标签, text：显示表现的内容
aLabel.grid(column=0, row=0)

def clickMe():   # 当acction被点击时,该函数则生效
  action.configure(text='Hello ' + name.get())     # 设置button显示的内容

action = ttk.Button(win, text="Click Me!", command=clickMe)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=1)

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

name = Tkinter.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Entry(win, width=12, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=0, row=1)

win.mainloop()      # 当调用mainloop()时,窗口才会显示出来