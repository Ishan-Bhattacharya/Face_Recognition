import cv2
import os

class MyVideoCapture(cv2.VideoCapture):
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.release()


class Dataset:
    def exists(self):
        if os.path.exists(r"dataset"):
            pass
        else:
            os.mkdir(r"dataset")

    def get_next_serial(self, dataset_name):
        serial_file = "serial.txt"
        if os.path.exists(serial_file):
            with open(serial_file, "r") as file:
                serial_data = file.read().strip().splitlines()
                serial = {name: int(value) for name, value in (line.split(':') for line in serial_data)}
        else:
            serial = {}
        if dataset_name not in serial:
            if serial:
                next_serial = max(serial.values()) + 1
            else:
                next_serial = 1
            serial[dataset_name] = next_serial
            with open(serial_file, "w") as file:
                file.writelines([f"{name}:{value}\n" for name, value in serial.items()])
            return next_serial
        else:
            return serial[dataset_name]

def main():
    check = Dataset()
    check.exists()
    haar_cascade = cv2.CascadeClassifier(r'''haarcascade_face.xml''')

    index = 0
    
    codenames = input("Enter name: ")

    with open("names.txt", "a+") as file:
        file.seek(0)
        names = file.read().splitlines()
        if codenames not in names:
            file.write(codenames + "\n")

    with MyVideoCapture(0) as stream:
        while True:
            isTrue, frame = stream.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            detect = haar_cascade.detectMultiScale(gray, 1.1, 6)

            for (x,y,w,h) in detect:
                file_path = r'dataset\Users.' + str(serial) + "." + str(index) + ".jpg"
                serial = check.get_next_serial(codenames)
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
