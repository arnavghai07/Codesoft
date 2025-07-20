from tkinter import *
root = Tk()

root.title("My Calc Tool")
root.configure(bg="lightblue")
# To add background color to the the whole gui then we have to add .configure(bg="color")
e=Entry(root,width=30,borderwidth=3,fg="lightblue",bg="white")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def insert_digit(number):
    # e.insert(0,number)
    current=e.get()
    e.delete(0,END) # Deleting whatever in the box
    e.insert(0,str(current)+str(number))

 
def clear_input():
    e.delete(0,END)

def add_operation():
    first_number=e.get()
    global f_num,operation
    f_num=int(first_number)
    operation = "add"
    e.delete(0,END)

def subtract_operation():
    global f_num, operation
    f_num = int(e.get())
    operation = "sub"
    e.delete(0,END)

def multiply_operation():
    global f_num, operation
    f_num = int(e.get())
    operation = "mul"
    e.delete(0, END)

def divide_operation():
    global f_num, operation
    f_num = int(e.get())
    operation = "div"
    e.delete(0,END)

def show_result():
    second_number = int(e.get())
    e.delete(0,END)
    
    if operation == "add":
        e.insert(0, f_num + second_number)
    elif operation == "sub":
        e.insert(0, f_num - second_number)
    elif operation == "mul":
        e.insert(0, f_num * second_number)
    elif operation == "div":
        if second_number != 0:
            e.insert(0, f_num / second_number)
        else:
            e.insert(0, "Error")

 
    
 

 
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:insert_digit(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:insert_digit(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:insert_digit(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:insert_digit(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:insert_digit(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:insert_digit(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:insert_digit(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:insert_digit(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:insert_digit(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:insert_digit(0))
add_operation=Button(root,text="+",padx=39,pady=20,command=add_operation)
show_result=Button(root,text="=",padx=90,pady=20,command=show_result)
clear_input=Button(root,text="Clear",padx=80,pady=20,command=clear_input)
subtract_operation=Button(root,text="-",padx=40,pady=20,command=subtract_operation)
multiply_operation=Button(root,text="*",padx=40,pady=20,command=multiply_operation)
divide_operation=Button(root,text="/",padx=40,pady=20,command=divide_operation)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
clear_input.grid(row=4,column=1,columnspan=2)
add_operation.grid(row=5,column=0)
show_result.grid(row=5,column=1,columnspan=2)
subtract_operation.grid(row=6,column=0,columnspan=1)
multiply_operation.grid(row=6,column=1,columnspan=1)
divide_operation.grid(row=6,column=2,columnspan=1)

root.mainloop()