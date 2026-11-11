import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import cv2

# Alejandra Rivera Valenzuela NC = 0200
print("Alejandra Rivera Valenzuela NC = 0200")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")

# 1. Cargar la imagen en escala de grises
alvarito_foto = cv2.imread('alvarito_0200_ml.webp', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(8, 6))
plt.imshow(alvarito_foto, cmap='gray')
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.title('Imagen Normal - Alejandra Rivera 0200')
plt.show()  # Muestra la primera ventana independiente

print("<3<3<3<3 Puntos de la imagen <3<3<3<3")

plt.figure(figsize=(8, 6))
plt.imshow(alvarito_foto, cmap='gray')

x = [100, 100, 300]
y = [100, 400, 500]

plt.scatter(x, y, s=40, c='red', label='Puntos')
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.title('Alvarito Diaz y Alejandra Rivera 0200')
plt.show()  

print("<3<3<3<3 Circulo de la imagen <3<3<3<3<3")

# Cargar la imagen a color y convertir de BGR a RGB para Matplotlib
alvarito_color = cv2.imread('alvarito_0200_ml.webp')
alvarito_rgb = cv2.cvtColor(alvarito_color, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 6))
plt.imshow(alvarito_rgb)

# Parámetros para dibujar un círculo centrado en la cara
centro_x, centro_y = 590, 425
radio = 120
theta = np.linspace(0, 2 * np.pi, 100)

x_circulo = centro_x + radio * np.cos(theta)
y_circulo = centro_y + radio * np.sin(theta)

plt.plot(x_circulo, y_circulo, c='green', linewidth=2, label='Círculo')
plt.xlabel('Coordenada X', fontsize=12)
plt.ylabel('Coordenada Y', fontsize=12)
plt.title('Alvarito Diaz y Alejandra Rivera 0200')
plt.show()

