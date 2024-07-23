from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operators=""

def btnbackspace():
    global operator
    operator= operator[:-1]
    text_Input.set(operator)

def btnpercentage():
    global operator
    try:
        result = str(eval(operator) / 100)
        text_Input.set(result)
        operator = result
    except:
        text_input.set(" error ")
        operator= ""    


cal=Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()



txtDisplay = Entry(cal,font=('Times New Roman', 20,'bold'), textvariable=text_Input, bd=20, insertwidth=4,
                   bg="white", justify='right').grid(columnspan=4)

#=================================================================================

btnc=Button(cal,padx=14,pady=14,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="c",command=btnClearDisplay).grid (row=1,column=0)

btn=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="%",command=btnpercentage).grid (row=1,column=1)

btn=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="#",command=btnbackspace).grid (row=1,column=2)

Division=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="/",command=lambda:btnClick("/")).grid (row=1,column=3)
#=================================================================================



btn7=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="7",command=lambda:btnClick(7)).grid (row=2,column=0)

btn8=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="8",command=lambda:btnClick(8)).grid (row=2,column=1)

btn9=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="9",command=lambda:btnClick(9)).grid (row=2,column=2)

Multiplication=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="*",command=lambda:btnClick("*")).grid (row=2,column=3)
#=================================================================================

btn4=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="4",command=lambda:btnClick(4)).grid (row=3,column=0)

btn5=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="5",command=lambda:btnClick(5)).grid (row=3,column=1)

btn6=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="6",command=lambda:btnClick(6)).grid (row=3,column=2)

Subtraction=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="-",command=lambda:btnClick("-")).grid (row=3,column=3)
#=================================================================================

btn1=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="1",command=lambda:btnClick(1)).grid (row=4,column=0)

btn2=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="2",command=lambda:btnClick(2)).grid (row=4,column=1)

btn3=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="3",command=lambda:btnClick(3)).grid (row=4,column=2)

Subtraction=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="+",command=lambda:btnClick("+")).grid (row=4,column=3)

#=================================================================================

btn0=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="0",command=lambda:btnClick(0)).grid (row=5,column=0)

btn00=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="00",command=lambda:btnClick(00)).grid (row=5,column=1)

btn=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text=".",command=lambda:btnClick(".")).grid (row=5,column=2)

Equal=Button(cal,padx=16,pady=16,bd=8, fg='black',font=('Times New Roman', 20,'bold'),
            text="=",command=btnEqualsInput).grid (row=5,column=3)








