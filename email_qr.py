import qrcode

email = input("Enter email: ")
qrcode.make(f"mailto:{email}").save("qr_email.png")

print("Email QR saved as qr_email.png")
