import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx= 20, pady= 20)

textbox = tk.Text(root, height=5, font=('Arial', 16))
textbox.pack(padx=20, pady=10)

buttonFrame = tk.Frame(root, padx=20, pady=10)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

buttonFrame.pack(fill='x')

anotherbtn = tk.Button(root, text="test")
anotherbtn.place(x=350, y=200, height=100, width= 100)





root.mainloop() # instead main function (if __name__ = main())
