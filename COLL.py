from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import sqlite3
conn = sqlite3.connect('Database.db')
c = conn.cursor()



def main():
    root = Tk()
    app = Window1(root)


class Window1:

    def __init__(self, master):
        self.master = master
        self.master.title("RAMRAO ADIK INSTITUTE OF TECHNOLOGY")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame,text="RAMRAO ADIK INSTITUTE OF TECHNOLOGY",font=('arial',40,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,pady=40,columnspan=2)

        self.LoginFrame1 = Frame(self.frame,width=1000,height=300,bd=20,relief='ridge')
        self.LoginFrame1.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.LoginFrame2.grid(row=2,column=0)

        self.LoginFrame3 = Frame(self.frame,width=100,height=200,bd=20,relief='ridge')
        self.LoginFrame3.grid(row=3,column=0,pady=2)

        #---------------------------------------------------

        self.lblusername = Label(self.LoginFrame1,text='Username',font=('arial',30,'bold'),bd=20)
        self.lblusername.grid(row=0,column=0)

        self.txtusername = Entry(self.LoginFrame1,text='Username',font=('arial',15,'bold'),bd=20,textvariable=self.Username)
        self.txtusername.grid(row=0,column=1)

        self.lblpassword = Label(self.LoginFrame1,text='Password',font=('arial',30,'bold'),bd=20)
        self.lblpassword.grid(row=1,column=0)

        self.txtpassword = Entry(self.LoginFrame1,text='Password',font=('arial',15,'bold'),bd=20,textvariable=self.Password, show="*")
        self.txtpassword.grid(row=1,column=1)

        

        #---------------------------------------------------------

        


        #---------------------------------------------------------
        self.btnLogin = Button(self.LoginFrame2 ,text="Login",width=15,font=('arial',20,'bold'), command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)
        self.btnReset = Button(self.LoginFrame2 ,text="Reset",width=15,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)
        self.btnExit = Button(self.LoginFrame2 ,text="Exit",width=15,font=('arial',20,'bold'), command=self.iExit)
        self.btnExit.grid(row=0,column=2)
        
        #------------------------------------------------------                       

        self.btnStudent = Button(self.LoginFrame3 ,text="STUDENT'S RECORD",font=('arial',20,'bold'),state=DISABLED,
                                                                                 command=self.studentRec)
        self.btnStudent.grid(row=0,column=0)

        self.btnTeacher = Button(self.LoginFrame3 , text="TEACHER'S RECORD",font=('arial',20,'bold'),state=DISABLED,
                                                                                  command=self.teacherRec)
        self.btnTeacher.grid(row=0, column=1,padx=22,pady=8)



        #------------------------------------------------------------

    def Login_System(self):

        user = (self.Username.get())
        pas = (self.Password .get())

        if (user == str('dypatil')) and (pas == str('12345')):
            

            self.btnStudent.config(state=NORMAL)
            self.btnTeacher.config(state=NORMAL)

        else:

            tkinter.messagebox.showwarning("RAMRAO ADIK INSTITUTE OF TECHNOLOGY","You have entered invalid details")

            self.btnStudent.config(state=DISABLED)
            self.btnTeacher.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtusername.focus()

    def Reset(self):

        self.btnStudent.config(state=DISABLED)
        self.btnTeacher.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtusername.focus()


    def iExit(self):

        self.iExit= tkinter.messagebox.askyesno("RAMRAO ADIK INSTITUTE OF TECHNOLOGY","Do you want to exit")

        if self.iExit >0:
            

            self.master.destroy()
            return

        

    
            
                
                

        
    

    def studentRec(self):
         

        self.newWindow = Toplevel(self.master)
        self.app = Student(self.newWindow)

    def teacherRec(self):

        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


class Student:

    def __init__(self,root):

        self.root = root
        self.root.title("----------------STUDENT'S RECORD---------------------")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='white')



        self.entryName = StringVar()
        self.entryAdd = StringVar()
        self.entryMobileNo = StringVar()
        self.lblentry = StringVar()
        self.lblDept = StringVar()
        self.lblYear = StringVar()

        #def iReset():

          #  self.entryName.set("")
          #  self.entryAdd.set("")
        #    self.entryMobileNo.set("")
            #self.lblentry.set("")
            #self.lblDept.set("")
          #  self.lblYear.set("")

        #def iclearImage():

         #   iReset()
          #  cont.delete("all")

        
            


        #def iDelete():

         #   iDelete  = tkinter.messagebox.askyesno("Student's Record","Confirm if you want to permanently delete the records")


            #if iDelete >0:
            #    iReset()
                #self.txtdisplayR.delete("1.0", END)
            #return


        def iExit():

            iExit = tkinter.messagebox.askyesno("Student's Record","Confirm if you want to Exit")

            if iExit >0:
                root.destroy()
                return

        def iDisplay():

            self.txtdisplayR.insert(END, "\t\t"+str(self.entryName.get())+"\t\t\t"+ str(self.entryAdd.get())+"\t\t\t"+ str(self.entryMobileNo.get())+"\t\t\t"+ str(self.lblentry.get())+"\t\t\t"+ str(self.lblDept.get())+"\t\t"+ str(self.lblYear.get())+ "\n")


        #-----------------------------Creating Frames-------------------------------

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=30, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=70, font=('arial', 20, 'bold'), text="STUDENT'S RECORD", padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, width=1350, height=50, padx=20, bd=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, width=1350, height=400, padx=20, bd=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, width=1300, height=200, padx=20, bd=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        dataFrameLeft = LabelFrame(DataFrame, width=800, height= 200, font=('arial', 12, 'bold'), text="STUDENT DETAILS", padx=20, bd=10, relief=RIDGE)
        dataFrameLeft.pack(side=LEFT)

        dataFrameRight = LabelFrame(DataFrame, width=450, height=200, font=('arial', 12, 'bold'),text="STUDENT PICTURE", padx=20, bd=10, relief=RIDGE)
        dataFrameRight.pack(side=RIGHT)



        #--------------------------------------Creating Widgets---------------------------------------

        self.lblName = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Name:', padx=2, pady=2)
        self.lblName .grid(row=0, column=0, sticky=W)

        self.entryName = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=self.entryName)
        self.entryName .grid(row=0, column=1, sticky=W)

        self.lblAdd = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Address:', padx=2, pady=2)
        self.lblAdd.grid(row=1, column=0, sticky=W)

        self.entryAdd = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=self.entryAdd)
        self.entryAdd.grid(row=1, column=1, sticky=W)

        self.lblMobileNo = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Contact No:', padx=2, pady=2)
        self.lblMobileNo.grid(row=2, column=0, sticky=W)

        self.entryMobileNo = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=self.entryMobileNo)
        self.entryMobileNo.grid(row=2, column=1, sticky=W)

        self.lblGender = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Gender:', padx=2, pady=2)
        self.lblGender.grid(row=3, column=0, sticky=W)

        self.lblentry = ttk.Combobox(dataFrameLeft, font=('arial', 8, 'bold'), state='readonly', textvariable=self.lblentry)
        self.lblentry["values"] = ('', 'M', 'F')
        self.lblentry.current(0)
        self.lblentry.grid(row=3, column=1)

        self.lblDept = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Department:', padx=2, pady=2)
        self.lblDept.grid(row=4, column=0, sticky=W)

        self.lblDept = ttk.Combobox(dataFrameLeft, font=('arial', 8, 'bold'), state='readonly',textvariable=self.lblDept)
        self.lblDept["values"] = ('', 'EXTC', 'IT', 'CE', 'EE')
        self.lblDept.current(0)
        self.lblDept.grid(row=4, column=1)

        self.lblYear = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Year:', padx=2, pady=2)
        self.lblYear.grid(row=5, column=0, sticky=W)

        self.lblYear = ttk.Combobox(dataFrameLeft, font=('arial', 8, 'bold'), state='readonly', textvariable=self.lblYear)
        self.lblYear["values"] = ('', 'FE', 'SE', 'TE', 'BE')
        self.lblYear.current(0)
        self.lblYear.grid(row=5, column=1)

        #------------------Creating Images-------------------------------


        #image1 = PhotoImage(file="C:\\Users\\Anupama Jadhav\\Desktop\\Capture1.png")

        #def pic1():
            #cont.delete("all")

            #image = cont.create_image(200,100, image=image1)


        #image2 = PhotoImage(file="C:\\Users\\Anupama Jadhav\\Desktop\\Capture2.png")

        #def pic2():
            #cont.delete("all")

            #image = cont.create_image(200, 100, image=image2)

        #image3 = PhotoImage(file="C:\\Users\\Anupama Jadhav\\Desktop\\Capture3.png")

        #def pic3():
            #cont.delete("all")

            #image = cont.create_image(200, 100, image=image3)

        #



        #def iPhoto():

            #user1 = entryName.get()

            #if (user1 == str('Akshat')):
                #pic1()

            #elif (user1 == str('Sufiyaan')):
                #pic2()


            #else:
                #pic3()



        #--------------------------Creating Buttons----------------------------

        #self.imagebutton = Button(dataFrameRight, text='Image', font=('arial', 12, 'bold'), width=30, height=1, bd=4,
                                  #command=iPhoto).grid(row=1, column=0)

        # self.imagebutton1 = Text(dataFrameRight, font=('arial', 10, 'bold'), pady=4, padx=2, width=10, height=10)
        # self.imagebutton1.grid(row=0, column=1, sticky=W)

        # dataFrameRight1 = Button(dataFrameRight, width=10, height=2, font=('arial', 12, 'bold'),
        #                          text="Image", padx=20, bd=10, command=iPhoto, relief=RIDGE)
        # dataFrameRight1.grid()

        # dataFrameRight2 = Text(dataFrameRight, width=40, height=2, font=('arial', 12, 'bold'), padx=20, bd=10,
        #                        relief=RIDGE)
        # dataFrameRight2.grid(row=0, column=0)


        def add_database():

            val1=self.entryName.get()
            val2=self.entryAdd.get()
            val3=self.entryMobileNo.get()
            val4=self.lblentry.get()
            val5=self.lblDept.get()
            val6=self.lblYear.get()

            sql = c.execute("INSERT INTO 'Database' (Name, Address, MobileNo, Gender, Department, year) VALUES (?,?,?,?,?,?)",(val1,val2,val3,val4,val5,val6))
           # c.execute(sql,(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6))
            conn.commit()
            




        self.displaybutton = Button(ButtonFrame, text='Display Data', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iDisplay).grid(row=0, column=0)
        self.deletebutton = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=add_database).grid(row=0, column=1)
        #self.resetbutton = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iclearImage).grid(row=0, column=2)
        self.exitbutton = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iExit).grid(row=0, column=3)



        # self.lblImage = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Image', padx=2, pady=2)
        # self.lblImage.grid(row=6, column=0, sticky=W)
        # self.lblImage = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=image)
        # self.lblImage.grid(row=6, column=1, sticky=W)

        #--------------------------Displaying the data--------------------------

        self.lbldisplay = Label(FrameDetail, font=('arial', 12, 'bold'), pady=8, text="Name\t\tAddress\t\tContact_No\tGender\t\tDepartment\t   Year ",)
        self.lbldisplay.grid(row=0, column=0)

        self.txtdisplayR = Text(FrameDetail, font=('arial', 10, 'bold'), pady=4, padx=2, width=150, height=8)
        self.txtdisplayR.grid(row=1, column=0, sticky=W)



#


class Window3:

     def __init__(self,root):

        self.root = root
        self.root.title("----------------TEACHER'S RECORD---------------------")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='white')



        entryName = StringVar()
        entryAdd = StringVar()
        entryMobileNo = StringVar()
        lblentry = StringVar()
        lblDept = StringVar()
        lblYear = StringVar()

        def iReset():

            entryName.set("")
            entryAdd.set("")
            entryMobileNo.set("")
            lblentry.set("")
            lblDept.set("")
            lblYear.set("")

        def iclearImage():

            iReset()
            cont.delete("all")


        def iDelete():

            iDelete  = tkinter.messagebox.askyesno("Teacher's Record","Confirm if you want to permanently delete the records")


            if iDelete >0:
                iReset()
                self.txtdisplayR.delete("1.0", END)
            return


        def iExit():

            iExit = tkinter.messagebox.askyesno("Teacher's Record","Confirm if you want to Exit")

            if iExit >0:
                root.destroy()
                return

        def iDisplay():

            self.txtdisplayR.insert(END, "\t\t"+str(entryName.get())+"\t\t\t"+ str(entryAdd.get())+"\t\t\t"+ str(entryMobileNo.get())+"\t\t\t"+ str(lblentry.get())+"\t\t\t"+ str(lblDept.get())+"\t\t"+ str(lblYear.get())+ "\n")


        #-----------------------------Creating Frames-------------------------------

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=30, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, width=70, font=('arial', 20, 'bold'), text="TEACHER'S RECORD", padx=12)
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, width=1350, height=50, padx=20, bd=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, width=1350, height=400, padx=20, bd=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, width=1300, height=200, padx=20, bd=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        dataFrameLeft = LabelFrame(DataFrame, width=800, height= 200, font=('arial', 12, 'bold'), text="TEACHER DETAILS", padx=20, bd=10, relief=RIDGE)
        dataFrameLeft.pack(side=LEFT)

        dataFrameRight = LabelFrame(DataFrame, width=450, height=200, font=('arial', 12, 'bold'),text="TEACHER PICTURE", padx=20, bd=10, relief=RIDGE)
        dataFrameRight.pack(side=RIGHT)



        #--------------------------------------Creating Widgets---------------------------------------

        self.lblName = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Name:', padx=2, pady=2)
        self.lblName .grid(row=0, column=0, sticky=W)

        self.entryName = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=entryName)
        self.entryName .grid(row=0, column=1, sticky=W)

        self.lblAdd = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Address:', padx=2, pady=2)
        self.lblAdd.grid(row=1, column=0, sticky=W)

        self.entryAdd = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=entryAdd)
        self.entryAdd.grid(row=1, column=1, sticky=W)

        self.lblMobileNo = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Contact No:', padx=2, pady=2)
        self.lblMobileNo.grid(row=2, column=0, sticky=W)

        self.entryMobileNo = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=entryMobileNo)
        self.entryMobileNo.grid(row=2, column=1, sticky=W)

        self.lblGender = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Gender:', padx=2, pady=2)
        self.lblGender.grid(row=3, column=0, sticky=W)

        self.lblentry = ttk.Combobox(dataFrameLeft, font=('arial', 8, 'bold'), state='readonly', textvariable=lblentry)
        self.lblentry["values"] = ('', 'M', 'F')
        self.lblentry.current(0)
        self.lblentry.grid(row=3, column=1)

        self.lblDept = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Department:', padx=2, pady=2)
        self.lblDept.grid(row=4, column=0, sticky=W)

        self.lblDept = ttk.Combobox(dataFrameLeft, font=('arial', 8, 'bold'), state='readonly',textvariable=lblDept)
        self.lblDept["values"] = ('', 'EXTC', 'IT', 'CE', 'EE')
        self.lblDept.current(0)
        self.lblDept.grid(row=4, column=1)

        self.lblYear = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Role:', padx=2, pady=2)
        self.lblYear.grid(row=5, column=0, sticky=W)

        self.lblYear = ttk.Combobox(dataFrameLeft, font=('arial', 8, 'bold'), state='readonly', textvariable=lblYear)
        self.lblYear["values"] = ('','Professor','Assistant Professor','HOD','Principal','Vise-Principal')
        self.lblYear.current(0)
        self.lblYear.grid(row=5, column=1)

        #------------------Creating Images-------------------------------


        cont = Canvas(dataFrameRight, width=450, height=200)
        cont.grid(row=0, column=0)

        #
        
        image2 = PhotoImage(file="C:\\Users\\Anupama Jadhav\\Desktop\\Capture4.png")

        def pic4():
            
            cont.delete("all")

            image = cont.create_image(200, 100, image=image2)
            

        image3 = PhotoImage(file="C:\\Users\\Anupama Jadhav\\Desktop\\Capture3.png")

        def pic3():
            cont.delete("all")

            image = cont.create_image(200, 100, image=image3)


        #



        def iPhoto():

            user1 = entryName.get()

            if (user1 == str('Madhav')):
                pic4()

            else:
                pic3()

            

            #



        #--------------------------Creating Buttons----------------------------

        self.imagebutton = Button(dataFrameRight, text='Image', font=('arial', 12, 'bold'), width=30, height=1, bd=4,
                                  command=iPhoto).grid(row=1, column=0)

        # self.imagebutton1 = Text(dataFrameRight, font=('arial', 10, 'bold'), pady=4, padx=2, width=10, height=10)
        # self.imagebutton1.grid(row=0, column=1, sticky=W)

        # dataFrameRight1 = Button(dataFrameRight, width=10, height=2, font=('arial', 12, 'bold'),
        #                          text="Image", padx=20, bd=10, command=iPhoto, relief=RIDGE)
        # dataFrameRight1.grid()

        # dataFrameRight2 = Text(dataFrameRight, width=40, height=2, font=('arial', 12, 'bold'), padx=20, bd=10,
        #                        relief=RIDGE)
        # dataFrameRight2.grid(row=0, column=0)




        self.displaybutton = Button(ButtonFrame, text='Display Data', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iDisplay).grid(row=0, column=0)
        self.deletebutton = Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iDelete).grid(row=0, column=1)
        self.resetbutton = Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iclearImage).grid(row=0, column=2)
        self.exitbutton = Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=30, height=1, bd=4, command=iExit).grid(row=0, column=3)



        # self.lblImage = Label(dataFrameLeft, font=('arial', 12, 'bold'), text='Image', padx=2, pady=2)
        # self.lblImage.grid(row=6, column=0, sticky=W)
        # self.lblImage = Entry(dataFrameLeft, font=('arial', 8, 'bold'), width=25, textvariable=image)
        # self.lblImage.grid(row=6, column=1, sticky=W)

        #--------------------------Displaying the data--------------------------

        self.lbldisplay = Label(FrameDetail, font=('arial', 12, 'bold'), pady=8, text="Name\t\tAddress\t\tContact_No\tGender\t\tDepartment\t   Year ",)
        self.lbldisplay.grid(row=0, column=0)

        self.txtdisplayR = Text(FrameDetail, font=('arial', 10, 'bold'), pady=4, padx=2, width=150, height=8)
        self.txtdisplayR.grid(row=1, column=0, sticky=W)


if __name__ == '__main__':
    main()
