(target-getting-started)=
# Getting Started

Project Aeon is a collaborative effort to perform behavioral neuroscience 
experiments where the behavior and neural activity of freely moving animals 
engaging in a complex task are continuously recorded... 
Further information about the project can be found in the 
[About](target-about) section.

(target-repositories)=
## Repositories

Project Aeon spans multiple repositories, each serving a different purpose. 
The following is a list of repositories that are part of the project:
::::{grid} 1 2 2 2
:gutter: 3 

:::{grid-item-card} {fas}`database;sd-text-primary` aeon_mecha
:link: https://github.com/SainsburyWellcomeCentre/aeon_mecha
:link-type: url
Project Aeon's main library for interfacing with acquired data
:::

:::{grid-item-card} {fas}`flask;sd-text-primary` aeon_experiments
:link: https://github.com/SainsburyWellcomeCentre/aeon_experiments
:link-type: url
Aeon experiment workflows written in the Bonsai visual programming language
:::

:::{grid-item-card} {fas}`computer;sd-text-primary` aeon_acquisition
:link: https://github.com/SainsburyWellcomeCentre/aeon_acquisition
:link-type: url
Source code for the `aeon_acquisition` Bonsai package used in 
Aeon experiment workflows
:::

:::{grid-item-card} {fas}`chart-line;sd-text-primary` aeon_analysis
:link: https://github.com/SainsburyWellcomeCentre/aeon_analysis
:link-type: url
Python modules for analysis of Aeon experiment data
:::

:::{grid-item-card} {fas}`gear;sd-text-primary` aeon_lineardrive
:link: https://github.com/SainsburyWellcomeCentre/aeon_lineardrive
:link-type: url
Source code for actuating a linear drive motor used in Aeon experiments
:::

:::{grid-item-card} {fas}`cookie-bite;sd-text-primary` aeon_feeder
:link: https://github.com/SainsburyWellcomeCentre/aeon_feeder
:link-type: url
Source code for pellet delivery via feeders used in Aeon experiments
:::
::::

:::{note}
All experiment data is acquired and/or triggered and/or synced by 
[Harp devices](https://www.cf-hw.org/harp). 
Code in the `aeon_acquisition` and `aeon_mecha` repositories makes use of 
the [Harp protocol](harp-tech:articles/about) during data acquisition, 
raw data file writing, and raw data file reading. 
See also the documentation on 
[Harp device operation and common registers](harp-tech:protocol/Device), 
the [Harp binary protocol](harp-tech:protocol/BinaryProtocol-8bit), and 
[Harp clock synchronization](harp-tech:protocol/SynchronizationClock).
:::

## Installation

### `aeon_mecha`

:::{admonition} Note
:class: note
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

## Accessing Data

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
:::{admonition} Note
:class: note
The links below point to the SWC internal wiki, which is only accessible from within the SWC network (or using VPN).
:::
In order to access Aeon data locally, you need to be on the SWC network or connected via VPN. You also need to [mount the Ceph storage on your local machine](https://wiki.ucl.ac.uk/display/SSC/How+to+Mount). The Ceph storage path for different operating systems can be found [here](https://wiki.ucl.ac.uk/display/SSC/Storage%3A+Ceph), replacing `xxxxxxxx` with `aeon`.
::::

::::{tab-item} Remote
For using an IDE (e.g. PyCharm, VS Code, Jupyter, etc.), you will need to set up local port forwarding from a specified port on the HPC. These instructions can typically be found in your IDE's online documentation. Here are instructions for [PyCharm Professional](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html), and for [VS Code](https://code.visualstudio.com/docs/remote/ssh).
::::
:::::

Within the `aeon` conda environment, Aeon data can be accessed directly from Ceph or the DataJoint database using the [Aeon API](target-api-reference). Examples for retrieving and visualizing the data can be found in the [User Guide](target-user-guide).