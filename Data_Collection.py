import cv2
import os

class MyVideoCapture(cv2.VideoCapture):
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.release()


class Dataset:
    def exists(self):
        if os.path.exists(r"C:\Users\L\OneDrive\Desktop\Face_Recognition\data\dataset"):
            pass
        else:
            os.mkdir(r"C:\Users\L\OneDrive\Desktop\Face_Recognition\data\dataset")

def main():
    check = Dataset()
    check.exists()
    haar_cascade = cv2.CascadeClassifier(r'''C:\Users\L\OneDrive\Desktop\Face_Recognition\data\haarcascade_face.xml''')

    index = 0

    serial = input("Enter serial number: ")
    
    codenames = input("Enter name: ")

    with open("names.txt", "a") as file:
         file.write(codenames + "\n")

    with MyVideoCapture(0) as stream:
        while True:
            isTrue, frame = stream.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            detect = haar_cascade.detectMultiScale(gray, 1.1, 6)

            for (x,y,w,h) in detect:
                file_path = r'C:\Users\L\OneDrive\Desktop\Face_Recognition\data\dataset\Users.' + str(serial) + "." + str(index) + ".jpg"
                print("Saving image to:", file_path)
                cv2.imwrite(file_path, gray[y:y+h, x:x+w])
                index += 1
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                cv2.putText(frame,f"Collecting Data {str(int(500-index))} ", (50,50), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

            cv2.imshow("Streaming", frame)

            if cv2.waitKey(27) & 0xFF == ord('q') or index==500:
                break

    cv2.destroyAllWindows()

    print("---------Data Collection Complete--------")

if __name__=="__main__":
    main()
