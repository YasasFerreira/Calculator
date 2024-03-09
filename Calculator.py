import tkinter 
from tkinter import *
from tkinter import messagebox
#import tkinter that is helps to create GUI easily

var = ''
A=0
Operator =''

#button_1_clicked
def button_1_clicked():
    global var
    var = var+'1'
    the_data.set(var)

#button_2_clicked
def button_2_clicked():
    global var 
    var = var+'2'
    th_data.set(var)
    
#button_3_clicked
def button_3_clicked():
    global var
    var = var+'3'
    the_data.set(var)
    
#button_4_clicked
def button_4_clicked():
    global var 
    var = var+'4'
    the_data.set(var)
    
#button_5_clicked
def button_5_clicked():
    global var 
    var = var+'5'
    the_data.set(var)
    
#button_6_clicked
def button_6_clicked():
    global var 
    var = var+'6'
    the_data.set(var)
    
#button_7_clicked
def button_7_clicked():
    global var 
    var = var+'7'
    the_data.set(var)
    
#button_8_clicked
def button_8_clicked():
    global var 
    var = var+'8'
    the_data.set(var)
    
#button_9_clicked
def button_9_clicked():
    global var 
    var = var+'9'
    the_data.set(var)
    
#button_0_clicked
def button_0_clicked():
    global var
    var = var+'0'
    the_datal.set(var)
    
#button_plus_clicked
def button_plus_clicked():
    global A
    global var
    global operator
    
    A  = float(var)
    operator = '+'
    var = var + '+'
    the_data.set(var)
    
#button_minus_clicked
def button_minus_clicked():
    global A
    global var
    global operator
    
    A = float(var)
    operator = '-'
    var =var + '-'
    the_data.set(var)
    
#button_mul_clicked
def button_mul_clicked():
    global A
    global var
    global operator
    
    A = float(var)
    operator = 'x'
    var = var + 'x'
    the_data.set(var)
    
#button_div_clicked
def button_div_clicked():
    global A
    global var
    global operator
    
    A = float(var)
    operator = '/'
    var = var+'/'
    the_data.set(var)
    
#button_eql_clicked
def button_eql_clicked():
    global A
    global var
    global operator
    
    A = float(var)
    operator = '='
    var = var + '='
    the_data.set(var)
    
#button_c_clicked
def button_c_clicked():
    global A
    global var
    global operator
    
    A = 0
    var = ''
    operator = ''
    the_data.set(var)
    
# defining the function to display result  
def res():  
    global A  
    global operator  
    global var  
    var2 = var  
    if operator == "+":  
        a = float((var2.split("+")[1]))  
        x = A + a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "-":  
        a = float((var2.split("-")[1]))  
        x = A - a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "*":  
        a = float((var2.split("*")[1]))  
        x = A * a  
        the_data.set(x)  
        var = str(x)  
    elif operator == "/":  
        a = float((var2.split("/")[1]))  
        if a == 0:  
            messagebox.showerror("Division by 0 Not Allowed.")  
            A == ""  
            var = ""  
            the_data.set(var)  
        else:  
            x = float(A/a)  
            the_data.set(x)  
            var = str(x)  


#create object for tkinter

Guiwindow = tkinter.Tk()

Guiwindow.geometry("370x400+400+80")
Guiwindow.title('Calculator')

# creating the label for the window  
the_data = StringVar()  
guiLabel = Label(  
    Guiwindow,  
    text = "Label",  
    anchor = SE,  
    font = ("Cambria Math", 20),  
    textvariable = the_data,  
    background = "#ffffff",  
    fg = "#000000"  
)  

# using the pack() method  
guiLabel.pack(expand = True, fill = "both")  

# creating the frames for the buttons  
# first frame  
frameOne = Frame(Guiwindow, bg = "#000000")  
frameOne.pack(expand = True, fill = "both") # frame can expand if it gets some space 

# second frame  
frameTwo = Frame(Guiwindow, bg = "#000000")  
frameTwo.pack(expand = True, fill = "both")  
  
# third frame  
frameThree = Frame(Guiwindow, bg = "#000000")  
frameThree.pack(expand = True, fill = "both")  

# fourth frame  
frameFour = Frame(Guiwindow, bg = "#000000")  
frameFour.pack(expand = True, fill = "both")  
 

# creating buttons 
# buttons for first frame  
# button 1  
buttonONE = Button(  
    frameOne,  
    text = "1",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_1_clicked
)  
# placing buttons side by side  
buttonONE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 2  
buttonTWO = Button(  
    frameOne,  
    text = "2",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_2_clicked
)  
# placing buttons side by side  
buttonTWO.pack(side = LEFT, expand = True, fill = "both")  
  
# button 3  
buttonTHREE = Button(  
    frameOne,  
    text = "3",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,   
    command = button_3_clicked   
)  
# placing buttons side by side  
buttonTHREE.pack(side = LEFT, expand = True, fill = "both")  
  
# button C  
buttonC = Button(  
    frameOne,  
    text = "C",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    command = button_c_clicked   
)  
# placing buttons side by side  
buttonC.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for second frame  
# button 4  
buttonFOUR = Button(  
    frameTwo,  
    text = "4",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
    command = button_4_clicked 
)  
# placing buttons side by side  
buttonFOUR.pack(side = LEFT, expand = True, fill = "both")  
  
# button 5  
buttonFIVE = Button(  
    frameTwo,  
    text = "5",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
    command = button_5_clicked   
)  
# placing buttons side by side  
buttonFIVE.pack(side = LEFT, expand = True, fill = "both")  
  
# button 6  
buttonSIX = Button(  
    frameTwo,  
    text = "6",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
    command = button_6_clicked   
)  
# placing buttons side by side  
buttonSIX.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonADD = Button(  
    frameTwo,  
    text = "+",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    
    command = button_plus_clicked   
)  
# placing buttons side by side  
buttonADD.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for third frame  
# button 7  
buttonSEVEN = Button(  
    frameThree,  
    text = "7",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
    
    command = button_7_clicked  
)  
# placing buttons side by side  
buttonSEVEN.pack(side = LEFT, expand = True, fill = "both")  
  
# button 8  
buttonEIGHT = Button(  
    frameThree,  
    text = "8",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
    
    command = button_8_clicked
)  
# placing buttons side by side  
buttonEIGHT.pack(side = LEFT, expand = True, fill = "both")  
  
# button 9  
buttonNINE = Button(  
    frameThree,  
    text = "9",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
    
    command = button_9_clicked  
)  
# placing buttons side by side  
buttonNINE.pack(side = LEFT, expand = True, fill = "both")  
  
# button -  
buttonSUB = Button(  
    frameThree,  
    text = "-",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    
    command = button_minus_clicked  
)  
# placing buttons side by side  
buttonSUB.pack(side = LEFT, expand = True, fill = "both")  
  
# buttons for fourth frame  
# button 0  
buttonZERO = Button(  
    frameFour,  
    text = "0",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    
    command = button_0_clicked 
)  
# placing buttons side by side  
buttonZERO.pack(side = LEFT, expand = True, fill = "both")  
  
# button *  
buttonMUL = Button(  
    frameFour,  
    text = "*",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0, 
   
    command = button_mul_clicked
)  
# placing buttons side by side  
buttonMUL.pack(side = LEFT, expand = True, fill = "both")  
  
# button /  
buttonDIV = Button(  
    frameFour,  
    text = "/",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,
    
    command = button_div_clicked  
)  
# placing buttons side by side  
buttonDIV.pack(side = LEFT, expand = True, fill = "both")  
  
# button +  
buttonEQUAL = Button(  
    frameFour,  
    text = "=",  
    font = ("Cambria", 22),  
    relief = GROOVE,  
    border = 0,  
    
    command = res
)  
    
# placing buttons side by side  
buttonEQUAL.pack(side = LEFT, expand = True, fill = "both")  

#running gui window

Guiwindow.mainloop()
