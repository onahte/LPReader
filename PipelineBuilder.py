import os
import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format

from ImageCounter import count_images
from CONFIG import *

def buildPipeline(pretrained_model_path, all_image_folder_path, annotation_path, label_map, pipeline_config_path):
    os.system(f'cp {os.path.join(pretrained_model_path, "pipeline.config")} {pipeline_config_path}')
    config = config_util.get_configs_from_pipeline_file('pipeline.config')
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    with tf.io.gfile.GFile(pipeline_config_path, 'r') as f:
        proto_str = f.read()
        text_format.Merge(proto_str, pipeline_config)
    pipeline_config.model.ssd.num_classes = 1
    pipeline_config.train_config.batch_size = count_images(all_image_folder_path)
    pipeline_config.train_config.fine_tune_checkpoint = os.path.join(pretrained_model_path, 'checkpoint', 'ckpt-0')
    pipeline_config.train_config.fine_tune_checkpoint_type = 'detection'
    pipeline_config.train_input_reader.label_map_path = label_map
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = [os.path.join(annotation_path, 'train.record')]
    pipeline_config.eval_input_reader[0].label_map_path = label_map
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = [os.path.join(annotation_path, 'test.record')]

    config_text = text_format.MessageToString(pipeline_config)
    with tf.io.gfile.GFile(pipeline_config_path, 'wb') as f:
        f.write(config_text)
