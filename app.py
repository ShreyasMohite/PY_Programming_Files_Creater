from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import touch
import tkinter.filedialog



class File:
    def __init__(self,root):
        self.root=root
        self.root.title("Programming File Creater")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo310.ico")
        self.root.resizable(0,0)

        path=StringVar()
        filename=StringVar()
        filextention=StringVar()
#======================================================================================#

        def clear():
            filename.set("")
            path.set("")
            lab_filecreated.config(text="")
            lab_selectpath.config(text="Select Path")
            filextention.set("Select File Extention")

        def browse():
            #golbal files
            a=tkinter.filedialog.askdirectory(title="choose folder")
            path.set(a)
            if a:
                lab_selectpath.config(text="Path Is Selected")
            #files=a

        def genrate():
            try:
                if path.get()!="":
                    a=path.get()
                    lab_filecreated.config(text="File Created Successfully")

                    
                    if filextention.get()!="Select File Extention":
                        if filename.get()!="":

                            if filextention.get()=="python" and filename.get()!="":
                                touch.touch(a+"/{}.py".format(filename.get()))
                            
                            if filextention.get()=="c" and filename.get()!="":
                                touch.touch(a+"/{}.c".format(filename.get()))
                        

                            if filextention.get()=="c++" and filename.get()!="":
                                touch.touch(a+"/{}.cpp".format(filename.get()))
                            

                            if filextention.get()=="cs" and filename.get()!="":
                                touch.touch(a+"/{}.cs".format(filename.get()))
                        
                            if filextention.get()=="java" and filename.get()!="":
                                touch.touch(a+"/{}.java".format(filename.get()))
                            
                            if filextention.get()=="javascript" and filename.get()!="":
                                touch.touch(a+"/{}.js".format(filename.get()))
                            
                            if filextention.get()=="html" and filename.get()!="":
                                touch.touch(a+"/{}.html".format(filename.get()))
                            
                            if filextention.get()=="css" and filename.get()!="":
                                touch.touch(a+"/{}.css".format(filename.get()))
                            
                            if filextention.get()=="json" and filename.get()!="":
                                touch.touch(a+"/{}.json".format(filename.get()))
                            
                            if filextention.get()=="xml" and filename.get()!="":
                                touch.touch(a+"/{}.xml".format(filename.get()))
                        
                            if filextention.get()=="go" and filename.get()!="":
                                touch.touch(a+"/{}.go".format(filename.get()))
                            
                            if filextention.get()=="less" and filename.get()!="":
                                touch.touch(a+"/{}.less".format(filename.get()))
                        
                            if filextention.get()=="scss" and filename.get()!="":
                                touch.touch(a+"/{}.scss".format(filename.get()))

                            if filextention.get()=="text" and filename.get()!="":
                                touch.touch(a+"/{}.txt".format(filename.get()))

                            if filextention.get()=="visualbasic" and filename.get()!="":
                                touch.touch(a+"/{}.vb".format(filename.get()))

                            if filextention.get()=="swift" and filename.get()!="":
                                touch.touch(a+"/{}.swift".format(filename.get()))

                            if filextention.get()=="shell" and filename.get()!="":
                                touch.touch(a+"/{}.sh".format(filename.get()))

                            if filextention.get()=="php" and filename.get()!="":
                                touch.touch(a+"/{}.php".format(filename.get()))

                            if filextention.get()=="perl" and filename.get()!="":
                                touch.touch(a+"/{}.pl".format(filename.get()))

                            if filextention.get()=="kotlin" and filename.get()!="":
                                touch.touch(a+"/{}.kt".format(filename.get()))

                            if filextention.get()=="Asp" and filename.get()!="":
                                touch.touch(a+"/{}.asp".format(filename.get()))

                            if filextention.get()=="jsp" and filename.get()!="":
                                touch.touch(a+"/{}.jsp".format(filename.get()))
                            
                            if filextention.get()=="Aspx" and filename.get()!="":
                                touch.touch(a+"/{}.aspx".format(filename.get()))

                            if filextention.get()=="Coldfusion" and filename.get()!="":
                                touch.touch(a+"/{}.cfm".format(filename.get()))

                            if filextention.get()=="Erlang" and filename.get()!="":
                                touch.touch(a+"/{}.yaws".format(filename.get()))

                            if filextention.get()=="R" and filename.get()!="":
                                touch.touch(a+"/{}.r".format(filename.get()))
                            
                            if filextention.get()=="ruby" and filename.get()!="":
                                touch.touch(a+"/{}.rb".format(filename.get()))

                            if filextention.get()=="dart" and filename.get()!="":
                                touch.touch(a+"/{}.dart".format(filename.get()))

                            if filextention.get()=="scala" and filename.get()!="":
                                touch.touch(a+"/{}.scala".format(filename.get()))

                            if filextention.get()=="rust" and filename.get()!="":
                                touch.touch(a+"/{}.rust".format(filename.get()))

                            if filextention.get()=="matlab" and filename.get()!="":
                                touch.touch(a+"/{}.m".format(filename.get()))

                            
                        else:
                            tkinter.messagebox.showerror("Error","Please write a proper filename")

                    else:
                        tkinter.messagebox.showerror("Error","Please choose an extension ")
                else:
                    tkinter.messagebox.showerror("Error","Please choose path first")
            except Exception as e:
                print(e)

#======================================================================================#
        def on_enter1(e):
            but_browsepath['background']="black"
            but_browsepath['foreground']="cyan"
  
        def on_leave1(e):
            but_browsepath['background']="SystemButtonFace"
            but_browsepath['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_generate['background']="black"
            but_generate['foreground']="cyan"
  
        def on_leave3(e):
            but_generate['background']="SystemButtonFace"
            but_generate['foreground']="SystemButtonText"

#======================================================================================#
        mainframe=Frame(self.root,width=500,height=400,bd=4,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=493,height=300,bd=4,relief="ridge",bg="#70d6ff")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=493,height=90,relief="ridge",bd=3,bg="#272640")
        secondframe.place(x=0,y=300)

#======================================================================================#
        but_browsepath=Button(firstframe,text="Browse Path",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=browse)
        but_browsepath.place(x=160,y=15)
        but_browsepath.bind("<Enter>",on_enter1)
        but_browsepath.bind("<Leave>",on_leave1)

        lab_selectpath=Label(firstframe,text="Select Path",font=('times new roman',12),bg="#70d6ff")
        lab_selectpath.place(x=200,y=90)

        ent_path=Entry(firstframe,width=55,font=('times new roman',12),relief="ridge",bd=4,textvariable=path)
        ent_path.place(x=15,y=120)

        lab_filecreated=Label(firstframe,text="",font=('times new roman',12),bg="#70d6ff",fg="red")
        lab_filecreated.place(x=170,y=150)

        lab_selectfilename=Label(firstframe,text="Select FileName",font=('times new roman',12),bg="#70d6ff")
        lab_selectfilename.place(x=20,y=200)

        ent_filename=Entry(firstframe,width=30,font=('times new roman',12),relief="ridge",bd=4,textvariable=filename)
        ent_filename.place(x=200,y=200)


        lab_selectfilename=Label(firstframe,text="Select File Extention",font=('times new roman',12),bg="#70d6ff")
        lab_selectfilename.place(x=20,y=250)

        fileselect=["python","c","c++","java","cs","css","json","javascript","html",\
                    "xml","go","less","scss","visualbasic","swift","shell","php","perl"\
                    ,"kotlin","Asp","jsp","Aspx","Coldfusion","Erlang","R","ruby","dart"\
                    ,"matlab","scala","rust"]
        fileselect_combo=Combobox(firstframe,values=fileselect,font=('arial',12),width=25,state="readonly",textvariable=filextention)
        fileselect_combo.set("Select File Extention")
        fileselect_combo.place(x=200,y=250)
            

#======================================================================================#


        but_clear=Button(secondframe,text="Clear",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=clear)
        but_clear.place(x=30,y=15)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

        but_generate=Button(secondframe,text="Generate File",font=('times new roman',12,'bold'),width=17,height=2,cursor="hand2",command=genrate)
        but_generate.place(x=290,y=15)
        but_generate.bind("<Enter>",on_enter3)
        but_generate.bind("<Leave>",on_leave3)



if __name__ == "__main__":
    root=Tk()
    app=File(root)
    root.mainloop()