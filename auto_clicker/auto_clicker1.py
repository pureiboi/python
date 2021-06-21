import pyautogui, math
from pyautogui import *
import keyboard  # using module keyboard
# from tkinter import *
import tkinter as tk
from tkinter import Canvas, Tk, messagebox, PhotoImage, ttk, CENTER, NO, LEFT, W
import datetime
import json
import time


class Action:
    def __init__(self):
        # self.action = ""
        # self.interval = ""
        # self.x = 0
        # self.y = 0
        self.action = tk.StringVar()
        self.intervalMin = tk.IntVar()
        self.intervalMax = tk.IntVar()
        self.x = tk.IntVar()
        self.y = tk.IntVar()
        self.status = True

    def coordinate(self, coor= None):
        """
        getter and setter of coordinate

        :param coor: tuple of x,y
        :return: x,y when coor not provided
        """
        if coor is None:
            return self.x.get(), self.y.get()
        x,y = coor
        self.x.set(x)
        self.y.set(y)

    def getX(self):
        return self.x.get()

    def getY(self):
        return self.y.get()

    def interval_min(self):
        return self.intervalMin.get()

    def interval_max(self):
        return self.intervalMax.get()

    def __str__(self):
        # return json.dumps(self.__dict__)
        return f"action {{action={self.action.get()}, interval min-max={self.intervalMin.get()}-{self.intervalMax.get()}, x={self.x.get()}, y={self.y.get()}}}"

class Table:

    def __init__(self, parent):
        self.tv = ttk.Treeview(parent, columns=('Action', 'X', 'Y', 'Min-Interval', 'Max-Interval', 'Remark')
                               # ,displaycolumns=('Action', 'X', 'Y', 'Min-Interval', 'Max-Interval', 'Remark')
                               )
        # tv['columns']=('Action', 'X', 'Y', 'Min-Interval', 'Max-Interval', 'Remark')
        self.tv.column('#0', width=40, stretch=NO)
        self.tv.column('#1', anchor=CENTER, width=80)
        self.tv.column('#2', anchor=CENTER, width=50)
        self.tv.column('#3', anchor=CENTER, width=50)
        self.tv.column('#4', anchor=CENTER, width=80)
        self.tv.column('#5', anchor=CENTER, width=80)
        self.tv.column('#6', anchor=tk.W, width=150)

        self.tv.heading('#0', text='#', anchor=W)
        self.tv.heading('Action', text='Action', anchor=CENTER)
        self.tv.heading('X', text='X', anchor=CENTER)
        self.tv.heading('Y', text='Y', anchor=CENTER)
        self.tv.heading('Min-Interval', text='Min-Interval', anchor=CENTER)
        self.tv.heading('Max-Interval', text='Max-Interval', anchor=CENTER)
        self.tv.heading('Remark', text='Remark', anchor=CENTER)


        # tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
        # tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
        # tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
        # tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
        # tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
        self.iid = 0
        self.tv.pack()

    def insert(self, action):
        self.tv.insert(parent='', index=self.iid, iid=self.iid,
                       text=str(self.iid),
                       values=('action_' + str(self.iid),
                               str(action.getX()), str(action.getY()),
                               str(action.interval_min()), str(action.interval_max()), 'Echo'))
        self.iid += 1

class Overlay:
    def __init__(self, parent):
        self.parent = parent
        self.verticalLineColor = "red"
        self.horizontalLineColor = "blue"
        self.textItem = tk.StringVar();

    def getCoordinate(self):
        screenWidth, screenHeight = pyautogui.size()

        self.toplevel = tk.Toplevel(self.parent)
        self.toplevel.geometry(f"{screenWidth}x{screenHeight}")
        self.toplevel.attributes('-alpha', 0.5)
        self.toplevel.overrideredirect(1)
        cursorX, cursorY = pyautogui.position()
        self.mycanva = Canvas(self.toplevel, width=screenWidth, height=screenHeight)
        self.line2 = self.drawLine(cursorX, 0, cursorX, screenHeight, self.horizontalLineColor) # myCanvas.create_line(x, 0, x, 1080, fill="black")
        self.line1 = self.drawLine(0, cursorY, screenWidth, cursorY, self.verticalLineColor) # myCanvas.create_line(0, y, 1920, y, fill="red")
        self.text1 = self.drawText("")

        screenY = screenHeight / 2  - 100
        screenX = screenWidth / 2
        self.ScreenSize = self.drawText(f"width: {screenWidth}   height: {screenHeight}", screenX, screenY)

        self.mycanva.bind('<Motion>', self.onMouseMove)
        self.mycanva.bind("<Button-1>", self.onClickCanvas)
        self.mycanva.pack()
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        return self.clickedX, self.clickedY

    def drawLine(self, x1, y1, x2, y2, fill):
        line = self.mycanva.create_line(x1, y1, x2, y2, fill=fill)
        return line

    def drawText(self, text, screenX = None, screenY = None):
        screenWidth, screenHeight = pyautogui.size()
        screenWidth /= 2
        screenHeight /= 2

        if screenX is not None:
            screenWidth = screenX

        if screenY is not None:
            screenHeight = screenY

        return self.mycanva.create_text(screenWidth, screenHeight,font=("Purisa", 25), text=text)

    def onMouseMove(self, event):
        x, y = event.x, event.y
        dy, dx = 0,0
        screenWidth, screenHeight = pyautogui.size()
        # if self.line1:
        #     self.mycanva.delete(self.line1)
        #
        # if self.line2:
        #     self.mycanva.delete(self.line2)

        # if self.text1:
        #     self.mycanva.delete(self.text1)

        self.mycanva.coords(self.line1, 0, y, screenWidth, y)
        self.mycanva.coords(self.line2, x, 0, x, screenHeight)
        # self.mycanva.itemconfigure(self.line1, 0, y, screenWidth, y,)
        # self.text1 = self.drawText(f"X: {x} , Y: {y}")
        self.mycanva.itemconfig(self.text1, text=f"X: {x}   Y: {y}")
        # dx, dy = x, y

    def onClickCanvas(self, event):
        self.clickedX = event.x
        self.clickedY = event.y
        print(f"record method {self.clickedX} {self.clickedY}")
        self.toplevel.destroy()

class ActionForm:

    def __init__(self, parent):
        self.parent = parent
        self.toplevel = tk.Toplevel(parent)

    def show(self):

        lbl_coor = tk.Label(self.toplevel, text= f"x =  y = ").pack()
        lb_interval_min = tk.Label(self.toplevel, text="Minimum: ").pack()
        input_interval_min = tk.Entry(self.toplevel).pack()
        lb_interval_max = tk.Label(self.toplevel, text="Maximum: ").pack()
        input_interval_max = tk.Entry(self.toplevel).pack()

        lb_remark = tk.Label(self.toplevel, text= "remark").pack()
        input_remark = tk.Entry

        self.toplevel.deiconify


def add_action_function(actionList):
    # messagebox.showinfo("Say Hello", "Hello World")
    global overlay, actionInfo

    x,y = overlay.getCoordinate()
    action = Action()
    action.coordinate((x,y))

    print("action added: " )
    print(action)
    actionList.append(action)
    print("action count: " + str(len(actionList)))

    actionInfo.insert(action)

    actForm = ActionForm(root)

    actForm.show()


def showFunction():
    global actionList
    print("number of action " + str(len(actionList)))
    for act in actionList:
        print(act)


def timer_tick():
    global lb_lapsed_time_counter
    lb_lapsed_time_counter += 1
    lb_lapse_text_var.set(f"Lapsed: {str(datetime.timedelta(seconds=lb_lapsed_time_counter))}")
    lb_lapse_call_back_id.set(lb_lapse_time.after(1000, timer_tick))


def cycle_count():
    global lb_cycle_counter
    lb_cycle_counter += 1
    lb_cycle_text_var.set(f"Cycle: {lb_cycle_counter}")
    lb_cycle_call_back_id.set(lb_cycle.after(500, cycle_count))


def init_cycle():
    global lb_cycle_counter
    lb_cycle_counter = 0
    lb_cycle_text_var.set(f"Cycle: {lb_cycle_counter}")
    lb_cycle_call_back_id.set(None)


def start_cycle_counter():
    if lb_cycle_call_back_id.get().casefold() == 'none':
        cycle_count()


def start_lapse_timer():
    if lb_lapse_call_back_id.get().casefold() == 'none':
        timer_tick()


def init_lapse():
    global lb_lapsed_time_counter
    lb_lapsed_time_counter = 0
    lb_lapse_text_var.set(f"Lapsed: {str(datetime.timedelta(seconds=lb_lapsed_time_counter))}")
    lb_lapse_call_back_id.set(None)


def startLoop():
    start_lapse_timer()
    start_cycle_counter()


def stopLoop(event):
    if lb_cycle_call_back_id.get().casefold() == 'none':
        root.after_cancel(lb_cycle_call_back_id.get())

    if not lb_lapse_call_back_id.get().casefold() == 'none':
        root.after_cancel(lb_lapse_call_back_id.get())

    init_cycle()
    init_lapse()
    print("stoppping")


if __name__ == '__main__':


    appWidth, appHeight = 800,800
    root = Tk()
    root.title("Auto Clicker")
    # root.geometry(f"{appWidth}x{appHeight}")
    actionList = []
    overlay = Overlay(root)
    topFrame = tk.Frame(root)
    middleFrame = tk.Frame(root)
    bottomFrame = tk.Frame(root)

    topFrame.grid(column = 0, row = 0, sticky=tk.W)
    middleFrame.grid(column = 0, row = 1)
    bottomFrame.grid(column = 0, row = 2)

    lb_cycle_counter = 0
    lb_cycle_text_var = tk.StringVar()
    lb_cycle_call_back_id = tk.StringVar()

    lb_lapsed_time_counter = 0
    lb_lapse_text_var = tk.StringVar()
    lb_lapse_call_back_id = tk.StringVar()

    init_cycle()
    init_lapse()

    photoAdd = PhotoImage(file = r"auto_clicker\img\add_black_36dp.png")
    photoEdit = PhotoImage(file = r"auto_clicker\img\edit_black_36dp.png")
    photoDelete = PhotoImage(file = r"auto_clicker\img\remove_black_24dp.png")


    button1 = tk.Button(topFrame, text ="Add",  command = lambda : add_action_function(actionList), image = photoAdd)\
        .grid(column = 0, row = 0)
    button2 = tk.Button(topFrame, text ="Edit", command = add_action_function, image = photoEdit)\
        .grid(column = 1, row = 0)
    button3 = tk.Button(topFrame, text ="Delete", command = add_action_function, image = photoDelete)\
        .grid(column = 2, row = 0)
    button4 = tk.Button(topFrame, text ="Clear", command = add_action_function).grid(column = 4, row = 0)
    button5 = tk.Button(topFrame, text ="Show", command = showFunction).grid(column = 5, row = 0)
    button6 = tk.Button(topFrame, text ="Start", command = startLoop).grid(column = 6, row = 0)

    # canva = Canvas(middleFrame, bg="white").grid(column=0, row =0)
    # canva.grid(column=0, row =0)

    lb_cycle = tk.Label(bottomFrame, text = "Cycle: ",relief="groove", textvariable=lb_cycle_text_var)
    lb_cycle.grid(column=0, row = 0)
    lb_cycle.bind("<Button-1>", func=stopLoop)

    lb_lapse_time = tk.Label(bottomFrame, textvariable = lb_lapse_text_var, relief="groove")
    lb_lapse_time.grid(column=1, row=0)
    lb_lapse_time.bind("<Button-1>", func=stopLoop)

    actionInfo = Table(middleFrame)

    root.mainloop()

