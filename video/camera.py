import cv2

class Camera:
    def __init__(self, port = 'http://192.168.0.37:8080/video'):
        self.port = port

    def connect(self):
        self.cap = cv2.VideoCapture(self.port)

    def frame(self):
        ret, frame = self.cap.read()
        print(1)
        return frame

    def reshape(self, frame, scale_percent = 0.6, size = None):
        if size == None:
            width = int(frame.shape[1] * scale_percent)
            height = int(frame.shape[0] * scale_percent)
            size = (width, height)
        frame = cv2.resize(frame, size, interpolation = cv2.INTER_AREA)
        return frame

    def display(self, image, title = 'Stream'):
        cv2.imshow(title, image)
        cv2.waitKey(1)