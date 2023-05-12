import os
import subprocess

from CONFIG import *

splitTestTrain(ALL_IMAGE_FOLDER, TEST_IMAGES, TRAIN_IMAGES)

build_TF_record = 'python GenerateTFRecord.py -x '
