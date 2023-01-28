import qrcode

qr = qrcode.QRCode(
    version = 1,
    box_size = 15,
    border = 15
)

data = "IMAC-Өрөөний дугаар 315"

qr.add_data(data)

qr.make(fir=True)

img = qr.make_image(fill = 'black', back_color = "white")
img.save('Linked-code.png')