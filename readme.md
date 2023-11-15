# aeon_docs

This repo contains the source for the currently WIP version of Project Aeon's online docs. 

The docs are built via Sphinx, and hosted via GitHub Pages at: sainsburywellcomecentre.github.io/aeon_docs/. `src/` is the Sphinx source directory, and the site is built and deployed from the `gh-pages` branch. This is handled by a GitHub actions workflow (`.github/workflows/docs_build_and_deploy.yml`). The build job is triggered on each PR, ensuring that the documentation build is not broken by new changes. The deployment job is only triggered whenever a tag is pushed to the main branch.

All organizational details will eventually be available on the docs, but for now some useful info can be found in the sections below:

## Building the documentation locally

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
You can view the local build by opening ``docs/html/index.html`` in a browser.

To apply new changes to the documentation, remove all automatically generated files and folders, and rebuild:
```bash
make clean html
```

## Project Aeon Organization Overview

ProjectAeon is a collaborative effort to perform behavioral neuroscience experiments where the behavior and neural activity of freely moving animals engaging in a complex task are continuously recorded. This project is contributed to by researchers and support staff at UCL's SWC, Neurogears, and Datajoint.

If you are interested in joining this project, please contact the [project maintainers](#project-maintainers).

## Credentials

Below are the required sets of credentials for Project Aeon's members: 

- Microsoft Teams: contact Jai Bhagat, Goncalo Lopes, or Dario Campagner
- SWC Github organization: contact SWC Helpdesk (helpdesk@swc.ucl.ac.uk)
- SWC Github 'aeon' project: contact Jai Bhagat or Goncalo Lopes
- SWC HPC: contact SWC Helpdesk
- 'aeon' HPC Linux group: contact SWC Helpdesk
- Datajoint database username: contact Thinh Nguyen (thinh@vathes.com)

To be granted these credentials, please send a single email to all contact parties requesting this access.

## Repositories

You must be an SWC Github 'aeon' project member to view some of these repositories.

### [aeon_mecha](https://github.com/SainsburyWellcomeCentre/aeon_mecha)

![aeon_mecha_env_build_and_tests](https://github.com/SainsburyWellcomeCentre/aeon_mecha/actions/workflows/build_env_run_tests.yml/badge.svg?branch=main)
[![aeon_mecha_tests_code_coverage](https://codecov.io/gh/SainsburyWellcomeCentre/aeon_mecha/branch/main/graph/badge.svg?token=973EC1CG03)](https://codecov.io/gh/SainsburyWellcomeCentre/aeon_mecha)

Project Aeon's main library for interfacing with acquired data. Contains Python modules for raw data file io, data querying, data processing, data qc, database ingestion, and building computational data pipelines. This is the main user repository.

*Note*: All experiment data is acquired and/or triggered and/or synced by [Harp devices](https://www.cf-hw.org/harp). Code in the 'aeon_acquisition' and 'aeon_mecha' repos makes use of the [Harp protocol](https://github.com/harp-tech/protocol) during data acquisition, raw data file writing, and raw data file reading. In the 'harp-tech/protocol' Github repo, you can find documentation on [Harp device operation and common registers](https://github.com/harp-tech/protocol/blob/master/Device%201.0%201.4%2020200901.pdf), the [Harp binary protocol](https://github.com/harp-tech/protocol/blob/master/Binary%20Protocol%201.0%201.1%2020180223.pdf), and [Harp clock synchronization](https://github.com/harp-tech/protocol/blob/master/Synchronization%20Clock%201.0%201.0%2020200712.pdf).

### [aeon_experiments](https://github.com/SainsburyWellcomeCentre/aeon_experiments)

Contains experiment workflows written in the Bonsai visual programming language.

### [aeon_acquisition](https://github.com/SainsburyWellcomeCentre/aeon_acquisition)

Contains the source code for the 'aeon_acquisition' Bonsai package, which is heavily used in workflows in 'aeon_experiments'.

### [aeon_analysis](https://github.com/SainsburyWellcomeCentre/aeon_analysis)

Contains Python modules for analysis of Aeon experiment data.

### [aeon_lineardrive](https://github.com/SainsburyWellcomeCentre/aeon_lineardrive)

Contains source code for actuating a linear drive motor used in Aeon experiments (designed primarily for moving electrophysiology cabling during freely-moving experiments).

### [aeon_feeder](https://github.com/SainsburyWellcomeCentre/aeon_feeder)

Contains low-level source code for pellet delivery via feeders used in Aeon experiments.

### [aeon_docs](https://github.com/SainsburyWellcomeCentre/aeon_docs)

Contains source code for the Aeon docs site, built via Sphinx. Built docs at: https://sainsburywellcomecentre.github.io/aeon_docs/

## Dev Practices

### Software Development Life Cycle (SDLC)

Our SDLC roughly follows the [iterative model](https://www.tutorialspoint.com/sdlc/sdlc_iterative_model.htm).

### Versioning

We version all the following, according to [SemVer](http://semver.org/) numbering: 

- Experiments, by name, including full hardware specs (arena, I/O devices, 
  acquisition computer, etc.)
- Repositories, including code related to:
  - Bonsai experiment workflows
  - Quality Control protocols (for raw and preprocessed data)
  - Data processing algorithms
- aeon-db Database
  - aeon-db tables

### Issue Tracking

We prioritize and track dev progress using Github Discussions and Github Issues in Github Projects. Issues and Discussions should ideally be created in the specific repository appropriate for the Issue/Discussion; all experiment and general Issues and Discussions should be created in 'aeon_experiments'.

### Continuous Integration (CI)

We use Github Actions to run CI. We run unit tests on Github Virtual Machines on Windows, MacOS, and Ubuntu. We run integration tests on the SWC HPC. Workflows of the CI jobs we run can be found in each repo's respective `.github/workflows/` directory.

### Contributing

Each repository roughly follows the [github flow](https://guides.github.com/introduction/flow/) (which is adapted from the more general 
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)). 

In brief, each of our repos has 'main' and 'prod' branches. Feature and bug fix branches are branched off of 'main', with Pull Requests sent back into 'main'. 'main' contains the full commit history of the project, up to the latest stable commit. Upon merges into 'main', a squash merge is performed into 'prod', such that 'prod' contains an abbreviated commit history of the project, with commits pertaining only to Pull Request merges. 'prod' thus serves as a "production" branch to allow for easier readability of project history and easier reversion of uncaught bug commits. At certain agreed upon timepoints we create "stable releases" (available in the "releases" section of the repository) which serve as a snapshot of the code at the time, version numbered according to [SemVer](http://semver.org/).

When contributing to any repository, the change to be made should first be discussed in a Github Discussion or a Github Issue. Thereafter, contributors should create a new branch (branched off of 'main') that contains the changes/additions they wish to make, and then create a pull request for merging this branch into 'main'.

All pull requests will be reviewed by the [project maintainers](#project-maintainers). Minimally, maintainers should follow the below steps when reviewing pull requests:

1) Ensure new code adheres to the [style and documentation guidelines](#style-and-documentation-guidelines), is covered by a test, and passes a build test. These can all be checked via CI.

2) As necessary, ensure `changelog`, `readme`, config and doc files are updated.

3) When a branch is ready to be merged back into 'main', always make sure to first pull 'main' locally, then rebase the feature branch onto 'main' (cleaning up any merge conflicts as necessary), before merging the PR. The squash merge into 'prod' can be handled via CI. E.g., see [here](https://github.com/SainsburyWellcomeCentre/aeon_mecha/tree/main/.github/workflows/squash_merge_to_prod.yml)

### Style and Documentation Guidelines

Please see our [style and documentation guidelines](https://github.com/ProjectAeon/blog/blob/main/style_and_doc_guidelines.md).

We also believe in the [readme manifesto](http://thinkinghard.com/blog/TheREADMEManifesto.html), which says that `readme` files should provide at least a general description that covers _all_ of a project's files, and that one `readme` per subdirectory is generally good practice.

### Code of Conduct

Please see our [code of conduct](https://github.com/ProjectAeon/blog/blob/main/code_of_conduct.md).

## Project Maintainers

Jai Bhagat (jai.bhagat.21@ucl.ac.uk)

Gonçalo Lopes (g.lopes@neurogears.org)

Dario Campagner (d.campagner@ucl.ac.uk)

## Citation Policy

If you use this software, please cite it as below:

Sainsbury Wellcome Centre Foraging Behaviour Working Group. (2023). Aeon: An open-source platform to study the neural basis of ethological behaviours over naturalistic timescales,  https://doi.org/10.5281/zenodo.8413142

[![DOI](https://zenodo.org/badge/485512362.svg)](https://zenodo.org/badge/latestdoi/485512362)


