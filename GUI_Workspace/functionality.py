import tkinter as tk
from tkinter import messagebox
class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x400")

        self.label = tk.Label(self.root, text="Your Message", font=('Aerial', 18))
        self.label.pack(padx=10, pady=10)


        self.textbox = tk.Text(self.root, height=5, font=('Arial', 18), )
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.BooleanVar()

        self.message_box = tk.Message(self.root)
        
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", 
            font=('Arial', 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, 
            text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()


    def print_message(self):
        input = self.textbox.get('1.0', 'end-1c')
        if input == "nart" :
            print("klasik bir ibne")
        elif input == "savas" :
            print("got deli")
        elif input == "osman" :
            print("31 damage ile sampiyon")
        elif input == "asrin" :
            print("ben bu kadina asik olsam beni yargilar misiniz")
        elif input == "nuri" :
            print("yargilarim")     
        else :
            messagebox.showinfo(title="message", message=input)

        self.textbox.delete('1.0', 'end')
        input = ""


    def show_message(self):
        if (self.check_state.get()): 
            self.print_message()
    
    def shortcut(self, event):
        if(event.keysym == "Return"):
            self.print_message()


MyGUI()