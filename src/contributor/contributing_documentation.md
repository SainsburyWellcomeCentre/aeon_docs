(target-contributing-documentation)=
# Contributing Documentation
The documentation is built via [Sphinx](https://www.sphinx-doc.org/en/master/), 
and hosted at [aeon.swc.ucl.ac.uk](aeon-docs:). 
`src/` is the Sphinx source directory, where you can find the Markdown (`.md`) and RestructuredText (`.rst`) files that make up the documentation. 
The site is built and deployed from the `gh-pages` branch. 
This is handled by a GitHub actions workflow (`.github/workflows/docs_build_and_deploy.yml`), triggered by the following events:
- **Push to the main branch**
- **Tag push**
- **Pull request**
- **Manual dispatch** via the "Run workflow" button in the Actions tab.

The workflow comprises two jobs: `build_sphinx_docs` and `deploy_sphinx_docs`. 
The build job is triggered by all the listed events to ensure the documentation build remains intact with new changes. 
The deployment job is only triggered on manual dispatch or [when a tag is pushed](#deploying-the-documentation).

## Editing the documentation
To edit the documentation, clone the [`aeon_docs` repository](aeon-docs-github:), and work on a new branch, following the same guidelines as for [code changes](target-contributing-code). 
We recommend [building the documentation locally](#building-the-documentation-locally) to check that the changes are rendered correctly before pushing them to the repository.

### Adding a new page
If you are adding a new documentation source file (e.g. `new_file.md` or `new_file.rst`), 
you will need to place the file in the appropriate directory within `src/`. 
In each directory, you will find a parent file (typically an `index.md` or `index.rst` file) that serves as the main page for the subpages in that directory.
For the new file to be included in the documentation, you will need to add an entry for the new file in the [`toctree` directive](myst-parser:syntax/organising_content.html#using-toctree-to-include-other-documents-as-children) in the parent file.
Depending on the file format of the parent file (`.md`or `.rst`), the `toctree` directive syntax will differ.

::::{tab-set}
:::{tab-item} Markdown
For example, to add `new_file.md` or `new_file.rst` as a subpage of the [Contributor Guide](aeon-docs:contributor), place the new file in `src/contributor/`. 
As the parent file is `src/contributor/index.md`, add `new_file` to the `toctree` in the parent file as follows:
```markdown
:::{toctree}
:maxdepth: 1
:hidden:

new_file
```
This new page will then be included as a subpage of [Contributor Guide](aeon-docs:contributor).
:::

:::{tab-item} RestructuredText
If the parent file is a `.rst` file, add `new_file` to the `toctree` in the parent file as follows:
```rst
.. toctree::
   :maxdepth: 1
   :hidden:

   new_file
```
This new page will then be included as a subpage of the parent page.
:::
::::

### Adding Bonsai workflow code
Bonsai workflows can be inserted using a custom `workflow` container that displays the workflow image and allows the workflow code to be copied. 
The `.bonsai` workflow file and its corresponding `.svg` file should be placed in the `src/workflows/` directory.
In order for the workflow to be displayed correctly, the `.bonsai` file and its corresponding `.svg` file must have the same name, e.g. `alertLogs.bonsai` and `alertLogs.svg`.

:::::{tab-set}
::::{tab-item} Markdown
```markdown
:::workflow
![Alt text](src/workflows/alertLogs.bonsai)
:::
```
::::

::::{tab-item} RestructuredText
```rst
.. container:: workflow

    .. image:: src/workflows/alertLogs.bonsai
        :alt: Alt text
```
::::
:::::

### Cross-referencing pages
#### Internal references
For ease of referencing, we use [explicit targets](myst-parser:syntax/cross-referencing.html#creating-explicit-targets) to refer to specific pages and sections within the documentation. 
::::{tab-set}
:::{tab-item} Markdown
To create an explicit target in a `.md` file, use the `(target-name)=` syntax and add the target name before the page/section header, e.g.:
```markdown
(target-hardware)=
# Hardware Overview
```
To reference the [](target-hardware) section, use the `[](target-name)` syntax:
```markdown
[](target-hardware)
```
The link text will be displayed as the title of the referenced section.

To display a custom link text (e.g. [custom text](target-hardware)), use the `[link text](target-name)` syntax:
```markdown
[custom text](target-hardware)
```
:::

:::{tab-item} RestructuredText
To create an explicit target in a `.rst` file, use the `.. _target-name:` syntax and add the target name before the page/section header, e.g.:
```rst
.. _target-hardware:

Hardware Overview
=================
```
To reference the [](target-hardware) section, use the `` :ref:`target-name` `` syntax, e.g.:
```rst
:ref:`target-hardware`
```
The link text will be displayed as the title of the referenced section.

To display a custom link text (e.g. [custom text](target-hardware)), use the `` :ref:`link text<target-name>` `` syntax, e.g.:
```rst
:ref:custom text<target-hardware>`
```
:::
::::

#### External references
If you are adding references to an external URL (e.g. `https://github.com/SainsburyWellcomeCentre/aeon_docs/issues`) in a `.md` file, you will need to check if a matching URL scheme (e.g. `https://github.com/SainsburyWellcomeCentre/aeon_docs/`) is defined in `myst_url_schemes` in `src/conf.py`. If it is, the following `[](scheme:loc)` syntax will be converted to the [full URL](aeon-docs-github:issues/1) during the build process:
```markdown
[link text](aeon-docs-github:issues/1)
```

If it is not yet defined and you have multiple external URLs pointing to the same base URL, you will need to [add the URL scheme](myst-parser:syntax/cross-referencing.html#customising-external-url-resolution) to `myst_url_schemes` in `src/conf.py`.

### Updating the API reference
The [API reference](target-api-reference) is auto-generated as part of the documentation build process.

#### `aeon_api`
For the `aeon_api` Python package, the `make_api_doctree.py` script generates the `src/reference/api/aeon_api.rst` file containing the list of modules to be included in the [API reference](target-aeon-api-reference). 
The [sphinx-autodoc](sphinx-doc:extensions/autodoc.html) and [sphinx-autosummary](sphinx-doc:extensions/autosummary.html) extensions are then used to generate the API reference pages for each module listed in `aeon_api.rst`, based on the docstrings in the source code. 
By default, all modules are documented. If you wish to exclude a module from the API reference, you can add it to the `ignore_modules` list in the `make_api_doctree.py` script.

#### `aeon_acquisition` 
For the `aeon_acquisition` Bonsai package, the `make_acquisition_doctree.py` script first calls [`docfx`](https://dotnet.github.io/docfx/index.html) to generate the API reference pages for each module as Markdown files in `src/reference/api/acquisition/`, and the table of contents (TOC) in the `src/reference/api/acquisition/toc.yml` file. 
This TOC is then used to generate the `src/reference/api/acquisition.rst` file containing the list of modules to be included in the [API reference](target-aeon-acquisition-reference).

## Building the documentation locally
To build the documentation locally, first make sure you have cloned the [`aeon_docs` repository](aeon-docs-github:). 
The following commands should be run from the root directory of the repository.

:::{note}
Windows PowerShell users should prepend `make` commands with `.\` (e.g. `.\make html`).
:::

Create a `conda` environment with the required dependencies and activate it:
```bash
conda create -n aeon_docs python dotnet -c conda-forge
conda activate aeon_docs
```

Make the `docfx` tool available in the environment:
```bash
dotnet tool restore
```

From the root of the repository, install the requirements for building the documentation:
```bash
pip install -r requirements.txt
``` 

Then, populate submodules:
```bash
git submodule init
git submodule update
``` 

(Optional) Update submodules and point to the latest commits:
```bash
git submodule sync
git submodule update --remote
```

Finally, build the documentation:
```bash
make html
```
You can view the local build by opening `docs/html/index.html` in a browser.

To apply new changes to the documentation, remove all automatically generated files and folders, and rebuild:
```bash
make clean && make html
```

To check that external URLs are correctly resolved, run:
```bash
make linkcheck
```

If the linkcheck step incorrectly marks URLs with valid anchors as broken, 
you can skip checking the anchors in specific URLs by adding them to 
`linkcheck_anchors_ignore_for_url` in `src/conf.py`, e.g.: 
```python
# linkcheck will skip verifying that anchors exist when checking
# these URLs
linkcheck_anchors_ignore_for_url = [
    "https://example.com",
]
```

To skip linkcheck for specific URLs, add them to
`linkcheck_ignore` in `src/conf.py`, e.g.:
```python
# linkcheck will skip checking these URLs entirely
linkcheck_ignore = [
    "https://github.com/org/private_repository",
]
```

To suppress warnings for expected redirects, add them to 
`linkcheck_allowed_redirects` in `src/conf.py`, e.g.:
```python
# linkcheck will treat redirections from these source URI:canonical URI
# mappings as "working".
linkcheck_allowed_redirects = {
    r"https://zenodo\.org/doi/.*": r"https://zenodo\.org/records/.*",
}
```

## Deploying the documentation
As mentioned above, the deployment job is triggered by the following events:
- **Tag push**: for releasing a new version of the documentation
- **Manual dispatch**: for testing purposes

### Manual dispatch
To deploy the documentation manually on GitHub, go to the Actions tab of the repository, 
select the `Docs` workflow, and click "Run workflow".

### Tag push
To deploy the documentation with a new tag, follow these steps:

Fetch all tags:
```bash	
git fetch --tags
```

Identify the latest tag:
```bash
git describe --tags
```

Create a new tag by incrementing the [version](target-contributor-versioning) number:
```bash
git tag <tag_name>
```

Push the tag to the remote repository:
```bash
git push origin <tag_name>
```