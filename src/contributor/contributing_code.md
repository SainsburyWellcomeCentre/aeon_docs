(target-contributing-code)=
# Contributing Code
Each repository roughly follows the [github flow](https://docs.github.com/en/get-started/using-github/github-flow), 
which is adapted from the more general [gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). 

In brief, each of our repositories has 'main' and 'prod' branches. 
Feature and bug fix branches are branched off of 'main', with Pull Requests sent back into 'main'. 
'main' contains the full commit history of the project, up to the latest stable commit. 
Upon merges into 'main', a squash merge is performed into 'prod', such that 'prod' contains an abbreviated commit history of the project, with commits pertaining only to Pull Request merges. 
'prod' thus serves as a "production" branch to allow for easier readability of project history and easier reversion of uncaught bug commits. 
At certain agreed upon timepoints we create "stable releases" (available in the "releases" section of the repository) which serve as a snapshot of the code at the time, version numbered according to [SemVer](semver:).

When contributing to any repository, the change to be made should first be discussed in a GitHub Discussion or a GitHub Issue. 
Thereafter, contributors should create a new branch (branched off of 'main') that contains the changes/additions they wish to make, and then create a pull request for merging this branch into 'main'.

All pull requests will be reviewed by the [project maintainers](target-project-maintainers). 
Minimally, maintainers should follow the below steps when reviewing pull requests:

1) Ensure new code adheres to the [style and documentation guidelines](target-style-doc-guidelines), is covered by a test, and passes a build test. These can all be checked via CI.

2) As necessary, ensure `changelog`, `readme`, config and doc files are updated.

3) When a branch is ready to be merged back into 'main', always make sure to first pull 'main' locally, then rebase the feature branch onto 'main' (cleaning up any merge conflicts as necessary), before merging the Pull Request. 
The squash-merge into 'prod' can be handled via CI, e.g. see [here](aeon-mecha-github:blob/main/.github/workflows/squash_merge_to_prod.yml).

(target-style-doc-guidelines)=
## Style and documentation guidelines
We generally adhere to [pep8](python-pep:0008), [pep257](python-pep:0257), and [google's style guide](https://google.github.io/styleguide/pyguide.html) for code and docstring style guidelines. 
We run ruff and pyright to format our Python code, the config settings for which can be found in a repository's `pyproject.toml`. 
We also believe in the [readme manifesto](https://www.thinkinghard.com/blog/TheREADMEManifesto), which says that `readme` files should provide at least a general description that covers _all_ of a project's files, and that one `readme` per subdirectory is generally good practice.

### General guidelines
* All files contain a header that briefly describes the contents within a few sentences.
* In general, more lines for the sake of clarity is preferred over brevity.

### Function and class docstrings
* Function names should describe the action they perform. Functions have the following sections in the given order:
  - One-line summary description, typically as a verb phrase
  - Long description (optional)
  - Inputs
  - Outputs
  - Examples (optional if included in a separate file)
  - Warnings/Exceptions (optional)
  - Additional notes (optional)
  - See also (optional)
  - Todos (optional)
* Class names should describe the entity they represent. Classes have the following sections in the given order:
  - One-line summary description, typically as a noun phrase
  - Properties / Attributes
  - Long description (optional)
  - Examples (optional if included in a separate file)
  - Warnings/Exceptions (optional)
  - Additional notes (optional)
  - See also (optional)
  - Todos (optional)

### Whitespace conventions
* A tab/indent is set at four spaces.
* Vertical whitespace is used sparingly, but can be used to improve readability between code blocks/sections.
* Horizontal whitespace is used sparingly, but can be used to improve readability between long and/or complex operations and conditionals.
* Each line contains no more than 108 characters.
* Line terminations are LF, not CRLF.

### Comment conventions
* Block comments are written as full sentences above the corresponding code. 
* Inline comments are written as a short phrase that starts two spaces after the corresponding code.
* Code referenced in comments are surrounded by back ticks for readability.
* Comments are used to describe variables where they are declared.

### Additional conventions
* Naming conventions:
  - Variable and function names are in lower snake_case (e.g. `exp_ref`, `infer_parameters` with a `_` in between each individual word representation).
  - Classes are in upper Snake_Case (e.g. `Alyx_Panel`).
  - Prefix 'n' is used for integer values e.g. `n_items`.
  - Suffix 'num' is used for referring to a particular instance e.g. `item_num`.
  - Suffixes that indicate unit measurement are used when using multiple units e.g. `wheel_deg` and `wheel_mm`.
  - Reuse of variable names (i.e. mutation) is generally avoided.
  - Variables across related files which share names should share meanings.
* Comments are for explaining _what_ a particular chunk of code does when it may be unintuitive, not for explaining exactly _how_ the code does what it does.
* Block comments read as a narrative.
* In function calls, keyword arguments should should be specified when not obvious.
* Leading underscores are reserved for "private" functions.