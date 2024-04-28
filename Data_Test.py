import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
dataset_path = r"C:\Users\L\OneDrive\Desktop\FaceRecognition\data\dataset"

def load_images(path):
    imgPath = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    labels = []

    print("--------------------Loading data------------------------")

    for imgp in imgPath:
        faceimage = Image.open(imgp).convert('L')
        face_np = np.array(faceimage)
        id = (os.path.split(imgp)[-1].split(".")[1])
        Id = int(id)
        faces.append(face_np)
        labels.append(Id)

    return labels, faces

try:
    labels, faces = load_images(dataset_path)

    print("-----------Training model-----------")

    recognizer.train(faces, np.array(labels))
    recognizer.write("Trainer.yml")
    
    print("---------------Training Complete-----------------")

except:
    print("An error occured during training")


