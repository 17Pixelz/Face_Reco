import pyrebase
import os
import pyrebaseconfig as cfg
from dotenv import load_dotenv

load_dotenv()

IMG_DIR = os.getenv('UNKNOWN_DIR')

def getAllImages():
    old_imgs = [f for f in os.listdir(IMG_DIR)]
    for f in old_imgs:
        os.remove(os.path.join(IMG_DIR,f))

    firebase_storage = pyrebase.initialize_app(cfg.config)

    storage = firebase_storage.storage()

    all_imgs = storage.list_files()

    for img in all_imgs:
        img.download_to_filename(IMG_DIR + "IMG_" +img.name)
        storage.delete(img.name)
