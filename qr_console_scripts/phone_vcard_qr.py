import qrcode

name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email (optional): ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

qrcode.make(vcard).save("qr_contact.png")

print("Contact QR saved as qr_contact.png")
