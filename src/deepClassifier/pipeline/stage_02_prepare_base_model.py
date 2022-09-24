from deepClassifier.components import PrepareBaseModel
from deepClassifier.config import ConfigurationManager
from deepClassifier import logger



STAGE_NAME="Base model preparation Stage"

def main():
    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()



if __name__=="__main__":
    try:
        logger.info(f">>>>>>> {STAGE_NAME} has started <<<<<<<")
        main()
        logger.info(f">>>>>>> {STAGE_NAME} has ended <<<<<<<")
    except Exception as e:
        raise e