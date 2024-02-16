i = 5
while True:
    if i%0o11 == 0:
        break
    print(i)
    i += 1




from tkinter import *
import tkinter.messagebox

window = Tk()
window.wm_withdraw()

# message at x:200,y:200
window.geometry("1x1+200+200")  # remember its.geometry("WidthxHeight(+or-)X(+or-)Y")
tkinter.messagebox.showerror(title="error", message="Error Message", parent=window)

# center screen message
window.geometry(f"1x1+{round(window.winfo_screenwidth() / 2)}+{round(window.winfo_screenheight() / 2)}")
tkinter.messagebox.showinfo(title="Greetings", message=f"Hello World! {i}")


#zeki@torontotec
#Go@2030!  
