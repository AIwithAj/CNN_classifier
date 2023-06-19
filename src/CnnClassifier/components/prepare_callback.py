import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from CnnClassifier.entity import PrepareCallnacksConfig

class PrepareCallnacks:
    def __init__(self,config: PrepareCallnacksConfig):
    
        self.config=config

    @property
    def create_tb_callbacks(self):
        timestamp=time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir=os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_log_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_chkpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_tb_chkpt_callbacks(self):
        return [
            self.create_tb_callbacks,
            self._create_chkpt_callbacks
        ]
    