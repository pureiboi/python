import pyautogui, math
import keyboard  # using module keyboard
# from tkinter import *
import tkinter as tk
from tkinter import Canvas, Tk, messagebox
import datetime

import time
#
# # Radius
# R = 400
#
screenWidth, screenHeight = pyautogui.size()
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
class Overlay:
    def __init__(self, srnWidth, srnHeight, cursorX, cursorY):
        self.clickedX = 0
        self.clickedY = 0
        self.screenWidth =srnWidth
        self.screenHeight =srnHeight
        self.root = Tk()
        self.root.geometry()
        self.root.overrideredirect(1)
        self.root.attributes('-alpha', 0.5)
        self.myCanvas = Canvas(self.root)
        (self.dx, self.dy) = (0,0)
        self.verticalLineColor = "red"
        self.horizontalLineColor = "blue"
        self.myCanvas = Canvas(self.root, width=self.screenWidth, height=self.screenHeight)
        self.line1 = self.drawLine(self.myCanvas, 0, cursorY, self.screenWidth, cursorY, self.verticalLineColor) # myCanvas.create_line(0, y, 1920, y, fill="red")
        self.line2 = self.drawLine(self.myCanvas, cursorX, 0, cursorX, self.screenHeight, self.horizontalLineColor) # myCanvas.create_line(x, 0, x, 1080, fill="black")

        self.myCanvas.pack(expand=True)
        self.root.bind('<Motion>', self.drawCrossLine)
        self.myCanvas.bind("<Button-1>", self.recordLeftClick)
        self.root.mainloop()

    def drawLine(self, canvas, x1, y1, x2, y2, fill):
        line = canvas.create_line(x1, y1, x2, y2, fill=fill)
        return line

    def getClickCoordinate(self):
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
        self.root.destroy()


class Action:

    def __init__(self):
        self.action = ""
        self.interval = ""
        self.x = 0
        self.y = 0

    def coordinate(self, coor=""):
        """
        getter and setter of coordinate

        :param coor: tuple of x,y
        :return: x,y when coor not provided
        """
        if not coor:
            return self.x, self.y
        x,y = coor
        self.x = x
        self.y = y


curX, curY = pyautogui.position()


a = Overlay(screenWidth, screenHeight, curX, curY)

action1 = Action()

action1.coordinate(a.getClickCoordinate())

print(action1.coordinate())


clickLoop = 10

while(clickLoop>0):
    clickLoop -= 1
    pyautogui.click(x=action1.x, y=action1.y)
    # time.sleep(1)


appWidth, appHeight = 400,400

root = Tk()
root.title("Auto Clicker")
root.geometry(f"{appWidth}x{appHeight}")
w = Canvas(root, width=appWidth, height=appHeight)
# w.pack()

canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
# mainloop()


# lbLapse = tk.Label(root, text = "lapsed: ")
# lbLapse.grid(column=0, row=0)
#
# dt = datetime.datetime.now()
# dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
#
# lbLapse_time = tk.Label(root, text = dt.strftime("%H:%M:%S"))
# lbLapse_time.grid(column=1, row=0)


def addFunction():
    messagebox.showinfo("Say Hello", "Hello World")

button1 = tk.Button(root, text ="Add", command = addFunction)
button1.grid(column = 0, row = 0)

button2 = tk.Button(root, text ="Edit", command = addFunction)
button2.grid(column = 1, row = 0)

button3 = tk.Button(root, text ="Delete", command = addFunction)
button3.grid(column = 2, row = 0)

button4 = tk.Button(root, text ="Clear", command = addFunction)
button4.grid(column = 4, row = 0)

root.mainloop()
