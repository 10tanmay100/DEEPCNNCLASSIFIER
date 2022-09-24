import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

#functional approach
class Test_read_yaml:


    yaml_files=[
        'tests/data/empty.yaml',
        'tests/data/demo.yaml'
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[0]))

    def test_read_yaml_return_type(self):
        response=read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(response,ConfigBox)
# Here we try to apply the test case on both the yaml files so we have passed here the deorator by which all files in that will be stored in path_to_yaml and will check iteratively
    @pytest.mark.parametrize("path_to_yaml",yaml_files)
    def test_read_yaml_bad_datatype(self,path_to_yaml):
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)





