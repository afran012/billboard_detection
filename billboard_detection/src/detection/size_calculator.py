def calculate_billboard_size(detected_bounding_box):
    """
    Calculate the size of the detected billboard based on its bounding box.

    Parameters:
    detected_bounding_box (tuple): A tuple containing the coordinates of the bounding box
                                    in the format (x_min, y_min, x_max, y_max).

    Returns:
    float: The area of the detected billboard.
    """
    x_min, y_min, x_max, y_max = detected_bounding_box
    width = x_max - x_min
    height = y_max - y_min
    area = width * height
    return area


def calculate_aspect_ratio(detected_bounding_box):
    """
    Calculate the aspect ratio of the detected billboard.

    Parameters:
    detected_bounding_box (tuple): A tuple containing the coordinates of the bounding box
                                    in the format (x_min, y_min, x_max, y_max).

    Returns:
    float: The aspect ratio of the detected billboard.
    """
    x_min, y_min, x_max, y_max = detected_bounding_box
    width = x_max - x_min
    height = y_max - y_min
    if height == 0:
        return 0
    aspect_ratio = width / height
    return aspect_ratio