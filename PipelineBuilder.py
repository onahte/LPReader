import os
import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

from ImageCounter import count_images
from CONFIG import *


config = config_util.get_configs_from_pipeline_file('pipeline.config')
pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
with tf.io.gfile.GFile('pipeline.config', 'r') as f:
    proto_str = f.read()
    text_format.Merge(proto_str, pipeline_config)
pipeline_config.model.ssd.num_classes = 1
pipeline_config.train_config.batch_size = count_images(IMAGE_FOLDER)
pipeline_config.train_config.fine_tune_checkpoint = os.path.join(PRETRAINED_MODEL, 'checkpoint', 'ckpt-0')
pipeline_config.train_config.fine_tune_checkpoint_type = 'detection'
pipeline_config.train_input_reader.label_map_path = LABEL_MAP
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:]
pipeline_config.eval_input_reader[0].label_map_path = LABEL_MAP
pipeline_config.eval