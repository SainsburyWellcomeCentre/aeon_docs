(target-contributing-code)=
# Contributing Code
Each repository roughly follows the [github flow](https://docs.github.com/en/get-started/using-github/github-flow) (which is adapted from the more general 
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)). 

In brief, each of our repos has 'main' and 'prod' branches. Feature and bug fix branches are branched off of 'main', with Pull Requests sent back into 'main'. 'main' contains the full commit history of the project, up to the latest stable commit. Upon merges into 'main', a squash merge is performed into 'prod', such that 'prod' contains an abbreviated commit history of the project, with commits pertaining only to Pull Request merges. 'prod' thus serves as a "production" branch to allow for easier readability of project history and easier reversion of uncaught bug commits. At certain agreed upon timepoints we create "stable releases" (available in the "releases" section of the repository) which serve as a snapshot of the code at the time, version numbered according to [SemVer](semver:).

When contributing to any repository, the change to be made should first be discussed in a GitHub Discussion or a GitHub Issue. Thereafter, contributors should create a new branch (branched off of 'main') that contains the changes/additions they wish to make, and then create a pull request for merging this branch into 'main'.

All pull requests will be reviewed by the [project maintainers](target-project-maintainers). Minimally, maintainers should follow the below steps when reviewing pull requests:

1) Ensure new code adheres to the [style and documentation guidelines](target-style-doc-guidelines), is covered by a test, and passes a build test. These can all be checked via CI.

2) As necessary, ensure `changelog`, `readme`, config and doc files are updated.

3) When a branch is ready to be merged back into 'main', always make sure to first pull 'main' locally, then rebase the feature branch onto 'main' (cleaning up any merge conflicts as necessary), before merging the PR. The squash merge into 'prod' can be handled via CI. E.g., see [here](aeon-mecha-github:blob/main/.github/workflows/squash_merge_to_prod.yml)
