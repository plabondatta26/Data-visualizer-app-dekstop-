import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu,Toplevel,Button, DISABLED,Label

from tkinter.filedialog import askopenfile, asksaveasfile
import  pandas as pd
import matplotlib
from matplotlib import pyplot,style
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk, FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

matplotlib.use("TkAgg")
style.use("ggplot")
figure=Figure(figsize=(12,8),dpi=100)
axes=figure.add_subplot(111)

import  numpy as np
#import matplotlib.style as style
#import matplotlib.pyplot as plt

import random
def home():
    if visualize.state() == 'normal':
        visualize.withdraw()
        root = tk.Tk()
        MainApplication(root)

        # MenuBar



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


def FileProcessing(path):
    ext = path.split('.')[-1]
    global df
    if ext!=None:
        if ext == 'csv':
            df = pd.read_csv(path)
            visualizer = Button(root, text="Visualize", padx=12, pady=7, fg="white", bg="blue",
                                command=donothing)
            exit = Button(root, text="Exit", padx=10, pady=6, fg="white", bg="red", command=root.quit)
            return df

        elif ext == 'xlsx':
            df = pd.read_excel(path)

            visualizer = Button(root, text="Visualize", padx=12, pady=7, fg="white", bg="blue",
                                command=donothing)
            return df

        else:
            messagebox.showerror("File open", "File formate is not supported")
    else:
        return openFile()

def Saveimage():
    pass

def Data_in_column(x):
    element = ''
    FileProcessing(path)

    for i in range(len(df[[x]])):
        element = element + df.columns[i] + '\n'
    return element
def columnsButtonsApply():
    element =''
    FileProcessing(path)

    for i in range(len(df.columns)):
        element=element+df.columns[i]+'\n'
    return element
def columnsButtons():
    cB = textButton()
    global columnsButtton
    try:
        if text.state() == 'normal':
            columnsButtton.focus()
    except:
        text.withdraw()
        columnsButtton = Toplevel()
        FileProcessing(path)
        columnsButtton.iconphoto(False, tk.PhotoImage(file='icon.png'))
        columnsButtton.geometry('1280x768')
        columnsButtton.title("Data Visualizer")
        columnsButtton.configure(background='#0E2F47')
        label = tk.Label(columnsButtton, text="Columns in Dataset", font="calibri 16", bg='#0E2F47')
        label.pack()

        canvas = tk.Canvas(columnsButtton, bg="white", width=980, height=580, highlightthickness=0)
        canvas.pack()
        canvas_scroll = tk.Scrollbar(canvas, command=canvas.yview)
        canvas_scroll.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        canvas.configure(yscrollcommand=canvas_scroll.set, scrollregion=())


        column_names = tk.Label(canvas, text=columnsButtonsApply(), font="calibri 13", bg="white")
        canvas.create_window(33, 33, window=column_names, anchor=tk.NW)

def add_peer(peer):
    peers=[]
    if peers is None:
        peer=[]
    peers.append(peer)
def columnsValuesOk():
    global cvo

    try:
        if columnsValButton.state() =='normal':
            cvo.focas()
    except:
        columnsValButton.withdraw()
        cvo = Toplevel()
        FileProcessing(path)
        cvo.iconphoto(False, tk.PhotoImage(file='icon.png'))
        cvo.geometry('1280x768')
        cvo.title("Data Visualizer")
        cvo.configure(background='#0E2F47')


        x = comboCV1.get()
        y = comboCV2.get()
        #Data_in_column(x)
        #Data_in_column(y)
        label = tk.Label(cvo, text="Column Data in Dataset", font="calibri 16", bg='#0E2F47')
        label.pack()

        canvas = tk.Canvas(cvo, bg="white", width=450, height=1000, highlightthickness=0)

        #canvas_scroll = tk.Scrollbar(canvas, command=canvas.yview)
        #canvas_scroll.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        #canvas.configure(yscrollcommand=canvas_scroll.set, scrollregion=())

        canvas2 = tk.Canvas(cvo, bg="white", width=450, height=1000, highlightthickness=0)
        canvas.add_peer(canvas2)
        canvas.pack(side="left", fill="both", expand=True)
        canvas2.pack(side="left", fill="both", expand=True)
        #canvas_scroll2 = tk.Scrollbar(canvas2, command=canvas.yview)
        #canvas_scroll2.place(relx=1, rely=0, relheight=1, anchor=tk.NE)
        #canvas2.configure(yscrollcommand=canvas_scroll2.set, scrollregion=())
        if x !=None or y!=None:
            if y != None:
                column_data2 = tk.Label(canvas2, text=df[[y]], font="calibri 13", bg="white")
                canvas2.create_window(33, 33, window=column_data2, anchor=tk.NW)
            if x != None:
                column_data = tk.Label(canvas, text=df[[x]], font="calibri 13", bg="white")
                canvas.create_window(33, 33, window=column_data, anchor=tk.NW)
        else:
            messagebox.showerror("Selection Error", "Please select minimum one column first")
        print(df[[x]])
        print(df[[y]])

        #messagebox.showinfo("page not found", " This page is not completed")

def columnsValues():
    global columnsValButton
    try:
        if text.state() == 'normal':
            columnsValButton.focus()
    except:
        text.withdraw()
        columnsValButton = Toplevel()
        columnsValButton.iconphoto(False, tk.PhotoImage(file='icon.png'))
        columnsValButton.geometry('1280x768')
        columnsValButton.title("Data Visualizer")
        columnsValButton.configure(background='#0E2F47')
        dfList = []
        FileProcessing(path)
        for a in df.columns:
            dfList.append(a)
            #canvas = Canvas(columnsValButton, height=height_value / 2, width=width_value / 2 + 100 + 50)
        #canvas.grid()
        global comboCV1
        global comboCV2
        comboCV1 = ttk.Combobox(columnsValButton, values=dfList, width=25)
        comboCV1.set("select one")
        comboCV2 = ttk.Combobox(columnsValButton, values=dfList, width=25)
        comboCV1.set("select one")

        #comboCV3 = ttk.Combobox(columnsValButton, values=dfList, width=25, state=DISABLED)
        button = Button(columnsValButton, text="Done", padx=10, pady=6, fg="white", bg="blue", command=columnsValuesOk)

        comboCV1.grid()
        comboCV2.grid()
        #comboCV3.grid()
        button.grid()


def columnsAdditionsOk():
    ca=columnsAdditions()
    global  columnsAddOk
    try:
        if columnsAddition.state()=='normal':
            columnsAddOk.focus()
    except:
        columnsAddition.withdraw()
        columnsAddOk=Toplevel()
        FileProcessing(path)
        columnsAddOk.iconphoto(False, tk.PhotoImage(file='icon.png'))
        columnsAddOk.geometry('1280x768')
        columnsAddOk.title("Data Visualizer")
        columnsAddOk.configure(background='#0E2F47')


        comboCA1val = comboCA1.get()
        comboCA2val = comboCA2.get()
        #x = df[[comboCA1val]]
        #y = df[[comboCA2val]]
        """z=[]
        for x in df[[comboCA1val]]:
            for y in df[[comboCA2val]]:
                z.append(x+y)
        print(z)"""

def columnsAdditions():
    global columnsAddition
    try:
        if text.state() == 'normal':
            columnsAddition.focus()
    except:
        text.withdraw()
        columnsAddition = Toplevel()
        FileProcessing(path)
        columnsAddition.iconphoto(False, tk.PhotoImage(file='icon.png'))
        columnsAddition.geometry('1280x768')
        columnsAddition.title("Data Visualizer")
        columnsAddition.configure(background='#0E2F47')


        columnsAddition.iconphoto(False, tk.PhotoImage(file='icon.png'))
        #canvas = tk.Canvas(root, height=300, width=300, bg="pink")
        #canvas.pack()

        dfList = []
        for a in df.columns:
            dfList.append(a)
        global comboCA1
        global comboCA2
        comboCA1 = ttk.Combobox(columnsAddition, values=dfList, width=25)
        comboCA1.set("select one")
        comboCA2 = ttk.Combobox(columnsAddition, values=dfList, width=25)
        comboCA2.set("select one")
        comboCA3 = ttk.Combobox(columnsAddition, values=dfList, width=25, state=DISABLED)
        button = Button(columnsAddition, text="Done", padx=10, pady=6, fg="white", bg="blue", command=columnsAdditionsOk)

        comboCA1.grid()
        comboCA2.grid()
        comboCA3.grid()
        button.grid()




def PiechartOk():
    pc=Piechart()
    global pco
    try:
        if pie_chart.state()=='normal':
            pco.focus()
    except:
        pie_chart.withdraw()
        pco=Toplevel()
        FileProcessing(path)
        pco.iconphoto(False, tk.PhotoImage(file='icon.png'))
        pco.geometry('1280x768')
        pco.title("Data Visualizer")
        pco.configure(background='#0E2F47')
        types=combopie1.get()
        value=combopie2.get()
        x=df[types]
        y=df[value]
        explo_d = np.zeros(len(df[types]))
        if x.dtypes == object and y.dtypes == float or y.dtypes == int:
            axes.pie(y, labels=x, explode=explo_d, autopct='%1.1f%%', shadow=True, startangle=90)
            axes.grid()
        elif y.dtypes == object and x.dtypes == float or x.dtypes == int:
            axes.pie(x, labels=y, explode=explo_d, autopct='%1.1f%%', shadow=True, startangle=90)
            axes.grid()
        else:
            messagebox.showerror("Input Error","Select one 'String type' and other one 'Numerical type' colmun")
        canvas = FigureCanvasTkAgg(figure, master=pco)
        canvas.draw()
        graph_widget = canvas.get_tk_widget()
        graph_widget.grid()

def Piechart():
    sub_gb1 = graphButton()
    global pie_chart
    try:
        if gb.state() == 'normal':
            pie_chart.focas()
    except:
        gb.withdraw()
        pie_chart = Toplevel()
        dflist = []
        FileProcessing(path)
        pie_chart.iconphoto(False, tk.PhotoImage(file='icon.png'))
        pie_chart.geometry('1280x768')
        pie_chart.title("Data Visualizer")
        pie_chart.configure(background='#0E2F47')


        for a in df:
            dflist.append(a)
        global combopie1
        global combopie2
        combopie1 = ttk.Combobox(pie_chart, values=dflist, width=25)
        combopie1.set("Select one")
        combopie2 = ttk.Combobox(pie_chart, values=dflist, width=25)
        combopie2.set("Select one")
        combopie1.grid()
        combopie2.grid()

        button = Button(pie_chart, text='Ok', padx=12, pady=8, fg='white', bg='blue', command=PiechartOk)
        button.grid()
        save = Button(pie_chart, text="Save Image", padx=12, pady=8, fg='white', bg='blue',command=Saveimage)
        save.grid()


def BarChartOk():
    sp = Barchart()
    global bco
    try:
        if bar_chart.state() == 'normal':
            bco.focus()
    except:
        bar_chart.withdraw()
        bco = Toplevel()
        FileProcessing(path)
        bco.iconphoto(False, tk.PhotoImage(file='icon.png'))
        bco.geometry('1280x768')
        bco.title("Data Visualizer")
        bco.configure(background='#0E2F47')


        val1 = combobar1.get()
        val2 = combobar2.get()
        x = df[val1]
        y = df[val2]
        if x.dtypes==object and y.dtypes==float or y.dtypes==int:
            if len(x) < 15:
                axes.bar(x, y, color='b', align='center', alpha=0.5)
                axes.set_xlabel(val2, color="g")
                axes.set_ylabel(val1, color="g")
                axes.grid()
            else:
                axes.barh(x, y, color='b', align='center', alpha=0.5)
                axes.set_xlabel(val2, color="g")
                axes.set_ylabel(val1, color="g")
                axes.grid()
        elif y.dtypes==object and x.dtypes==float or x.dtypes==int:
            if len(x) < 15:
                axes.bar(x, y, color='b', align='center', alpha=0.5)
                axes.set_xlabel(val2, color="g")
                axes.set_ylabel(val1, color="g")
                axes.grid()
            else:
                axes.barh(x, y, color='b', align='center', alpha=0.5)
                axes.set_xlabel(val2, color="g")
                axes.set_ylabel(val1, color="g")
                axes.grid()
        else:
            messagebox.showerror("Input Error", "Select one 'String type' and other one 'Numerical type' colmun")
        canvas = FigureCanvasTkAgg(figure, master=bco)
        canvas.draw()
        graph_widget = canvas.get_tk_widget()
        graph_widget.grid()

def Barchart():
    sub_gb1 = graphButton()
    global bar_chart
    try:
        if gb.state() == 'normal':
            bar_chart.focas()
    except:
        gb.withdraw()
        bar_chart = Toplevel()
        dflist = []
        FileProcessing(path)
        bar_chart.iconphoto(False, tk.PhotoImage(file='icon.png'))
        bar_chart.geometry('1280x768')
        bar_chart.title("Data Visualizer")
        bar_chart.configure(background='#0E2F47')

        for a in df:
            dflist.append(a)
        global combobar1
        global combobar2
        combobar1 = ttk.Combobox(bar_chart, values=dflist, width=25)
        combobar1.set("Select one")
        combobar2 = ttk.Combobox(bar_chart, values=dflist, width=25)
        combobar2.set("Select one")
        combobar1.grid()
        combobar2.grid()

        button = Button(bar_chart, text='Ok', padx=12, pady=8, fg='white', bg='blue', command=BarChartOk)
        button.grid()



def ScatterplotOk():
    sp=Scatterplot()
    global spo
    try:
        if scatter_plot.state()=='normal':
            spo.focus()
    except:
        scatter_plot.withdraw()
        spo=Toplevel()
        FileProcessing(path)
        spo.iconphoto(False, tk.PhotoImage(file='icon.png'))
        spo.geometry('1280x768')
        spo.title("Data Visualizer")
        spo.configure(background='#0E2F47')

        val1=combomsc1.get()
        val2=combomsc2.get()
        x = df[val1]
        y = df[val2]
        if x.dtypes == object and y.dtypes == float or y.dtypes == int:
            if len(x) < 15:
                axes.scatter(x, y, marker='s', color='b')
                axes.set_xlabel(val1, color="g")
                axes.set_ylabel(val2, color="g")
                axes.grid()
            else:
                axes.scatter(y, x, marker='s', color='b')
                axes.set_xlabel(val2, color="g")
                axes.set_ylabel(val1, color="g")
                axes.grid()
        canvas=FigureCanvasTkAgg(figure,master=spo)
        canvas.draw()
        graph_widget=canvas.get_tk_widget()
        graph_widget.grid()

def Scatterplot():
    sub_gb = graphButton()
    global scatter_plot
    try:
        if gb.state()== 'normal':
            scatter_plot.focas()
    except:
        gb.withdraw()
        scatter_plot = Toplevel()
        dflist = []
        FileProcessing(path)
        scatter_plot.iconphoto(False, tk.PhotoImage(file='icon.png'))
        scatter_plot.geometry('1280x768')
        scatter_plot.title("Data Visualizer")
        scatter_plot.configure(background='#0E2F47')


        for a in df:
            dflist.append(a)
        global combomsc1
        global combomsc2
        combomsc1 = ttk.Combobox(scatter_plot, values=dflist, width=25)
        combomsc1.set("Select one")
        combomsc2 = ttk.Combobox(scatter_plot, values=dflist, width=25)
        combomsc2.set("Select one")
        combomsc1.grid()
        combomsc2.grid()
        button=Button(scatter_plot,text='Ok',padx=12,pady=8,fg='white',bg='blue',command=ScatterplotOk)
        button.grid()

def LinechartokBack():
    global linechart

    if lco.state() == 'normal':
        lco.withdraw()
        linechart = Toplevel()

        FileProcessing(path)
        linechart.iconphoto(False, tk.PhotoImage(file='icon.png'))
        linechart.geometry('1280x768')
        linechart.title("Data Visualizer")
        linechart.configure(background='#0E2F47')
        linechart.configure(background='#0E2F47')

        # MenuBar
        menubar = Menu(linechart)
        back = Menu(menubar, tearoff=0)
        back.add_command(label="back", command=LineBack)
        menubar.add_cascade(label="<-- Back", menu=back)

        homeMenu = Menu(menubar, tearoff=0)
        homeMenu.add_command(label="Go to home", command=home)
        menubar.add_cascade(label="Home", menu=homeMenu)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        linechart.config(menu=menubar)

        # Sidebar

        text = tk.Button(linechart, bg='#191E31', width=25, text="Text Visualization", fg="white",
                         command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(linechart, bg='#191E31', width=25, text="Graph Visualization", fg="white",
                          command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        BackButton = tk.Button(linechart, bg='#191E31', width=25, text="Back", fg="white", command=LineBack)
        BackButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        exitButton = tk.Button(linechart, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=4, rowspan=1, sticky="ne")

        # properties
        linlabel = Label(linechart, text="Linechart data selection")
        # ok = Button(linechart, text="Ok", padx=12, pady=8, fg="white", bg="blue", command=linechart.quit)
        dfList = []
        for a in df.columns:
            dfList.append(a)
        global comboLine1
        global comboLine2
        comboLine1 = ttk.Combobox(linechart, values=dfList, width=25)
        comboLine1.set("Select One")
        comboLine2 = ttk.Combobox(linechart, values=dfList, width=25)
        comboLine2.set("Select One")
        ok = Button(linechart, text="Ok", padx=12, pady=8, fg="white", bg="blue", command=LinechartOk)
        linlabel.grid()
        comboLine1.grid()
        comboLine2.grid()
        ok.grid()


def LinechartOk():
    Lc=Linechart()
    global lco
    try:

        if linechart.state()=='normal':
            lco.focus()
    except:
        linechart.withdraw()
        lco=Toplevel()
        lco.iconphoto(False, tk.PhotoImage(file='icon.png'))
        lco.geometry('1280x768')
        lco.title("Data Visualizer")
        lco.configure(background='#0E2F47')


        lineokLabel=Label(lco,text="Line Chart")
        val1 = comboLine1.get()
        val2 = comboLine2.get()
        x = df[val1]
        y = df[val2]

        if len(x) < 15:
            axes.plot(x, y, marker='o', color='b')
            axes.set_xlabel(val1, color="g")
            axes.set_ylabel(val2, color="g")
            axes.grid()
        else:
            axes.plot(y, x, marker='o', color='b')
            axes.set_xlabel(val2, color="g")
            axes.set_ylabel(val1, color="g")
            axes.grid()

        linecanvas = FigureCanvasTkAgg(figure, master=lco)
        linecanvas.draw()
        graph_widget = linecanvas.get_tk_widget()
        graph_widget.grid()

def LineBack():
    global gb
    #global linechart
    if linechart.state() == 'normal':
        linechart.withdraw()
        gb = Toplevel()
        gb.iconphoto(False, tk.PhotoImage(file='icon.png'))
        gb.geometry('1280x768')
        gb.title("Data Visualizer")
        gb.configure(background='#0E2F47')

    # MenuBar
        menubar = Menu(gb)
        back = Menu(menubar, tearoff=0)
        back.add_command(label="back", command=graphBack)
        menubar.add_cascade(label="<-- Back", menu=back)

        homeMenu = Menu(menubar, tearoff=0)
        homeMenu.add_command(label="Go to home", command=home)
        menubar.add_cascade(label="Home", menu=homeMenu)  # ,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        gb.config(menu=menubar)

        # Sidebar
        text = tk.Button(gb, bg='#191E31', width=25, text="Text Visualization", fg="white", command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(gb, bg='#191E31', width=25, text="Graph Visualization", fg="white",
                          command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        BackButton = tk.Button(gb, bg='#191E31', width=25, text="Back", fg="white", command=graphBack)
        BackButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        exitButton = tk.Button(gb, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=4, rowspan=1, sticky="ne")

        # properties
        gbLabel = Label(gb, text="Choose Graph type")

        lineChart = Button(gb, text='Line Chart', padx=12, pady=8, fg='white', bg='blue', comman=Linechart)
        scatter = Button(gb, text='Scatter Plot', padx=12, pady=8, fg='white', bg='blue', command=Scatterplot)
        barChart = Button(gb, text='Bar Chart', padx=12, pady=8, fg='white', bg='blue', command=Barchart)
        pieChart = Button(gb, text='Pie Chart', padx=12, pady=8, fg='white', bg='blue', command=Piechart)
        gbLabel.grid(column=3, row=1, rowspan=1, sticky="nw")
        lineChart.grid(column=3, row=3, rowspan=1, sticky="ns")
        scatter.grid(column=3, row=4, rowspan=1, sticky="ns")
        barChart.grid(column=3, row=5, rowspan=1, sticky="ns")
        pieChart.grid(column=3, row=6, rowspan=1, sticky="ns")
        return gb


def Linechart():

    global linechart
    try:
       if gb.state()=='normal':
           linechart.focus()
    except:
        gb.withdraw()
        linechart = Toplevel()

        FileProcessing(path)
        linechart.iconphoto(False, tk.PhotoImage(file='icon.png'))
        linechart.geometry('1280x768')
        linechart.title("Data Visualizer")
        linechart.configure(background='#0E2F47')
        linechart.configure(background='#0E2F47')

        # MenuBar
        menubar = Menu(linechart)
        back = Menu(menubar, tearoff=0)
        back.add_command(label="back", command=LineBack)
        menubar.add_cascade(label="<-- Back", menu=back)

        homeMenu = Menu(menubar, tearoff=0)
        # home_button= Button(homeMenu, text= "Home" command=home(visualize, root))
        homeMenu.add_command(label="Go to home", command=home)
        menubar.add_cascade(label="Home", menu=homeMenu)  # ,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        linechart.config(menu=menubar)

        # Sidebar

        text = tk.Button(linechart, bg='#191E31', width=25, text="Text Visualization", fg="white", command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(linechart, bg='#191E31', width=25, text="Graph Visualization", fg="white",
                          command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        BackButton = tk.Button(linechart, bg='#191E31', width=25, text="Back", fg="white", command=LineBack)
        BackButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        exitButton = tk.Button(linechart, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=4, rowspan=1, sticky="ne")

    # properties
        linlabel=Label(linechart,text="Linechart data selection")
        #ok = Button(linechart, text="Ok", padx=12, pady=8, fg="white", bg="blue", command=linechart.quit)
        dfList = []
        for a in df.columns:
            dfList.append(a)
        global comboLine1
        global comboLine2
        comboLine1 = ttk.Combobox(linechart, values=dfList, width=25)
        comboLine1.set("Select One")
        comboLine2 = ttk.Combobox(linechart, values=dfList, width=25)
        comboLine2.set("Select One")
        ok = Button(linechart, text="Ok", padx=12, pady=8, fg="white", bg="blue",command=LinechartOk)
        linlabel.grid()
        comboLine1.grid()
        comboLine2.grid()
        ok.grid()


def textBack( ):
    global visualize
    global text
    if text.state() == 'normal':
        text.withdraw()

        visualize = Toplevel()

        # UI
        visualize.iconphoto(False, tk.PhotoImage(file='icon.png'))
        visualize.geometry('1280x768')
        visualize.title("Data Visualizer")
        visualize.configure(background='#0E2F47')
        visualize.grid_rowconfigure(20, weight=2)
        # main=tk.Tk()
        # MenuBar

        menubar = Menu(visualize)
        back = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="<-- Back", menu=back, command=visualizeButtonBack)

        homeMenu = Menu(menubar, tearoff=0)
        # home_button= Button(homeMenu, text= "Home" command=home(visualize, root))
        homeMenu.add_command(label="Go to home")  # ,command=home(visualize))
        menubar.add_cascade(label="Home", menu=homeMenu)  # ,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        visualize.config(menu=menubar)

        # Sidebar

        text = tk.Button(visualize, bg='#191E31', width=25, text="Text Visualization", fg="white", command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(visualize, bg='#191E31', width=25, text="Graph Visualization", fg="white", command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        BackButton = tk.Button(visualize, bg='#191E31', width=25, text="Back", fg="white", command=textBack)
        BackButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        exitButton = tk.Button(visualize, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=4, rowspan=1, sticky="ne")

    return visualize
def textButton():
    global text
    try:
        if visualize.state() == 'normal':
            text.focus()
    except:
        visualize.withdraw()
        text = Toplevel()
        text.iconphoto(False, tk.PhotoImage(file='icon.png'))
        text.geometry('1280x768')
        text.title("Data Visualizer")
        text.configure(background='#0E2F47')
        text.grid_rowconfigure(20, weight=2)

        # MenuBar
        menubar = Menu(text)
        back = Menu(menubar, tearoff=0)
        back.add_command(label="back", command=textBack)
        menubar.add_cascade(label="<-- Back", menu=back)

        homeMenu = Menu(menubar, tearoff=0)
        # home_button= Button(homeMenu, text= "Home" command=home(visualize, root))
        homeMenu.add_command(label="Go to home", command=home)
        menubar.add_cascade(label="Home", menu=homeMenu)  # ,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        text.config(menu=menubar)

        # Sidebar


        BackButton = tk.Button(text, bg='#191E31', width=25, text="Back", fg="white", command=textBack)
        BackButton.grid(column=0, row=1, rowspan=1, sticky="ne")

        exitButton = tk.Button(text, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=2, rowspan=1, sticky="ne")

    # properties
        label = Label(text, text="Choose Analysis type")

        columns = Button(text, text="Columns", padx=12, pady=8, fg="white", bg="blue", command=columnsButtons)
        columnsvalue = Button(text, text="Data of Columns", padx=12, pady=8, fg="white", bg="blue", command=columnsValues)
        columnsAddition = Button(text, text="Columns Addition", padx=12, pady=8, fg="white", bg="blue", command=columnsAdditions)

        label.grid(column=3, row=1, rowspan=1 )
        columns.grid(column=3, row=3, rowspan=1)
        columnsvalue.grid(column=3, row=4, rowspan=1)
        columnsAddition.grid(column=3, row=5, rowspan=1)
        return text


def graphBack( ):
    global visualize

    if gb.state() == 'normal':
        gb.withdraw()
        visualize = Toplevel()

        # UI
        visualize.iconphoto(False, tk.PhotoImage(file='icon.png'))
        visualize.geometry('1280x768')
        visualize.title("Data Visualizer")
        visualize.configure(background='#0E2F47')
        visualize.grid_rowconfigure(20, weight=2)
        # main=tk.Tk()
        # MenuBar

        menubar = Menu(visualize)
        back = Menu(menubar, tearoff=0)
        # back= Button(backm, text= "Back",command=Back )
        # back.add_command(label="back", command=Back)
        menubar.add_cascade(label="<-- Back", menu=back, command=visualizeButtonBack)

        homeMenu = Menu(menubar, tearoff=0)
        # home_button= Button(homeMenu, text= "Home" command=home(visualize, root))
        homeMenu.add_command(label="Go to home")  # ,command=home(visualize))
        menubar.add_cascade(label="Home", menu=homeMenu)  # ,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        visualize.config(menu=menubar)

        # Sidebar

        text = tk.Button(visualize, bg='#191E31', width=25, text="Text Visualization", fg="white",
                         command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(visualize, bg='#191E31', width=25, text="Graph Visualization", fg="white",
                          command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        exitButton = tk.Button(visualize, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        return visualize
def graphButton():

    global gb
    try:
        if visualize.state() == 'normal':
            gb.focus()
    except:
        visualize.withdraw()
        gb = Toplevel(root)
        gb.iconphoto(False, tk.PhotoImage(file='icon.png'))
        gb.geometry('1280x768')
        gb.title("Data Visualizer")
        gb.configure(background='#0E2F47')

        # MenuBar
        menubar = Menu(gb)
        back = Menu(menubar, tearoff=0)
        back.add_command(label="back", command=graphBack)
        menubar.add_cascade(label="<-- Back", menu=back)

        homeMenu = Menu(menubar, tearoff=0)
        # home_button= Button(homeMenu, text= "Home" command=home(visualize, root))
        homeMenu.add_command(label="Go to home", command=home)
        menubar.add_cascade(label="Home", menu=homeMenu)  # ,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        gb.config(menu=menubar)

        # Sidebar

        text = tk.Button(gb, bg='#191E31', width=25, text="Text Visualization", fg="white", command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(gb, bg='#191E31', width=25, text="Graph Visualization", fg="white",
                          command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        BackButton = tk.Button(gb, bg='#191E31', width=25, text="Back", fg="white", command=graphBack)
        BackButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        exitButton = tk.Button(gb, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=4, rowspan=1, sticky="ne")

        gbLabel=Label(gb,text="Choose Graph type")

        lineChart = Button(gb, text='Line Chart', padx=12, pady=8, fg='white', bg='blue', comman=Linechart)
        scatter = Button(gb, text='Scatter Plot', padx=12, pady=8, fg='white', bg='blue', command=Scatterplot)
        barChart = Button(gb, text='Bar Chart', padx=12, pady=8, fg='white', bg='blue',command=Barchart)
        pieChart = Button(gb, text='Pie Chart', padx=12, pady=8, fg='white', bg='blue', command=Piechart)
        gbLabel.grid(column=3, row=1, rowspan=1, sticky="nw")
        lineChart.grid(column=3, row=3, rowspan=1, sticky="ns")
        scatter.grid(column=3, row=4, rowspan=1, sticky="ns")
        barChart.grid(column=3, row=5, rowspan=1, sticky="ns")
        pieChart.grid(column=3, row=6, rowspan=1, sticky="ns")

        return gb

def visualizeButtonBack( ):

    if visualize.state()=='normal':
        visualize.withdraw()
        root = tk.Tk()
        MainApplication(root)
def visualizeButton():
    global visualize
    try:
        if root.state() == "normal":
            visualize.focus()
    except:
        root.withdraw()
        visualize = Toplevel()

    #UI
        visualize.iconphoto(False, tk.PhotoImage(file='icon.png'))
        visualize.geometry('1280x768')
        visualize.title("Data Visualizer")
        visualize.configure(background='#0E2F47')
        visualize.grid_rowconfigure(20, weight=2)

        # MenuBar

        menubar = Menu(visualize)
        back = Menu(menubar, tearoff=0)
        #bback= Button(back, text= "Back",command=visualizeButtonBack )
        back.add_command(label="back", command=visualizeButtonBack)
        menubar.add_cascade(label="<-- Back", menu=back, command= visualizeButtonBack)

        homeMenu = Menu(menubar, tearoff=0)
        #home_button= Button(homeMenu, text= "Home" command=home(visualize, root))
        homeMenu.add_command(label="Go to home",command=home)
        menubar.add_cascade(label="Home", menu=homeMenu)#,command= openFile)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=openFile)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Close")
        menubar.add_cascade(label="File", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        visualize.config(menu=menubar)

        # Sidebar

        text = tk.Button(visualize, bg='#191E31', width=25, text="Text Visualization", fg="white", command=textButton)
        text.grid(column=0, row=1, rowspan=1, sticky="ne")

        graph = tk.Button(visualize, bg='#191E31', width=25, text="Graph Visualization", fg="white", command=graphButton)
        graph.grid(column=0, row=2, rowspan=1, sticky="ne")

        exitButton = tk.Button(visualize, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
        exitButton.grid(column=0, row=4, rowspan=1, sticky="ne")
        BackButton = tk.Button(visualize, bg='#191E31', width=25, text="Back", fg="white", command=visualizeButtonBack)
        BackButton.grid(column=0, row=3, rowspan=1, sticky="ne")

        return visualize


def openFile():
    messagebox.showinfo("File opening", 'Select a file to visualize...')
    global path
    extention = (('csv', '*.csv'), ('Excel', '*.xlsx'))
    # extention1 = []
    path = askopenfile(initialdir="~", title='Select a file', filetypes=extention).name
    if path == None:
        messagebox.showerror("File open failed", "open a file first...")

def donothing():
    pass
    global path



def MainApplication(root):
    root.geometry('1280x768')
    root.title('Data Visualizer')
    root.configure(background='#0E2F47')
    root.grid_rowconfigure(20, weight=2)


#MenuBar

    menubar = Menu(root)
    homeMenu = Menu(menubar, tearoff=0)
    homeMenu.add_command(label="Go to home", command=donothing)
    menubar.add_cascade(label="Home", menu=homeMenu)



    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=openFile)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Close")
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

#Sidebar

    Visualize = tk.Button(root, bg='#191E31', width=25, text="Visualize", fg="white", command =visualizeButton)
    Visualize.grid(column=0, row=1, rowspan=1, sticky="ne")



    settingButton = tk.Button(root, bg='#191E31', width=25, text="Setting", fg="white")
    settingButton.grid(column=0, row=4, rowspan=1,  sticky="ne")

    userGuideButton = tk.Button(root, bg='#191E31', width=25, text="User Guide", fg="white")
    userGuideButton.grid(column=0, row=5,  rowspan=1, sticky="ne")

    about_usButton = tk.Button(root, bg='#191E31', width=25, text="About us", fg="white")
    about_usButton.grid(column=0, row=6, rowspan=1,sticky="ne" )

    exitButton = tk.Button(root, bg='#191E31', width=25, text="Exit", fg="white", command=on_closing)
    exitButton.grid(column=0, row=7, rowspan=1,sticky="ne")


if __name__ == "__main__":
    root= tk.Tk()
    MainApplication(root)
    root.mainloop()