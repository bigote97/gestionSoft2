import argparse
import cv2

# Obtenemos el fichero de imagen QR para leer, o bien por parámetro o bien pidiéndolo al usuario
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fichero", type=str, 
    help="Ruta y nombre del fichero de imagen QR a leer")
parser.add_argument("-s", "--Solo_Valor", type=str, 
    help="Mostrar sólo el valor leído (sí/no)")
args = parser.parse_args()

# Obtenemos el parámetro -f (fichero QR a leer)
if args.fichero:
    ficheroQR = args.fichero
else:
    ficheroQR = input("Introduzca el fichero QR a leer: ")

# Obtenemos el parámetro -s (mostrar sólo el valor leído)
if args.Solo_Valor:
    soloValor = args.Solo_Valor
else:
    soloValor = "sí"

# Leer un código QR de imagen
img = cv2.imread(ficheroQR)
det = cv2.QRCodeDetector()
valorQRLeido, pts, st_code = det.detectAndDecode(img)

# Mostramos el valor del QR leído
if soloValor.upper() == "NO":
    print("El valor del QR leído es: ", valorQRLeido)
else:
    print(valorQRLeido)