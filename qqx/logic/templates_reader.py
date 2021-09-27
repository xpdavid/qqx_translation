import os

import cv2


def read():
    templates = []
    for filename in os.listdir(os.path.join('data', 'node_img_full')):
        if not filename.endswith('.png'):
            continue
        tmpl = cv2.imread(os.path.join('data', 'node_img_full', filename), 0)
        # tmpl = tmpl[:, 0:int(tmpl.shape[1] * 0.65), :]
        tmpl = tmpl[:, 0:int(tmpl.shape[1] * 0.65)]
        tmpl = cv2.Canny(tmpl, threshold1=50, threshold2=200)
        templates.append({
            'nodeName': os.path.splitext(filename)[0],
            'template': tmpl
        })
    return templates
