import cv2

# Função videoCapture()
cap = cv2.VideoCapture('assets/videos/dog.mp4')

# Lendo os Frames do Vídeo
while True:
   _, frame = cap.read() 
   
   cv2.imshow('Vídeo do Dog', frame)
   
    # waitKey para vídeos
   if cv2.waitKey(20) & 0xFF==ord('d'):
        break

cap.release()
cv2.destroyAllWindows()