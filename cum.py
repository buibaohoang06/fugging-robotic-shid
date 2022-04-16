import cv2
from face_rec import Facerec
import time
import json

cap = cv2.VideoCapture(0)

sfr = Facerec()
sfr.load_encoding_images("faces/")


while True:
    ret, frame = cap.read()
    face_locations, face_name = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_name):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 200  ), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 2)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if len(face_name) == 0:
        status = False
    else:
        status = True
    dict = {
        "status": status
    }
    json_object = json.dumps(dict, indent = 4)
    with open('shid.json', 'w') as shid:
        shid.write(json_object)

