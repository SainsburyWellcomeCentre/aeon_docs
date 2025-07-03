(target-installation)=
# Installation

This guide will walk you through the installation of the Aeon's [Python packages](target-repositories), `aeon_api` and `aeon_mecha`, using [uv](https://docs.astral.sh/uv/getting-started/installation/). 
It also includes instructions for setting up data access to the Aeon data hosted on Sainbury Wellcome Centre's (SWC) Ceph storage (currently only applicable to SWC members).

(target-install-aeon-api)=
## `aeon_api`
::::{tab-set}
:::{tab-item} PyPI
To install `aeon_api` from [PyPI](https://pypi.org/project/swc-aeon/):
```sh
uv pip install swc-aeon
```
:::

:::{tab-item} Source
To install `aeon_api` from source, first clone the repository and switch to the `aeon_api` directory:
```sh
git clone https://github.com/SainsburyWellcomeCentre/aeon_api
cd aeon_api
```
(Optional) To select a specific branch, replace `branch_name` with the desired branch name:
```sh
git checkout branch_name
```
To install the package alongside all optional dependencies:
```sh
uv sync --all-extras
```
If you wish to install only the core dependencies, simply drop the `--all-extras` flag from the command above.
:::
::::

(target-install-aeon-mecha)=
## `aeon_mecha`
As `aeon_mecha` depends on `aeon_api`, installing `aeon_mecha` will also install `aeon_api` and its dependencies. 
In other words, you only need to install `aeon_mecha` to access both packages.

To install `aeon_mecha`, first clone the repository and switch to the `aeon_mecha` directory:
```sh
git clone https://github.com/SainsburyWellcomeCentre/aeon_mecha
cd aeon_mecha
```
(Optional) To select a specific branch, replace `branch_name` with the desired branch name:
```sh
git checkout branch_name
```
To install the package alongside all optional dependencies:
```sh
uv sync --all-extras
```
If you wish to install only the core dependencies, simply drop the `--all-extras` flag from the command above.
:::
::::

## SWC Ceph data access
:::{important}
You must be an SWC `aeon` project member to access Aeon data hosted on 
SWC's Ceph storage. The required sets of credentials are as follows: 
- Microsoft Teams: contact [Jai Bhagat](mailto:jai.bhagat.21@ucl.ac.uk), [Gonçalo Lopes](mailto:g.lopes@neurogears.org), or [Dario Campagner](mailto:d.campagner@ucl.ac.uk)
- SWC GitHub organisation: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- SWC GitHub `aeon` project: contact [Jai Bhagat](mailto:jai.bhagat.21@ucl.ac.uk) or [Gonçalo Lopes](mailto:g.lopes@neurogears.org)
- SWC HPC: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- `aeon` HPC Linux group: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- Datajoint database username: contact [Thinh Nguyen](mailto:thinh@vathes.com)

To be granted these credentials, please send a single email to 
[all contact parties](mailto:jai.bhagat.21@ucl.ac.uk,g.lopes@neurogears.org,d.campagner@ucl.ac.uk,helpdesk@swc.ucl.ac.uk,thinh@vathes.com?subject=Request%20for%20Aeon%20credentials) 
requesting this access.
:::

:::::{tab-set}
::::{tab-item} Local
:::{note}
The links below point to the SWC Intranet on SharePoint, which is only accessible with a UCL account.
:::
In order to access Aeon data locally, you need to be on the SWC network or connected via VPN. 
You also need to [mount the Ceph storage on your local machine](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-How-to-Mount-137134430.aspx). 
The Ceph storage path for different operating systems can be found [here](https://liveuclac.sharepoint.com/sites/SSC/SitePages/SSC-Storage-Ceph-198906998.aspx), replacing `xxxxxxxx` with `aeon`.
::::

::::{tab-item} Remote

For using an IDE (e.g. VS Code, PyCharm Professional) to access Aeon data, you will need to configure the connection to SWC's HPC using SSH. 
Please ensure you have met all the [prerequisites](niu-howto:SSH-SWC-cluster#prerequisites) before proceeding. 
In order to avoid typing the SSH commands each time you log into the HPC, we recommend modifying the SSH config file following [this guide](niu-howto:SSH-SWC-cluster#ssh-config-file).
The next step is to request an interactive job on the HPC, connect to the assigned compute node, and start a remote development session in your IDE (full details for VS Code can be found in [this guide](niu-howto:vscode-with-slurm-job)).
::::
:::::

Raw Aeon data can be accessed using [`aeon_api`](#aeon_api), whereas processed data can be queried from the [Aeon DataJoint pipeline](target-aeon-dj-pipeline) using [`aeon_mecha`](#aeon_mecha). 
Examples for retrieving and visualising the data can be found in the [User Guide](target-user-guide).