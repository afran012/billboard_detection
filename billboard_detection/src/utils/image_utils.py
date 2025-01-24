def resize_image(image, target_size):
    from PIL import Image
    
    return image.resize(target_size, Image.ANTIALIAS)

def convert_to_grayscale(image):
    return image.convert("L")

def normalize_image(image):
    import numpy as np
    
    return np.array(image) / 255.0

def filter_image(image, filter_type):
    from PIL import ImageFilter
    
    if filter_type == 'blur':
        return image.filter(ImageFilter.BLUR)
    elif filter_type == 'sharpen':
        return image.filter(ImageFilter.SHARPEN)
    else:
        raise ValueError("Unsupported filter type. Use 'blur' or 'sharpen'.")