import os
from box.exceptions import BoxValueError
import yaml
from TextSummary.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns
    Args: path_to_yaml (Path): path to yaml file
    Returns: ConfigBox: config box

    Raises: BoxValueError: if yaml file is empty
    e: empty file
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Args:
    path_to_directories (list): list of directories
    verbose (bool, optional): ingore if multiple directories are created. Defaults to True.
    """    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in kB

    Args:
    path (Path): path to file

    Returns: str: size in kB            

    """
    size_in_kB = round(os.path.getsize(path) / 1024)
    return f"{str(size_in_kB)} in kB"