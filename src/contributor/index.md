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

## Issue Tracking

We prioritize and track dev progress using Github Discussions and Github Issues in Github Projects. Issues and Discussions should ideally be created in the specific repository appropriate for the Issue/Discussion; all experiment and general Issues and Discussions should be created in 'aeon_experiments'.

## Continuous Integration (CI)

We use Github Actions to run CI. We run unit tests on Github Virtual Machines on Windows, MacOS, and Ubuntu. We run integration tests on the SWC HPC. Workflows of the CI jobs we run can be found in each repo's respective `.github/workflows/` directory.

## Contributing

Each repository roughly follows the [github flow](https://docs.github.com/en/get-started/quickstart/github-flow) (which is adapted from the more general 
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)). 

In brief, each of our repos has 'main' and 'prod' branches. Feature and bug fix branches are branched off of 'main', with Pull Requests sent back into 'main'. 'main' contains the full commit history of the project, up to the latest stable commit. Upon merges into 'main', a squash merge is performed into 'prod', such that 'prod' contains an abbreviated commit history of the project, with commits pertaining only to Pull Request merges. 'prod' thus serves as a "production" branch to allow for easier readability of project history and easier reversion of uncaught bug commits. At certain agreed upon timepoints we create "stable releases" (available in the "releases" section of the repository) which serve as a snapshot of the code at the time, version numbered according to [SemVer](semver:).

When contributing to any repository, the change to be made should first be discussed in a Github Discussion or a Github Issue. Thereafter, contributors should create a new branch (branched off of 'main') that contains the changes/additions they wish to make, and then create a pull request for merging this branch into 'main'.

All pull requests will be reviewed by the [project maintainers](target-project-maintainers). Minimally, maintainers should follow the below steps when reviewing pull requests:

1) Ensure new code adheres to the [style and documentation guidelines](#style-and-documentation-guidelines), is covered by a test, and passes a build test. These can all be checked via CI.

2) As necessary, ensure `changelog`, `readme`, config and doc files are updated.

3) When a branch is ready to be merged back into 'main', always make sure to first pull 'main' locally, then rebase the feature branch onto 'main' (cleaning up any merge conflicts as necessary), before merging the PR. The squash merge into 'prod' can be handled via CI. E.g., see [here](aeon-mecha-github:blob/main/.github/workflows/squash_merge_to_prod.yml)

## Style and Documentation Guidelines

Please see our [style and documentation guidelines](target-style-doc-guidelines).

We also believe in the [readme manifesto](http://thinkinghard.com/blog/TheREADMEManifesto.html), which says that `readme` files should provide at least a general description that covers _all_ of a project's files, and that one `readme` per subdirectory is generally good practice.


:::{toctree}
:maxdepth: 1
:hidden:

style_and_doc_guidelines
