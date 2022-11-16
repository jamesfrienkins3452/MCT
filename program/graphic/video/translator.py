import cv2

class Camera:
    def __init__(self, port):
        self.port = port + '/video'

    def connect(self):
        self.cap = cv2.VideoCapture(self.port)

    def frame(self):
        ret, frame = self.cap.read()
        return frame

    def reshape(self, frame, scale_percent = 0.6, size = None):
        if size == None:
            width = int(frame.shape[1] * scale_percent)
            height = int(frame.shape[0] * scale_percent)
            size = (width, height)
        frame = cv2.resize(frame, size, interpolation = cv2.INTER_AREA)
        return frame

    def display(self, title = 'Stream'):
        cv2.imshow(title, self.reshape(self.frame()))
        cv2.waitKey(5)