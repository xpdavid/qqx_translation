import cv2

from . import templates_reader, image_generator, candidates_spliter

# Specify a threshold
threshold = 0.32


def process(img_rgb, progress_updater=lambda x: None, logger=lambda txt: None, is_robust=False):
    # Read the templates
    templates = templates_reader.read()
    # Generate images
    images = image_generator.generate(img_rgb, is_robust)
    # Found matches
    candidates = []
    for idx, template in enumerate(templates):
        found = None
        tH, tW = template['template'].shape
        # loop over images
        for img in images:
            (resized, scale, angle) = img
            if resized.shape[0] < tH or resized.shape[1] < tW:
                break
            result = cv2.matchTemplate(resized, template['template'], cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, scale, angle)

        if found is None:
            continue
        # unpack the bookkeeping variable and compute the (x, y) coordinates
        # of the bounding box based on the resized ratio
        (maxVal, maxLoc, scale, angle) = found

        logger('{}: {} - ({:.4f})({:.4f})'.format(template['nodeName'], maxVal, angle, scale))
        if maxVal <= threshold:
            continue

        r = 1
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
        # draw a bounding box around the detected result and display the image
        cv2.rectangle(img_rgb, (startX, startY), (endX, endY), (0, 0, 255), 2)
        candidates.append({
            'pos': (startX, startY),
            'score': maxVal,
            'name': template['nodeName'],
            'angle': angle,
            'scale': scale
        })

        # update progress
        progress_updater(int((idx + 1.0) * 100.0 / len(templates)))

    progress_updater(100)
    (top_cards, bottom_cards) = candidates_spliter.split(candidates)

    logger(list(map(lambda ele: ele['name'], top_cards)))
    logger(list(map(lambda ele: ele['name'], bottom_cards)))
    logger(list(dict.fromkeys(map(lambda ele: ele['angle'], top_cards))))
    logger(list(dict.fromkeys(map(lambda ele: ele['scale'], bottom_cards))))

    return list(map(lambda ele: ele['name'], top_cards)), list(map(lambda ele: ele['name'], bottom_cards)), img_rgb
