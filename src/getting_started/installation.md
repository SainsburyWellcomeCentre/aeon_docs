(target-installation)=
# Installation

This guide will walk you through the installation of the `aeon_mecha` package, the main package for interacting with raw Aeon data. It also includes instructions for setting up data access to the Aeon data hosted on SWC's Ceph storage (currently only applicable to SWC members).

(target-install-aeon-mecha)=
## `aeon_mecha`

:::{note}
We always recommend installing `aeon_mecha` inside a 
[conda](https://docs.conda.io/en/latest/)
or [mamba](https://mamba.readthedocs.io/en/latest/) environment, 
to avoid dependency conflicts with other packages.
In the following we assume you have `conda` installed,
but the same commands will also work with `mamba`/`micromamba`.

All commands below should be run in a bash shell 
(Windows users can use the 'mingw64' terminal that is included when 
installing git).
:::

:::{dropdown} Setting up on SWC's HPC
:color: primary
:icon: server
If setting up on SWC's remote HPC system, you will have to first connect to the HPC using SSH and add miniconda to your system path.
```sh
ssh <your_SWC_username>@ssh.swc.ucl.ac.uk
ssh hpc-gw1
module load miniconda
```
**Optional**: Add the following commands to the `.profile` file to add miniconda as an environment module and Bonsai and its dependencies to your system path on startup (this will be initialized each time you SSH into the HPC). This file should be located in the home directory, i.e. `~/.profile`. If it does not exist, create it with `touch ~/.profile`.

```{code-block} sh
:caption: .profile
# Set env modules
module load miniconda

# Save Bonsai and deps to path
export PATH=$PATH:/ceph/aeon/aeon/code/bonsai/Bonsai.Player/bin/Debug/net5.0
export DOTNET_ROOT=/ceph/aeon/aeon/code/dotnet
export PATH=$PATH:/ceph/aeon/aeon/code/dotnet
```
:::

Clone the `aeon_mecha` repository into the `~/ProjectAeon/aeon_mecha` directory. 
```sh
mkdir ~/ProjectAeon 
cd ~/ProjectAeon
git clone https://github.com/SainsburyWellcomeCentre/aeon_mecha
cd aeon_mecha
```

Create the `aeon` conda environment and activate it.
```sh
conda create -n aeon -c conda-forge python>=3.11
conda activate aeon
```

Install the `aeon_mecha` package in editable mode.
::::{tab-set}
:::{tab-item} Users
```sh
pip install -e .
```
:::

:::{tab-item} Developers
```sh
pip install -e .[dev]  # works on most shells
```
or 
```sh
pip install -e '.[dev]'  # works on zsh (the default shell on macOS)
```
This will install the package alongside all `dev` dependencies.
:::
::::

## Setting up SWC Ceph data access

:::{important}
You must be an SWC `aeon` project member to access Aeon data hosted on 
SWC's Ceph storage. The required sets of credentials are as follows: 
- Microsoft Teams: contact [Jai Bhagat](mailto:jai.bhagat.21@ucl.ac.uk), [Gonçalo Lopes](mailto:g.lopes@neurogears.org), or [Dario Campagner](mailto:d.campagner@ucl.ac.uk)
- SWC Github organization: contact [SWC Helpdesk](mailto:helpdesk@swc.ucl.ac.uk)
- SWC Github `aeon` project: contact [Jai Bhagat](mailto:jai.bhagat.21@ucl.ac.uk) or [Gonçalo Lopes](mailto:g.lopes@neurogears.org)
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
The links below point to the SWC internal wiki, which is only accessible from within the SWC network (or using VPN).
:::
In order to access Aeon data locally, you need to be on the SWC network or connected via VPN. You also need to [mount the Ceph storage on your local machine](https://wiki.ucl.ac.uk/display/SSC/How+to+Mount). The Ceph storage path for different operating systems can be found [here](https://wiki.ucl.ac.uk/display/SSC/Storage%3A+Ceph), replacing `xxxxxxxx` with `aeon`.
::::

::::{tab-item} Remote

For using an IDE (e.g. VS Code, PyCharm Professional, Jupyter, etc.) to access Aeon data, you will need to configure the connection to SWC's HPC using SSH. 
Please ensure you have met all the [prerequisites](niu-howto:#prerequisites) before proceeding. 
In order to avoid typing the SSH commands each time you log into the HPC, we recommend modifying the SSH config file following this [guide](niu-howto:#ssh-config-file).
The next step is to configure your IDE to connect to the `swc-gateway` node via SSH. These instructions can typically be found in your IDE's online documentation. Here are the instructions for [VS Code](https://code.visualstudio.com/docs/remote/ssh), and for [PyCharm Professional](https://www.jetbrains.com/help/pycharm/remote-development-overview.html#client_to_server).
::::
:::::

Within the `aeon` conda environment, Aeon data can be accessed from Ceph using the [`aeon_mecha` API](target-mecha-reference) or queried from the [Aeon DataJoint pipeline](target-aeon-dj-pipeline). Examples for retrieving and visualizing the data can be found in the [User Guide](target-user-guide).