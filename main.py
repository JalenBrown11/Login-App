import tkinter as tk
from tkinter import font
import string

# Global Colors 
TEXT_COLOR = 'white'
TRANSPARENT_BG = '#171924'
ENTRY_BG = '#2B2D36'
BUTTON_BG = '#787FB8'
BUTTON_ACTIVE_BG = '#353852'

class App(tk.Tk):
    """ Custom App Window """
    def __init__(self, window_title: str="App", icon_path: str=None):
        """ Initialize App Widget"""
        super(App, self).__init__()
        self.title(window_title)
        self.iconbitmap(icon_path)
        self.configure(
            background='#171924'
        )

        # Variables
        username = tk.StringVar()
        password = tk.StringVar()

        """ Frames """
        self.mainFrame = Frame(self)
        self.titleFrame = Frame(self.mainFrame)
        self.inputFrame = Frame(self.mainFrame)
        self.btnFrame = Frame(self.mainFrame)
        
        """ Widgets """
        self.title_lbl = Label(self.titleFrame, 'Login')
        self.user_lbl = Label(self.inputFrame, 'Username')
        self.pass_lbl = Label(self.inputFrame, 'Password')
        self.user_err_lbl = Label(self.inputFrame, "")
        self.pass_err_lbl = Label(self.inputFrame, "")
        self.user_entry = Entry(self.inputFrame, username)
        self.pass_entry = Entry(self.inputFrame, password, True)
        self.btn1 = Button(self.btnFrame, 'Submit')

        """ Commands """
        self.btn1.set_command(self.submit_btn_click)

        """ Layout """
        # Widget layout (Frames)
        self.title_lbl.pack()
        self.user_lbl.grid(row=0,column=0, ipady=4)
        self.user_entry.grid(row=0,column=1, ipadx=12, ipady=2, padx=4)
        self.pass_lbl.grid(row=2,column=0, ipady=4)
        self.pass_entry.grid(row=2,column=1, ipadx=12, ipady=2, padx=4)
        self.btn1.pack()
        
        # Frame layout (Main Frame)
        self.titleFrame.pack(side=tk.TOP, pady=[0, 24])
        self.inputFrame.pack(side=tk.TOP)
        self.btnFrame.pack(side=tk.TOP, pady=[16, 0])

        # Window layout (Main Window)
        self.mainFrame.pack(padx=16, pady=16)
   
        """ Style Widgets """
        # Set title font
        self.title_lbl.set_font(size=24)

        # Set error messages font
        self.user_err_lbl.set_font(size=10, weight='normal', color='#FF8C8C')
        self.pass_err_lbl.set_font(size=10, weight='normal', color='#FF8C8C')

    def submit_btn_click(self):
        """ Button command for login"""
        # Input flag variables
        is_valid_username = False
        is_valid_password = False
        
        # Check entry inputs
        user_flag_list = self.check_user()
        pass_flag_list = self.check_pass()

        # If error found in user_flag_list
        if user_flag_list: 
            user_err_message = "\n".join(user_flag_list) # Join username error messages 
            self.user_err_lbl.set_text(user_err_message) # Set messages to Label
            self.user_err_lbl.grid(row=1, column=0, columnspan=3, ipady=2) # Place Label into grid
        else:
            self.user_err_lbl.grid_remove() # Remove widget
            is_valid_username = True

        # If error found in pass_flag_list
        if pass_flag_list: 
            pass_err_message = "\n".join(pass_flag_list) # Join password error messages  
            self.pass_err_lbl.set_text(pass_err_message) # Set messages to Label
            self.pass_err_lbl.grid(row=3, column=0, columnspan=3, ipady=2) # Place Label into grid
        else: 
            self.pass_err_lbl.grid_remove() # Remove widget
            is_valid_password = True

        # If username and password is valid, then create login file
        if is_valid_username and is_valid_password:
            self.create_login()      
    
    def check_user(self):
        """ Check password input entry """
        username_err_messages = [] # Error message list

        user_txt = self.user_entry.get() # Store password entry text 

        # Check if username is greater than 8 length
        if len(user_txt) < 8: 
            username_err_messages.append("- Must have at least 8 characters")
        # Check if username has a space
        if any(char == " " for char in user_txt):
            username_err_messages.append("- Cannot have any space(s)")
        
        # Return error list
        return username_err_messages

    def check_pass(self):
        """ Check password input entry """
        password_err_messages = [] # Error message list
        symbol = string.punctuation # Symbols list

        pass_txt = self.pass_entry.get() # Store password entry text

        # Check if password is greater than 8 length
        if len(pass_txt) < 8: 
            password_err_messages.append("- Must have at least 8 characters")
        # Check if password has uppercase
        if not any(char.isupper() for char in pass_txt): 
            password_err_messages.append("- Must have at least one uppercase letter")
        # Check if password has lowercase
        if not any(char.islower() for char in pass_txt): 
            password_err_messages.append("- Must have at least one lowercase letter")
        # Check if password has digit
        if not any(char.isdigit() for char in pass_txt): 
            password_err_messages.append("- Must have at least one digit")
        # Check if password has a alphabet letter
        if not any(char.isalpha() for char in pass_txt): 
            password_err_messages.append("- Must have at least one characters")
        # Check if password has a symbol
        if not any(char in symbol for char in pass_txt): 
            password_err_messages.append("- Must have at least one symbol")
        # Check if password has a space
        if any(char == " " for char in pass_txt):
            password_err_messages.append("- Cannot have any space(s)")

        # Return error list
        return password_err_messages
    
    def create_login(self):
        """ Create login credential file """
        with open('Login.txt', 'w') as f:
            f.write(self.user_entry.get())
            f.write(self.pass_entry.get())
            f.close()


class Frame(tk.Frame):
    """ Custom Tkinter Frame """
    def __init__(self, parent: tk.Widget):
        """ Initialize Frame Widget """
        super(Frame, self).__init__(master=parent)
        
        # Frame Style
        self.configure(
            background= '#171924'
        )

class Entry(tk.Entry):
    """ Custom Tkinter Frame """
    def __init__(self, parent: tk.Widget, default_textvar: tk.StringVar, display_flag: bool=False):
        """ Initialize Entry Widget """
        super(Entry, self).__init__(master=parent, textvariable=default_textvar)

        # Variables
        self.flag = display_flag # Flag for input display style
        self.text_var = default_textvar # Store input stringvar

        # Entry Style
        self.configure(
            foreground=TEXT_COLOR,
            background=ENTRY_BG,
            insertbackground=TEXT_COLOR,
            font=font.Font(family='Segoe UI', size=12, weight='normal'),
            border=0
        )        

        # Widget binds (Key, KeyPress, Mouse, etc.)
        self.bind('<Button-1>', self.click) # Left Click           

    def click(self, event):
        """ Click Entry Event """
        if self.flag == True: 
            self.configure(show='*') # Change input display style
    
    def set_text(self, text: str):
        """ Set input text """
        self.text_var.set(text)


class Label(tk.Label):
    """ Custom Tkinter Frame """
    def __init__(self, parent: tk.Widget, default_text: str="Label"):
        """ Initialize Label Widget"""
        super(Label, self).__init__(master=parent, text=default_text)

        # Label Style
        self.configure(
            foreground=TEXT_COLOR,
            background=TRANSPARENT_BG,
            font=font.Font(family='Segoe UI', size=12, weight='bold'),
            justify='center'
        )

    def set_font(self, family: str='Segoe UI', size: int=12, weight: str='bold', color: str=TEXT_COLOR):
        """ Set Label font """
        self.configure(
            foreground=color,
            font=font.Font(family=family, size=size, weight=weight)
        )
    
    def set_text(self, text: str):
        """ Set Label text """
        self.configure(text=text)


class Button(tk.Button):
    """ Custom Tkinter Frame """
    def __init__(self, parent: tk.Widget, default_text: str="Button"):
        """ Initialize Button Widget"""
        super(Button, self).__init__(master=parent, text=default_text)

        # Button Style
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

    def set_command(self, func: None):
        """ Set Button command """
        self.configure(command=func)
    

if __name__ == '__main__':
    root = App('Login Test', 'images\Bill-Cipher\Windows\icons8-bill-cipher-windows-11-310.ico')    
    root.mainloop()