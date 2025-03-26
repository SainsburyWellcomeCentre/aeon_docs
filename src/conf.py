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
        os.path.abspath("."),
        os.path.abspath("../aeon_mecha/"),
        os.path.abspath("../aeon_api/"),
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
    "sphinx.ext.graphviz",
    "sphinx_autodoc_typehints",
    "myst_nb",
    "sphinx_design",
    "sphinx_copybutton",
    "convertworkflow",
    "breathe",
    "sphinx_csharp",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_templates"]

# Suppress warnings for non-consecutive header level
suppress_warnings = ["myst.header"]

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
    "js/workflow.js",  # javascript for embedded workflows
]

# linkcheck will skip checking these URLs entirely
linkcheck_ignore = [
    r"https://wiki\.ucl\.ac\.uk/.*",  # This is the UCL internal wiki
    r"http://SubjectExpressionBuilder.Name",  # Broken URL
    r"https://learn.microsoft.com/dotnet/api/.*",  # 429 Client Error: Too Many Requests for url
]

# linkcheck will treat redirections from these source URI:canonical URI
# mappings as "working".
linkcheck_allowed_redirects = {
    r"https://doi\.org/10\.5281/zenodo\..*": r"https://zenodo\.org/records/.*",
    r"https://zenodo\.org/doi/.*": r"https://zenodo\.org/records/.*",
}

# -- Extensions configuration ---------------------------------------------------

# Configure Breathe
breathe_projects = {
    "aeon_acquisition_xml": "xml",
}
breathe_default_project = "aeon_acquisition_xml"
breathe_show_define_initializer = True
breathe_show_enumvalue_initializer = True
# breathe_default_members = ("members", "undoc-members", "protected-members")

# Configure C# domain
sphinx_csharp_multi_language = True
sphinx_csharp_test_links = False  # This will be handled by linkcheck
sphinx_csharp_ext_search_pages = {
    "bonsai": ("https://bonsai-rx.org/docs/api/%s",),
    "bonsai-sleap": ("https://bonsai-rx.org/sleap/api/Bonsai.Sleap.%s",),
    "harp": ("https://harp-tech.org/api/%s",),
    "mathdotnet": ("https://numerics.mathdotnet.com/api/%s.htm",),
    "msdn": ("https://learn.microsoft.com/en-us/dotnet/api/%s",),
    "mysqlconnector": ("https://mysqlconnector.net/api/%s",),
    "opencv.net": ("https://horizongir.github.io/opencv.net/api/%s",),
    "reactive": ("https://horizongir.github.io/reactive/api/%s",),
}
sphinx_csharp_ext_type_map = {
    "bonsai": {
        "Bonsai": ["Combinator", "INamedElement", "Source"],
        "Bonsai.Audio": ["AudioCapture"],
        "Bonsai.Design": ["DialogTypeVisualizer"],
        "Bonsai.Expressions": [
            "FormatBuilder",
            "SingleArgumentExpressionBuilder",
            "SubjectBuilder",
            "TypeMapping",
            "UnitBuilder",
        ],
        "Bonsai.Vision": ["ConnectedComponent", "ConnectedComponentCollection"],
    },
    "bonsai-sleap": {
        "": ["Pose", "PoseCollection", "PoseIdentity", "PoseIdentityCollection"],
    },
    "harp": {
        "Bonsai.Harp": ["HarpMessage", "Timestamped"],
    },
    "mathdotnet": {
        "MathNet.Numerics": ["IInterpolation"],
    },
    "msdn": {
        "System": [
            "Attribute",
            "DateTime",
            "Exception",
            "IObservable",
            "IObserver",
            "IServiceProvider",
            "TimeSpan",
            "Type",
        ],
        "System.Collections": ["IEnumerator"],
        "System.Collections.Generic": ["IDictionary", "List"],
        "System.Collections.ObjectModel": ["KeyedCollection"],
        "System.ComponentModel": [
            "CustomTypeDescriptor",
            "ExpandableObjectConverter",
            "IComponent",
            "IContainer",
            "ICustomTypeDescriptor",
            "ISite",
            "ITypeDescriptorContext",
            "PropertyDescriptor",
            "PropertyDescriptorCollection",
            "StringConverter",
            "TypeDescriptionProvider",
        ],
        "System.ComponentModel.TypeConverter": ["StandardValuesCollection"],
        "System.Globalization": ["CultureInfo"],
        "System.Linq.Expressions": ["Expression"],
        "System.Windows.Forms": ["UserControl"],
    },
    "mysqlconnector": {
        "": ["MySqlConnection", "MySqlDataReader"],
    },
    "opencv.net": {
        "OpenCV.Net": ["IplImage", "Mat", "Point", "Point2f"],
    },
    "reactive": {
        "System.Reactive": ["Unit"],
        "System.Reactive.Subjects": ["ISubject"],
    },
}
sphinx_csharp_external_type_rename = {
    "IInterpolation": "Interpolation/IInterpolation",
    "IDictionary": "IDictionary-2",
    "IObservable": "IObservable-1",
    "IObserver": "IObserver-1",
    "ISubject": "ISubject-1",
    "KeyedCollection": "KeyedCollection-2",
    "List": "List-1",
    "MySqlConnection": "mysqlconnector/mysqlconnectiontype",
    "MySqlDataReader": "mysqlconnector/mysqldatareadertype",
    "Source": "Source-1",
}
# Do not create cross references for these standard/build-in/undocumented types
sphinx_csharp_ignore_xref = [
    "Bonsai.Pylon.PylonCapture",
    "Bonsai.Spinnaker.SpinnakerCapture",
    "IGroupedObservable",
    "IManagedCamera",
    "IRepository",
    "T",
    "TMetadata",
    "TRecord",
    "TSource",
    "TState",
]

# Configure myst parser to enable cool markdown features
# See https://sphinx-design.readthedocs.io
myst_enable_extensions = [
    "colon_fence",
    "linkify",
    "deflist",
    "attrs_inline",
]
# Automatically add anchors to markdown headings
myst_heading_anchors = 3
myst_render_markdown_format = "myst"
myst_url_schemes = {
    "http": None,
    "https": None,
    "ftp": None,
    "mailto": None,
    "aeon-docs": "https://sainsburywellcomecentre.github.io/aeon_docs/{{path}}",
    "aeon-docs-github": "https://github.com/SainsburyWellcomeCentre/aeon_docs/{{path}}",
    "aeon-mecha-github": "https://github.com/SainsburyWellcomeCentre/aeon_mecha/{{path}}",
    "aeon-acquisition-github": "https://github.com/SainsburyWellcomeCentre/aeon_acquisition/{{path}}",
    "aeon-experiments-github": "https://github.com/SainsburyWellcomeCentre/aeon_experiments/{{path}}",
    "aeon-lineardrive-github": "https://github.com/SainsburyWellcomeCentre/aeon_lineardrive/{{path}}",
    "aeon-feeder-github": "https://github.com/SainsburyWellcomeCentre/aeon_feeder/{{path}}",
    "aeon-api-github": "https://github.com/SainsburyWellcomeCentre/aeon_api/{{path}}",
    "datajoint": "https://datajoint.com/{{path}}",
    "sample-data-single-mouse-foraging": "https://doi.org/10.5281/zenodo.13881884",
    "myst-parser": "https://myst-parser.readthedocs.io/en/latest/{{path}}#{{fragment}}",
    "semver": "https://semver.org/",
    "sleap": "https://sleap.ai/{{path}}#{{fragment}}",
    "harp-tech": "https://harp-tech.org/{{path}}#{{fragment}}",
    "python-pep": "https://peps.python.org/pep-{{path}}",
    "sphinx-doc": "https://www.sphinx-doc.org/en/master/usage/{{path}}#{{fragment}}",
    "niu-howto": "https://howto.neuroinformatics.dev/programming/SSH-SWC-cluster#{{fragment}}",
}

# Disable notebook execution
nb_execution_mode = "off"

# Configure autosummary and autodoc
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "show-inheritance": True,
    "undoc-members": True,
}
