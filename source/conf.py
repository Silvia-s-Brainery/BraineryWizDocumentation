# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BraineryWiz'
copyright = '2023, Bijan Sayyafzaden - Silvia Mazzoni'
author = 'Bijan Sayyafzaden - Silvia Mazzoni'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_static_path = ['_static']

html_theme_options={
    'navigation_with_keys':False
    }
    

html_context = {"default_mode": "light"}
html_short_title = "BraineryWiz"
html_logo = "_static/BraineryWizLogo.png"
