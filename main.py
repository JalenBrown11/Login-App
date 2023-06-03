import tkinter as tk
from tkinter import font
import string

TEXT_COLOR = 'white'
TRANSPARENT_BG = '#171924'
ENTRY_BG = '#2B2D36'
BUTTON_BG = '#787FB8'
BUTTON_ACTIVE_BG = '#353852'

class App(tk.Tk):
    
    def __init__(self, window_title: str="App", icon_path: str=None):
        # Set up Gui class
        super(App, self).__init__()
        self.title(window_title)
        self.iconbitmap(icon_path)
        self.configure(
            background='#171924'
        )

        # Variables
        username = tk.StringVar()
        password = tk.StringVar()

        # Add Frames
        self.mainFrame = Frame(self)
        self.titleFrame = Frame(self.mainFrame)
        self.inputFrame = Frame(self.mainFrame)
        self.btnFrame = Frame(self.mainFrame)
        
        # Add Widgets
        self.title_lbl = Label(self.titleFrame, 'Login')
        self.user_lbl = Label(self.inputFrame, 'Username')
        self.pass_lbl = Label(self.inputFrame, 'Password')
        self.user_err_lbl = Label(self.inputFrame, "")
        self.pass_err_lbl = Label(self.inputFrame, "")
        self.user_entry = Entry(self.inputFrame, username)
        self.pass_entry = Entry(self.inputFrame, password, True)
        self.btn1 = Button(self.btnFrame, 'Submit')

        # Commands
        self.btn1.command(self.submit_btn_click)

        # Layout
        self.title_lbl.pack()

        self.user_lbl.grid(row=0,column=0, ipady=4)
        self.user_entry.grid(row=0,column=1, ipadx=12, ipady=2, padx=4)

        self.pass_lbl.grid(row=2,column=0, ipady=4)
        self.pass_entry.grid(row=2,column=1, ipadx=12, ipady=2, padx=4)
        
        self.btn1.pack()
        
        self.titleFrame.pack(side=tk.TOP, pady=[0, 24])
        self.inputFrame.pack(side=tk.TOP)
        self.btnFrame.pack(side=tk.TOP, pady=[16, 0])

        self.mainFrame.pack(padx=16, pady=16)
   
        # Style Widgets
        self.title_lbl.set_font(size=24)
        self.user_err_lbl.set_font(size=10, weight='normal', color='#FF8C8C')
        self.pass_err_lbl.set_font(size=10, weight='normal', color='#FF8C8C')

    def submit_btn_click(self):
        # Check entry inputs
        user_flag = self.check_user()
        pass_flag = self.check_pass()

        # If user_flag is not empty
        if user_flag: 
            user_err_message = "\n".join(user_flag)
            self.user_err_lbl.set_text(user_err_message)
            self.user_entry.set_text('')
            self.user_err_lbl.grid(row=1, column=0, columnspan=3, ipady=2)
        else:
            self.user_err_lbl.grid_remove()

        # If pass_flag is not empty
        if pass_flag: 
            pass_err_message = "\n".join(pass_flag)
            self.pass_err_lbl.set_text(pass_err_message)
            self.pass_entry.set_text('')
            self.pass_err_lbl.grid(row=3, column=0, columnspan=3, ipady=2)
        else: 
            self.pass_err_lbl.grid_remove()        
    
    def check_user(self):
        username_err_messages = [] # Error message list

        user_txt = self.user_entry.get() # Store password entry text 

        # Check username is greater than 8 length
        if len(user_txt) < 8: 
            username_err_messages.append("- Must have at least 8 characters")
        # Check username has a space
        if any(char == " " for char in user_txt):
            username_err_messages.append("- Cannot have any space(s)")
        
        # Return error list
        return username_err_messages

    def check_pass(self):
        password_err_messages = [] # Error message list
        symbol = string.punctuation # Symbols list

        pass_txt = self.pass_entry.get() # Store password entry text

        # Check password is greater than 8 length
        if len(pass_txt) < 8: 
            password_err_messages.append("- Must have at least 8 characters")
        # Check password has uppercase
        if not any(char.isupper() for char in pass_txt): 
            password_err_messages.append("- Must have at least one uppercase letter")
        # Check password has lowercase
        if not any(char.islower() for char in pass_txt): 
            password_err_messages.append("- Must have at least one lowercase letter")
        # Check password has digit
        if not any(char.isdigit() for char in pass_txt): 
            password_err_messages.append("- Must have at least one digit")
        # Check password has a alphabet letter
        if not any(char.isalpha() for char in pass_txt): 
            password_err_messages.append("- Must have at least one characters")
        # Check password has a symbol
        if not any(char in symbol for char in pass_txt): 
            password_err_messages.append("- Must have at least one symbol")
        # Check password has a space
        if any(char == " " for char in pass_txt):
            password_err_messages.append("- Cannot have any space(s)")

        # Return error list
        return password_err_messages


class Frame(tk.Frame):

    def __init__(self, parent: tk.Widget):
        super(Frame, self).__init__(master=parent)

        self.configure(
            background= '#171924'
        )

class Entry(tk.Entry):

    def __init__(self, parent: tk.Widget, default_textvar: tk.StringVar, display_flag: bool=False):
        super(Entry, self).__init__(master=parent, textvariable=default_textvar)

        self.flag = display_flag
        self.text_var = default_textvar

        self.configure(
            foreground=TEXT_COLOR,
            background=ENTRY_BG,
            insertbackground=TEXT_COLOR,
            font=font.Font(family='Segoe UI', size=12, weight='normal'),
            border=0
        )        

        self.bind('<Button-1>', self.click)           

    def click(self, event):
        if self.flag == True:
            self.configure(show='*')
        
    def set_text(self, text: str):
        self.text_var.set(text)


class Label(tk.Label):

    def __init__(self, parent: tk.Widget, default_text: str="Label"):
        super(Label, self).__init__(master=parent, text=default_text)
        
        self.configure(
            foreground=TEXT_COLOR,
            background=TRANSPARENT_BG,
            font=font.Font(family='Segoe UI', size=12, weight='bold'),
            justify='center'
        )

    def set_font(self, family: str='Segoe UI', size: int=12, weight: str='bold', color: str=TEXT_COLOR):
        self.configure(
            foreground=color,
            font=font.Font(family=family, size=size, weight=weight)
        )
    
    def set_text(self, text: str):
        self.configure(text=text)


class Button(tk.Button):

    def __init__(self, parent: tk.Widget, default_text: str="Button"):
        super(Button, self).__init__(master=parent, text=default_text)

        self.configure(
            foreground=TEXT_COLOR,
            background=BUTTON_BG,
            activeforeground=TEXT_COLOR,
            activebackground=BUTTON_ACTIVE_BG,
            border=0,
            font=font.Font(family='Segoe UI', size=12, weight='bold'),
            justify='center',
            default='normal',
        )

    def command(self, func: None):
        self.configure(command=func)
    

if __name__ == '__main__':
    root = App('Login Test', 'images\Bill-Cipher\Windows\icons8-bill-cipher-windows-11-310.ico')    
    root.mainloop()