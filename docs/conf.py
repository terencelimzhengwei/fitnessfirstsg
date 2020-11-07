"""Sphinx configuration."""
from datetime import datetime


project = "Unofficial API client for Fitness First SG"
author = "Terence Lim"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
