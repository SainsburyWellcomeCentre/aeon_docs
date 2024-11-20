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
        os.path.abspath("../aeon_acquisition"),
        os.path.abspath("../aeon_experiments"),
    ]
)


# -- Project information -----------------------------------------------------

project = "Aeon"
author = "Jai Bhagat, Goncalo Lopes, Chang Huan Lo"
copyright = f"2022–{date.today().year}, {author}"
organisation = "Sainsbury Wellcome Centre"


def get_current_release_tag():
    try:
        # Get the current release tag from git
        return (
            subprocess.check_output(["git", "describe", "--tags", "--abbrev=0"])
            .strip()
            .decode("utf-8")
        )
    except subprocess.CalledProcessError:
        # If this fails, just return a default
        return ""


# The full version, including alpha/beta/rc tags
release = get_current_release_tag()

# GitHub repo URL
github_url = f"https://github.com/{organisation.replace(' ', '')}/aeon_docs"

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
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
]

# Configure the myst parser to enable cool markdown features
# See https://sphinx-design.readthedocs.io
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "deflist",
    "attrs_inline",
]

# Automatically add anchors to markdown headings
myst_heading_anchors = 3

# Set the Markdown format to myst
myst_render_markdown_format = "myst"

# Disable notebook execution
nb_execution_mode = "off"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "show-inheritance": True,
    "undoc-members": True,
}

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
    "announcement": (
        f"This website is currently under active development. "
        f"Please report any issues on <a href='{github_url}/issues'>GitHub</a>."
    ),
    "logo": {
        "text": f"{project} {release}"
        # "image_light": "images/logo-light.png",
        # "image_dark": "images/logo-dark.png",
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
    "show_toc_level": 3,  # Show the first 3 levels of the local TOC
    "footer_start": ["footer_start"],
    "footer_end": ["footer_end"],
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "css/custom.css",
]
html_js_files = [
    'js/workflow.js', # javascript for embedded workflows
]

# linkcheck will skip checking these URLs entirely
linkcheck_ignore = [
    r"https://wiki\.ucl\.ac\.uk/.*",  # This is the UCL internal wiki
    r"http://SubjectExpressionBuilder.Name",  # Broken URL
]

# linkcheck will treat redirections from these source URI:canonical URI
# mappings as "working".
linkcheck_allowed_redirects = {
    r"https://doi\.org/10\.5281/zenodo\..*": r"https://zenodo\.org/records/.*",
    r"https://zenodo\.org/doi/.*": r"https://zenodo\.org/records/.*",
    r"https://learn.microsoft.com/dotnet/api/.*": r"https://learn.microsoft.com/en-us/dotnet/api/.*",
}

myst_url_schemes = {
    "http": None,
    "https": None,
    "ftp": None,
    "mailto": None,
    "aeon-mecha-github": "https://github.com/SainsburyWellcomeCentre/aeon_mecha/{{path}}",
    "aeon-acquisition-github": "https://github.com/SainsburyWellcomeCentre/aeon_acquisition/{{path}}",
    "aeon-experiments-github": "https://github.com/SainsburyWellcomeCentre/aeon_experiments/{{path}}",
    "aeon-lineardrive-github": "https://github.com/SainsburyWellcomeCentre/aeon_lineardrive/{{path}}",
    "aeon-feeder-github": "https://github.com/SainsburyWellcomeCentre/aeon_feeder/{{path}}",
    "semver": "https://semver.org/",
    "harp-tech": "https://harp-tech.org/{{path}}#{{fragment}}",
    "python-pep": "https://peps.python.org/pep-{{path}}",
    "niu-howto": "https://howto.neuroinformatics.dev/programming/SSH-SWC-cluster#{{fragment}}",
}
