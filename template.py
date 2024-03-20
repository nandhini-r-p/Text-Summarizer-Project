import os
from pathlib import Path # to handle slash issues related to path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep/", # hidden file that will be deleted later
    f"src/{project_name}/__init__.py", # to import components from local packages
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py", # used to do setups of folder structures
    "research/trails.ipynb"
]

for filepath in list_of_files:
    # detects OS and then gives the path of file
    filepath = Path(filepath)

    # 1st we need to create folders and then inside them
    # the actual files will be created
    # Hence, we are splitting the folder & file path
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            # just create the file and don't perform any ops,
            # that's why just pass
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")