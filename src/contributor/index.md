(target-contributor-guide)=
# Contributor Guide

## Software Development Life Cycle (SDLC)

Our SDLC roughly follows the [iterative model](https://www.tutorialspoint.com/sdlc/sdlc_iterative_model.htm).

## Versioning

We version all the following, according to [SemVer](semver:) numbering: 

- Experiments, by name, including full hardware specs (arena, I/O devices, 
  acquisition computer, etc.)
- Repositories, including code related to:
  - Bonsai experiment workflows
  - Quality Control protocols (for raw and preprocessed data)
  - Data processing algorithms
- aeon-db Database
  - aeon-db tables

## Issue tracking

We prioritize and track dev progress using Github Discussions and Github Issues in Github Projects. Issues and Discussions should ideally be created in the specific repository appropriate for the Issue/Discussion; all experiment and general Issues and Discussions should be created in 'aeon_experiments'.

## Continuous integration (CI)

We use Github Actions to run CI. We run unit tests on Github Virtual Machines on Windows, MacOS, and Ubuntu. We run integration tests on the SWC HPC. Workflows of the CI jobs we run can be found in each repo's respective `.github/workflows/` directory.

## Contributing code
Each repository roughly follows the [github flow](https://docs.github.com/en/get-started/using-github/github-flow) (which is adapted from the more general 
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)). 

In brief, each of our repos has 'main' and 'prod' branches. Feature and bug fix branches are branched off of 'main', with Pull Requests sent back into 'main'. 'main' contains the full commit history of the project, up to the latest stable commit. Upon merges into 'main', a squash merge is performed into 'prod', such that 'prod' contains an abbreviated commit history of the project, with commits pertaining only to Pull Request merges. 'prod' thus serves as a "production" branch to allow for easier readability of project history and easier reversion of uncaught bug commits. At certain agreed upon timepoints we create "stable releases" (available in the "releases" section of the repository) which serve as a snapshot of the code at the time, version numbered according to [SemVer](semver:).

When contributing to any repository, the change to be made should first be discussed in a Github Discussion or a Github Issue. Thereafter, contributors should create a new branch (branched off of 'main') that contains the changes/additions they wish to make, and then create a pull request for merging this branch into 'main'.

All pull requests will be reviewed by the [project maintainers](target-project-maintainers). Minimally, maintainers should follow the below steps when reviewing pull requests:

1) Ensure new code adheres to the [style and documentation guidelines](target-style-doc-guidelines), is covered by a test, and passes a build test. These can all be checked via CI.

2) As necessary, ensure `changelog`, `readme`, config and doc files are updated.

3) When a branch is ready to be merged back into 'main', always make sure to first pull 'main' locally, then rebase the feature branch onto 'main' (cleaning up any merge conflicts as necessary), before merging the PR. The squash merge into 'prod' can be handled via CI. E.g., see [here](aeon-mecha-github:blob/main/.github/workflows/squash_merge_to_prod.yml)

## Contributing documentation
The documentation is built via [Sphinx](https://www.sphinx-doc.org/en/master/), 
and hosted via GitHub Pages at [sainsburywellcomecentre.github.io/aeon_docs/](aeon-docs:). 
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

### Editing the documentation
To edit the documentation, clone the [`aeon_docs` repository](aeon-docs-github:), and work on a new branch, following the same guidelines as for [code changes](#contributing-code). Make sure that the header levels in the `.md` or `.rst` files are incremented consistently (H1 > H2 > H3, etc.) without skipping any levels.

#### Adding a new page
If you are adding a new documentation source file (e.g. `new_file.md` or `new_file.rst`), 
you will need to add it to the [`toctree` directive](myst-parser:syntax/organising_content.html#using-toctree-to-include-other-documents-as-children) 
in the parent file (i.e. the page that will contain the link to the new page) 
for it to be included in the documentation website.
Depending on the file format of the parent file (`.md`or `.rst`), the `toctree` directive syntax will differ.

::::{tab-set}
:::{tab-item} Markdown
For example, to add `new_file.md` or `new_file.rst` under [Contributor Guide](aeon-docs:contributor), 
you would add `new_file` to the `toctree` in `src/contributor/index.md` as follows:
```markdown
:::{toctree}
:maxdepth: 1
:hidden:

new_file
```
This new page will then be included as a section under [Contributor Guide](aeon-docs:contributor).
:::

:::{tab-item} RestructuredText
If the parent file is a `.rst` file, you would add `new_file` to the `toctree` in the parent file as follows:
```rst
.. toctree::
   :maxdepth: 1
   :hidden:

   new_file
```
This new page will then be included as a section under the parent page.
:::
::::

#### Cross-referencing pages
##### Internal references
For ease of referencing, we use [explicit targets](myst-parser:syntax/cross-referencing#creating-explicit-targets) to refer to specific pages and sections within the documentation. 
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

##### External references
If you are adding references to an external URL (e.g. `https://github.com/SainsburyWellcomeCentre/aeon_docs/issues`) in a `.md` file, you will need to check if a matching URL scheme (e.g. `https://github.com/SainsburyWellcomeCentre/aeon_docs/`) is defined in `myst_url_schemes` in `src/conf.py`. If it is, the following `[](scheme:loc)` syntax will be converted to the [full URL](aeon-docs-github:issues/1) during the build process:
```markdown
[link text](aeon-docs-github:issues/1)
```

If it is not yet defined and you have multiple external URLs pointing to the same base URL, you will need to [add the URL scheme](myst-parser:syntax/cross-referencing#customising-external-url-resolution) to `myst_url_schemes` in `src/conf.py`.

#### Updating the API reference
...

### Building the documentation locally
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

### Deploying the documentation
As mentioned above, the deployment job is triggered whenever a tag is pushed to the main branch. To deploy the documentation, follow these steps:

Fetch all tags:
```bash	
git fetch --tags
```

Identify the latest tag:
```bash
git describe --tags
```

Create a new tag:
```bash
git tag <tag_name>
```

Push the tag to the main branch:
```bash
git push origin <tag_name>
```

:::{toctree}
:maxdepth: 1
:hidden:

style_and_doc_guidelines
