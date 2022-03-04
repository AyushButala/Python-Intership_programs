import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=20,
    border=1
)
message = "Hello"
qr.add_data(message)
qr.make(fit=True)
data=qr.make_image()
data.save("Qrdemo.png")