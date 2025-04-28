from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name = "wine_quality_ml_project"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb" "templates/index.html",
]


for list_of_file in list_of_files:
    file_path=Path(list_of_file)
    
    file_dir,file_name=os.path.split(file_path)
    
    
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for the file: {file_name}")
        
        
    if (not os.path.exists(list_of_file) or os.path.getsize(list_of_file) == 0):
        with open(list_of_file,"w") as f:
            pass
            logging.info(f"Creating empty file: {list_of_file}")
    else:
        logging.info(f"File already exists: {list_of_file}")