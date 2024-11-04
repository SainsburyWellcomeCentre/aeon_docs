# aeon_docs

This repo contains the source for the [Aeon online documentation](https://sainsburywellcomecentre.github.io/aeon_docs/). 

> [!CAUTION] 
> The documentation is currently under active development and may be incomplete.
> Please report any issues or suggestions for improvement by [opening an issue](https://github.com/SainsburyWellcomeCentre/aeon_docs/issues).

To contribute to the documentation, please see the [Contributor Guide](https://sainsburywellcomecentre.github.io/aeon_docs/contributor/index.html).

## Aeon organisation overview

Aeon is a collaborative effort to perform behavioural neuroscience experiments where the behaviour and neural activity of freely moving animals engaging in a complex task are continuously recorded. This project is contributed to by researchers and support staff at UCL's SWC, Neurogears, and Datajoint.

If you are interested in joining this project, please contact the [project maintainers](#project-maintainers).

## Credentials

Below are the required sets of credentials for Aeon members:

- Microsoft Teams: contact [Jai Bhagat](mailto:jai.bhagat.21@ucl.ac.uk), [Gonçalo Lopes](mailto:g.lopes@neurogears.org), or [Dario Campagner](mailto:d.campagner@ucl.ac.uk)
- SWC Github organization: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- SWC Github `aeon` project: contact [Jai Bhagat](mailto:jai.bhagat.21@ucl.ac.uk) or [Gonçalo Lopes](mailto:g.lopes@neurogears.org)
- SWC HPC: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- `aeon` HPC Linux group: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- Datajoint database username: contact [Thinh Nguyen](mailto:thinh@vathes.com)

To be granted these credentials, please send a single email to [all contact parties](mailto:jai.bhagat.21@ucl.ac.uk,g.lopes@neurogears.org,d.campagner@ucl.ac.uk,helpdesk@swc.ucl.ac.uk,thinh@vathes.com?subject=Request%20for%20Aeon%20credentials) requesting this access.

## Repositories
### [aeon_mecha](https://github.com/SainsburyWellcomeCentre/aeon_mecha)

![aeon_mecha_env_build_and_tests](https://github.com/SainsburyWellcomeCentre/aeon_mecha/actions/workflows/build_env_run_tests.yml/badge.svg?branch=main)
[![aeon_mecha_tests_code_coverage](https://codecov.io/gh/SainsburyWellcomeCentre/aeon_mecha/branch/main/graph/badge.svg?token=973EC1CG03)](https://codecov.io/gh/SainsburyWellcomeCentre/aeon_mecha)

Aeon's main library for interfacing with acquired data. Contains Python modules for raw data file io, data querying, data processing, data qc, database ingestion, and building computational data pipelines. This is the main user repository.

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

Contains source code for the Aeon docs site, built via Sphinx. 


## Project Maintainers

- Jai Bhagat (jai.bhagat.21@ucl.ac.uk)
- Gonçalo Lopes (g.lopes@neurogears.org)
- Dario Campagner (d.campagner@ucl.ac.uk)
- Chang Huan Lo (changhuan.lo@ucl.ac.uk)

## Citation Policy

If you use this software, please cite it as below:

Sainsbury Wellcome Centre Foraging Behaviour Working Group. (2023). Aeon: An open-source platform to study the neural basis of ethological behaviours over naturalistic timescales,  https://doi.org/10.5281/zenodo.8411157

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8411157.svg)](https://zenodo.org/doi/10.5281/zenodo.8411157)