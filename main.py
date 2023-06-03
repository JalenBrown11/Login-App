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
    def __init__(self, window_title: str="App", icon_path: str=None, width: int=400, height: int=380):
        """ Initialize App Widget"""
        super(App, self).__init__()
        self.title(window_title)
        self.iconbitmap(icon_path)
        self.geometry(f'{width}x{height}')
        self.configure(
            background='#171924'
        )

        # Variables
        username = tk.StringVar()
        password = tk.StringVar()

        """ Frames """
        self.mainFrame = Frame(self)
        self.titleFrame = Frame(self.mainFrame)
        self.msgFrame = Frame(self.mainFrame)
        self.inputFrame = Frame(self.mainFrame)
        self.btnFrame = Frame(self.mainFrame)
        
        """ Widgets """
        self.title_lbl = Label(self.titleFrame, 'Registration')
        self.user_lbl = Label(self.inputFrame, 'Username')
        self.pass_lbl = Label(self.inputFrame, 'Password')
        self.user_err_lbl = Label(self.inputFrame, '')
        self.pass_err_lbl = Label(self.inputFrame, '')
        self.msg_lbl = Label(self.msgFrame, '')
        self.user_entry = Entry(self.inputFrame, username)
        self.pass_entry = Entry(self.inputFrame, password, True)
        self.btn1 = Button(self.btnFrame, 'Sign Up')

        """ Commands """
        self.btn1.set_command(self.signup_btn_click)

        """ Binding """
        self.bind('<Key>', self.key_event) # Receive all key events
        self.user_entry.bind('<Key-space>', lambda _:'break') # Disable space key
        self.pass_entry.bind('<Key-space>', lambda _:'break') # Disable space key

        """ Layout """
        # Widget layout (Frames)
        self.title_lbl.pack()
        self.user_lbl.grid(row=0,column=0, ipady=4)
        self.user_entry.grid(row=0,column=1, ipadx=12, ipady=2, padx=4)
        self.pass_lbl.grid(row=2,column=0, ipady=4)
        self.pass_entry.grid(row=2,column=1, ipadx=12, ipady=2, padx=4)
        self.btn1.pack()
        
        # Frame layout (Main Frame)
        self.titleFrame.pack(side=tk.TOP, pady=[0, 4])
        self.inputFrame.pack(side=tk.TOP)
        self.msgFrame.pack(side=tk.TOP)
        self.btnFrame.pack(side=tk.TOP, pady=[8, 0])

        # Window layout (Main Window)
        self.mainFrame.place(relx=.5, rely=.45,anchor=tk.CENTER)
   
        """ Style Widgets """
        # Set title font
        self.title_lbl.set_font(size=24)

        # Set error messages font
        self.user_err_lbl.set_font(size=10, weight='normal', color='#FF8C8C')
        self.pass_err_lbl.set_font(size=10, weight='normal', color='#FF8C8C')

        # Set message font
        self.msg_lbl.set_font(size=12, weight='normal', color='#B2FF8C')
    
    def key_event(self, event: tk.Event):
        """ Key event handler """
        # If 'Escape' key pressed
        if event.keysym == 'Escape':
            self.destroy() # Close application
        # If 'Enter' key pressed
        if event.keysym == 'Return':
            self.btn1.invoke() # Trigger login/sign up button commmand

    def signup_btn_click(self):
        """ Button command for Sign Up"""
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
            self.create_login() # Create Login.txt file

            # Update Labels, Entries and Buttons (Login)
            self.title_lbl.set_text('Login') 
            self.user_entry.set_text('')
            self.pass_entry.set_text('')
            self.msg_lbl.set_text('Your registration has been successfully completed!')
            self.msg_lbl.set_padding(0,8)
            self.btn1.set_text('Submit')
            self.btn1.set_command(self.login_btn_click)

            # Update layout
            self.msg_lbl.pack()
            self.msgFrame.pack() 

    def login_btn_click(self):
        """ Button command for Login"""
        # If input match login credentials, update label
        if self.check_login() == True:
            self.msg_lbl.set_font(size=12, weight='normal', color='#B2FF8C')
            self.msg_lbl.set_text('Successful Login!')   

        # Else input doesn't match login credentials, update label
        if self.check_login() == False:
            self.msg_lbl.set_font(size=12, weight='normal', color='#FF8C8C')
            self.msg_lbl.set_text('Invalid Login!')

    def check_user(self):
        """ Check password input entry """
        username_err_messages = [] # Error message list

        user_txt = self.user_entry.get() # Store password entry text 

        # Check if username is greater than 8 length
        if len(user_txt) < 8: 
            username_err_messages.append("- Must have at least 8 characters")
        
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

        # Return error list
        return password_err_messages
    
    def check_login(self):
        """ Check login credential file """
        # Read login file
        with open('Login.txt', 'r') as f:
            # Store login information (strip any white space)
            username = f.readline().strip()
            password = f.readline().strip()
            f.close()

        # If login information is valid
        if username == self.user_entry.get() and password == self.pass_entry.get():
            return True
        else:
            return False
    
    def create_login(self):
        """ Create login credential file """
        # Store and clean input
        new_username = self.user_entry.get().strip()
        new_password = self.pass_entry.get().strip()

        # Write login file
        with open('Login.txt', 'w') as f:
            f.write(f'{new_username}\n')
            f.write(f'{new_password}\n')
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

        # If Entry flag true 
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

    def set_padding(self, x: int, y: int):
        self.configure(
            padx=x,
            pady=y
        )

    def set_text(self, text: str):
        """ Set Label text """
        self.configure(
            text=text
        )


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

    def set_text(self, text: str):
        """ Set Button text """
        self.configure(text=text)

    def set_command(self, func: None):
        """ Set Button command """
        self.configure(command=func)
    

if __name__ == '__main__':
    root = App('Login Test', 'images\Bill-Cipher\Windows\icons8-bill-cipher-windows-11-310.ico')    
    root.mainloop()