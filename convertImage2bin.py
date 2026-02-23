import numpy as np
from PIL import Image

def rgb2gray(rgb_image):
    """
    Convert RGB image to gray tons (0–255)
    """
  
    img = np.array(rgb_image).astype(np.float32)

    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    gray = 0.299 * R + 0.587 * G + 0.114 * B
    gray = np.clip(gray, 0, 255).astype(np.uint8)

    return gray

def gray2bin(gray_image, lim=128):
    """
    Converte imagem em tons de cinza para binária (0 e 255)
    """
    bin = np.where(gray_image >= lim, 255, 0).astype(np.uint8)
    return bin



# Carrega imagem colorida
img_rgb = Image.open("bird.png").convert("RGB")

# Converte para cinza
img_gray = rgb2gray(img_rgb)

# Converte para binária
img_bin = gray2bin(img_gray, lim=128)

# Salva resultados
Image.fromarray(img_gray).save("gray_image.png")
Image.fromarray(img_bin).save("bin_image.png")



