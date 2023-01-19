import webbrowser 
import cv2 
cap = cv2.VideoCapture(0) 
# initialize the cv2 QRCode detector 
detector = cv2.QRCodeDetector()
# from dbr import *

# BarcodeReader.init_license("DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ==")
while True: 
    _, img = cap.read()
    # detect and decode 
    data, bbox, _ = detector.detectAndDecode(img) 
    # check if there is a QRCode in the image 
    if data: 
        a=data 
        break
    cv2.imshow("QRCODEscanner", img)     
    if cv2.waitKey(1) == ord("q"): 
        break
b=webbrowser.open(str(a)) 
print(a)
cap.release() 
cv2.destroyAllWindows()