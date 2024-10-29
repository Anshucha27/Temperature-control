from tkinter import*
def convertF():
 c=eval(n1.get())
 f=(c*9/5)+32
 out.config(text=str(f))
def convertC():
 f=eval(n1.get())
 c=(f-32)*5/9
 out.config(text=str(c))
root=Tk()
root.title("Temperature Converter")
root.geometry("500x400")
root.config(bg="skyblue")
root.resizable(False,False)
lbl=Label(root,text="Temperature Converter",fg="white",bg="black",font=("Arial 20 bold"))
lbl.place(x=90,y=20)
n1=Entry(root,font=("Arial 15"))
n1.place(x=130,y=70)
out=Label(root,fg="black",font=("Arial 15 bold"))
out.place(x=200,y=130)
btn1=Button(root,text="C to F",font=("Arial 15"),fg="black",command=convertF)
btn1.place(x=100,y=280)
btn2=Button(root,text="F to C",font=("Arial 15"),fg="black",command=convertC)
btn2.place(x=300,y=280)
root.mainloop()
