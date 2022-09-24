from deepClassifier.components import DataIngestion
from deepClassifier.config import ConfigurationManager
from deepClassifier import logger

STAGE_NAME="Data Ingestion Stage"

def main():
    config=ConfigurationManager()
    data_ingestion_config=config.get_data_ingestion_config()
    data_ingestion=DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()





if __name__=="__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} has started <<<<<<<")
        main()
        logger.info(f">>>>>>> {STAGE_NAME} has ended <<<<<<<")
    except Exception as e:
        raise e