import os

CWD = os.getcwd()
APIMODEL_PATH = os.path.join(CWD, 'tensorflow', 'models')
CUSTOM_MODEL = 'custom_efficientdet'
CUSTOM_MODEL_PATH = os.path.join(APIMODEL_PATH, 'custom_efficientdet')
ALL_IMAGE_FOLDER = os.path.join(CWD, 'train_img', 'lp_labeled')
ANNOTATIONS = os.path.join(CWD, 'tensorflow', 'annotations')
PRETRAINED_MODEL = 'efficientdet_d2_coco17_tpu-32'
PRETRAINED_MODEL_PATH = os.path.join(CWD, PRETRAINED_MODEL)
LABEL_MAP_FILE = os.path.join(CWD, 'tensorflow', 'annotations', 'label_map.pbtxt')
TEST_IMAGES = os.path.join(CWD, 'tensorflow', 'images', 'test')
TRAIN_IMAGES = os.path.join(CWD, 'tensorflow', 'images', 'train')
GENERATE_TF_RECORD = os.path.join(CWD, 'GenerateTFRecord.py')
PIPELINE_CONFIG = os.path.join(CUSTOM_MODEL_PATH, 'pipeline.config')
TRAINING_SCRIPT = os.path.join(APIMODEL_PATH, 'research', 'object_detection', 'model_main_tf2.py')