from TextSummary.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummary.pipeline.stage_o2_data_validation import DataValidationTrainingPipeline
from TextSummary.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

from TextSummary.logging import logger



STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(STAGE_NAME + " started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(STAGE_NAME + " completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(STAGE_NAME + " started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(STAGE_NAME + " completed")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation stage"

try:
    logger.info(STAGE_NAME + " started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(STAGE_NAME + " completed")
except Exception as e:
    logger.exception(e)
    raise e