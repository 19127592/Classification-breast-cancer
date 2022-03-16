import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from sklearn.linear_model import LogisticRegression
import pandas as pd
from tkinter import ttk
brcc_df = pd.read_csv('data.csv')
brcc_df
root = Tk()
root.title('Graph')
root.geometry("700x400")





def file_new(): 
    frame1=Frame(root)
    frame1.pack(fill='both', expand=True)
    # myButton = Button(frame1, text="bar chart")
    myButton = Button(frame1, text="bar chart", command=lambda: barChart(variable.get(),printInputY(),printInputYX()))
    myButton.pack()
    # myButton.destroy()
    

my_menu=Menu(root)
root.config(menu=my_menu)
file_menu=Menu(my_menu)
my_menu.add_cascade(label='Data analytics',menu=file_menu)
file_menu.add_command(label='visualization',command=file_new)



def boxPlot(column,ylabel,xlabel):
    brcc_df.boxplot(['radius_mean'])  
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

def barChart(column,ylabel,xlabel):
    b = brcc_df[column].value_counts()
    plt.bar(b.keys(), b.values)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()




def statictis():
    listBox = ttk.Treeview(root)
    listBox.pack(fill=X)

    desc = brcc_df.describe()
    desc = desc.reset_index()

    listBox["column"] = list(desc.columns)
    listBox["show"] = "headings"

    for column in listBox["column"]:
        listBox.heading(column, text=column)
        listBox.column(column, anchor=CENTER)

    desc = brcc_df.describe().reset_index().to_numpy().tolist()
    for row in desc:
        listBox.insert("", "end", values=row)

s = Button(text="Statistic", command=statictis)
s.pack()

OPTIONS = [
    "diagnosis",
    "Feb",
    "Mar"
]


variable = StringVar(root)
variable.set(OPTIONS[0])  # default value

w = OptionMenu(root, variable, *OPTIONS)
w.pack()


def dropdown():
    print("value is:" + variable.get())


button = Button(root, text="OK", command=dropdown)
button.pack()


def printInputY():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text="Provided Input: "+inp)
    return inp

# TextBox Creation
inputtxt = Text(root, height=2, width=10)

inputtxt.pack()

# Button Creation
printButton = Button(root,text="Print",command=printInputY)
printButton.pack()

# Label Creation
lbl = Label(root, text="")
lbl.pack()

def printInputYX():
    inp = inputtxt1.get(1.0, "end-1c")
    lbl1.config(text="Provided Input: "+inp)
    return inp

# TextBox Creation
inputtxt1 = Text(root, height=2, width=10)

inputtxt1.pack()

# Button Creation
printButton1 = Button(root,text="Print",command=printInputYX)
printButton1.pack()

# Label Creation
lbl1 = Label(root, text="")
lbl1.pack()

def openWindows():
    top=Toplevel()
    top.title("Hello")
    
    def boxPlot():
        brcc_df.boxplot(['radius_mean'])  
        plt.ylabel('ylabel')
        plt.xlabel('xlabel')
        plt.show()
    display = Button(top,text="box",command=boxPlot)
    display.pack()  


display = Button(root,text="display",command=openWindows)
display.pack()  

root.mainloop()
