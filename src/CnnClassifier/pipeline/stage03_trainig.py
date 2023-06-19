from CnnClassifier.config import ConfigurationManager
from CnnClassifier.components import PrepareCallnacks,Training
from CnnClassifier import logger

class ModelTrainingPipelie:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        prepare_callback_config=config.get_prepare_callbacks_config()
        prepare_callbacks=PrepareCallnacks(config=prepare_callback_config)
        callback_list=prepare_callbacks.get_tb_chkpt_callbacks()


        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callaback_list=callback_list
        )