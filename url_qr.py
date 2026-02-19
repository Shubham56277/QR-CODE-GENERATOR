import qrcode
url = input("Enter text or URL: ")
qrcode.make(url).save("qrcode.png")
print("QR saved as qrcode.png")