# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Vertillusion'
copyright = '2019 - 2023, Vertillusion Studio - Meet, Inspire, Create.'
author = 'Vertillusion Studio'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark','sphinx_markdown_tables']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_copy_source = False
html_context = {
    'display_github': True,
    'github_user': 'KaguraiYoRoy',
    'github_repo': 'docs.vertillusion.xyz',
    'github_version': 'source/'
}

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

source_suffix = {'.rst': 'restructuredtext','.md': 'markdown'}