import cv2
import numpy as np

cap = cv2.VideoCapture('assets/videos/dog.mp4')

# criar função que faz o rescale para cada frame individual

def rescale_frame(frame: np.array,
                  scale: float=0.75):
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)
    
    return cv2.resize(frame, (largura, altura), interpolation=cv2.INTER_AREA)

def resize_frame(width: int, height: int):
    cap.set(3, width)
    cap.set(4, height)
    
    
# IMAGEM ##########
# img = cv2.imread('assets/fotos/cat.jpg')
# cv2.imshow('Cat', img)

# resized_img = rescale_frame(img, 0.2)
# cv2.imshow('Cat', resized_img)
# cv2.waitKey(0)

while True:
    _, frame = cap.read()
    
    frame_resized = rescale_frame(frame, 0.5)
    
    cv2.imshow('Video do Dog', frame_resized)
    
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break