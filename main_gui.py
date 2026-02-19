import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk   # needed for preview

img = None
tkimg = None

def generate(data):
    global img, tkimg

    if not data.strip():
        messagebox.showerror("Error", "Enter required fields")
        return

    img = qrcode.make(data)
    img.save("temp_qr.png")

    # convert for Tkinter preview
    pil_img = Image.open("temp_qr.png").resize((180,180))
    tkimg = ImageTk.PhotoImage(pil_img)

    preview.config(image=tkimg)
    preview.image = tkimg

    status.config(text="QR Generated (click Save)")

def text_qr():
    generate(entry.get())

def wifi_qr():
    wifi = f"WIFI:T:WPA;S:{entry.get()};P:{entry2.get()};;"
    generate(wifi)

def phone_qr():
    name = entry.get().strip()
    phone = entry2.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Enter name and phone number")
        return

    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
END:VCARD"""

    generate(vcard)


def save():
    if img is None:
        messagebox.showwarning("Warning", "Generate QR first")
        return
    img.save("saved_qr.png")
    status.config(text="Saved as saved_qr.png")
    messagebox.showinfo("Saved", "QR saved successfully")

def clear():
    entry.delete(0, END)
    entry2.delete(0, END)
    preview.config(image="")
    status.config(text="Fields cleared")

# window
root = Tk()
root.title("QR Generator by -> _Shubham")
root.geometry("500x600")

Label(root, text="Name / Text / URL:", font=("Arial",12)).pack(pady=4)
entry = Entry(root, width=35)
entry.pack()

Label(root, text="WiFi Password / Phone No:", font=("Arial",10)).pack(pady=3)
entry2 = Entry(root, width=35)
entry2.pack()

Button(root, text="Text / Website QR", width=28, command=text_qr).pack(pady=3)
Button(root, text="WiFi QR", width=28, command=wifi_qr).pack(pady=3)
Button(root, text="Phone QR", width=28, command=phone_qr).pack(pady=3)

Button(root, text="Save QR", width=28, command=save).pack(pady=6)
Button(root, text="Clear Fields", width=28, command=clear).pack(pady=3)

preview = Label(root, relief="solid")
preview.pack(pady=10)

status = Label(root, text="Ready", fg="green")
status.pack()

root.mainloop()
