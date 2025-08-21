from stlitepack import pack, setup_github_pages
from stlitepack.pack import get_stlite_versions, list_files_in_folders

# get_stlite_versions()

data_files = list_files_in_folders(
    ["input_data_f", "input_data_ind", "input_data_m", "input_data_other"]
    )

data_files.extend([
    "pages/longer_equation.png",
    "pages/single_equation.png",
    "pages/video_tutorial.mp4",
    "pages/where.png"
    ])

print(data_files)

pack(
    "efit_tool.py",
    requirements=["plotly"],
    extra_files_to_embed=[
        ".streamlit/config.toml",
        "indicators_n_pop_data_25_26.py"
        ],
    extra_files_to_link=data_files,
    prepend_github_path="pete4nhs/eFIT-tool",
    use_raw_api=True
    )

setup_github_pages(mode="gh-actions")
