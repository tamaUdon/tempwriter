#!/usr/bin/env python

# ref. https://www.tensorflow.org/tutorials/images/data_augmentation

# - サイズを327*510に正規化
#   - 元データに合わせる
# - 1クラスあたり現状100枚を3倍にする
#     回転(20度まで)、拡大or縮小
#         - 回転、拡大、縮小それぞれランダムにかける
#         - 1枚あたり3回で実装

# Import library
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

from tensorflow.keras import layers

# Download images
(train_ds, val_ds, test_ds), metadata = tfds.load(
    'tf_flowers',
    split=['train[:80%]', 'train[80%:90%]', 'train[90%:]'],
    with_info=True,
    as_supervised=True,
)

# Count classes 
num_classes = metadata.features['label'].num_classes
print(num_classes)

# Data augmentation
# tf.keras.layers.RandomFlip (反転)
# tf.keras.layers.RandomRotation (回転)

data_augmentation = tf.keras.Sequential([
  layers.RandomRotation(0.2),
])

# Flip images (only "E")


aug_ds = train_ds.map(
  lambda x, y: (resize_and_rescale(x, training=True), y))
