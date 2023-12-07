# aeon_docs

This repo contains the source for the currently WIP version of Project Aeon's online docs. 

The docs are built via Sphinx, and hosted via GitHub Pages at: sainsburywellcomecentre.github.io/aeon_docs/. `src/` is the Sphinx source directory, and the site is built and deployed from the `gh-pages` branch. This is handled by a GitHub actions workflow (`.github/workflows/docs_build_and_deploy.yml`). The build job is triggered on each PR, ensuring that the documentation build is not broken by new changes. The deployment job is only triggered whenever a tag is pushed to the main branch.


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

> [!IMPORTANT] 
> You must be an SWC Github 'aeon' project member to view some of these repositories.

### [aeon_mecha](https://github.com/SainsburyWellcomeCentre/aeon_mecha)

![aeon_mecha_env_build_and_tests](https://github.com/SainsburyWellcomeCentre/aeon_mecha/actions/workflows/build_env_run_tests.yml/badge.svg?branch=main)
[![aeon_mecha_tests_code_coverage](https://codecov.io/gh/SainsburyWellcomeCentre/aeon_mecha/branch/main/graph/badge.svg?token=973EC1CG03)](https://codecov.io/gh/SainsburyWellcomeCentre/aeon_mecha)

Project Aeon's main library for interfacing with acquired data. Contains Python modules for raw data file io, data querying, data processing, data qc, database ingestion, and building computational data pipelines. This is the main user repository.

> [!NOTE]
> All experiment data is acquired and/or triggered and/or synced by [Harp devices](https://www.cf-hw.org/harp). Code in the 'aeon_acquisition' and 'aeon_mecha' repos makes use of the [Harp protocol](https://harp-tech.org/articles/about.html) during data acquisition, raw data file writing, and raw data file reading. See also the documentation on [Harp device operation and common registers](https://harp-tech.org/protocol/Device.html), the [Harp binary protocol](https://harp-tech.org/protocol/BinaryProtocol-8bit.html), and [Harp clock synchronization](https://harp-tech.org/protocol/SynchronizationClock.html).

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


## Project Maintainers

Jai Bhagat (jai.bhagat.21@ucl.ac.uk)

Gonçalo Lopes (g.lopes@neurogears.org)

Dario Campagner (d.campagner@ucl.ac.uk)

## Citation Policy

If you use this software, please cite it as below:

Sainsbury Wellcome Centre Foraging Behaviour Working Group. (2023). Aeon: An open-source platform to study the neural basis of ethological behaviours over naturalistic timescales,  https://doi.org/10.5281/zenodo.8411157

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8411157.svg)](https://zenodo.org/doi/10.5281/zenodo.8411157)