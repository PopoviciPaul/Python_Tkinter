from tkinter import *
from tkinter import font
from numbers import Number
import operator


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        self.ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }
        
        self.UserIn = StringVar();
        self.UserIn.set("")
        self.task = "" # a value that is used to get the final value which will be displayed
        self.result = 0
        self.grid()
        self.create_widgets()

    def Return_Calculus(self, current, sign):
        #self.result = abs(self.ops[sign](current,self.result)) # add current to result
        last_pressed = 0
        if sign=="+":
            self.result += current
            
        elif sign=="-":
            if self.result==0:
                self.result = current
            else:
                self.result -= current

        elif sign=="*":
            if self.result==0:
                self.result = current
            else:
                self.result *= current

        elif sign=="/":
            if self.result==0:
                self.result = current
            else:
                self.result /= current

        self.task=""

        self.UserIn.set(str(self.result))


    def buttonClick(self, pressed_button):
        if pressed_button == "C":
            self.UserIn.set("")
            self.task = ""
            self.result = 0
        elif pressed_button in ["+", "-", "/", "*", "="]:   
            # IMPLEMENT THIS: SAVE PREV, CURRENT, AND GET NEW RESULT
            self.UserIn.set("")
            current = float(self.task)
            self.Return_Calculus(current, pressed_button)

        elif isinstance(int(pressed_button), Number):
            self.task = str(self.task) + str(pressed_button)
            self.UserIn.set(self.task)
            
    def create_widgets(self):
        #print(self.some_var)
        # The entry which will display the result as well as the numbers as they are entered by the user
        self.user_input = Entry(self, bg="#33C4FF", font=("Verdana", 20, "bold"),justify=RIGHT, textvariable=self.UserIn)
        self.user_input.grid(row = 0, columnspan = 4)
        
        # The frame which contains all the button widgets
        self.button_1 = Button(self, text="1", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("1")).grid(row=1, column=0, sticky=N+S+W+E)
        self.button_2 = Button(self, text="2", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("2")).grid(row=1, column=1, sticky=N+S+W+E)
        self.button_3 = Button(self, text="3", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("3")).grid(row=1, column=2, sticky=N+S+W+E)
        self.button_plus = Button(self, text="+", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("+")).grid(row=1, column=3, sticky=N+S+W+E)

        self.button_4 = Button(self, text="4", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("4")).grid(row=2, column=0, sticky=N+S+W+E)
        self.button_5 = Button(self, text="5", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("5")).grid(row=2, column=1, sticky=N+S+W+E)
        self.button_6 = Button(self, text="6", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("6")).grid(row=2, column=2, sticky=N+S+W+E)
        self.button_minus = Button(self, text="-", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("-")).grid(row=2, column=3, sticky=N+S+W+E)

        self.button_7 = Button(self, text="7", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("7")).grid(row=3, column=0, sticky=N+S+W+E)
        self.button_8 = Button(self, text="8", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("8")).grid(row=3, column=1, sticky=N+S+W+E)
        self.button_9 = Button(self, text="9", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("9")).grid(row=3, column=2, sticky=N+S+W+E)
        self.button_mul = Button(self, text="*", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("*")).grid(row=3, column=3, sticky=N+S+W+E)

        self.button_clc = Button(self, text="C", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("C")).grid(row=4, column=0, sticky=N+S+W+E)
        self.button_0 = Button(self, text="0", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("0")).grid(row=4, column=1, sticky=N+S+W+E)
        self.button_equ = Button(self, text="=", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("=")).grid(row=4, column=2, sticky=N+S+W+E)
        self.button_div = Button(self, text="/", font = ("Helvetica", 20, "bold"), bg = "#138FC2", command = lambda : self.buttonClick("/")).grid(row=4, column=3, sticky=N+S+W+E)
        

calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width = False, height=False)
calculator.mainloop()
