from tkinter import *
import tkinter.filedialog

class TkDemo:
    # master = None

    def __init__(self):
        print("init")
        global root
        root = Tk()
        root.title("TK leaning")
        root.geometry("600x400")
        root.resizable(width=True,height=False)

        self.start()

        root.mainloop()


    def start(self):
        print("")
        self.createLabel()
        self.createTextField()
        # self.openFileChoose()
        self.layout()

        self.createMenu()

    def createMenu(self):
        menu = Menu(root)
        root.config(menu=menu)
        # menu.pack()

        filemenu = Menu(menu,tearoff=0)
        menu.add_cascade(label="文件",menu=filemenu)
        filemenu.add_command(label="新建...",command=self.newfile)

    def createLabel(self):
        label = Label(root, text="Label", bg="pink", font=("Arial", 12), width=8, height=3)
        label.pack(side=LEFT)


    def createTextField(self):
        var = Variable()
        var.set("Entry")
        textfield = Entry(root,textvariable=var)
        textfield.pack()

    def openFileChoose(self):
        # filename = tkinter.filedialog.askopenfilename(filetypes=[("bmp格式","bmp")]) #文件
        filename = tkinter.filedialog.askdirectory() #文件夹
        print(filename)

    def layout(self):
        frame = Frame(root)
        button = Button(frame,text="Top")
        button.pack(side = TOP,anchor=W,fill=X,expand=YES)

        button1 = Button(frame, text="Center")
        button1.pack(side=TOP, anchor=W, fill=X, expand=YES)

        frame.pack(side=LEFT,fill=BOTH,expand=YES)

    def newfile(self):
        print("")



