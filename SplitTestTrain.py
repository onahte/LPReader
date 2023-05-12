import os
import random

from ImageCounter import count_images


def splitTestTrain(all_labeled_images, train_path, test_path):
    image_count = count_images(all_labeled_images)
    train_count = image_count * 0.8
    test_count = image_count * 0.2
    all_images = []
    for root, dirs, files in os.walk(all_labeled_images):
        for file in files:
            f = file.split('.')
            if f[1] == 'jpg':
                all_images.append(int(f[0]))

    train_included = []
    test_included = []
    while(len(train_included) < train_count):
        random_num = random.randint(0, len(all_images))
        train_included.append(all_images[random_num])
        if random_num < len(all_images) - 1:
            all_images = all_images[:random_num, random_num + 1:]
        else:
            all_images = all_images[:random_num]