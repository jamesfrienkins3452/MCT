import numpy as np
import cv2

thres = 0.5
nms_threshold = 0.2

classNames = []

with open('graphic\\video\\data\\dataset.names','r') as f:
    classNames = f.read().splitlines()


font = cv2.FONT_HERSHEY_PLAIN
Colors = np.random.uniform(0, 255, size=(len(classNames), 3))

weightsPath = "graphic\\video\\data\\graph.pb"
configPath = "graphic\\video\\data\\dataset_settings.pbtxt"
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def recognize_image(img):
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1,-1)[0])
    confs = list(map(float,confs))

    indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
    if len(classIds) != 0:
        for i in indices:
            box = bbox[i]
            confidence = str(round(confs[i],2))
            color = Colors[classIds[i]-1]
            x,y,w,h = box[0],box[1],box[2],box[3]
            cv2.rectangle(img, (x,y), (x+w,y+h), color, thickness=2)
            cv2.putText(img, classNames[classIds[i]-1]+" "+confidence,(x+10,y+20),
                        font,1,color,2)
        print(indices)
    return img