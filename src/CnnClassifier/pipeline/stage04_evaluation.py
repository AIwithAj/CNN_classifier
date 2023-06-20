from CnnClassifier.config import ConfigurationManager
from CnnClassifier.components import Evaluation
from CnnClassifier import logger

class evaluationPipelie:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        val_config=config.get_validation_config()
        evaluation=Evaluation(val_config)
        evaluation.evaulation()
        evaluation.save_model()
