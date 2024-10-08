from typing import Literal, List, Union
from . import Loss

import torch
import tensorflow as tf
from torch.nn import functional as F
from tensorflow.keras.losses import categorical_crossentropy


class CategoricalCrossEntropy(Loss):
    def __init__(self,
                 framework: Literal["torch", "tf"]
                 ) -> None:
        super().__init__(framework)

    def calculate(self, 
                  predictions: Union[torch.Tensor, tf.Tensor], 
                  targets: Union[torch.Tensor, tf.Tensor]):
        return super().calculate(predictions, targets)

    def torch_op(self, 
                 predictions: torch.Tensor, 
                 targets: torch.Tensor
                 ) -> torch.Tensor:
        loss = F.cross_entropy(predictions, targets)
        return loss

    def tf_op(self, 
              predictions: tf.Tensor, 
              targets: tf.Tensor
              ) -> tf.Tensor:
        loss = categorical_crossentropy(targets, predictions)
        return tf.reduce_mean(loss)
