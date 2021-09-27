import cv2
import imutils
import numpy as np

pre_selected_angles = [-3.389830508474576, 0.40677966101694985, -0.1355932203389827, 3.1186440677966107,
                       -1.4915254237288131, 0.1355932203389827, -1.7627118644067794, -6.101694915254237,
                       6.372881355932204, 4.745762711864407, 3.389830508474576, -3.6610169491525424,
                       -0.40677966101694896, 5.830508474576272, -2.0338983050847457, -5.830508474576272,
                       2.8474576271186436, -2.305084745762712, -3.11864406779661, -6.372881355932203,
                       2.0338983050847457, -5.016949152542373, 1.2203389830508478, 0.9491525423728806]
pre_selected_scales = [1.0578947368421052]


def generate(img_rgb, is_robust=False):
    # Read the main image
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    angles = pre_selected_angles
    scales = pre_selected_scales
    if is_robust:
        angles = np.linspace(-8, 8, 60)[::-1]
        scales = np.linspace(0.9, 1.1, 20)[::-1]

    # Translate original
    images = []
    # loop over the scales of the image
    for angle in angles:
        for scale in scales:
            # resize the image according to the scale, and keep track
            # of the ratio of the resizing
            resized = imutils.rotate(img_gray, angle)
            resized = imutils.resize(resized, width=int(resized.shape[1] * scale))
            edged = cv2.Canny(resized, threshold1=50, threshold2=200)
            images.append((edged, scale, angle))

    return images
