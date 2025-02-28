import tkinter as tk 
from tkinter import  Button,Text,END
import re
def intern():
    class Calculator:
        def __init__(self,master):
            self.master=master
            master.title("CodSoft Calculator")
            master.configure(bg='#cb464e')
            # creating the screen widget
            self.screen=Text(master,state='disabled',width=60,height=3,background="#fcfcec",foreground="#cb464e",font=("times",12,"bold"))
            # positioning the screen in window
            self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
            self.screen.configure(state='normal')
            self.equation=''
            # creating buttons(as shown on calculators)
            b1=self.createButton(7)
            b2=self.createButton(8)
            b3=self.createButton(9)
            b4=self.createButton(u"\u232B",None)
            b5=self.createButton(4)
            b6=self.createButton(5)
            b7=self.createButton(6)
            b8=self.createButton(u"\u00F7")
            b9=self.createButton(1)
            b10=self.createButton(2)
            b11=self.createButton(3)
            b12=self.createButton('*')
            b13=self.createButton('.')
            b14=self.createButton(0)
            b15=self.createButton('+')
            b16=self.createButton('-')
            b17=self.createButton('=',None,34)
            
            buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]
            # initalizing the counter
            count=0
            for row in range(1,5):
                for column in range(4):
                    buttons[count].grid(row=row,column=column)
                    count+=1
                    # '=' button should be arranged at the bottom
                    buttons[16].grid(row=5,column=0,columnspan=4)
        
        def createButton(self,val,write=True,width=7):
            return Button(self.master,text=val,command=lambda: self.click(val,write),width=width,background='#4b7fa4',foreground="#fcfcec",font=("times",20))
        def click(self,text,write):
            # if 'write' argument is true,means the 'val' should be written on screen,if none, it should not be written.
            if write == None:
                if text=='=' and self.equation:
                    self.equation=re.sub(u"\u00F7",'/',self.equation)
                    try:
                        answer=str(eval(self.equation))
                    except ZeroDivisionError:
                        answer = "Error"
                    except Exception:
                        answer="Error"
                    self.clear_screen()
                    self.insert_screen(answer,newline=True)
                elif text==u"\u232B":
                    self.clear_screen()
            else:
                # adding text to the screen
                self.insert_screen(text)
        def clear_screen(self):
            # in order to clear the screen ,equation must be set to empty before deleting screen
            self.equation=''
            self.screen.configure(state='normal')
            self.screen.delete('1.0',END)
        def insert_screen(self,value,newline=False):
            self.screen.configure(state='normal')
            self.screen.insert(END,value)
            # to record every value that is inserted on the screen
            self.equation+=str(value)
            self.screen.configure(state='disabled')
    root=tk.Tk()
    my_gui=Calculator(root)
    root.mainloop()
intern()

        