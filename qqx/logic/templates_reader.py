import os

import cv2
import numpy as np
import sys


def resource_path(*relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, *relative_path)


def read():
    templates = []
    for filename in os.listdir(resource_path('data', 'node_img_full')):
        if not str(filename).endswith('.png'):
            continue
        file_stream = open(resource_path('data', 'node_img_full', str(filename)), "rb")
        file_bytes = bytearray(file_stream.read())
        img_array = np.asarray(file_bytes, dtype=np.uint8)
        tmpl = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
        tmpl = tmpl[:, 0:int(tmpl.shape[1] * 0.65)]
        tmpl = cv2.Canny(tmpl, threshold1=50, threshold2=200)
        templates.append({
            'nodeName': os.path.splitext(filename)[0],
            'template': tmpl
        })
    return templates
