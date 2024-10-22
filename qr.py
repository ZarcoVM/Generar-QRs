# este es el comando para instalar qrcode 
# pip install qrcode[pil]

import qrcode #Se importa la libreria que posteriormente instalamos

# URL que se desea codificar en el QR.
url = "https://github.com/angel-manuel-zarco"

qr = qrcode.QRCode(
    version=1,
    box_size=25,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

imagen = qr.make_image(fill_color="black", back_color="white")
imagen.save("QR.png")  # Agregamos la extensión .png
