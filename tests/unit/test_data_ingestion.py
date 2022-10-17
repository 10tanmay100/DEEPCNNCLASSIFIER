import pytest
from deepClassifier.components import DataIngestion
from deepClassifier.entity import DataIngestionConfig
import os
import glob


class Test_data_ingestion_dwld_unzip:
    data_ingestion_config=DataIngestionConfig(
        root_dir='E:/Ineuron/Project/Deep Learning Project2/DEEPCNNCLASSIFIER/tests/data/',
        source_URL='https://raw.githubusercontent.com/c17hawke/raw_data/main/sample_data.zip',
        local_data_file='E:/Ineuron/Project/Deep Learning Project2/DEEPCNNCLASSIFIER/tests/data/sample_data/data.zip',
        unzip_dir='E:/Ineuron/Project/Deep Learning Project2/DEEPCNNCLASSIFIER/tests/data/'
    )
    def test_dwld(self):
        data_ingestion=DataIngestion(config=self.data_ingestion_config)
        data_ingestion.download_file()
        if len(glob.glob(self.data_ingestion_config.local_data_file))>0:
            assert True
        else:
            assert False
    def test_unzip(self):
        data_ingestion=DataIngestion(config=self.data_ingestion_config)
        data_ingestion.unzip_and_clean()
        if glob.glob(self.data_ingestion_config.unzip_dir)[0]=='PetImages':
            assert True
        else:
            False
