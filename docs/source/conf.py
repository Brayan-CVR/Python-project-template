# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

#Agregamos la ruta de la carpeta utils
sys.path.insert(0, os.path.abspath('../../src/'))  # Ajusta la ruta según tu estructura

project = 'Python-project-template'
copyright = '2025, Brayan Camilo Valenzuela Rincon'
author = 'Brayan Camilo Valenzuela Rincon'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser',
              'sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


# Si usas Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}