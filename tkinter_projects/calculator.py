from tkinter import *

first_num = second_num = operator = None
result_used = False

def get_digit(digit):
  global result_used
  if result_used:
    result_label.config(text="")
    result_used = False
  current = result_label["text"]
  new = current + str(digit)
  result_label.config(text = new)

def clear():
  result_label.config(text="")

def get_operator(op):
  global first_num, operator
  if first_num is not None and result_label["text"] != "":
    get_result()
    first_num = int(result_label["text"])
  else:
    first_num = int(result_label["text"])
  operator = op
  result_label.config(text="")

def get_result():
  global first_num, second_num, operator, result_used
  second_num = int(result_label["text"])

  if operator == "+":
    result_label.config(text=str(first_num+second_num))
  
  elif operator == "-":
    result_label.config(text=str(first_num-second_num))

  elif operator == "*":  
    result_label.config(text=str(first_num*second_num))

  else:
    if second_num == 0:
       result_label.config(text="Error")
    else:
      result_label.config(text=str(first_num/second_num))

  first_num = second_num = operator = None
  result_used = True
    
root = Tk()
root.title("Calculator")
root.geometry("280x380")
root.resizable(0,0)
root.configure(background="black")

result_label = Label(root, text="", bg="black", fg="white")
result_label.grid(row=0, column=0, columnspan=10, sticky="w", pady=(50,25))
result_label.config(font=("verdana",30,"bold"))

Btn7 = Button(root, text=7, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(7))
Btn7.grid(row=1,column=0)

Btn8 = Button(root, text=8, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(8))
Btn8.grid(row=1,column=1)

Btn9 = Button(root, text=9, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(9))
Btn9.grid(row=1,column=2)

Btn_add = Button(root, text="+", bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda: get_operator("+"))
Btn_add.grid(row=1,column=3)

Btn4 = Button(root, text=4, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(4))
Btn4.grid(row=2,column=0)

Btn5 = Button(root, text=5, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(5))
Btn5.grid(row=2,column=1)

Btn6 = Button(root, text=6, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(6))
Btn6.grid(row=2,column=2)

Btn_sub = Button(root, text="-", bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_operator("-"))
Btn_sub.grid(row=2,column=3)

Btn1 = Button(root, text=1, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(1))
Btn1.grid(row=3,column=0)

Btn2 = Button(root, text=2, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(2))
Btn2.grid(row=3,column=1)

Btn3 = Button(root, text=3, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(3))
Btn3.grid(row=3,column=2)

Btn_mul = Button(root, text="*", bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_operator("*"))
Btn_mul.grid(row=3,column=3)

Btn_clear = Button(root, text="C", bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:clear())
Btn_clear.grid(row=4,column=0)

Btn0 = Button(root, text=0, bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_digit(0))
Btn0.grid(row=4,column=1)

Btn_equal = Button(root, text="=", bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=get_result)
Btn_equal.grid(row=4,column=2)

Btn_div = Button(root, text="/", bg="#00a65a", fg="white", width=5, height=2, font=("verdana",14), command=lambda:get_operator("/"))
Btn_div.grid(row=4,column=3)

root.mainloop()