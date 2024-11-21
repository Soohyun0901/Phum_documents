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

templates_path = ['_templates']
exclude_patterns = []   

language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'readable'
#html_theme_path = ['C:\doc_wiki']
#html_static_path = ['_static']
#import sphinx_readable_theme
#html_theme = 'readable'
#html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_theme = 'sphinx_book_theme'

#import os   # 기존주석 해제
#import sys  # 기존주석 해제
#sys.path.insert(0, os.path.abspath('.')) # 기존주석 해제

# 다음코드 추가
from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}
extensions = ['recommonmark']

html_favicon='favicon.ico'
#html_extra_path = ['source/img']