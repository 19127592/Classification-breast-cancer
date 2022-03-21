from tkinter import font
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import numpy as np
from tkinter import *
from sklearn.linear_model import LogisticRegression
import pandas as pd
from tkinter import ttk
import tkinter
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import statsmodels.api as sm
import statsmodels.formula.api as smf


root = Tk()
root.title('Project 2')
root.geometry("720x650")
root.resizable(0, 0)

brcc_df = pd.read_csv('modified_data.csv')
brcc_df
cols_remove = ['compactness_mean','fractal_dimension_mean','smoothness_se']
brcc_df2 = brcc_df.drop(cols_remove, axis=1)
brcc_df2

def barPlot():
    
    fig,ax= plt.subplots()
    b = brcc_df['diagnosis'].value_counts()
    ax.bar(b.keys(), b.values)
    plt.ylabel("Sô lượng")
    plt.xlabel('Chẩn đoán')
    for p in ax.containers:
        ax.bar_label(p, fmt='%.f', label_type='edge',fontsize=10)
    plt.show()

def boxPlot():  
    top = Toplevel()
    top.title(combo_data.get()+' boxplot')
    
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).boxplot(brcc_df[combo_data.get()])
  
    canvas = FigureCanvasTkAgg(fig, master=top)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, top)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    
def histPlot():  
    top = Toplevel()
    top.title(combo_data.get()+' histplot')
    
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).hist(brcc_df[combo_data.get()])
  
    canvas = FigureCanvasTkAgg(fig, master=top)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, top)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def heatPlot():
    corr = brcc_df.corr().round(2)
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    f, ax = plt.subplots(figsize=(20, 20))

    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, cbar_kws={"shrink": 0.5}, annot=True)

    plt.show()
def statictis():
    desc=brcc_df[combo_data.get()].describe().reset_index().to_numpy().tolist()
    for row in desc:
        my_tree_data.insert(parent="", index="end", text="", values=row)    
        
def remove_all():
    for record in my_tree_data.get_children():
        my_tree_data.delete(record)
    


my_menu=Menu(root)
root.config(menu=my_menu)
my_notebook = ttk.Notebook(root)
# tabs.grid(row=0, column=0, sticky='nsew')
my_notebook.pack(fill='both')

Data_frame = Frame(root,width=1000,height=1000)
Class_frame = Frame(root,width=1000,height=1000)

Data_frame.pack(fill='both',expand=1)
Class_frame.pack(fill='both',expand=1)

my_notebook.add(Data_frame,text='Data Analytics')
my_notebook.add(Class_frame,text='Classification')

lbl1 = Label(Data_frame,text='Vẽ biểu đồ cho mô hình',font=('Arial',30,'bold')).pack(pady=10)

Label(Data_frame,text="Chọn thuộc tính",font=('Helvetica', 10, 'bold')).place(x=300, y=80)

#bảng data
option1 = list(brcc_df.columns[1:])

combo_data = ttk.Combobox(Data_frame,value=option1)
combo_data.current(0)
combo_data.place(x=300,y=105)

box_chart_btn = Button(Data_frame,text='Create Boxplot',command=boxPlot)

box_chart_btn.place(x=90, y=145)

hist_chart_btn = Button(Data_frame,text='Create Histplot',command=histPlot)
hist_chart_btn.place(x=210, y=145)

heat_chart_btn = Button(Data_frame,text='Create Heatplot',command=heatPlot)
heat_chart_btn.place(x=420, y=145)

bar_chart_btn = Button(Data_frame,text='Create Barplot',command=barPlot)
bar_chart_btn.place(x=535, y=145)

statistic_btn = Button(Data_frame,text='Show Statictis ',command=statictis)
statistic_btn.place(x=320, y=195)

my_tree_data = ttk.Treeview(Data_frame)
my_tree_data.pack(side=BOTTOM,fill=X)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial',10,'bold'))

remove_btn = Button(Data_frame,text='Remove All ',command=remove_all)
remove_btn.pack(side=BOTTOM)

my_tree_data['columns']=('Statictis','Value')

my_tree_data.column('#0',width=0,stretch=NO)
my_tree_data.column('Statictis',anchor=W,width=120)
my_tree_data.column('Value',anchor=W, width=120)

my_tree_data.heading('#0',text='',anchor=W)
my_tree_data.heading('Statictis',text='Statictis',anchor=CENTER)
my_tree_data.heading('Value',text='Value',anchor=CENTER)


#bảng classification

def predictModel():
    X = brcc_df2
    y = brcc_df2['diagnosis']
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=40)
    cols = brcc_df2.columns.drop('diagnosis')
    formula = 'diagnosis ~ ' + ' + '.join(cols)

    logistic_fit = smf.glm(formula=formula, data=X_train, family=sm.families.Binomial()).fit()
    
    input_pre = pd.Series([float(e0.get()),float(e1.get()),float(e2.get()),float(e3.get()),float(e4.get())
                           ,float(e5.get()),float(e6.get()),float(e7.get()),float(e8.get())],index=brcc_df2.columns.drop('diagnosis'))
    prediction = logistic_fit.predict(input_pre)
    predictions_nominal = [ "M" if x < 0.5 else "B" for x in prediction]
    if predictions_nominal=='B':
        predictions_nominal='Chẩn đoán mô vú: LÀNH TÍNH (benign)'
    else:
        predictions_nominal='Chẩn đoán mô vú: ÁC TÍNH (malignant)'
    label = Label(Class_frame,text=predictions_nominal,font=('Arial',15,'bold'))
    label.pack()






lbl2 = Label(Class_frame,text='Dự đoán mô hình',font=('Arial',30,'bold')).pack(pady=10)

title = Label(Class_frame,text='Nhập các giá trị đầu vào',font=('Arial',12,'bold')).pack(pady=10)

option2 = list(brcc_df2.columns[1:])


for x in range(0, 9):
    globals()['l%s' % x] = Label(Class_frame,text=option2[x]).pack()
    globals()['e%s' % x] = Entry(Class_frame)
    globals()['e%s' % x].pack()

predict_model_btn = Button(Class_frame,text='Predict Model',command=predictModel)
predict_model_btn.pack(pady=10)

root.mainloop()