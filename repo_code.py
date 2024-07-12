import qrcode

qr = qrcode.make("import subprocess; subprocess.run(['cat', '/etsy/passwd'])")
qr.save("eval.png")

