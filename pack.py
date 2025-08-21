import os
import re
from stlitepack import pack, setup_github_pages
from stlitepack.pack import get_stlite_versions

get_stlite_versions()

def list_files_in_folders(folders, recursive=False, pattern=None):
    """
    Given a list of folder paths, return a list of all files inside them
    with their relative paths (including the folder name).

    Parameters
    ----------
    folders : list of str
        List of folder paths to search in.
    recursive : bool, default=False
        If True, include files in subfolders recursively.
    pattern : str, optional
        A regex pattern to filter file paths. If None, all files are included.
    """
    all_files = []
    regex = re.compile(pattern) if pattern else None

    for folder in folders:
        folder = os.path.abspath(folder)  # normalize path
        if recursive:
            # Walk through all subfolders
            for root, _, files in os.walk(folder):
                for file in files:
                    rel_path = os.path.relpath(os.path.join(root, file), start=os.path.dirname(folder))
                    rel_path = rel_path.replace(os.sep, "/")
                    if regex is None or regex.search(rel_path):
                        all_files.append(rel_path)
        else:
            # Just immediate files
            for file in os.listdir(folder):
                full_path = os.path.join(folder, file)
                if os.path.isfile(full_path):
                    rel_path = os.path.relpath(full_path, start=os.path.dirname(folder))
                    rel_path = rel_path.replace(os.sep, "/")
                    if regex is None or regex.search(rel_path):
                        all_files.append(rel_path)

    return all_files

data_files = list_files_in_folders(["input_data_f", "input_data_ind", "input_data_m", "input_data_other"], pattern="csv")

data_files.extend([".streamlit/config.toml",
                   "indicators_n_pop_data_25_26.py"
                #    , "pages/longer_equation.png", "pages/single_equation.png",
                #    "pages/video_tutorial.mp4", "pages/where.png"
                   ])

# data_files = [{filepath: f"https://raw.githubusercontent.com/pete4nhs/eFIT-tool/refs/heads/main/{filepath}"} for filepath in data_files]


print(data_files)

pack(
    "efit_tool.py",
    requirements=["plotly"],
    extra_files=data_files
    )

setup_github_pages(mode="gh-actions")
