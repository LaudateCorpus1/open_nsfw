import numpy as np
import skimage
import skimage.io
from PIL import Image
from io import BytesIO

VGG_MEAN = [104, 117, 123]

"""Yahoo open_nsfw image loading mechanism

Approximation of the image loading mechanism defined in
https://github.com/yahoo/open_nsfw/blob/79f77bcd45076b000df71742a59d726aa4a36ad1/classify_nsfw.py#L40
"""


def yahoo_load_image(img_data):
    im = Image.open(BytesIO(img_data))

    if im.mode != "RGB":
        im = im.convert('RGB')

    imr = im.resize((256, 256), resample=Image.BILINEAR)

    fh_im = BytesIO()
    imr.save(fh_im, format='JPEG')
    fh_im.seek(0)

    image = (skimage.img_as_float(skimage.io.imread(fh_im, as_gray=False))
             .astype(np.float32))

    H, W, _ = image.shape
    h, w = (224, 224)

    h_off = max((H - h) // 2, 0)
    w_off = max((W - w) // 2, 0)
    image = image[h_off:h_off + h, w_off:w_off + w, :]

    # RGB to BGR
    image = image[:, :, :: -1]

    image = image.astype(np.float32, copy=False)
    image = image * 255.0
    image -= np.array(VGG_MEAN, dtype=np.float32)
    expand_dims = True
    if expand_dims:
        image = np.expand_dims(image, axis=0)

    return image
