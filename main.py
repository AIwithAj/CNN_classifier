from CnnClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipelie
from CnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipelie
from CnnClassifier import logger
STAGE_NAME="Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion=DataIngestionTrainingPipelie()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Prepare base model"
try:
    logger.info(f"************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model=PrepareBaseModelTrainingPipelie()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



