import subprocess
import sys
import numpy as np # para conveter arrays

# Garantindo que as dependências estão instaladas em cada máquina que rodar esse script
# comandos = ["pip3 install opencv-python", "pip3 install pytesseract", "pip3 install pyautogui"]

# try:
#     for comando in comandos:
#         resultado = subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, text=True)
# except subprocess.CalledProcessError as error:
#     sys.exit(error)
# else:
#   print(resultado.stdout)

import cv2 # opencv
import numpy as np
import pytesseract # para detectar texto em imagem
import pyautogui # para tirar print da tela

pytesseract.tesseract_cmd = r"F:\ProgramFiles(x64)\Tesseract-OCR\tesseract.exe"

# Ler a imagem
img = cv2.imread("C:\\Users\\Yuri\\Desktop\\WakfuMarket\\BackEnd\\data\\image.png")

# Converter a imagem para o espaço de cores HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir intervalo de cor para a cor branca (em HSV)
lower_white = np.array([0, 0, 200]) # Ajuste conforme necessário
upper_white = np.array([180, 30, 255]) # Ajuste conforme necessário

# Criar máscara para identificar pixels brancos
mask = cv2.inRange(hsv_img, lower_white, upper_white)

# Interessante para testar alguns parâmetros de branco
# cv2.imshow("Display window", mask)
# k = cv2.waitKey(0) # Wait for a keystroke in the window

# Aplicar a máscara na imagem original
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Converter imagem para escala de cinza para a detecção de letras
gray_img = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)

# Reconhecimento de letras
letter_boxes = pytesseract.image_to_boxes(gray_img)

# Desenhar retângulos
height, width, c = img.shape
for box in letter_boxes.splitlines():
    box = box.split()
    x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
    cv2.rectangle(img, (x, height - y), (w, height - h), (0, 0, 255), 1)

# Exibir resultado
print(letter_boxes)
cv2.imshow("Display window", img)
k = cv2.waitKey(0) # Wait for a keystroke in the window
