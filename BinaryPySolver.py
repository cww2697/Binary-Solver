from tkinter import *
from tkinter import messagebox
from os import system

class Binary_GUI:
    # constructor for GUI
    def __init__(GUI):
        GUI.main_window = Tk()                               
        GUI.main_window.title("Binary Sodoku Solver")
        GUI.main_window.resizable(width=TRUE,height=TRUE)
        GUI.main_window.configure(background="#FFF")
        GUI.MainFrame = Frame(width=6, height=6)             
        GUI.MainFrame.grid(row=0,column=0,pady=5)
        GUI.MainFrame.config(highlightbackground="#CBCBCB",highlightthickness="2")
        GUI.subFrame = [([0]*6) for i in range(6)]           
        for i in range(3):
            for j in range(3):
                
                # create 9 subframes
                # layout:
                #   1 2 3
                #   4 5 6
                #   7 8 9
                GUI.subFrame[i][j] = Frame(GUI.MainFrame,bd=0,relief='flat',highlightbackground="#CBCBCB",highlightthickness="1")
                GUI.subFrame[i][j].grid(row=i*2,column=j*2,rowspan=2,columnspan=2)
        
        # create cell array (6x6)
        GUI.cell = [([0]*6) for i in range(6)]               
        for i in range(6):
            for j in range(6):
                
                # create cells
                GUI.cell[i][j] = Entry(GUI.subFrame[i//2][j//2], width = 2, fg='black',highlightbackground="#CBCBCB",highlightthickness="1")
                GUI.cell[i][j].grid(row=i,column=j)

        # create and activate button frames        
        GUI.buttons = Frame()                             
        GUI.buttons.grid(row=10,column=0,pady=1)                 

        # Create Buttons for GUI
        GUI.button_solve = Button(GUI.buttons,relief='ridge', text='Solve Puzzle',command=GUI.solve,bg="#3CD070")
        GUI.button_clear = Button(GUI.buttons,relief='ridge', text='Clear Board',command=GUI.clear, bg="#ff9933")
        GUI.button_quit = Button(GUI.buttons,relief='ridge', text='Quit Program',command=GUI.main_window.destroy, bg="#f04848")
        GUI.button_solve.grid(row=0,column=0)
        GUI.button_clear.grid(row=0,column=1)
        GUI.button_quit.grid(row=0,column=2)

        # wait for input from user
        mainloop()                                            

        
    def create_input(GUI):
        v = True
        
        # create temp file and open for writing
        fhandle = open('binary_temp.sm','w')
        for i in range(6):                                    
            for j in range(6):
                data = GUI.cell[i][j].get()

                # check link to determine if cell is empty
                if len(data) > 0:

                    # check if cell is 1 character and is a digit
                    if len(data)==1 and data.isdigit():     
                        if data=='1' or data=='0':
                            
                            fhandle.write('pos('+data+','+str(i+1)+','+str(j+1)+').\n')
                            # if value is invalid    
                        else:                                     
                            GUI.cell[i][j].delete(0,END)         
                            v = False
                    else:                                     
                            GUI.cell[i][j].delete(0,END)         
                            v = False

        fhandle.close()

        # invalid input message box
        if not v:                                         
            messagebox.showinfo('Invalid Input','An entered value was invalid.')
        return v                                         

    def display(GUI):

        # Open output file from BinaryPy.sm
        fhand2 = open('binaryout.sm','r')

        # read file into array
        solution = fhand2.readlines()

        # No solution messagebox
        if solution[0][0] == '*':
            messagebox.showinfo('No Solution','No solutions have been found.')

        # Print output to GUI if there is a solution
        else:
            for item in solution:                             
                if item[0] == 'p':                            
                    i = int(item[6])-1                        
                    j = int(item[8])-1                        
                    if len(GUI.cell[i][j].get()) == 0:       
                        GUI.cell[i][j].config(fg='blue')      
                        GUI.cell[i][j].insert(0,item[4])     
                    GUI.cell[i][j].config(state='readonly')  
            GUI.button_solve.config(state=DISABLED)          

    def solve(GUI):

        # System call for clingo and mkatoms for BinaryPy.sm
        if GUI.create_input():
            system("clingo binary_temp.sm BinaryPy.sm | mkatoms > binaryout.sm")
            GUI.display()
                    

    def clear(GUI):

        # Clear board cell by cell
        GUI.button_solve.config(state=NORMAL)
        for i in range(6):
            for j in range(6):
                GUI.cell[i][j].config(state=NORMAL,fg='black')
                GUI.cell[i][j].delete(0,END)
                
        
# Create the GUI      
Binary_GUI()
        

