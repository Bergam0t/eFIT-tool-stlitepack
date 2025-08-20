from stlitepack import pack, setup_github_pages

pack(
    "efit_tool.py",
    requirements=["plotly"]
    )

setup_github_pages(mode="gh-actions")
