(target-contributor-guide)=
# Contributor's Guide

## Software Development Life Cycle (SDLC)
Our SDLC roughly follows the [iterative model](https://www.tutorialspoint.com/sdlc/sdlc_iterative_model.htm).

(target-contributor-versioning)=
## Versioning
We version all the following, according to [SemVer](semver:) numbering: 

- Experiments, by name, including full hardware specs (habitat, I/O devices, 
  acquisition computer, etc.)
- Repositories, including code related to:
  - Bonsai experiment workflows
  - Quality Control protocols (for raw and preprocessed data)
  - Data processing algorithms
- aeon-db Database
  - aeon-db tables

## Issue tracking
We prioritise and track dev progress using GitHub Discussions and GitHub Issues in GitHub Projects. Issues and Discussions should ideally be created in the specific repository appropriate for the Issue/Discussion; all experiment and general Issues and Discussions should be created in 'aeon_experiments'.

## Continuous integration (CI)
We use GitHub Actions to run CI. We run unit tests on GitHub Virtual Machines on Windows, MacOS, and Ubuntu. We run integration tests on the SWC HPC. Workflows of the CI jobs we run can be found in each repository's respective `.github/workflows/` directory.

:::{toctree}
:maxdepth: 1
:hidden:

contributing_code
contributing_documentation
