import os
from zipfile import ZipFile
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from deepClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path
import requests


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL, stream=True)
            with open(self.config.local_data_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=512):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            logger.info(f"{self.config.local_data_file} downloaded!")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):

        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logger.info(f"unzipping file and removing unawanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)