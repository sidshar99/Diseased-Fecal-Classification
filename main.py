from CVClassifier import logger

from CVClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CVClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion stage"


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<<\n\nX==========X")

    except Exception as e:
        raise e
    

    try:
        logger.info(f">>>>>> stage{STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage{STAGE_NAME} completed <<<<<<\n\nX==========X")

    except Exception as e:
        raise e