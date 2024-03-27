from tkinter import  ttk,Tk
from tkinter import *
# from tkinter.ttk import _Padding
# from typing import Any, Optional, Tuple, Union
# from typing_extensions import Literal
from PIL import ImageTk,Image
import tkinter as tk
import customtkinter
import pymysql
import copy
import random
import threading 
import multiprocessing
# import 


class sc(tk.Tk):
    print("helo")
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  
        self.main_frame = tk.Frame(self,bg='black')     
        self.main_frame.pack(side='top',fill='both',expand=True)
        self.main_frame.grid_rowconfigure(0,weight=1,minsize=70)
        self.main_frame.grid_columnconfigure(0,weight=6)
        # main_frame..
        self.main_frame.grid_columnconfigure((0,2),weight=1)        
        # main_frame.grid_columnconfigure(0,weight=1)
        # main_frame.grid_columnconfigure(1,weight=9)
        self.main_frame.grid_rowconfigure(3,weight=7,minsize=50)
        
        self.main_frame.grid_columnconfigure(2,weight=1)
        
        self.geometry("800x800")
        self.resizable(False, False)
        self.frames = []
        
        self.views = (side_view,main_view,heading_view)
        self.place = ([1,0],[1,1],[0,0])
        
        self.options_to_switch={}
        
        # self.log = login_sign_in(main_frame,self)
        # self.log.pack(side='top',fill='both',expand=True)
        
        # self.sig = sign_up(main_frame,self)
        # self.sig.pack(side='top',fill='both',expand=True)
        
        self.log_sign_taker ={}
        
        
        self.log_sign(self.main_frame)
        # self.inital_frame(self)
        
        
        self.imgg = ImageTk.PhotoImage(Image.open('menu_img.png').resize((20,20)))
        print(self.frames)
        # self.show_frame(side_view)
    
    def switch(self,trigger):

        if trigger == 'login_sign':
            
            a = self.log_sign_taker['sign_up']
            b  = self.log_sign_taker['login_sign_in']
            a.pack_forget()
            b.pack(side='top',fill='both',expand=True)
            
            b.tkraise()
        elif trigger == 'sign_up':
            a = self.log_sign_taker['sign_up']
            b  = self.log_sign_taker['login_sign_in']
            a.pack(side='top',fill='both',expand=True)
            b.pack_forget()
            a.tkraise()
            
            
        else:
            pass
        
    
    def log_sign(self,main_frame):
        self.log = login_sign_in(main_frame,self)
        self.log.pack(side='top',fill='both',expand=True)
        self.log_sign_taker['login_sign_in'] = self.log
        
        self.sig = sign_up(main_frame,self)
        self.log_sign_taker['sign_up'] = self.sig
        self.sig.pack(side='top',fill='both',expand=True)
        self.sig.pack_forget()
        self.log.tkraise()    
    def inital_frame(self,main_frame  ):
        for i,j in zip(self.views,self.place):
            frame = i(main_frame,self)
            # frame.grid(row=j[0], column=j[1], sticky="NW") 
            self.frames.append(frame)          
    def show_frame(self, cont):  
        frame = self.frames[cont]  
        frame.tkraise() 
    def back_to_login(self):
        print('back to login')
        
        for  i in self.frames[1].options:
            print(i)
            self.frames[1].options[i].pack_forget()
            if i != 'home':
                
                self.frames[1].options['home'].on = 1
                
                self.frames[1].options[i].on = 0
            
            print(i,self.frames[1].options[i].on)
        for i in self.frames:
            
            # self.grid_forget
            
            i.grid_forget()
        a = self.log_sign_taker['login_sign_in']
        a.pack(side='top',fill='both',expand=True)
        self.frames
    def option_switcher(self,frame):
        print('option switcher')
        
        print(frame,self.frames[1].options[frame].on )
        
        # main = copy.copy(self.frames[1].options[frame])
        # others = []
        
        # for i in self.frames[1].options:
        #     others.append(i)
        
        if  self.frames[1].options[frame].on != 1:
            self.frames[1].options[frame].on = 1
            print(frame,self.frames[1].options[frame].on )
            print('done')
            for  i in self.frames[1].options:
                
                if  str(i) != frame:
                    print(i,self.frames[1].options[i].on)
                    self.frames[1].options[i].on = 0
                    print(i,self.frames[1].options[i].on)
                    self.frames[1].options[i].pack_forget()
            
            width= self.frames[1].options[frame].width
            height = self.frames[1].options[frame].height
            # self.frames[1].options[frame].configure(width = width,height = height)
            self.frames[1].options[frame].pack(side = TOP,fill =   BOTH, expand  = True)            
            self.frames[1].options[frame].tkraise()
            
        else:
            print('on is false')  

        

        
        
        
            
class heading_view(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent,bg='#86bdbb')
        self.config(height=200,width=1550)
        # self.pack(fill='x')
        
        self.grid(row=0,column=0,columnspan=2,sticky='N')
        self.imgg = ImageTk.PhotoImage(Image.open('menu_img.png').resize((30,30)))
        t = tk.Button(self,image=self.imgg,bg='#86bdbb',relief='flat',activebackground='#86bdbb',command=lambda :self.trig(controller))
        
        
        t.place(x=15,y=8)

        t.bind('<Button>',func=lambda A :t.config(activeforeground='#86bdbb',activebackground='#86bdbb',relief='flat',bd=0))
        # self.place(side='top',fill='x',expand=True)
        self.on = 0
        
        self.logout_frame = customtkinter.CTkFrame(self,fg_color='#86bdbb')
        self.logout_frame.place(x = 1410,y=20)
        
        self.log_img = ImageTk.PhotoImage(Image.open('logout_img.png').resize((30,30)))
        self.log_out_but = customtkinter.CTkButton(self.logout_frame, command=controller.back_to_login, image=self.log_img,text='',width=25,fg_color='#86bdbb',hover_color='#c1deca')
        self.log_out_but.place(x = 1,y=1)
        
        self.logout_labal = customtkinter.CTkLabel(self.logout_frame,text='Logout',font=('arial',15,'bold'),width=10,text_color='black')
        self.logout_labal.place(x=50,y=5)
        
        self.leave = 'enter'
        self.logout_frame.bind('<Enter>',command=lambda a : self.littel_frame(action=self.leave))

    def littel_frame(self,action):
        if action =='enter':
            self.logout_labal.configure(text_color = '#414542')
            self.leave  = 'leave'
        else:
            self.logout_labal.configure(text_color = 'white')
            self.leave = 'enter'
            
    def trig(self,controller):
        # side = controller.frames['side_view']
        # print("side")
        if self.on  == 0:
            print(controller.frames)
            a = controller.frames[0]
            b =  controller.frames[1]
            b.configure(width=1476,height=750)
            
            a.home.config(text=' ',width = 40)
            a.emp.config(text=' ',width = 40)
            a.dep.config(text=' ',width = 40)
            a.configure(width=60,height=750)
            for i  in b.options:
                b.options[i].height = 750
                b.options[i].width = 1476
                b.options[i].configure(width=1476,height=750)
            self.on = 1
             
        else:
            a = controller.frames[0]
            b =  controller.frames[1]

            b.configure(width=1250,height=750)
            
            a.home.configure(text='HOME',width = 90)
            a.emp.configure(text='EMPLOYEES',width = 150)
            a.dep.configure(text='DEPARTMENT',width = 150)
            a.configure(width=900,height=750)
            for i  in b.options:
                b.options[i].height = 750
                b.options[i].width = 1250
                b.options[i].configure(width=1250,height=750)
            self.on = 0
        
class upper_frame(tk.Frame):
    def __init__(self,parent,controler):
        super().__init__(self,parent)
class StartPage(Frame):  
  
    def __init__(self, parent, controller):  
        super.__init__(self,parent,bg='yellow')  
        label = Label(self, text="Start Page")  
        label.pack(pady=10,padx=10)  
  
        button = Button(self, text="Visit Page 1",  
                            command=lambda: controller.show_frame(side_view))  
        button.pack()  
  
        button2 = Button(self, text="Visit Page 2",  
                            command=lambda: controller.show_frame(main_view))  
        button2.pack()  
class side_view(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg='#86bdbb')
        self.config(width=300,height=780)
        # self.pack(side='right',fill='y',expand=True)
        # self.config(width=300)
       
        # img = Image.open('menu_img.png').resize((20,20),Image.ANTIALIAS)
        # img.convert(mode='gif')
        self.imgg = ImageTk.PhotoImage(Image.open('home.png').resize((30,30)))
        # # img = customtkinter.CTkImage('menu_img.png')
        # self.img  = PhotoImage(file='on.png')
        # # print(imgg)
        self.home = tk.Button(self,image=self.imgg,  command= lambda:controller.option_switcher('home') ,relief='flat',bg='#86bdbb',bd=0,activebackground='#86bdbb',compound='left',padx=20,width=90,height=50,text='HOME',font=('arial',15,'bold'))
        self.home.config(relief='flat')
        self.home.bind('<Button>',func=lambda b :self.home.config(activebackground='#86bdbb',bg='#86bdbb'))
        
        self.home.bind('<Enter>',func=lambda h: self.home.config(foreground='white'))
        self.home.bind('<Leave>',func=lambda h :self.home.config(background='#86bdbb',foreground='black'))
        self.home.place(x=10)
        
        
        
        self.img = ImageTk.PhotoImage(Image.open('emp_img.png').resize((30,30)))
        self.emp = tk.Button(self,image=self.img, relief='flat',command= lambda:controller.option_switcher('employees') ,bg='#86bdbb',bd=0,activebackground='#86bdbb',compound='left',padx=20,width=150,height=50,text='EMPLOYEES',font=('arial',15,'bold'))
        self.emp.config(relief='flat')
        self.emp.bind('<Button>',func=lambda b :self.home.config(activebackground='#86bdbb',bg='#86bdbb'))
        self.emp.place(x=10,y=75)
        self.emp.bind('<Button>',func=lambda b :self.emp.config(activebackground='#86bdbb',bg='#86bdbb'))
        
        self.emp.bind('<Enter>',func=lambda h: self.emp.config(foreground='white'))
        self.emp.bind('<Leave>',func=lambda h :self.emp.config(background='#86bdbb',foreground='black'))
        
        self.imgs= ImageTk.PhotoImage(Image.open('dep_img.png').resize((30,30)))
        
        self.dep = tk.Button(self,image=self.imgs,command= lambda:controller.option_switcher('department') , relief='flat',bg='#86bdbb',bd=0,activebackground='#86bdbb',compound='left',padx=20,width=170,height=60,text='DEPARTMENT',font=('arial',15,'bold'))
        # self.dep.config(relief='flat')
        self.dep.bind('<Button>',func=lambda b :self.home.config(activebackground='#86bdbb',bg='#86bdbb'))
        self.dep.place(x=12,y=150)
        self.dep.bind('<Button>',func=lambda b :self.dep.config(activebackground='#86bdbb',bg='#86bdbb'))
        self.dep.bind('<Enter>',func=lambda h: self.dep.config(foreground='white'))
        self.dep.bind('<Leave>',func=lambda h :self.dep.config(background='#86bdbb',foreground='black'))
        
        self.sal = ImageTk.PhotoImage(Image.open('salary_img.png').resize((30,30)))
        
        self.sal_but = Button(self, image=self.sal, text='SALARY',command= lambda:controller.option_switcher('salary') , compound='left',relief='flat',bd=0,activebackground='#86bdbb',bg='#86bdbb',padx=20,width=120,height=60,font=('arial',15,'bold'))
        self.sal_but.place(x=9,y=225)
        self.sal_but.bind('<Button>',func=lambda b :self.sal_but.config(activebackground='#86bdbb',bg='#86bdbb'))
        self.sal_but.bind('<Enter>',func=lambda h: self.sal_but.config(foreground='white'))
        self.sal_but.bind('<Leave>',func=lambda h :self.sal_but.config(background='#86bdbb',foreground='black'))
        
        # self.home = tk.Button(self,image=self.imgg, relief='flat',bg='#86bdbb',bd=0,activebackground='#86bdbb',compound='left',padx=20,width=90,height=50,text='HOME',font=('arial',15,'bold'))
        # self.home.config(relief='flat')
        # self.home.bind('<Button>',func=lambda b :self.home.config(activebackground='#86bdbb',bg='#86bdbb'))
        # self.home.place(x=10)
        # togel = customtkinter.CTkButton(self,text='HOME',image=self.imgg,bg_color='#86bdbb',activebackground='#86bdbb')
        # togel.place(x=2)
        self.grid(row=1,column=0,sticky='N')        

    def switch(self,frame):
        pass



    
    def h(self):
        self.home.config(bg='yellow',foreground='white')
   
   
# class employees_view(customtkinter.CTkFrame):
#     def __init__(self,parent,controller):
#         customtkinter.CTkFrame.__init__(self,parent)
   
        
class main_view(customtkinter.CTkFrame):
    print('contoroller') 
    def __init__(self, parent,controller):
        self.detail ={'id': 100, 'first_name': 'Steven', 'last_name': 'King', 'gmail': 'sking@gmail.com', 'phone_no': '515.123.4567', 'work': 'AD_PRES', 'salary': 2400000, 'manager': 'None', 'department': 90}
        self.main_color = '#212c40'
        customtkinter.CTkFrame.__init__(self,parent,corner_radius=20,bg_color='#86bdbb',fg_color='#212c40')
        # l = customtkinter.CTkFrame(/)
        self.grid(row=1,column=1,sticky='E')
        # self.configuer(width=1250,height=780)
        self.configure(width=1290,height=790)
        # self.count_tree1 = self.tere_emp(self,controller)

        self.home_frame_tab =self.home_frame(self,controller)
        self.employees_tab =  self.employees_frame(self,controller)
        self.department_tab = self.department_frame(self,controller)
        self.salary_tab=  self.salary_frame(self,controller)
        # self.home_frame_tab.pack_forget()
        # self.employees_tab.tkraise()
        
        three ='#212c40'
        self.Three_holder = customtkinter.CTkFrame(self.home_frame_tab,fg_color=three)
        self.Three_holder.configure(width=540,height=140)
        self.Three_holder.place(x=700,y=10)
        
        self.emp_frame =  Frame(self.home_frame_tab,bg=self.main_color)
        # self.emp_frame.configure()
        self.emp_frame.place(x=1000,y=200)
        # self.emp_frame.pack(fill=Y,expand=Y)
        
        # three holder  this
        self.dep_count  = self.count_dep(self.Three_holder,controller)
        self.count_emp1 =  self.count_emp(self.Three_holder,controller)
        self.man_count = self.count_man(self.Three_holder,controller)
        
        
        
        self.emp_tree = self.employee_tree(self.home_frame_tab,controller,self)
        self.make_tab=  self.making_img(self.emp_frame,controller)
        self.info = self.making_info(self.emp_frame,controller,self)
    
        self.options= {'home':self.home_frame_tab,'employees':self.employees_tab,'department':self.department_tab,"salary":self.salary_tab}
        
    #   this is start of all over detail  
    class home_frame(customtkinter.CTkFrame):
        def __init__(self,parent,controller ):
            self.on = 1
            self.width = 1290
            self.height = 790
            self.size = (self.width,self.height)
            self.detail ={'id': 100, 'first_name': 'Steven', 'last_name': 'King', 'gmail': 'sking@gmail.com', 'phone_no': '515.123.4567', 'work': 'AD_PRES', 'salary': 2400000, 'manager': 'None', 'department': 90}
            self.main_color = '#212c40'

            customtkinter.CTkFrame.__init__(self,parent,corner_radius=20,bg_color='#86bdbb',fg_color='#212c40')
            self.configure(width=1290,height=790)
            self.pack(side=LEFT,expand = True, fill= BOTH)
 
    class employees_frame(customtkinter.CTkFrame):
        def __init__(self,parent,controller):
            customtkinter.CTkFrame.__init__(self,parent,corner_radius=20,bg_color='#86bdbb',fg_color='#163138')
            
            self.main_color =  '#163138'
            self.bg_main_color = '#86bdbb'
            self.ok =  False
            self.main_update_widget = []
            self.on = 0
            self.width = 1290
            self.height = 790
            self.names = ('id','First_name','Last_name','Email','Phone_no','Position','Salary','Manager','Department')
            self.size = (self.width,self.height)
            # self.frames = Frame(self,bg=self.main_color)
            # self.frames.place(relx=0.02,rely=0.02)
           
            self.tree_view_created = self.tree_view_of_employe(self,controller=controller,self = self)
            
            self.configure(width=1290,height=790)
            self.on_of_thread =  threading.BoundedSemaphore(value=5)

           
            self.a = self.small_emp_man_info_frame(self)
            
        def emp_data(self):
            
            self.on_of_thread.acquire()
            record = []
        
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            row = corser.execute("select * from employees")
            a = corser.fetchall()
            c = []
            m = 0
            def listToString(s):
                str1 = ""
            
                for ele in s:
                    str1 += ele
                return str1
            for i in a:
                c.append(i[0])
                c.append(i[1])
                c.append(i[2])
                x= str(i[3])
                e =x.lower()+'@gmail.com'
                c.append(e)
                c.append(i[4])
                c.append(i[6])
                sa  = [p for p in str(i[7]) if p.isdigit()]
                l = listToString(sa)
                c.append(l)
                c.append(i[9])
                c.append(i[10])
                record.append(c.copy())
                m+=1
                c.clear()
            conobj.close()
            self.on_of_thread.release()
            return record
            # self.pack(side=LEFT,expand = True, fill= BOTH)  
        def man_data(self):
            query= 'select * from employees  where employee_id  in (select distinct(manager_id) from employees );'

            # self.on_of_thread.acquire()
            record = []
        
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            row = corser.execute('select * from employees  where employee_id  in (select distinct(manager_id) from employees)')
            a = corser.fetchall()
            c = []
            m = 0
            def listToString(s):
                str1 = ""
            
                for ele in s:
                    str1 += ele
                return str1
            for i in a:
                c.append(i[0])
                c.append(i[1])
                c.append(i[2])
                x= str(i[3])
                e =x.lower()+'@gmail.com'
                c.append(e)
                c.append(i[4])
                c.append(i[6])
                sa  = [p for p in str(i[7]) if p.isdigit()]
                l = listToString(sa)
                c.append(l)
                c.append(i[9])
                c.append(i[10])
                record.append(c.copy())
                m+=1
                c.clear()
            conobj.close()
            # self.on_of_thread.release()
            return record
            # self.pack(side=LEFT,expand = True, fill= BOTH)  
        
        class tree_view_of_employe(Frame):
            def __init__(s,parent,controller,self):
                Frame.__init__(s,parent,bg='white')
                s.config(width=600,height=500)
                # f = Frame()
                s.parent = parent
                
                frames = Frame(s)
                frames.pack(side='top',fill=X,expand=True)

                frames.config(width=600,height=500)
                s.place(relx=0.01,rely=0.01)
                s.style = ttk.Style()
                s.style.theme_use('default')
                s.style.configure('Treeview',
                                     background = '#D3D3D3',
                                     foreground='black',
                                     rowheight='25',
                                     fieldbackground = '#D3D3D3')
                s.style.map('Treeview',background=[('selected','#347083')])

                scrollbar = Scrollbar(frames)
                scrollbar.pack(side = RIGHT,fill=Y)

                my_tree = ttk.Treeview(frames,yscrollcommand = scrollbar.set, selectmode = 'extended')
                my_tree.pack(side='top' ,fill='both',expand=True)
                scrollbar.config(command = my_tree.yview)

                names = ('id','First_name','Last_name','Email','Phone_no','Position','Salary','Manager','Department')

                my_tree['columns'] = names


                my_tree.column('#0',stretch=NO,width=0,minwidth=0)
            
            # em.data.heading(em)
                my_tree.tag_configure('oddrow',background='white')
                my_tree.tag_configure('evenrow',background='#8db2f2')
                for i in names:
                    my_tree.column(i,width=100,anchor=W,minwidth=20)
                    my_tree.heading(i,text=i,anchor=W)

                my_tree.tag_configure('oddrow',background = 'white')
                my_tree.tag_configure('evenrow',background = 'lightblue')

                
                count = 0
                rows = s.getting()
                global kkk
                kkk = 0
                for i in rows:
                    if kkk %2 ==0:
                        my_tree.insert(parent='',index='end',iid =kkk,text='',values=i,tags=('evenrow',))
                    else:
                        my_tree.insert(parent='',index='end',iid =kkk,text='',values=i,tags=('oddrow',))
                    kkk +=1
                my_tree.pack()
                    
                    
                data_frame = LabelFrame(s,text='Add Data',bg='white')
                data_frame.pack(fill=X,expand=True,pady=10,padx=10)


                id_label = Label(data_frame,text='ID')
                id_label.grid(row=0,column=0,padx = 10,pady=10)
                id_entery  = Entry(data_frame)
                id_entery.grid(row=0,column=1,padx=10,pady = 10)


                fn_label = Label(data_frame,text='First Name')
                fn_label.grid(row=0,column=2,padx = 10,pady=10)
                fn_entery  = Entry(data_frame)
                fn_entery.grid(row=0,column=3,padx=10,pady = 10)
                
                ln_label = Label(data_frame,text='last Name')
                ln_label.grid(row=0,column=4,padx = 10,pady=10)
                ln_entery  = Entry(data_frame)
                ln_entery.grid(row=0,column=5,padx=10,pady = 10)
                
                
                Email_label = Label(data_frame,text='Email')
                Email_label.grid(row=1,column=0,padx = 10,pady=10)
                Email_entery  = Entry(data_frame)
                Email_entery.grid(row=1,column=1,padx=10,pady = 10)
                
                
                Phone_no_label = Label(data_frame,text='Phone_no')
                Phone_no_label.grid(row=1,column=2,padx = 10,pady=10)
                Phone_no_entery  = Entry(data_frame)
                Phone_no_entery.grid(row=1,column=3,padx=10,pady = 10)
                
                Salary_label = Label(data_frame,text='Salary')
                Salary_label.grid(row=1,column=4,padx = 10,pady=10)
                Salary_entery  = Entry(data_frame)
                Salary_entery.grid(row=1,column=5,padx=10,pady = 10)
                
                
                
                
                
                
                Manager_label = Label(data_frame,text='Manager Name')
                Manager_label.grid(row=2,column=0,padx = 10,pady=10)
                Manager_entery  = Entry(data_frame)
                Manager_entery.grid(row=2,column=1,padx=10,pady = 10)
                
                
                
                
                
                Position_label = Label(data_frame,text='Position')
                Position_label.grid(row=2,column=2,padx = 10,pady=10)
                Position_entery  = Entry(data_frame)
                Position_entery.grid(row=2,column=3,padx=10,pady = 10)
                
                
                Department_label = Label(data_frame,text='Department Name')
                Department_label.grid(row=2,column=4,padx = 10,pady=10)
                Department_entery  = Entry(data_frame)
                Department_entery.grid(row=2,column=5,padx=10,pady = 10)

                
            
            def getting(s):
                record = []
                conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
                corser = conobj.cursor()
                row = corser.execute("select * from employees")
                a = corser.fetchall()
                c = []
                m = 0
                def listToString(s):
                    str1 = ""
                
                    for ele in s:
                        str1 += ele
                    return str1
                for i in a:
                    c.append(i[0])
                    c.append(i[1])
                    c.append(i[2])
                    x= str(i[3])
                    e =x.lower()+'@gmail.com'
                    c.append(e)

                    
                    c.append(i[4])

                    c.append(i[6])

                    sa  = [p for p in str(i[7]) if p.isdigit()]
                    l = listToString(sa)
                    c.append(l)

                    
                    c.append(i[9])
                    c.append(i[10])

                    record.append(c.copy())
                    m+=1
                    c.clear()
                
                
                conobj.close()
                return record
                
                        
        class small_emp_man_info_frame(customtkinter.CTkFrame):
            def __init__(selff,parent):
                selff.parent = parent
                selff.main_update_widget = []
                selff.main_color =  '#163138'
                selff.ok=False
                selff.trig = True
                selff.man_on =False
                
                selff.lock =threading.Lock() 
                customtkinter.CTkFrame.__init__(selff,parent,corner_radius=0,fg_color=selff.main_color)
                selff.place(relx = 0.75,rely = 0.03)
                # selff.pack(y)
                selff.configure(height = 530,width = 300)
                selff.emp_man_holder  =  customtkinter.CTkFrame(selff,fg_color='#8548b8',)
                selff.emp_man_holder.configure(height = 505,width = 300)
                selff.emp_man_holder.place(x=0,y=0)
                
                selff.both_frame = customtkinter.CTkFrame(selff.emp_man_holder,fg_color=selff.main_color,corner_radius=10,height=80,width=300)
                selff.both_frame.place(x = 0,y = 0)
                
                selff.frame_emp = customtkinter.CTkFrame(selff.both_frame,height=70,width=154,fg_color='#8548b8',bg_color=selff.main_color,corner_radius=15)
                selff.frame_emp.place(x = 0,y = 0)
                
                
                selff.frame_man = customtkinter.CTkFrame(selff.both_frame,height=70,width=154,fg_color=selff.main_color,bg_color=selff.main_color,corner_radius=15)
                selff.frame_man.place(x = 160,y = 0)
                
                
                
                # this is the holder of  whole frame which holdes the small info frame all indivisual frame
                selff.holder_emp = customtkinter.CTkScrollableFrame(selff.emp_man_holder,width=300,height=430,fg_color='#91908c',corner_radius=0)
                selff.holder_emp.place(x = 0,y=65)


                selff.holder_man =  customtkinter.CTkScrollableFrame(selff.emp_man_holder,width=300,height=430,fg_color='lightblue',corner_radius=0)
                
                selff.imgs= ImageTk.PhotoImage(Image.open('emp_img.png').resize((30,30)))
                selff.emp_but  = customtkinter.CTkButton(selff.frame_emp,text='Employees',command=lambda:selff.emp_but_fun(True),image=selff.imgs,corner_radius=10, compound='left',border_color=selff.main_color,font=('profile',15),hover=True,hover_color='#de597a',height=50,width=100)
                selff.emp_but.place(x = 9,y = 6)
                
                
                selff.imgs= ImageTk.PhotoImage(Image.open('emp_img.png').resize((30,30)))
                selff.man_but  = customtkinter.CTkButton(selff.frame_man,text='Manager',command=lambda:selff.man_but_fun(True),image=selff.imgs,corner_radius=10, compound='left',font=('profile',15),hover=True,hover_color='#de597a',height=50,width=100)
                selff.man_but.place(x = 10,y = 6)
                # selff.lock = threading.Lock()
                
                # self.emp_but.bind('<Button-1>',command=lambda a:self.emp_but_fun(a))
                # self.man_but.bind('<Button-1>',command=lambda a:self.man_but_fun(a))
                # selff.t = multiprocessing.Process(target=selff.emp_auto_frame)
                selff.t = threading.Thread(target=selff.emp_auto_frame)
                selff.t.start()
                    
                
            
            
            def emp_but_fun(selff,a):
                
                print('emp')
                selff.frame_emp.configure(fg_color='white')
                selff.frame_man.configure(fg_color= selff.main_color)
                selff.emp_man_holder.configure(fg_color = '#8548b8')
                selff.frame_emp.configure(fg_color = '#8548b8')
                if selff.trig != True:
                    
                    selff.holder_emp.place(x = 0,y=65)
                    # selff.holder_emp.tkraise()
                    selff.holder_man.place_forget()
                    selff.trig = True
                    
                
                    
            
            def man_but_fun(selff,a):
                print('man')

                selff.frame_man.configure(fg_color='white')
                selff.frame_emp.configure(fg_color= selff.main_color)
                selff.emp_man_holder.configure(fg_color = '#bed444')
                selff.frame_man.configure(fg_color = '#bed444')
                
                if selff.trig != False:
                    
                    selff.holder_man.place(x = 0,y=65)
                    # selff.holder_man.tkraise()
                    selff.holder_emp.place_forget()
                    selff.trig = False
                if selff.man_on != True:
                    selff.man_on = True
                    print('man but in clicked')
                    selff.man_auto_frame(False)
                    # selff.s = multiprocessing.Process(target=selff.man_auto_frame)
                    # selff.s.start

            def emp_man_frame(selff,auto=False):
                selff.lock.acquire()
                print('emp_man_frame')
                data = selff.parent.emp_data()
        
        
            def emp_auto_frame(selff,auto = False):
                print('hello emp_auto_frame')
                update_widget = []
                selff.lock.acquire()
                data = selff.parent.emp_data()
                b = 1
                
                color = ['#ebe7dd','#f2e5c2']
                choice = color[0]
                print('lock is on')
                
                if auto != True:
                    for i in data:
                        if b %2 == 0 :
                            choice = color[1]
                        else:
                            choice = color[0]
                        selff.frame   = customtkinter.CTkFrame(selff.holder_emp,width=300,height=70,fg_color=choice,corner_radius=10)
                        selff.frame.grid_columnconfigure(index=0,minsize=50)
                        selff.frame.grid_columnconfigure(index=1,minsize=10)
                        # selff.frame.grid_columnconfigure

                        # selff.frame.grid_rowconfigure(index=0,minsize=70)
                        # selff.frame.grid_rowconfigure(index=0,minsize=70)


                        selff.frame.pack(side= TOP)
                        
                        
                        selff.imgs= ImageTk.PhotoImage(Image.open('emp_info_img.png').resize((40,40)))    
                    
                        # # selff.img_frame = customtkinter.CTkFrame(selff.frame,width=60,height=70,corner_radius=0,fg_color=choice)
                        # # selff.img_frame.pack(side = LEFT)
                        selff.info_frame_img = customtkinter.CTkLabel(selff.frame,image=selff.imgs,text='',width=60,height=70,bg_color='transparent')
                        selff.info_frame_img.place(x=0,y=0      )
                        # selff.info_frame_img.grid(row = 0,column = 0,columnspan = 3)
                        
                        
                        # # here i am trying  to use minimum frame in my programe
                        
                        # # selff.info_frame = customtkinter.CTkFrame(selff.frame ,width=240,height=70,fg_color=choice,bg_color='transparent')
                        # # selff.info_frame.pack(side = RIGHT,fill= Y) 
                    
                        # # selff.name_work_dep_frame = customtkinter.CTkFrame(selff.info_frame,width=100,height=70,corner_radius=0,fg_color=choice)
                        # # selff.name_work_dep_frame.pack(side = LEFT,fill = Y)
                        
                        selff.name_tag  = customtkinter.CTkLabel(selff.frame,text=i[1],font=('Copperplate Gothic Light',15),text_color='#4d4d4d')     
                        selff.name_tag.place(x=65,y=10)
                        # update_widget.append(selff.name_tag)
                        
                        selff.work_tag  = customtkinter.CTkLabel(selff.frame,text=i[5],font=('Copperplate Gothic Light',15),text_color='#4d4d4d')     
                        selff.work_tag.place(x=65,y=30)
                        # update_widget.append(selff.work_tag)
                        
                        selff.dep_tag  = customtkinter.CTkLabel(selff.frame,text='Dep = {}'.format(i[-1]),font=('Copperplate Gothic Light',15),text_color='#4d4d4d')     
                        selff.dep_tag.place(x=65,y=50)       
                        # update_widget.append(selff.dep_tag)
                        
                        # # selff.contanct_tag = customtkinter.CTkFrame(selff.info_frame,width=140,height=70,fg_color=choice,corner_radius=0)
                        # # selff.contanct_tag.grid(row=)
                        # # selff.contanct_tag.pack(side = RIGHT,fill = Y)
                        
                        selff.gog= ImageTk.PhotoImage(Image.open('gog.png').resize((20,20)))    
                        selff.mail_emp = customtkinter.CTkButton(selff.frame,text='',command=lambda:print('hrlo'),compound=RIGHT,image=selff.gog,fg_color=choice,width=10,height=10,hover_color='white',hover=10)
                        selff.mail_emp.place(x=230,y= 5)
                        
                        # selff.gog =  ImageTk.PhotoImage(Image.open('gog.png').resize((25,25)))
                        # selff.google = Button(selff.frame,image=selff.gog,relief='flat',bd=0)
                        # # selff.google.bind('<Button>',func=lambda b :selff.google.config(activebackground='white',bg='white'))
                        # # selff.google.place(x=40,y=5)
                        # selff.grid(row =0,column = 2,columnspan = 2)
                        
                        
                        selff.arrow= ImageTk.PhotoImage(Image.open('arrow2.png').resize((20,20)))    
                        
                        selff.go_to = customtkinter.CTkButton(selff.frame,text='',command=lambda:print('hrlo'),compound=RIGHT,image=selff.arrow,fg_color=choice,width=10,height=10,hover_color='white',hover=10)
                        
                        # selff.go_to.bind("<Enter>", func=lambda e: selff.go_to.config(background= '#e5e6e3'))
                        # selff.go_to.bind("<Leave>", func=lambda e: selff.go_to.config(background='white'))
                        selff.go_to.place(x=260,y= 5)
                        # selff.grid(row = 0,column = 3)
                        
                        
                        selff.contact_labla_tag = customtkinter.CTkLabel(selff.frame,text = 'Contact',font=('Copperplate Gothic Light',9),text_color='#3b3b3b')
                        selff.contact_labla_tag.place(x = 230,y=30)
                        # selff.contact_labla_tag.grid(row=1,column = 2,columnspan = 2)
                        
                        # selff.contanct_phone_no_tag = customtkinter.CTkLabel(selff.frame,text='{}'.format(i[4]),font=('Copperplate Gothic Light',10),height=3,text_color='#3b3b3b')
                        # selff.contanct_phone_no_tag.place(x = 220,y=50)
                        # selff.contanct_phone_no_tag.grid(row=2,column =2,columnspan = 2)
                        # update_widget.append(selff.contanct_phone_no_tag)

                        selff.contanct_email_no_tag = customtkinter.CTkLabel(selff.frame,text='{}'.format(i[3]),font=('Copperplate Gothic Light',10),width=3,height=3,text_color='#3b3b3b')
                        selff.contanct_email_no_tag.place(x=200,y=50)
                        # selff.contanct_email_no_tag.grid(row= 3,column= 2,colmunspan = 2)
                        # # selff.contanct_email_no_tag.place(x = 15,y=75)
                        # update_widget.append(selff.contanct_email_no_tag)

                        # # THESE tHREE ARE TOGETHER     1111111111111111111111111
                
                        # selff.main_update_widget.append(update_widget)
                        # update_widget.clear()
                        b +=1
                else:
                    a = 0
                    index= [1,5,-1,4,3]
                    for i in selff.main_update_widget:
                        for j,k in zip(i,index):
                            
                            j.configure(text = data[k])
                            
                selff.lock.release()
                print('released')
                
            def man_auto_frame(selff,auto= False):

                print('hello emp_auto_frame')
                update_widget = []
                # selff.lock.acquire()
                data = selff.parent.man_data()
                b = 1
                
                color = ['#ebe7dd','#f2e5c2']
                choice = color[0]
                print('lock is on')
                
                if auto != True:
                    for i in data:
                        if b %2 == 0 :
                            choice = color[1]
                        else:
                            choice = color[0]
                        selff.frame   = customtkinter.CTkFrame(selff.holder_man,width=300,height=70,fg_color=choice,corner_radius=10)
                        selff.frame.grid_columnconfigure(index=0,minsize=50)
                        selff.frame.grid_columnconfigure(index=1,minsize=10)
                        # selff.frame.grid_columnconfigure

                        # selff.frame.grid_rowconfigure(index=0,minsize=70)
                        # selff.frame.grid_rowconfigure(index=0,minsize=70)


                        selff.frame.pack(side= TOP)
                        
                        
                        selff.imgs= ImageTk.PhotoImage(Image.open('emp_info_img.png').resize((40,40)))    
                    
                        # # selff.img_frame = customtkinter.CTkFrame(selff.frame,width=60,height=70,corner_radius=0,fg_color=choice)
                        # # selff.img_frame.pack(side = LEFT)
                        selff.info_frame_img = customtkinter.CTkLabel(selff.frame,image=selff.imgs,text='',width=60,height=70,bg_color='transparent')
                        selff.info_frame_img.place(x=0,y=0      )
                        # selff.info_frame_img.grid(row = 0,column = 0,columnspan = 3)
                        
                        
                        # # here i am trying  to use minimum frame in my programe
                        
                        # # selff.info_frame = customtkinter.CTkFrame(selff.frame ,width=240,height=70,fg_color=choice,bg_color='transparent')
                        # # selff.info_frame.pack(side = RIGHT,fill= Y) 
                    
                        # # selff.name_work_dep_frame = customtkinter.CTkFrame(selff.info_frame,width=100,height=70,corner_radius=0,fg_color=choice)
                        # # selff.name_work_dep_frame.pack(side = LEFT,fill = Y)
                        
                        selff.name_tag  = customtkinter.CTkLabel(selff.frame,text=i[1],font=('Copperplate Gothic Light',15),text_color='#4d4d4d')     
                        selff.name_tag.place(x=65,y=10)
                        # update_widget.append(selff.name_tag)
                        
                        selff.work_tag  = customtkinter.CTkLabel(selff.frame,text=i[5],font=('Copperplate Gothic Light',15),text_color='#4d4d4d')     
                        selff.work_tag.place(x=65,y=30)
                        # update_widget.append(selff.work_tag)
                        
                        selff.dep_tag  = customtkinter.CTkLabel(selff.frame,text='Dep = {}'.format(i[-1]),font=('Copperplate Gothic Light',15),text_color='#4d4d4d')     
                        selff.dep_tag.place(x=65,y=50)       
                        # update_widget.append(selff.dep_tag)
                        
                        # # selff.contanct_tag = customtkinter.CTkFrame(selff.info_frame,width=140,height=70,fg_color=choice,corner_radius=0)
                        # # selff.contanct_tag.grid(row=)
                        # # selff.contanct_tag.pack(side = RIGHT,fill = Y)
                        
                        selff.gog= ImageTk.PhotoImage(Image.open('gog.png').resize((20,20)))    
                        selff.mail_emp = customtkinter.CTkButton(selff.frame,text='',command=lambda:print('hrlo'),compound=RIGHT,image=selff.gog,fg_color=choice,width=10,height=10,hover_color='white',hover=10)
                        selff.mail_emp.place(x=230,y= 5)
                        
                        # selff.gog =  ImageTk.PhotoImage(Image.open('gog.png').resize((25,25)))
                        # selff.google = Button(selff.frame,image=selff.gog,relief='flat',bd=0)
                        # # selff.google.bind('<Button>',func=lambda b :selff.google.config(activebackground='white',bg='white'))
                        # # selff.google.place(x=40,y=5)
                        # selff.grid(row =0,column = 2,columnspan = 2)
                        
                        
                        selff.arrow= ImageTk.PhotoImage(Image.open('arrow2.png').resize((20,20)))    
                        
                        selff.go_to = customtkinter.CTkButton(selff.frame,text='',command=lambda:print('hrlo'),compound=RIGHT,image=selff.arrow,fg_color=choice,width=10,height=10,hover_color='white',hover=10)
                        
                        # selff.go_to.bind("<Enter>", func=lambda e: selff.go_to.config(background= '#e5e6e3'))
                        # selff.go_to.bind("<Leave>", func=lambda e: selff.go_to.config(background='white'))
                        selff.go_to.place(x=260,y= 5)
                        # selff.grid(row = 0,column = 3)
                        
                        
                        selff.contact_labla_tag = customtkinter.CTkLabel(selff.frame,text = 'Contact',font=('Copperplate Gothic Light',9),text_color='#3b3b3b')
                        selff.contact_labla_tag.place(x = 230,y=30)
                        # selff.contact_labla_tag.grid(row=1,column = 2,columnspan = 2)
                        
                        # selff.contanct_phone_no_tag = customtkinter.CTkLabel(selff.frame,text='{}'.format(i[4]),font=('Copperplate Gothic Light',10),height=3,text_color='#3b3b3b')
                        # selff.contanct_phone_no_tag.place(x = 220,y=50)
                        # selff.contanct_phone_no_tag.grid(row=2,column =2,columnspan = 2)
                        # update_widget.append(selff.contanct_phone_no_tag)

                        selff.contanct_email_no_tag = customtkinter.CTkLabel(selff.frame,text='{}'.format(i[3]),font=('Copperplate Gothic Light',10),width=3,height=3,text_color='#3b3b3b')
                        selff.contanct_email_no_tag.place(x=200,y=50)
                        # selff.contanct_email_no_tag.grid(row= 3,column= 2,colmunspan = 2)
                        # # selff.contanct_email_no_tag.place(x = 15,y=75)
                        # update_widget.append(selff.contanct_email_no_tag)

                        # # THESE tHREE ARE TOGETHER     1111111111111111111111111
                
                        # selff.main_update_widget.append(update_widget)
                        # update_widget.clear()
                        b +=1
                else:
                    a = 0
                    index= [1,5,-1,4,3]
                    for i in selff.main_update_widget:
                        for j,k in zip(i,index):
                            
                            j.configure(text = data[k])
                            
                # selff.lock.release()
                print('released')
                
                # pass           
            
            # def man_data(selff):
            #     query = 'select * from employees  where employee_id  in (select distinct(manager_id) from employees );'
        # class emp_and_man_emp(customtkinter.CTkFrame):
        #     def __init__(self,parent,controller):
        #         customtkinter.CTkFrame.__init__(self,parent)
                


        
        
        
        
        
            
            
    class department_frame(customtkinter.CTkFrame):
        def __init__(self,parent,controller):
            self.on = 0
            self.width = 1290
            self.height = 790
            self.size = (self.width,self.height)
            customtkinter.CTkFrame.__init__(self,parent,corner_radius=20,bg_color='#86bdbb',fg_color='#46609e')
            
            self.configure(width=1290,height=790)
    class salary_frame(customtkinter.CTkFrame):
        def __init__(self,parent,controller):
            self.on = 0
            self.width = 1290
            self.height = 790
            self.size = (self.width,self.height)
            customtkinter.CTkFrame.__init__(self,parent,corner_radius=20,bg_color='#86bdbb',fg_color='#50367a')
            
            self.configure(width=1290,height=790)
   
   
    class count_emp(customtkinter.CTkFrame):
        def __init__(own,parent,controller):
            customtkinter.CTkFrame.__init__(own,parent,fg_color='#4d4d6e',corner_radius=10)
            own.p = parent
            frame = GradientFrame(own, '#809ea8', "#18208f",borderwidth = 0,highlightthickness=0,width = 195,height =95)
            frame.place(x = 0,y =0)
            own.configure(width=200,height=100)
            own.place(x=10,y=30)
            
            own.title_emp = frame.create_text(95,0,text='NO OF Employees',font=('denmark',20),width=198,fill = '#19191a')

            # print(own.title_emp.winfo_height())
            # own.title_emp.place(x=0,y=0)
            c = own.conection()
            
            own.star = ImageTk.PhotoImage(Image.open('employees_logo.png').resize((80,80))) 
            own.p.star = own.star
            frame.create_image(150,70,image = own.star)      
            own.count = frame.create_text(95,55,text=c,font=('denmark',25,'bold'),width=198,fill = '#19191a')
            # own.count.wm_attributes('-transparentcolor', root['bg'])
            # own.count.place(x = 0,y = 45)
        def conection(own):
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            row = corser.execute('select * from employees; ')
            print(row)
            return row
        
        
    class count_dep(customtkinter.CTkFrame):
        def __init__(own1,parent,controller):
            
            customtkinter.CTkFrame.__init__(own1,parent,fg_color='#4d4d6e',corner_radius=10)
            own1.p = parent
            frame = GradientFrame(own1, "#644c75", "#490361",borderwidth = 0,highlightthickness=0,width = 195,height =95)
            frame.place(x = 0,y =0)
            own1.configure(width=200,height=100)
            own1.place(x=240,y=30)
            
            own1.title_emp = frame.create_text(95,15,text='Department',font=('denmark',20),width=198,fill = '#19191a')

            # print(own.title_emp.winfo_height())
            # own.title_emp.place(x=0,y=0)
            c = own1.conection()
            
            own1.star = ImageTk.PhotoImage(Image.open('employees_logo.png').resize((80,80)))
            own1.p.star = own1.star
            frame.create_image(150,70,image = own1.star)      
            own1.count = frame.create_text(95,55,text=c,font=('denmark',25,'bold'),width=198,fill = '#19191a')
            # own.count.wm_a
        def conection(own1):
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            corser.execute('select count(*) from departments ')
            
            a = corser.fetchall()
            corser.fetchall() 
            print(corser.fetchone(),a   )
            return a[0][0] 
        
        
        
               
    class count_man(customtkinter.CTkFrame):
        def __init__(own,parent,controller):
            customtkinter.CTkFrame.__init__(own,parent,fg_color='white',corner_radius=10)
            own.p = parent
            frame = GradientFrame(own, "#644c75", "#490361",borderwidth = 0,highlightthickness=0,width = 105,height =95)
            frame.place(x = 0,y =0)
            own.configure(width=100,height=100)
            own.place(x=470,y=30)
            
            own.title_emp = frame.create_text(55,0,text='NO OF Employees',font=('denmark',20),width=198)

            # print(own.title_emp.winfo_height())
            # own.title_emp.place(x=0,y=0)
            c = own.conection()
            
            own.star = ImageTk.PhotoImage(Image.open('employees_logo.png').resize((80,80)))
            own.p.star = own.star
            frame.create_image(70,70,image = own.star)      
            own.count = frame.create_text(95,55,text=c,font=('denmark',15,'bold'),width=198)
            # own.count.wm_a
        def conection(own):
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            corser.execute('select count(distinct(manager_id)) from employees; ')
            a = corser.fetchall()
            corser.fetchall() 
            print(a   )
            return a[0][0]
    
    # class footer(Frame):
    #     def __init__(main_ff,parent,controller):
    #         tk.Frame.__init__(main_ff,parent,bg=parent.main_color)
    #         # customtkinter.CTkFrame()
    #         main_ff.config(height=10)
    #         main_ff.place(x=0,y=540)
    #         main_ff.names,numbers = main_ff.maker_of_dep()
    #         main_ff.frames_name = {}
            
    #         # main_f = Frame(main_ff,height=100)
    #         # main_f.pack()
    #         # main_ff.scroller = ttk.Scrollbar(main_f,command=main_f.xview,orient="horizontal")
    #         # main_f.bind('<Control MouseWheel>',lambda event: main_f.xview_scroll(-int(event.delta/60),'units'))
    #         # # main_f.configure(xscrollcommand=main_ff.scroller.set)
            
    #         # main_ff.scroller.place()
    #         # main_ff.scroller

    #     # self.scroller.grid(row=2,column=0,columnspan=2)
        
    #     # ,xscrollcommand = h.set
    #         # main_ff.scroller.place(relx=0,rely=1,relwidth=1,anchor='sw')
    #         # main_ff.scroller.pack(side='bottom',fill=X)
    #         # main_f.configure(xscrollcommand=main_ff.scroller.set)
    #         # # main_f.create_window((0, 0), window=inner_frame, anchor="nw")
    #         # main_f.bind("<Control MouseWheel>",lambda event:main_f.xview_scroll(-int(event.delta/10),'units'))
    #         # def on_configure(event):
    #         #     main_f.configure(scrollregion=main_f.bbox("all"))
                
    #         # main_f.bind("<Configure>", on_configure)   
    #         # main_ff.scroller.config(command=main_f.xview)
    #         # main_ff.style = ttk.Style()
    #         # main_ff.style.configure("Treeview.Heading", font=('arial',15))
    #         # ttk.Style().configure("Treeview", background="#383838",foreground="white")
    #         # main_ff.style.configure("Custom.Treeview.Heading",
    #         #     background="blue", foreground="white", relief="flat")
    #         # main_ff.style.map("Custom.Treeview.Heading",
    #         #     relief=[('active','groove'),('pressed','sunken')])
    #         # main_ff.style.configure(".", font=('arial',15))

    #         # main_ff.xsb = ttk.Scrollbar(main_ff,orient=HORIZONTAL )
    #         # main_ff.xsb.pack(side='bottom',fill=X,expand=TRUE)
            
    #         main_ff.tre = ttk.Treeview(main_ff)

    #         # main_ff.xsb.config(command=main_ff.tre.xview)
    #         main_ff.tre['column'] = main_ff.names
    #         main_ff.tre.column('#0',stretch=NO,width=0,minwidth=0)

    #         for i in main_ff.names:
    #             main_ff.tre.column(i,width=180,anchor=W,minwidth=55)
    #             main_ff.tre.heading(i,text=i,anchor=W)
                
    #         # for i in numbers:
    #         main_ff.tre.insert(parent='',index='end',iid=0,text='Parent',values=numbers)
            
            
    #         # main_ff.tre['yscroll'] = ysb.set
    #         # main_ff.tre['xscroll'] = xsb.set
    #         main_ff.tre.tag_configure('evencolumn',background='black')
    #         # main_ff.tre
    #         main_ff.tre.pack()
    #         # for i,j,k in  zip(main_ff.names,range(25),numbers):
    #         #     frame = customtkinter.CTkCanvas(main_f,width=180,height=110)
    #         #     # main_f.create_window((0, 0), window=frame, anchor="s")
    #         #     # frame.update_idletasks()
    #         #     # frame.grid_rowconfigure(0,1)
    #         #     labal = customtkinter.CTkButton(frame,text=i,font=('arial',15,'bold'),width=180,fg_color='#bdd975',text_color='#2e313b',bg_color='transparent')
    #         #     labal.pack(side='top',fill  = X,expand  = True)
    #         #     labal2 = customtkinter.CTkLabel(frame,text=k,font=('arial',15,'bold'),width=180,fg_color='#bdd975',text_color='#2e313b')
    #         #     labal2.pack(side=BOTTOM,fill  = Y,expand  = True)
    #         #     frame.pack(side = 'left',fill= Y,padx  = 10)
    #         #     # frame.grid(row=0,column = j,padx = 10,pady = 10)
    #         #     main_ff.frames_name[i]  = frame
    #         # main_f.config(scrollregion=main_f.bbox("all"))    
            
            
            
            
    #     def maker_of_dep(main_ff):
    #         conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
    #         corser = conobj.cursor()
    #         row = corser.execute("select replace(department_name,' ','_') as names from departments ")
    #         a = corser.fetchall()
    #         names = []
    #         alfa_names = []
    #         for i in range(25):
    #             names.append(a[i][0])
                
    #         # print(names)
            
    #         v = corser.execute("select department_name  from departments ")
    #         c= corser.fetchall()
    #         print(v)
    #         print(c)
    #         for  i in range(v):
    #             corser.execute("select count(*) from employees where  department_id =  (select department_id from departments where  department_name = %s);",(c[i][0],))
    #             b = corser.fetchall()
    #             alfa_names.append(b[0][0])

                
    #         return names,alfa_names
            
    #         # own.title_emp = customtkinter.CTkLabel(own,text='NO OF Employees',font=('arial',15,'bold'),width=200,fg_color='#bdd975',text_color='#2e313b')
    #         # print(own.title_emp.winfo_height())
    #         # own.title_emp.place(x=0,y=0)
    #         # c = own.conection()
    #         # own.count = customtkinter.CTkLabel(own,text=c,font=('arial',25,'bold'),width=200,fg_color='white',bg_color='red',text_color='black')
    #         # own.count.place(x = 0,y = 45)
            
            
    #     # def conection(main_f):
    #     #     conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
    #     #     corser = conobj.cursor()
    #     #     row = corser.execute('select * from employees; ')
    #     #     print(row)
    #     #     return row
    # class foote0(ttk.Frame):
    #     def __init__(main_ff,parent,controller):
    #         tk.Frame.__init__(main_ff,parent,bg=parent.main_color)
    #         # customtkinter.CTkFrame()
    #         main_ff.config(width=1000,height=250)
    #         main_ff.place(x=20,y=620)
    #         main_ff.names,numbers = main_ff.maker_of_dep()
    #         main_ff.frames_name = {}
            
    #         main_f = Frame(main_ff)
    #         main_f.pack(side= 'top',fill = 'both',expand = True)
    #         # main_ff.scroller = Scrollbar(parent,orient="horizontal")
    #         # main_ff.scroller

    #     # self.scroller.grid(row=2,column=0,columnspan=2)
        
    #     # ,xscrollcommand = h.set
    #         # main_ff.scroller.grid(row=1, column=1)
    #         for i,j,k in  zip(main_ff.names,range(25),numbers):
    #             frame = customtkinter.CTkFrame(main_f,width=180,height=110,fg_color='white')
    #             # frame.grid_rowconfigure(0,1)
    #             labal = customtkinter.CTkButton(frame,text=i,font=('arial',15,'bold'),width=180,fg_color='#bdd975',text_color='#2e313b',bg_color='transparent')
    #             labal.pack(side='top',fill  = X,expand  = True)
    #             labal2 = customtkinter.CTkLabel(frame,text=k,font=('arial',15,'bold'),width=180,fg_color='#bdd975',text_color='#2e313b')
    #             labal2.pack(side=BOTTOM,fill  = Y,expand  = True)
    #             frame.grid(row=0,column = j,padx = 10,pady = 10)
    #             main_ff.frames_name[i]  = frame
                
            
            
            
            
    #     def maker_of_dep(main_ff):
    #         conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
    #         corser = conobj.cursor()
    #         row = corser.execute("select replace(department_name,' ','_') as names from departments ")
    #         a = corser.fetchall()
    #         names = []
    #         alfa_names = []
    #         for i in range(25):
    #             names.append(a[i][0])
                
    #         # print(names)
            
    #         v = corser.execute("select department_name  from departments ")
    #         c= corser.fetchall()
    #         print(v)
    #         print(c)
    #         for  i in range(v):
    #             corser.execute("select count(*) from employees where  department_id =  (select department_id from departments where  department_name = %s);",(c[i][0],))
    #             b = corser.fetchall()
    #             alfa_names.append(b[0][0])

                
    #         return names,alfa_names
            
    #         # own.title_emp = customtkinter.CTkLabel(own,text='NO OF Employees',font=('arial',15,'bold'),width=200,fg_color='#bdd975',text_color='#2e313b')
    #         # print(own.title_emp.winfo_height())
    #         # own.title_emp.place(x=0,y=0)
    #         # c = own.conection()
    #         # own.count = customtkinter.CTkLabel(own,text=c,font=('arial',25,'bold'),width=200,fg_color='white',bg_color='red',text_color='black')
    #         # own.count.place(x = 0,y = 45)
            
            
    #     # def conection(main_f):
    #     #     conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
    #     #     corser = conobj.cursor()
    #     #     row = corser.execute('select * from employees; ')
    #     #     print(row)
    #     #     return row


    class making_img(customtkinter.CTkFrame):
        def __init__(mk,parent,controller) -> None:
            customtkinter.CTkFrame.__init__(mk,parent)
            mk.configure(width=200,height=120,corner_radius=5,fg_color = 'lightblue',border_color='black')
            # a = customtkinter.CTkFrame(,corner_radius=25)
            mk.pack(side='top')
            
            # mk.f =  Frame(mk,width=200,height=60,bg='black')
            # mk.f.pack(side='top')
        def getting_image(mk,img):
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()  
            r= corser.execute("select image from pic where id = %s",(img))
            b = corser.fetchall()
            l = str(b[0][0])
            c = l.replace('b\'','')
            c = c.replace('\'','')
            print(c)
            conobj.close()
            return c        
            
    class making_info(customtkinter.CTkFrame):
        def __init__(mkk,parent,controller,self) -> None:
            customtkinter.CTkFrame.__init__(mkk,parent)
            mkk.c = self.detail
            print(mkk.c)
            mkk.man = [ 100, 101, 102, 103, 108, 114, 120, 121, 122, 123, 124, 145, 146, 147, 148, 149, 201, 205]
            mkk.configure(width=200,height=270,corner_radius=5,fg_color = 'white')
            # a = customtkinter.CTkFrame(corner_radius=25)
            mkk.pack(side='bottom',fill=Y,expand=Y)
            
            mkk.star = ImageTk.PhotoImage(Image.open('yellow_star.png').resize((25,25)))
            mkk.star = customtkinter.CTkLabel(mkk,image=mkk.star,width=20,height=20,text='')
            mkk.star.place(x=150,y=10)
            mkk.rib = ImageTk.PhotoImage(Image.open('rib.png').resize((30,30)))
            
            mkk.rib = customtkinter.CTkLabel(mkk,image=mkk.rib,width=20,height=20,text='')
            # mkk.rib.place(x=610,y=10)
            
            
            
            
            
            mkk.name = customtkinter.CTkLabel(mkk,text='Name: ',text_color='black',font=('Copperplate Gothic Light',13))
            mkk.name.place(x=5,y=15)
            
            
            mkk.name_x = customtkinter.CTkLabel(mkk,text=mkk.c['first_name'],text_color='black',font=('Copperplate Gothic Bold',17))
            mkk.name_x.place(x=25,y=35)

            
            mkk.work = customtkinter.CTkLabel(mkk,text='Work: ',text_color='black',font=('Copperplate Gothic Light',13))
            mkk.work.place(x=5,y=65)
            
            
            
            mkk.work_x = customtkinter.CTkLabel(mkk,text=mkk.c['work'],text_color='black',font=('Copperplate Gothic Bold',17))
            mkk.work_x.place(x=25,y=85)
            
            
            
            
            mkk.salary = customtkinter.CTkLabel(mkk,text='Salary: ',text_color='black',font=('Copperplate Gothic Light',11))
            mkk.salary.place(x=5,y=115)
            
            
            
            

            mkk.salary_x = customtkinter.CTkLabel(mkk,text=mkk.c['salary'],text_color='black',font=('Copperplate Gothic Bold',17))
            mkk.salary_x.place(x=25,y=135)
            
            
            
            mkk.dep = customtkinter.CTkLabel(mkk,text='Department:  ',text_color='black',font=('Copperplate Gothic Light',10))
            mkk.dep.place(x=5,y=165)

            mkk.dep_x = customtkinter.CTkLabel(mkk,text=mkk.c['department'],text_color='black',font=('Copperplate Gothic Bold',17))
            mkk.dep_x.place(x=25,y=185)
            
            
            mkk.manager = customtkinter.CTkLabel(mkk,text='Manager:',text_color='black',font=('Copperplate Gothic Light',10))
            mkk.manager.place(x=5,y=215)

            mkk.manager_x = customtkinter.CTkLabel(mkk,text=mkk.c['manager'],text_color='black',font=('Copperplate Gothic Bold',17))
            mkk.manager_x.place(x=25,y=235)
            
            mkk.all_info  = [mkk.name_x,mkk.work_x,mkk.salary_x,mkk.dep_x,mkk.manager_x]
            # mkk.name_x = customtkinter.CTkLabel(mkk,text='pritam',text_color='black',font=('arial',20))
            # mkk.name_x.place(x=30,y=23)
            # mkk.f =  Frame(mkk,width=200,height=60,bg='black')
            # mkk.f.pack(side='bottom',fill=Y,expand=Y)
            
        def update_info(mkk):
            v= ['first_name','work','salary','department','manager']
            man = [100, 101, 102, 103, 108, 114, 120, 121, 122, 123, 124, 145, 146, 147, 148, 149, 201, 205]
            
            if mkk.c['id'] in man:
                
                mkk.rib.place_forget()
                mkk.star.place(x=150,y=10)
            else :
                mkk.star.place_forget()
                mkk.rib.place(x=150,y=10)
                
            for i,j in zip(mkk.all_info,v):
                i.configure(text =mkk.c[j] )
              
    class employee_tree(ttk.Frame):
        def __init__(em,parent,controller,self):
            ttk.Frame.__init__(em,parent)
            em.c=self
            em.config(width=600,height=500)
            em.place(x=10,y=150)
            rows = em.getting()
            print('employees_tree')
            em.names = ('id','First_name','Last_name','Email','Phone_no','Position','Salary','Manager','Department')
            em.tree_scroll = ttk.Scrollbar(em)
            em.tree_scroll.pack(side='right',fill='y')
            
            
            s = ttk.Style()
            s.theme_use('clam')
            s.configure('Treeview',backgroud='#202d45',foreground='black',rowheight=25,fieldbackground='#2a5066')
            s.configure("Treeview.Heading",background = "#8fa2c4",foreground="Black",font=('Calibri',11),relief='none')
            s.map('Treeview',background =[('selected','#316325')])
            em.data =  ttk.Treeview(em,height=20,yscrollcommand=em.tree_scroll.set,selectmode='extended')
            em.data.bind('<<TreeviewSelect>>', em.item_selected)

            em.tree_scroll.config(command=em.data.yview)
            em.data['column'] = em.names
            em.data.column('#0',stretch=NO,width=0,minwidth=0)
            
            # em.data.heading(em)
            em.data.tag_configure('oddrow',background='white')
            em.data.tag_configure('evenrow',background='#8db2f2')
            for i in em.names:
                em.data.column(i,width=100,anchor=W,minwidth=25)
                em.data.heading(i,text=i,anchor=W)
            m = 0
            global kk
            kk = 0
            for i in rows:
                if kk %2 ==0:
                    em.data.insert(parent='',index='end',iid =kk,text='',values=i,tags=('evenrow',))
                else:
                    em.data.insert(parent='',index='end',iid =kk,text='',values=i,tags=('oddrow',))
                kk +=1
            em.data.pack()
        def item_selected(em,event):
            
            em.c.detail.clear()
            column = ['id','first_name','last_name','gmail','phone_no','work','salary','manager','department']
            b = None
            for i in em.data.selection():
                a = em.data.item(i)
                v = list(a['values'])
                print(v)
                for x,y in zip(v,column):
                    em.c.detail[y] = x
            print(em.c.detail)
            em.c.info.update_info()
        def getting(em):
            record = []
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            row = corser.execute("select * from employees")
            a = corser.fetchall()
            c = []
            m = 0
            def listToString(s):
                str1 = ""
            
                for ele in s:
                    str1 += ele
                return str1
            for i in a:
                c.append(i[0])
                c.append(i[1])
                c.append(i[2])
                x= str(i[3])
                e =x.lower()+'@gmail.com'
                c.append(e)

                
                c.append(i[4])

                c.append(i[6])

                sa  = [p for p in str(i[7]) if p.isdigit()]
                l = listToString(sa)
                c.append(l)

                
                c.append(i[9])
                c.append(i[10])

                record.append(c.copy())
                m+=1
                c.clear()
            
           
            conobj.close()
            return record
    def detail_makeing(self):
        pass      
            
            
class login_sign_in(tk.Frame):
    def __init__(self,parent,controller) -> None:
        tk.Frame.__init__(self,parent,bg='#9bace0')
        
        self.hr = ImageTk.PhotoImage(Image.open('hr_log.png').resize((60,80)))

        self.hr_lab = Label(self,image=self.hr,bg='#9bace0',text='HR LOGIN',compound='left',font=('profile',25),padx=20)
        self.hr_lab.place(x=20,y=10)
        
        # self.middel_frame = Frame(width=500,height=500,bg='white')
        # self.middel_frame.place(x=550,y=150)
        
        self.middel_frame = customtkinter.CTkFrame(self,width=500,height=700,corner_radius=30,fg_color='white')
        self.middel_frame.place(x=550,y=150)
        
        
        # self.middel_frame.pack(side='bottom',expand=False,fill='none')
        # self.update_rectangle_coords(self.middel_frame, 900, 20, 100, 100)
        # self.rounded_rect(self.middel_frame, 20, 20, 60, 40, 10)
        
        self.log_label = Label(self.middel_frame,text='Login',font=('tahoma',25,'bold'),fg='#3c3e42')
        self.log_label.place(x=200,y=30)
        
        self.em = ImageTk.PhotoImage(Image.open('em.png').resize((35,35)))
        self.email_logo = Label(self.middel_frame,text='Email',font=('tahoma',25),fg='#3c3e42',image=self.em,compound='left',padx=6)
        self.email_logo.place(x=50,y=100)
        Entry(border=1,borderwidth=2,insertborderwidth=10,highlightthickness=1,validate='key')
        
        self.email_entery = EntryWithPlaceholder(master=self.middel_frame,validate='key',highlightthickness=2,highlightcolor = '#84a0fa',placeholder='Email_id',width = 20,font=('profile',25),relief  = 'flat',bd=1,bg = '#d3d8e8',border=1,borderwidth=5)
        self.email_entery.place(x=50,y=160)
        
        # password
        self.pa = ImageTk.PhotoImage(Image.open('pas_img.png').resize((35,35)))
        self.pass_logo = Label(self.middel_frame,text='Password',font=('tahoma',25),width=0,fg='#3c3e42',image=self.pa,compound='left')
        self.pass_logo.place(x=50,y=240)
        Entry(border=1,borderwidth=2,insertborderwidth=10,highlightthickness=1)
        
        self.pass_entery = EntryWithPlaceholder(master=self.middel_frame,highlightthickness=2,validate='key',highlightcolor = '#84a0fa',placeholder='Password',width = 20,font=('profile',25),relief  = 'flat',bd=1,bg = '#d3d8e8',border=1,borderwidth=5)
        self.pass_entery.place(x=50,y=300)
        self.bind('<Return>',func=self.focus_in)
        
        
        # image=self.img,compound='left',padx=10,relief='flat'
        self.img = ImageTk.PhotoImage(Image.open('login_png.png').resize((30,30)))
        self.log_but = customtkinter.CTkButton(self.middel_frame,text='Log in', command=lambda:self.login_pro(self.email_entery.get(),self.pass_entery.get(),controller)  ,font=('profile',25),image=self.img,hover=True,hover_color='#de597a',height=50,width=300)
        self.log_but.place(x=95,y=400)
        
        self.line = Frame(self.middel_frame,width=400,height=1,bg='black')
        self.line.place(x=50,y=480)
        
        self.box = Frame(self.middel_frame,width=30,height=30,bg='black')
        self.box.place(x=235,y=465)
        
        self.or_lab = Label(self.box,text='or',font=('profile',15))
        self.or_lab.pack(side='top')
        
        self.gog =  ImageTk.PhotoImage(Image.open('gog.png').resize((30,30)))
        self.google = Button(self.middel_frame,image=self.gog,relief='flat',bd=0)
        self.google.bind('<Button>',func=lambda b :self.google.config(activebackground='white',bg='white'))
        self.google.place(x=227,y=520)
        
        
        self.sig =  ImageTk.PhotoImage(Image.open('sign.png').resize((30,30)))
        self.sign_up = customtkinter.CTkButton(self.middel_frame,text='Sign Up',font=('profile',25),image=self.sig,hover=True,hover_color='#84a0fa',height=50,width=300,command=lambda:controller.switch('sign_up'))
        self.sign_up.place(x=95,y=570)
    def focus_in(self,event):
        print('focus_in ')
        self.email_entery.config(validate='focusout')
        
        self.pass_entery.config(validate='focus')
        
        
    def log_second(self,controller):
        self.pack_forget()
        print('log_second')
        controller.inital_frame(controller.main_frame)
        
        
    
    def login_pro(self,email,pas,controller):
        
        print('yes it is taking')
        print(email)
        print(pas)
        
        import pymysql

        if email != 'Email_id' and pas != 'Password':
            conobj = pymysql.connect(host="localhost",port=3306,user="root",password="test!@#123",database="hr")    
            corser = conobj.cursor()
            row = corser.execute('select * from login where email = %s and password  = %s',(email,pas))
            if row==0:
                print('no user')
            else:
                self.log_second(controller)  
        
        else:   
            print('no')
        conobj.close()
class sign_up(tk.Frame):
    def __init__(self,parent,controller) -> None:
        tk.Frame.__init__(self,parent,bg='#9bace0')
        
        self.hr = ImageTk.PhotoImage(Image.open('hr_log.png').resize((60,80)))

        self.hr_lab = Label(self,image=self.hr,bg='#9bace0',text='HR LOGIN',compound='left',font=('profile',25),padx=20)
        self.hr_lab.place(x=20,y=10)
        
        # self.middel_frame = Frame(width=500,height=500,bg='white')
        # self.middel_frame.place(x=550,y=150)
        
        self.middel_frame = customtkinter.CTkFrame(self,width=500,height=730,corner_radius=30,fg_color='white')
        self.middel_frame.place(x=550,y=100)
        # self.middel_frame.pack(side='bottom',expand=False,fill='none')
        # self.update_rectangle_coords(self.middel_frame, 900, 20, 100, 100)
        # self.rounded_rect(self.middel_frame, 20, 20, 60, 40, 10)
        
        self.log_label = Label(self.middel_frame,text='Sign Up',font=('tahoma',25,'bold'),fg='#3c3e42')
        self.log_label.place(x=200,y=30)
        
        self.na = ImageTk.PhotoImage(Image.open('na_img.png').resize((35,35)))
        self.name_logo = Label(self.middel_frame,text='Name',font=('tahoma',25),fg='#3c3e42',image=self.na,compound='left',padx=5)
        self.name_logo.place(x=50,y=100)
        
        self.name_entery = EntryWithPlaceholder(master=self.middel_frame,highlightthickness=2,highlightcolor = '#84a0fa',placeholder='Name',width = 20,font=('profile',25),relief  = 'flat',bd=1,bg = '#d3d8e8',border=1,borderwidth=5)
        self.name_entery.place(x=50,y=150)
        
        # self.email_logo = Label(self.middel_frame,text='Email',font=('tahoma',25),fg='#3c3e42')
        # self.email_logo.place(x=50,y=100)
        # # Entry(border=1,borderwidth=2,insertborderwidth=10,highlightthickness=1,validate='key')
        
        # self.email_entery = EntryWithPlaceholder(master=self.middel_frame,highlightthickness=2,highlightcolor = '#84a0fa',placeholder='Email_id',width = 20,font=('profile',25),relief  = 'flat',bd=1,bg = '#d3d8e8',border=1,borderwidth=5)
        # self.email_entery.place(x=50,y=160)
        
        # password
        self.em = ImageTk.PhotoImage(Image.open('em.png').resize((35,35)))
        self.email_logo = Label(self.middel_frame,text='Email',font=('tahoma',25),width=0,fg='#3c3e42',image=self.em,compound='left',padx=5)
        self.email_logo.place(x=50,y=230)
        # Entry(border=1,borderwidth=2,insertborderwidth=10,highlightthickness=1)
        
        self.Email_entery = EntryWithPlaceholder(master=self.middel_frame,highlightthickness=2,highlightcolor = '#84a0fa',placeholder='Email',width = 20,font=('profile',25),relief  = 'flat',bg = '#d3d8e8',border=1,borderwidth=5)
        self.Email_entery.place(x=50,y=290)
        # image=self.img,compound='left',padx=10,relief='flat'


    # log in but
        self.img = ImageTk.PhotoImage(Image.open('login_png.png').resize((30,30)))
        self.log_but = customtkinter.CTkButton(self.middel_frame,text='Create',font=('profile',25),image=self.img,hover=True,hover_color='#de597a',height=50,width=300)
        self.log_but.place(x=95,y=600)
        # l
        
        self.pas = ImageTk.PhotoImage(Image.open('pas_img.png').resize((30,30)))
        self.pass_logo = Label(self.middel_frame,text='Password',font=('tahoma',25),width=0,fg='#3c3e42',image=self.pas ,compound='left')
        self.pass_logo.place(x=50,y=360)
        # Entry(border=1,borderwidth=2,insertborderwidth=10,highlightthickness=1)
        
        self.pass_entery = EntryWithPlaceholder(master=self.middel_frame,highlightthickness=2,highlightcolor = '#84a0fa',placeholder='Password',width = 20,font=('profile',25),relief  = 'flat',bd=1,bg = '#d3d8e8',border=1,borderwidth=5,show = '*')
        self.pass_entery.place(x=50,y=410)
        
        
        
        self.con_pass_logo = Label(self.middel_frame,text='Confirm Password',font=('tahoma',25),width=0,fg='#3c3e42',image=self.pas ,compound='left')
        self.con_pass_logo.place(x=50,y=470)
        # Entry(border=1,borderwidth=2,insertborderwidth=10,highlightthickness=1)
        
        self.con_pass_entery = EntryWithPlaceholder(master=self.middel_frame,highlightthickness=2,highlightcolor = '#84a0fa',placeholder='Password',width = 20,font=('profile',25),relief  = 'flat',bd=1,bg = '#d3d8e8',border=1,borderwidth=5,show = '*')
        self.con_pass_entery.place(x=50,y=520)
        
        self.back = ImageTk.PhotoImage(Image.open('back_log.png').resize((30,30)))
        self.back_log = customtkinter.CTkButton(self.middel_frame,text='Back To login',image=self.back,compound='right',fg_color='white',hover_color = '#7aa3c4',text_color='black',command=lambda:controller.switch("login_sign"))
        self.back_log.bind('<Button>',command=lambda a : self.back_log.config(text_color = 'white'))
        self.back_log.place(x=180,y=690)
        # self.line = Frame(self.middel_frame,width=400,height=1,bg='black')
        # self.line.place(x=50,y=480)
        
        # self.box = Frame(self.middel_frame,width=30,height=30,bg='black')
        # self.box.place(x=235,y=465)
        
        # self.or_lab = Label(self.box,text='or',font=('profile',15))
        # self.or_lab.pack(side='top')
        
        # self.gog =  ImageTk.PhotoImage(Image.open('gog.png').resize((30,30)))
        # self.google = Button(self.middel_frame,image=self.gog,relief='flat',bd=0)
        # self.google.bind('<Button>',func=lambda b :self.google.config(activebackground='white',bg='white'))
        # self.google.place(x=227,y=520)
        
        
        # self.sig =  ImageTk.PhotoImage(Image.open('sign.png').resize((30,30)))
        # self.sign_up = customtkinter.CTkButton(self.middel_frame,text='Sign Up',font=('profile',25),image=self.sig,hover=True,hover_color='#84a0fa',height=50,width=300)
        # self.sign_up.place(x=95,y=570)       
        
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey',**keyw):
        super().__init__(master)
        
        if keyw:
            print("yes")
            self.config(**keyw)
            del keyw
        else:
            print("no")

        self.placeholder = placeholder
        self.placeholder_color = '#9fa2ab'
        self.default_fg_color = self['fg']
        
        print(self['bd'])

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class GradientFrame(customtkinter.CTkCanvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="red", color2="black", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")
if __name__ == '__main__':
    screen  = sc()
    screen.resizable(width=False,height=False)
    screen.state('zoomed')
    screen.mainloop()