# makes the qr codes that the raspberry pi will scan
import qrcode

codes = []  # list of qrcodes for all event guests

# making qrcodes with the data structure in makeData

def image(qr):
    img = qr.make_image()
    return img


def encode(data):
    qr = qrcode.make(data)
    return qr

