import numpy as np
import cv2
from PIL import ImageGrab

def screenCast(name, x, y, fps, bbox):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(name + '.avi', fourcc, fps, refineDimensions(x, y, bbox))

    while 1==1:
        img = ImageGrab.grab(bbox)
        img_np = np.array(img)
        img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        
        video.write(img_np)
        cv2.imshow("Video Frame", img_np)
        key = cv2.waitKey(1)

        if key == 27:
            break

    video.release()
    cv2.destroyAllWindows()

def screenCastUserDefined():
    vidName = input('Name of video: ')
    writerXCord = int(input('Writer\'s top-left X: ')) #Dimensions for VideoWriter
    writerYCord = int(input('Writer\'s bottom-right Y: ')) #Dimensions for VideoWriter
    bboxLX = int(input('Bound-box top-left x: '))
    bboxLY = int(input('Bound-box top-left y: '))
    bboxRX = int(input('Bound-box bottom-right x: '))
    bboxRY = int(input('Bound-box bottom-right y: '))

    bbox = (bboxLX, bboxLY, bboxRX, bboxRY)

    screenCast(vidName, (writerXCord, writerYCord), 10, bbox)

def refineDimensions(x, y, bbox):
    x = x - bbox[0]
    y = y - bbox[1]

    return(x, y)
