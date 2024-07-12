import qrcode

qr = qrcode.make("https://github.com/et7118/BT-work-experience-qr-reading")
qr.save("repo.png")

