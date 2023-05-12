import os

def count_images(image_folder):
    count = 0
    for root, dirs, files in os.walk(image_folder):
        for file in files:
            if file.endswith('jpg'):
                count += 1
    return count