import cv2 

class MyVideoCapture(cv2.VideoCapture):
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.release()

detection = cv2.CascadeClassifier(r"C:\Users\L\OneDrive\Desktop\Face_Recognition\data\haarcascade_face.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r"C:\Users\L\OneDrive\Desktop\Face_Recognition\Trainer.yml")

names = ["", "Ishan Bhattacharya", "Shivangi Basu", "Tamanna Mandal", "Nabanita Bhattacharya", "Krishanu Bhattacharya"]

with open("names.txt", "r") as file:
    for name in file.readlines():
        name = name.strip()
        if name not in names:
            names.append(name)

threshold = 80

with MyVideoCapture(0) as stream:
    while True:
        isTrue,frame=stream.read()
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detection.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf<threshold:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
                cv2.rectangle(frame, (x,y-40), (x+w+60,y), (0,0,255), -1)
                cv2.putText(frame, names[serial], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
            else:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
                cv2.rectangle(frame, (x,y-40), (x+w,y), (0,0,255), -1)
                cv2.putText(frame, "Unknown Entity", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF==ord("q"):
            break

    cv2.destroyAllWindows()