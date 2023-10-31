# Configuration file for the Sphinx documentation builder.



# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'BraineryWiz'
copyright = '2023, Bijan Sayyafzaden - Silvia Mazzoni'
author = 'Bijan Sayyafzaden - Silvia Mazzoni'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

## Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.coverage",
    "sphinx.ext.githubpages",
    "numpydoc.numpydoc",
    # "sphinxext_altair.altairplot",
    # "sphinxext.altairgallery",
    # "sphinxext.schematable",
    # "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_static_path = ['_static']


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navigation_with_keys':False,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "primary_sidebar_end": [],
    "footer_items": [],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Silvia-s-Brainery/BraineryWiz",
            "icon": "fab fa-github fa-lg",
            "type": "fontawesome",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/brainerywiz",
            "icon": "fab fa-linkedin fa-xl",
            "type": "fontawesome",
        },
        {
            "name": "MainPage",
            "url": "https://www.silviasbrainery.com/brainerywiz",
            "icon": "_static/BraineryWizico.ico",
            "type": "local",
        },
    ],
    "header_links_before_dropdown": 6,
    "announcement": """The latest Released version: 0.91 - Email Address: <a href = 'mailto: BraineryWiz@Gmail.com'>BraineryWiz@Gmail.com</a>.""",
}
   

html_context = {"default_mode": "light"}
html_short_title = "BraineryWiz"
html_logo = "_static/BraineryWizLogo.png"
html_favicon="_static/BraineryWizico.ico"
