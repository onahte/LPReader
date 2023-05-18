import os

from CONFIG import *
from SplitTestTrain import splitTestTrain
from CreateLabelMap import createMap
from GenerateTFRecord import generateTFRecord
from PipelineBuilder import buildPipeline

def buildModel(labels):
    # Split images into training and testing.
    # Default is train_split=0.8. Change this value to configure to a different split.
    splitTestTrain(ALL_IMAGE_FOLDER, TEST_IMAGES, TRAIN_IMAGES)

    # Create label map
    createMap(labels)

    # Create TF Records --> train.record & test.record
    generateTFRecord(LABEL_MAP_FILE, os.path.join(ANNOTATIONS, "train.record"), TRAIN_IMAGES, TRAIN_IMAGES)
    generateTFRecord(LABEL_MAP_FILE, os.path.join(ANNOTATIONS, "test.record"), TEST_IMAGES, TEST_IMAGES)

    # Create pipeline.config
    buildPipeline(PRETRAINED_MODEL_PATH, ALL_IMAGE_FOLDER, ANNOTATIONS, LABEL_MAP_FILE, PIPELINE_CONFIG)

    print('Successfully built pretrained model.')

def trainModel(training_steps):
    training_script = f'python {TRAINING_SCRIPT} --model_dir={CUSTOM_MODEL_PATH} --pipeline_config_path={PIPELINE_CONFIG} --num_train_steps={training_steps}'
    print('Running: ', training_script)
    os.system(training_script)

    print('Successfully trained model.')

def main():
    labels = [{'name': 'license', 'id': '1'},]
    if not os.path.exists(PIPELINE_CONFIG):
        buildModel(labels)
    trainModel(training_steps=2000)

if __name__ == '__main__':
    main()