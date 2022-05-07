import numpy as np

def screenFuse(img1, img2):
    img1_f = np.float32(img1)  # BGR format
    img2_f = np.float32(img2)
    f_255 = np.float32(np.full_like(img1_f, 255))
    rlt = 255 - ((f_255-img1_f)*(f_255-img2_f))/255
    return rlt.round().clip(0,255).astype(np.uint8)

def RevScreenFuse(img1, rlt):
    img1_f = np.float32(img1)  
    rlt_f = np.float32(rlt)
    f_255 = np.float32(np.full_like(img1_f, 255))
    img2 = f_255 - (255 - rlt_f)*255/(f_255-img1_f)
    return img2.round().clip(0,255).astype(np.uint8)
