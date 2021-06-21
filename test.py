import keyboard  # using module keyboard

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         # if keyboard.read_key():
#         #     print(keyboard.read_key() + " is pressed ")
#         # else:
#         #     print("nothing presses")
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed
#             print('You Pressed A Key!')
#             break  # finishing the loop
#         else:
#             print("nothing presses")
#     except:
#         break  # if user pressed a key other than the given key the loop will break


# # import tkinter module
# from tkinter import *
# from tkinter.ttk import *
#
# # creating main tkinter window/toplevel
# master = Tk()
#
# # this will create a label widget
# l1 = Label(master, text = "Height")
# l2 = Label(master, text = "Width")
#
# # grid method to arrange labels in respective
# # rows and columns as specified
# l1.grid(row = 0, column = 0, sticky = W, pady = 2)
# l2.grid(row = 1, column = 0, sticky = W, pady = 2)
#
# # entry widgets, used to take entry from user
# e1 = Entry(master)
# e2 = Entry(master)
#
# # this will arrange entry widgets
# e1.grid(row = 0, column = 1, pady = 2)
# e2.grid(row = 1, column = 1, pady = 2)
#
# # checkbutton widget
# c1 = Checkbutton(master, text = "Preserve")
# c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)
#
# # adding image (remember image should be PNG and not JPG)
# # img = PhotoImage(file = r"F:\wing.png")
# # img1 = img.subsample(2, 2)
#
# # setting image with the help of label
# # Label(master, image = img1).grid(row = 0, column = 2,
# #                                  columnspan = 2, rowspan = 2, padx = 5, pady = 5)
#
# # button widget
# b1 = Button(master, text = "Zoom in")
# b2 = Button(master, text = "Zoom out")
#
# # arranging button widgets
# b1.grid(row = 2, column = 2, sticky = E)
# b2.grid(row = 2, column = 3, sticky = E)
#
# # infinite loop which can be terminated
# # by keyboard or mouse interrupt
# mainloop()


# import tkinter as tk
#
# colours = ['red','green','orange','white','yellow','blue']
#
# r = 0
# for c in colours:
#     tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r,column=0)
#     tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
#     r = r + 1
#
# tk.mainloop()









#
# import tkinter as tk
#
# app = tk.Tk()
# app.geometry('300x200')
# app.title("Basic Status Bar")
#
# statusbar = tk.Label(app, text="on the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W)
#
# statusbar.pack(side=tk.BOTTOM, fill=tk.X)
# app.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title('Timer')
# root.state('zoomed')
#
# sec = 0
#
# def tick():
#     global sec
#     sec += 1
#     time['text'] = sec
#     # Take advantage of the after method of the Label
#     time.after(1000, tick)
#
# time = Label(root, fg='green')
# time.pack()
# Button(root, fg='blue', text='Start', command=tick).pack()
#
# root.mainloop()


# import datetime
# print(str(datetime.timedelta(seconds=600)))




import tkinter as tk

class MyDialog(object):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)
        self.var = tk.StringVar()
        label = tk.Label(self.toplevel, text="Pick something:")
        om = tk.OptionMenu(self.toplevel, self.var, "one", "two","three")
        button = tk.Button(self.toplevel, text="OK", command=self.toplevel.destroy)
        label.pack(side="top", fill="x")
        om.pack(side="top", fill="x")
        button.pack()

    def show(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = self.var.get()
        return value


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.button = tk.Button(self, text="Click me!", command=self.on_click)
        self.label = tk.Label(self, width=80)
        self.label.pack(side="top", fill="x")
        self.button.pack(pady=20)

    def on_click(self):
        result = MyDialog(self).show()
        self.label.configure(text="your result: %s" % result)

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()



# import tkinter
#
# top = tkinter.Tk()
#
# top.geometry("200x200")
#
# C = tkinter.Canvas(top, bg="green", height=10800, width=300)
#
# coord = 10, 50, 240, 210
# # arc = C.create_arc(coord, start=0, extent=150, fill="red")
#
# C.pack()
# top.mainloop()