from CnnClassifier.config import ConfigurationManager
from CnnClassifier.components import DataIngestion
from CnnClassifier import logger

class DataIngestionTrainingPipelie:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.dwonload_file()
        data_ingestion.unzip_and_clean()
