from CVClassifier import logger

from CVClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CVClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from CVClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from CVClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

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

STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e