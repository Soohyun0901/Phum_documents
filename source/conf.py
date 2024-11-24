# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'doc'
copyright = '2024, The Phum'
author = 'The Phum'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

#templates_path = ['_templates']
#exclude_patterns = []   

language = 'ko'

# -- Options for HTML output -------------------------------------------------


html_theme = 'sphinx_book_theme'


# 다음코드 추가
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}
extensions = ['recommonmark']
extensions = [
    'sphinx.ext.duration',
]

html_favicon='favicon.ico'
#html_extra_path = ['source/img']