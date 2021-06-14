import os
import face_recognition
from PIL import Image, ImageDraw
from writeAbsence import giveAbsenceFile
from dotenv import load_dotenv

load_dotenv()

KNOWN_IMG_PATH = os.getenv('KNOWN_DIR')
UNKNOWN_IMG_PATH =os.getenv('UNKNOWN_DIR')

names = []
known_face_encodings = []
known_face_names = []

def loadFaces():
    for root, dirs, files in os.walk(KNOWN_IMG_PATH):
        for filename in files:
            known_face_names.append(filename.replace('_',' ').split('.')[0])
            image_of_bill = face_recognition.load_image_file(KNOWN_IMG_PATH + filename)
            known_face_encodings.append(face_recognition.face_encodings(image_of_bill)[0])

def detectFaces():
    loadFaces()
    for root, dirs, files in os.walk(UNKNOWN_IMG_PATH):
        for filename in files:
            print(filename)
            # Load test image to find faces in
            test_image = face_recognition.load_image_file(UNKNOWN_IMG_PATH + filename)

            # Find faces in test image
            face_locations = face_recognition.face_locations(test_image)
            face_encodings = face_recognition.face_encodings(test_image, face_locations)

            # Convert to PIL format
            pil_image = Image.fromarray(test_image)

            # Create a ImageDraw instance
            draw = ImageDraw.Draw(pil_image)

            # Loop through faces in test image
            for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown Person"

                # If match
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                # Draw box
                draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

                # Draw label
                text_width, text_height = draw.textsize(name)
                draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
                draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

            del draw
            # Display image
            pil_image.show()

            names.append(name)
            print(name)
    giveAbsenceFile(names)
