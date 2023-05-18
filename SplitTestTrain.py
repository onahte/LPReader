import os
import random
import glob
import shutil

from ImageCounter import count_images


def splitTestTrain(all_labeled_images, test_path, train_path, train_split=0.8):
    image_count = count_images(all_labeled_images)
    train_count = image_count * train_split
    all_images = []
    for root, dirs, files in os.walk(all_labeled_images):
        for file in files:
            print(f'Processing {file}')
            f = file.split('.')
            if f[1] == 'xml':
                all_images.append(f[0])

    train_included = []
    while(len(train_included) < train_count):
        random_num = random.randint(0, len(all_images) - 1)
        train_included.append(all_images[random_num])
        all_images.remove(all_images[random_num])
    #print(all_images, train_included)
    train_jpg, train_xml = allocateImages(train_included, all_labeled_images, train_path)
    test_jpg, test_xml = allocateImages(all_images, all_labeled_images, test_path)
    print(f'Total images: {image_count}')
    print(f'Total images:: training:{train_jpg}  testing:{test_jpg}')
    print(f'Total xml::    training:{train_xml}  testing:{test_xml}')

def allocateImages(image_list, source_path, destination_path):
    jpg_files = glob.glob(f'{source_path}**/*.jpg')
    xml_files = glob.glob(f'{source_path}**/*.xml')
    jpg_copied = 0
    xml_copied = 0
    for image in image_list:
        jpg_file = image + '.jpg'
        xml_file = image + '.xml'
        if os.path.join(source_path, jpg_file) in jpg_files:
            copy(source_path, destination_path, jpg_file)
            jpg_copied += 1
        if os.path.join(source_path, xml_file) in xml_files:
            copy(source_path, destination_path, xml_file)
            xml_copied += 1
    return jpg_copied, xml_copied

def copy(source_path, destination_path, file):
    to_copy_source = os.path.join(source_path, file)
    copy_destination = os.path.join(destination_path, file)
    shutil.copy(to_copy_source, copy_destination)
    print(f'Copied {to_copy_source} to {copy_destination}')