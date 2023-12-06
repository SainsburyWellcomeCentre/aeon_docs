# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys
from datetime import date

sys.path.extend(
    [
        os.path.abspath("../aeon_mecha/"),
        os.path.abspath("../aeon_analysis/aeon_analysis"),
        os.path.abspath("../aeon_acquisition"),
        os.path.abspath("../aeon_experiments"),
    ]
)


# -- Project information -----------------------------------------------------

project = "aeon_docs"
copyright = f"2022–{date.today().year}, Jai Bhagat, Goncalo Lopes, Chang Huan Lo"
author = "Jai Bhagat, Goncalo Lopes, Chang Huan Lo"
organisation = "Sainsbury Wellcome Centre"


def get_current_release_tag():
    return (
        subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
        .strip()
        .decode("utf-8")
    )


# The full version, including alpha/beta/rc tags
release = get_current_release_tag()
# release = "0.1.0"

# GitHub repo URL
github_url = f"https://github.com/{organisation.replace(' ', '')}/{project}"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "myst_parser",
    "sphinx_design",
]

# Configure the myst parser to enable cool markdown features
# See https://sphinx-design.readthedocs.io
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "deflist",
]

# Automatically add anchors to markdown headings
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

autosummary_generate = True
autodoc_default_flags = ["members", "inherited-members"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_templates"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "announcement": f"{project} is a WIP. Please report any issues on <a href='{github_url}/issues'>GitHub</a>.",
    "logo": {
        "text": f"{project} {release}"
        # "image_light": "_static/logo-light.png",
        # "image_dark": "_static/logo-dark.png",
    },
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": github_url,
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
    ],
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]
