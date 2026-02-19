import qrcode

place = input("Enter location: ")
qrcode.make("https://maps.google.com/?q=" + place).save("qr_map.png")

print("Map QR saved as qr_map.png")
