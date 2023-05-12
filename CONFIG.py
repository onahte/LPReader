import os

CWD = os.getcwd()
ALL_IMAGE_FOLDER = os.path.join(CWD, 'train_img', 'lp_labeled')
PRETRAINED_MODEL = os.path.join(CWD, 'efficientdet_d2_coco17_tpu-32')
LABEL_MAP = os.path.join(CWD, 'label_map.pbtxt')
TEST_IMAGES = os.path.join(CWD, 'tensorflow', 'images', 'test')
TRAIN_IMAGES = os.path.join(CWD, 'tensorflow', 'images', 'train')