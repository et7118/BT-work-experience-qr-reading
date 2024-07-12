# makes the qr codes that the raspberry pi will scan
import qrcode

codes = []  # list of qrcodes for all event guests


# making qrcodes with the data structure in makeData
def encode(data: str) -> qrcode.QRCode:
    qr = qrcode.make(data)
    return qr


def image(qr: qrcode.QRCode, index: int) -> None:
    qr.save(f'guest{index}.png')  # the index works with the primary key of the guest in George's database


# makes the qr code images for all of the codes in the list qrs
def image_all(qrs: list[qrcode.QRCode]) -> None:
    length = len(qrs)
    for i in range(length):
        image(qrs[i], i)
