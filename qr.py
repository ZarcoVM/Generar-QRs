# este es el comando para instalar qrcode 
# pip install qrcode[pil] 



import qrcode #Se importa la libreria que posteriormente instalamos



# URL que se desea codificar en el QR. esta ruta se cambia, 
# en mi ejemplo se redirije a mi plataforma de git hub pero 
# podria ser perferfectanebte cualquier cosa
url = "https://github.com/angel-manuel-zarco"

# Crea una instancia de QRCode con parámetros personalizados.
qr = qrcode.QRCode(
    version=1,      # Controla el tamaño del QR (1 es el más pequeño).
    box_size=25,    # Tamaño de cada cuadrado del código en píxeles.
    border=5        # Grosor del borde del QR (en cuadros blancos).
)


# Agrega la URL al objeto QRCode.
qr.add_data(url)

# Ajusta automáticamente el tamaño para que encaje con los datos proporcionados.
qr.make(fit=True)

# Genera la imagen del código QR con los colores deseados.
imagen = qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen generada en fo