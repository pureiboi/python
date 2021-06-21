import pyautogui, math
import keyboard  # using module keyboard
# from tkinter import *
import tkinter as tk
from tkinter import Canvas, Tk, messagebox, PhotoImage
import datetime
import json
import time

class Action:
    def __init__(self):
        self.action = ""
        self.interval = ""
        self.x = 0
        self.y = 0

    def coordinate(self, coor= None):
        """
        getter and setter of coordinate

        :param coor: tuple of x,y
        :return: x,y when coor not provided
        """
        if coor is None:
            return self.x, self.y
        x,y = coor
        self.x = x
        self.y = y

    def __str__(self):
        return json.dumps(self.__dict__)


class Overlay:
    def __init__(self):
        self.clickedX = 0
        self.clickedY = 0
        self.screenWidth, self.screenHeight = pyautogui.size()
        (self.dx, self.dy) = (0,0)
        self.verticalLineColor = "red"
        self.horizontalLineColor = "blue"

    def drawLine(self, canvas, x1, y1, x2, y2, fill):
        line = canvas.create_line(x1, y1, x2, y2, fill=fill)
        return line

    def start(self):
        cursorX, cursorY =pyautogui.position()
        screenWidth, screenHeight = pyautogui.size()
        self.overlayContainer = Tk()
        self.overlayContainer.geometry()
        self.overlayContainer.overrideredirect(1)
        self.overlayContainer.attributes('-alpha', 0.5)
        self.overlayContainer.bind('<Motion>', self.drawCrossLine)
        self.myCanvas = Canvas(self.overlayContainer, width=screenWidth, height=screenHeight)
        self.line2 = self.drawLine(self.myCanvas, cursorX, 0, cursorX, screenHeight, self.horizontalLineColor) # myCanvas.create_line(x, 0, x, 1080, fill="black")
        self.line1 = self.drawLine(self.myCanvas, 0, cursorY, self.screenWidth, cursorY, self.verticalLineColor) # myCanvas.create_line(0, y, 1920, y, fill="red")
        self.myCanvas.pack(expand=True)
        self.myCanvas.bind("<Button-1>", self.recordLeftClick)
        self.overlayContainer.mainloop()
        print("test")

    def coordinate(self):
        return self.clickedX, self.clickedY

    def drawCrossLine(self, event):
        x, y = event.x, event.y

        if self.line1:
            self.myCanvas.delete(self.line1)
        if self.line2:
            self.myCanvas.delete(self.line2)
        if x-self.dx or y-self.dy:
            self.line1 = self.drawLine(self.myCanvas, 0, y, self.screenWidth, y, self.verticalLineColor)
            self.line2 = self.drawLine(self.myCanvas, x, 0, x, self.screenHeight, self.horizontalLineColor)
        (self.dx,self.dy) = x, y

    def recordLeftClick(self, event):
        self.clickedX = event.x
        self.clickedY = event.y
        print(f"record method {self.clickedX} {self.clickedY}")
        self.overlayContainer.destroy()



#
# # Radius
# R = 400
#
#
# # measuring screen size
# (x,y) = pyautogui.size()
# # locating center of the screen
# # (X,Y) = pyautogui.position(x/2,y/2)
# (X,Y) = pyautogui.position()
#
# sizeList = []
# sizeList.append(R)
# sizeList.append(Y - 0)
# sizeList.append(X - 0)
# sizeList.append(y - Y)
# sizeList.append(x - X)
#
# R = min(sizeList)
#
# print(f"radius is: {R}")
#
# # offsetting by radius
# # pyautogui.moveTo(X+R,Y)
#
# isBreak = False
#
# loopCount = 5
#
#
# def isToExit() -> bool:
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):
#             return True
#         else:
#             return False
#     except Exception as e: print(e)
#
#
# # while loopCount > 0:
# #     for i in range(360):
# #         # setting pace with a modulus
# #         isBreak = isToExit()
# #         if i%10 == 0 and not isBreak:
# #             pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
# #             # pyautogui.moveTo(R*math.cos(math.radians(i)),R*math.sin(math.radians(i)))
# #
# #         if isBreak:
# #             break
# #     loopCount -= 1
#
#
# # while True:  # making a loop
# #     try:  # used try so that if user pressed other than the given key error will not be shown
# #         # if keyboard.read_key():
# #             # print(keyboard.read_key() + " is pressed ")
# #         if keyboard.is_pressed('q'):  # if key 'q' is pressed
# #             print('You Pressed A Key!')
# #             break  # finishing the loop
# #     except:
# #         break  # if user pressed a key other than the given key the loop will break
#
# # (dx,dy) = (0,0)
# # while True:
# #
# #     (x,y) = pyautogui.position()
# #     if x-dx or y-dy:
# #         print(f"current mouse position: {pyautogui.position()}")
# #     (dx, dy) = (x,y)
#
#
#
# # class Application(tk.Frame):
# #     def __init__(self, master=None):
# #         super().__init__(master)
# #         self.master = master
# #         self.pack()
# #         self.create_widgets()
# #
# #
# #     def create_widgets(self):
# #         self.hi_there = tk.Button(self)
# #         self.hi_there["text"] = "Hello World\n(click me)"
# #         self.hi_there["command"] = self.say_hi
# #         self.hi_there.pack(side="top")
# #
# #         self.quit = tk.Button(self, text="QUIT", fg="red",
# #                               command=self.master.destroy)
# #         self.quit.pack(side="bottom")
# #
# #     def say_hi(self):
# #         print("hi there, everyone!")
# #
#
#
#
#
# # app = Application(master=root)
# # app.mainloop()
#
# # root = Tk()
# # root.title("hallooo")
# # root.geometry("1920x1080")
# # root.overrideredirect(1)
# # myCanvas = Canvas(root, width=1920, height=1080)
# # root.attributes('-alpha', 0.5)
# # myCanvas.pack(expand=TRUE)
#
# # (dx,dy) = (0,0)
# # while True:
# #
# #     (x,y) = pyautogui.position()
# #     if x-dx or y-dy:
# #         print(f"current mouse position: {pyautogui.position()}")
# #         myCanvas.create_line(0, y, 1080, y, fill="red")
# #         root.mainloop()
# #     (dx, dy) = (x,y)
#
# # (dx,dy) = (0,0)
# #
# # line1 = myCanvas.create_line(0, y, 1920, y, fill="red")
# # line2 = myCanvas.create_line(x, 0, x, 1080, fill="black")
# #
# # def myfunction(event):
# #     global dx, dy, line1, line2
# #     myCanvas.delete(line1)
# #     myCanvas.delete(line2)
# #     x, y = event.x, event.y
# #     if x-dx or y-dy:
# #         line1 = myCanvas.create_line(0, y, 1920, y, fill="red")
# #         line2 = myCanvas.create_line(x, 0, x, 1080, fill="black")
# #     (dx,dy) = x, y
# #
# #
# # def callback(event):
# #     print("clicked at", event.x, event.y)
# #     root.destroy()
# #
# # myCanvas.bind("<Button-1>", callback)
# #
# #
# # root.bind('<Motion>', myfunction)
# # root.mainloop()
# # # root.overrideredirect(1)
# #
#
#



# curX, curY = pyautogui.position()



# action1 = Action()

# action1.coordinate(a.getClickCoordinate())

# print(action1.coordinate())


# clickLoop = 10
#
# while(clickLoop>0):
#     clickLoop -= 1
    # pyautogui.click(x=action1.x, y=action1.y)
    # time.sleep(1)


appWidth, appHeight = 400,400

root = Tk()

# overlay = Overlay()
root.title("Auto Clicker")
root.geometry(f"{appWidth}x{appHeight}")

actionList = []

def addFunction():
    # messagebox.showinfo("Say Hello", "Hello World")
    global actionList
    action = Action()

    overlay = Overlay()
    print("action added: " )
    overlay.start()
    x,y = overlay.coordinate()
    print(x,y)
    print(action)
    actionList.append(action)
    print("action count: " + str(len(actionList)))


def showFunction():
    global actionList
    print("number of action " + str(len(actionList)))
    for act in actionList:
        print(act)


lb_cycle_counter = 0
lb_cycle_text_var = tk.StringVar()
lb_cycle_call_back_id = tk.StringVar()

lb_lapsed_time_counter = 0
lb_lapse_text_var = tk.StringVar()
lb_lapse_call_back_id = tk.StringVar()


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


init_cycle()
init_lapse()


photo = PhotoImage(file = r"E:\Workspace\python\github_repo\auto_clicker\img\add_black_24dp.png")

button1 = tk.Button(root, text ="Add", command = addFunction, image = photo).grid(column = 0, row = 0)
button2 = tk.Button(root, text ="Edit", command = addFunction).grid(column = 1, row = 0)
button3 = tk.Button(root, text ="Delete", command = addFunction).grid(column = 2, row = 0)
button4 = tk.Button(root, text ="Clear", command = addFunction).grid(column = 4, row = 0)
button5 = tk.Button(root, text ="Show", command = showFunction).grid(column = 5, row = 0)
button6 = tk.Button(root, text ="Start", command = startLoop).grid(column = 6, row = 0)

lb_cycle = tk.Label(root, text = "Cycle: ",relief="groove", textvariable=lb_cycle_text_var)
lb_cycle.grid(column=0, row = 2)
lb_cycle.bind("<Button-1>", func=stopLoop)

lb_lapse_time = tk.Label(root, textvariable = lb_lapse_text_var, relief="groove")
lb_lapse_time.grid(column=1, row=2)
lb_lapse_time.bind("<Button-1>", func=stopLoop)


root.mainloop()
