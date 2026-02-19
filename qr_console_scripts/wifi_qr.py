import qrcode

ssid = input("WiFi Name: ")
password = input("Password: ")

wifi = f"WIFI:T:WPA;S:{ssid};P:{password};;"
qrcode.make(wifi).save("qr_wifi.png")

print("WiFi QR saved as qr_wifi.png")
