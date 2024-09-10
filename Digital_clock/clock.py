import tkinter as tk
import time

root = tk.Tk()
root.title = ("Digital CLock")
root.geometry("400x200") # Set the size of the window
root.config(bg="black") # Background color


lable = tk.Label(root, font=('Helvetica', 58), bg="black",fg="cyan")
lable.pack(pady=20)

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    lable.config(text=current_time)
    lable.after(1000, update_clock)
    
    
update_clock()  # Start the clock

root.mainloop()
