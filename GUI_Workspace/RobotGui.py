import tkinter as tk
import threading
from functools import partial

class RobotGUI:
    """Handles the Tkinter GUI."""
    def __init__(self, name, size="500x400"):

        self.root = tk.Tk()
        self.root.title(name)
        self.root.minsize(width=600, height=400)
        self.root.geometry(size) 

        self.move_label = ""
        self.x_coord = 0.0
        self.y_coord = 0.0

        label = tk.Label(self.root, text="Mobile Robot Controller UI", font=('Arial', 24), background="lightgreen", height=2)
        label.pack(fill='both')
        label = tk.Label(self.root, height=2)
        label.pack(fill='both')

        # Main frame with two equal columns
        pageFrame = tk.Frame(self.root, padx=10, pady=10)
        pageFrame.pack(fill='both', expand=True)
        pageFrame.columnconfigure(0, weight=1, minsize=250)  # Left column weight
        pageFrame.columnconfigure(1, weight=1, minsize=250)  # Right column weight
        
        # Left frame (contains a grid)
        leftFrame = tk.Frame(pageFrame)
        leftFrame.grid(row=0, column=0, sticky="nsew")
        leftFrame.columnconfigure(0, weight=1)
        leftFrame.rowconfigure(0, weight=1)

        # Right frame (dummy frame to balance layout)
        rightFrame = tk.Frame(pageFrame, width='2')
        rightFrame.grid(row=0, column=1, sticky="esn")
        rightFrame.rowconfigure(2, minsize=40) 
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ BUTTON FRAME

        # Button Frame inside the left frame (3x3 grid)
        buttonFrame = tk.Frame(leftFrame, width='12')
        buttonFrame.grid(row=0, column=0, sticky="w")
        
        # Configure button frame to allow proper resizing
        for i in range(3):  
            buttonFrame.columnconfigure(i, weight=1, minsize=50)  # Evenly distribute columns
            buttonFrame.rowconfigure(i, weight=1, minsize=50)     # Evenly distribute rows

        # Adding buttons
        btnUp = tk.Button(buttonFrame,name='button_up', text='U', height=2, width=4,
                  font=('Arial', 18), bg='lightgreen',
                  command=lambda: self.btn_up_function('button_up'))
        btnUp.grid(row=0, column=1, sticky="nsew")

        btnLeft = tk.Button(buttonFrame, name="button_left", text='L', height=2, width=4,
                  font=('Arial', 18), bg='lightgreen',
                  command=lambda: self.btn_up_function('button_left'))
        btnLeft.grid(row=1, column=0, sticky="nsew")

        btnRight = tk.Button(buttonFrame, name="button_right", text='R', height=2, width=4, font=('Arial', 18), bg='lightgreen', 
                             command=lambda: self.btn_right_function('button_right'))
        btnRight.grid(row=1, column=2, sticky="nsew")

        btnDown = tk.Button(buttonFrame, name="button_down", text='D', height=2, width=4,font=('Arial', 18), bg='lightgreen', 
                            command=lambda: self.btn_down_function('button_down'))
        btnDown.grid(row=2, column=1, sticky="nsew")

        
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@ Coordinate Frame

        coordinate_frame_label = tk.Label(rightFrame, text="Destination Coordinates", font=('Arial', 16), background="lightblue", anchor='w')
        coordinate_frame_label.grid(row=0, column=0, sticky='eswn')
        
        cord_frame = tk.Frame(rightFrame, padx=0, pady=0, bg="")
        cord_frame.grid(row=1, column=0, sticky='w')
        cord_frame.columnconfigure(0, weight=1)
        cord_frame.columnconfigure(1, weight=10)


        x_label = tk.Label(cord_frame, text="X:", height=1, width=3, font=('Arial', 14))
        x_label.grid(row=0, column=0, sticky='w')
        y_label = tk.Label(cord_frame, text="Y:", height=1, width=3, font=('Arial', 14))
        y_label.grid(row=1, column=0, sticky='w')
        self.textbox_x = tk.Text(cord_frame, height=1, width=10, font=('Arial',16), bg="white")
        self.textbox_x.grid(row=0, column=1, sticky='wsne')
        self.textbox_y = tk.Text(cord_frame, height=1, width =10, font=('Arial',16), bg='white')
        self.textbox_y.grid(row=1, column=1, sticky='w')

        btnMove = tk.Button(cord_frame, text="Move", height=2, width=8, font=('Arial', 16), command=self.btn_move_function)
        btnMove.grid(row=0, column=2, sticky='e', rowspan=2)


        position_frame_label = tk.Label(rightFrame, text="Robot Position", font=('Arial', 16), background="lightblue", anchor='w')
        position_frame_label.grid(row=3, column=0, columnspan=2, sticky='snew')

        position_frame = tk.Frame(rightFrame, padx=0, pady=0, bg="")
        position_frame.grid(row=4, column=0, sticky='snew')
        position_frame.columnconfigure(0, weight=1)
        position_frame.columnconfigure(1, weight=10)
        

        x_label = tk.Label(position_frame, text="X:", height=1, width=3, font=('Arial', 14))
        x_label.grid(row=0, column=0, sticky='w')
        y_label = tk.Label(position_frame, text="Y:", height=1, width=3, font=('Arial', 14))
        y_label.grid(row=1, column=0, sticky='w')
        self.textbox_x = tk.Text(position_frame, height=1, width=10, font=('Arial',16), bg="white", cursor="arrow", state='disabled')
        self.textbox_x.grid(row=0, column=1, sticky='w')
        self.textbox_y = tk.Text(position_frame, height=1, width =10, font=('Arial',16), bg='white',cursor="arrow", state='disabled')
        self.textbox_y.grid(row=1, column=1, sticky='w')



    def btn_up_function(self, button):
        self.movement(button)
    def btn_left_function(self, button):
        self.movement(button)
    def btn_right_function(self, button):
        self.movement(button)
    def btn_down_function(self, button):
        self.movement(button)

    def movement(self, button: tk.Button):
        print('Pressed the button:' + button)

    def btn_move_function(self):
        message = str('x: ' + str(self.x_coord) + 'y: ' + str(self.y_coord))
        print(message)

    def delete_text(self, text):
        text.delete('1.0', 'end')

    def run(self):
        """Starts the Tkinter event loop."""
        self.gui_thread = threading.Thread(target=self.root.mainloop(), daemon=True)
        self.gui_thread.start()


if __name__ == '__main__':
    gui = RobotGUI("nuri")
    gui.run()
