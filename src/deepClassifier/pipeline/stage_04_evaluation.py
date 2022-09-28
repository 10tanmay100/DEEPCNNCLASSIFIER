from deepClassifier.config import ConfigurationManager
from deepClassifier.components import *
from deepClassifier import logger

STAGE_NAME="Evaluation"

def main():
    config = ConfigurationManager()
    evaluation_config = config.get_evaluation_config()
    eval=Evaluation(evaluation_config)
    eval.evaluation()
    eval.save_score()

if __name__ == '__main__':
    
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e