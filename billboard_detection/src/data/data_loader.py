def load_data(file_path):
    """
    Load data from the specified file path.
    
    Parameters:
    file_path (str): The path to the data file to be loaded.
    
    Returns:
    data: Loaded data.
    """
    import pandas as pd
    
    data = pd.read_csv(file_path)
    return data

def load_multiple_files(file_paths):
    """
    Load multiple data files from the specified list of file paths.
    
    Parameters:
    file_paths (list): A list of paths to the data files to be loaded.
    
    Returns:
    list: A list of loaded data.
    """
    data_list = []
    for path in file_paths:
        data = load_data(path)
        data_list.append(data)
    return data_list

def load_image_data(image_path):
    """
    Load image data from the specified image path.
    
    Parameters:
    image_path (str): The path to the image file to be loaded.
    
    Returns:
    image: Loaded image data.
    """
    from PIL import Image
    
    image = Image.open(image_path)
    return image

def load_raw_data(raw_data_dir):
    """
    Load all raw data from the specified directory.
    
    Parameters:
    raw_data_dir (str): The directory containing raw data files.
    
    Returns:
    list: A list of loaded raw data.
    """
    import os
    
    raw_data_files = [os.path.join(raw_data_dir, f) for f in os.listdir(raw_data_dir) if f.endswith('.csv')]
    return load_multiple_files(raw_data_files)