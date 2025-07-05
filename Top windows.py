import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("main")

def Topwin():
    
    top = tk.Toplevel()
    top.geometry("180x100")
    top.title("Toplevel")
    
    l2 = tk.Label(top, text="This is toplevel window")
    l2.pack()
    
    top.mainloop()

l = tk.Label(root, text="this is root window")
btn = tk.Button(root, text="Click here to open another window",command=Topwin)

l.pack(pady=16)
btn.pack(pady=16)

root.mainloop()