import cv2

class qrCodeScanner:
    def __init__(self) -> None:
        self.vid = None #cv2.VideoCapture(0)
        self.detector = None #cv2.QRCodeDetector()

    def scanCode(self):
        self.vid = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        
        while True:
            ret, frame = self.vid.read()
            data, bbox, straight_qrcode = self.detector.detectAndDecode(frame)
            if len(data) > 0:
                print(data)
                return data
            
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            
    def closeCam(self):
        self.vid.release()
        cv2.destroyAllWindows()

# obj = qrCodeScanner()
# print(obj.scanCode())
# obj.closeCam()


'''
# import the opencv library
import cv2
# define a video capture object
vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    # Capture the video frame by frame
    ret, frame = vid.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if len(data) > 0:
        print(data)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
'''