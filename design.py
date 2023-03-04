import tkinter as tk
from tkinter import *
import random
# from combopicker import Combopicker
from tkinter import ttk
import easygui as g
from firework import *

class Design:
    def __init__(self,master,main):
        self.root = master
        self.main = main
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.num3 = StringVar()
        self.num4 = StringVar()
        self.num5 = StringVar()
        self.num6 = StringVar()
        # self.yanhua = []
        self.draw_design()



    def draw_design(self):
        Label(self.root, text="Choose to mix ", font=('Times New Roman', 18, 'bold','italic','underline')).grid(row=0)
        Label(self.root, text="Sr :", font=('Times New Roman', 15, 'bold','italic'),foreground='red').grid(row=1)
        Label(self.root, text="Cu :", font=('Times New Roman', 15,'bold','italic'),foreground='green').grid(row=2)
        Label(self.root, text="Na :", font=('Times New Roman', 15, 'bold','italic'),foreground='orange').grid(row=3)
        Label(self.root, text="K :", font=('Times New Roman', 15,'bold','italic'),foreground='purple').grid(row=4)
        Label(self.root, text="Height :", font=('Times New Roman', 16, 'bold','italic')).grid(row=5)
        Label(self.root, text="Location :", font=('Times New Roman', 16, 'bold','italic')).grid(row=6)
        Entry(self.root, textvariable=self.num1, width=5, justify='center').grid(row=1, column=1, padx=1, pady=1)
        Entry(self.root, textvariable=self.num2, width=5, justify='center').grid(row=2, column=1, padx=1, pady=1)
        Entry(self.root, textvariable=self.num3, width=5, justify='center').grid(row=3, column=1, padx=1, pady=1)
        Entry(self.root, textvariable=self.num4, width=5, justify='center').grid(row=4, column=1, padx=1, pady=1)
        Entry(self.root, textvariable=self.num5, width=5, justify='center').grid(row=5, column=1, padx=1, pady=1)
        Entry(self.root, textvariable=self.num6, width=5, justify='center').grid(row=6, column=12, padx=1, pady=1)
        Label(self.root, text="%").grid(row=1, column=2, padx=1, pady=1)
        Label(self.root, text="%").grid(row=2, column=2, padx=1, pady=1)
        Label(self.root, text="%").grid(row=3, column=2, padx=1, pady=1)
        Label(self.root, text="%").grid(row=4, column=2, padx=1, pady=1)
        Label(self.root, text="%").grid(row=5, column=2, padx=1, pady=1)
        Label(self.root, text="%").grid(row=6, column=13, padx=1, pady=1)
        Label(self.root, text="Model :", font=('Times New Roman', 15, 'bold'),foreground='blue').grid(row=7)
        # global COMBOPICKER
        def fun(event):
            global pos_choice
            pos_choice = c.get()
        c = ttk.Combobox(self.root, values=['random','determination'])
        c.bind("<<ComboboxSelected>>", fun)
        c.grid(row=6, column=1,columnspan=10)
        cbox = ttk.Combobox(self.root, values=['Common','Rekindle','Sunflower','Fountain','Rotation'])
        cbox.grid(row=7, column=1,columnspan=10)
        def func(event):
            global model
            model = cbox.get()
            print(f"Model:{cbox.get()}")
        cbox.bind("<<ComboboxSelected>>", func)
        Button(self.root, text="OK",width=6, command=self.show).grid(row=8,column=2)
        Button(self.root, text="Save",width=6, command=lambda: self.baocun(indexf)).grid(row=9, column=2)
        Button(self.root, text="Delete",width=6, command=lambda: self.sheqi(indexf)).grid(row=9, column=3)



    def show(self):
        print(f"锶:{self.num1.get()},铜:{self.num2.get()},钠:{self.num3.get()},钾:{self.num4.get()}")
        n1 = float(self.num1.get())
        n2 = float(self.num2.get())
        n3 = float(self.num3.get())
        n4 = float(self.num4.get())
        n5 = float(self.num5.get())

        if n1+n2 == 0:
            if n1 + n2 + n3 == 0:
                color_rgb = (255, 0, 255)
            else:
                n3 = n3/100
                r = round(255-(255-255))*(1-n3)
                g = round(255-(255-0))*(1-n3)
                b = round(0-(0-255))*(1-n3)
                color_rgb = (r, g, b)
        else:
            r1 = round(255-(255-0)*(1-n1/(n1+n2)))
            g1 = round(0-(0-255)*(1-n1/(n1+n2)))
            b1 = round(0-(0-0)*(1-n1/(n1+n2)))
            r2 = round(r1-(r1-255)*(1-(n1+n2)/(n1+n2+n3)))
            g2 = round(g1-(g1-255)*(1-(n1+n2)/(n1+n2+n3)))
            b2 = round(b1-(b1-0)*(1-(n1+n2)/(n1+n2+n3)))
            r = round(r2-(r2-255)*(1-(n1+n2+n3)/(n1+n2+n3+n4)))
            g = round(g2-(g2-0)*(1-(n1+n2+n3)/(n1+n2+n3+n4)))
            b = round(b2-(b2-255)*(1-(n1+n2+n3)/(n1+n2+n3+n4)))
            color_rgb = (r,g,b)
        print(f"混合颜色:{color_rgb}")
        height = round((n5/100)*self.main.canvasHeight)
        print(f"烟花燃放高度:{height}")
        if pos_choice == 'determination':
            n6 = float(self.num6.get())
            width = round((n6/100)*self.main.WIDTH)
        if pos_choice == 'random':
            width = random.randint(0,self.main.WIDTH)
        print(f"烟花燃放位置:{width}")
        print('\n')
        f = Firework(color_rgb,width,height,model)
        self.main.FireworkContainer.append(f)
        global indexf
        indexf = self.main.FireworkContainer.index(f)



    def baocun(self,num):
        for i in range(num+1):
            def handler(event):

                g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(self.main.FireworkContainer[n].color,self.main.FireworkContainer[n].height,self.main.FireworkContainer[n].width,self.main.FireworkContainer[n].model)),title='显示烟花信息')

            l = Label(self.root, text="Firework" + str(i + 1), font=('宋体', 11, 'italic'))
            l.place(x=80*i, y=330)
            # n = round(l.winfo_x() / 50)
            # self.yanhua.append(n)
            # print(l.place_info())
            # l.bind('<ButtonRelease-1>', handler)





    def sheqi(self,num):
        self.main.FireworkContainer.remove(self.main.FireworkContainer[num])
        Label(self.root, text="                  ").place(x=80*num, y=330)






# win = Tk()
# win.title('烟花设计窗口')
# win.geometry('350x700')

# win.mainloop()








