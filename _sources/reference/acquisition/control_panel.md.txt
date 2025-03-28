(target-module-control-panel)=
# Control Panel
In Aeon, it is crucial to both monitor the state of an experiment as well as control the experiment's hardware devices and parameters in real time. 
This is achieved through the construction of a [ControlPanel](target-node-controlpanel), which constructs visualisers and a control panel for a given Aeon experiment. Full control panels for individual experiments can be found in the `Extensions` folder (and the toolbox in the Bonsai editor) on the specific experimental branch.

## Nodes
(target-node-controlpanel)=
### ControlPanel 
In Aeon, the `ControlPanel` node constructs visualisers and a control panel for an Aeon experiment.
These are split into several categories, each implemented in a dedicated `GroupWorkflow` within the `ControlPanel`.

:::workflow
![ControlPanelWorkflow](../../workflows/miniAeon/controlPanel.bonsai)
:::

1. **PatchActivity**: Tracks the state of the foraging patches on the rig, including the current threshold, rolling and total distance travelled on the wheels of the foraging patches, information on the number and timing of food pellet deliveries and time since different subjects visited the different patches. 
2. **SubjectActivity**: Constructs additional controls for the environment and exposed properties of the workflow, as well as additional visualiser windows. In Aeon, these additional windows are used to display tracking or pose information and monitoring of light levels in the experiment room. 
3. **EnvironmentState**: Constructs a mashup of a general control panel displaying information and providing control dialogues for the [foraging patches](target-module-foraging-patch), the environment configuration and manual annotation and alert logs grouped into the "ExperimentMetadata" `GroupWorkflow`, as well as experimental subjects entered and removed from the habitat and subject weight measurements grouped into the "EnvironmentSubjectState" `GroupWorkflow`
4. **CameraSelector**: Displays a single image visualiser used to view any camera or other `OpenCV.Net.IplImage`, selected from a list of `Subject`s using the "SubjectActivity" control panel.

Additionally, the `ControlPanel` node enables manual control to start and stop the cameras on the setup through [`KeyDown`](https://bonsai-rx.org/docs/api/Bonsai.Windows.Input.KeyDown.html) nodes cast to 'StartCameras' and 'StopCameras' `Subject`s that trigger or halt acquisition of camera images by the [`CameraController`](target-module-camera-controller). 
Finally, it defines and splits the timestamped entry and exit events of experimental subjects, defined by the [`SubjectDatabase`](target-node-subjectdatabase) inside 'ExperimentMetadata'.
These events are then utilised by the `RepeatEverySubject` workflow to begin and end subscription to the attached sequence on entry and exit of an experimental subject.

Visualisers and control panel are displayed when the workflow is run from the editor or the CLI. 
As with any other visualisers in Bonsai, the visibility, position, size and layout configuration are stored and loaded from the workflow's `.bonsai.layout` file, saved with the workflow. 

These control panels are largely supported and configured using in-built functionality provided by nodes in [`Bonsai.GUI`](https://bonsai-rx.org/gui/), but some visualisers are constructed using custom auxiliary nodes for Aeon experiments in the `Aeon.Environment` namespace or as an extension in C#. 
These include:

- [`ExperimentProperties`](target-node-experimentproperties)
- [`AnnotationSource`](target-node-annotationsource)
- [`EnvironmentState`](target-node-environmentstate)
- [`LabelControl`](target-node-labelcontrol)
- [`ButtonSource`](target-node-buttonsource)

and the external workflow:
- [`SubjectDatabase`](target-node-subjectdatabase)

## Usage
### PatchActivity
<!-- TODO: Any general description for the workflow? -->
The example below shows the "PatchActivity" `GroupWorkflow` used to construct a control panel for a single foraging patch, camera and RFID reader. 

:::workflow
![PatchActivityWorkflow](../../workflows/miniAeon/patchActivity.bonsai)
:::


### SubjectActivity
The "SubjectActivity" `GroupWorkflow` uses an [`ExperimentProperties`](target-node-experimentproperties) node to allow online access to exposed properties during an experiment, and a [`ButtonSource`](target-node-buttonsource) node (triggered through a shared `Subject` "ReloadEnvironment") to generate a labelled button that reloads an environment file. 
Additionally, the results from pose tracking modules ("SubjectPoses") and images from a camera monitoring the status of controlled light sources in the room ("CameraLightMonitor") are subscribed to and organised into [`TableLayoutPanel`s](https://learn.microsoft.com/en-gb/dotnet/api/system.windows.forms.tablelayoutpanel), which then create the full visualiser window.

:::workflow
![SubjectActivityWorkflow](../../workflows/miniAeon/subjectActivity.bonsai)
:::

### EnvironmentState
The "EnvironmentState" control panel or visualiser is created by combining the outputs of the "ExperimentMetadata" and "EnvironmentSubjectState" `GroupWorkflows`.

#### ExperimentMetadata
The "ExperimentMetadata" `GroupWorkflow` creates a visualiser window that enables control of basic functions for each [foraging patch](target-module-foraging-patch) in an experiment, through the [control panels](target-node-patchdispenser-control-panel) created by the corresponding[`PatchDispenser`](target-node-patchdispenser) node. 
Patch dispenser events are parsed into "Reset" or manual "Deliver" command `Subject`s which are used by the [`UndergroundFeeder`](target-node-undergroundfeeder) node to control the behaviour of the foraging patch hardware.

In addition, the [`AnnotationSource`](target-node-annotationsource), [`EnvironmentState`](target-node-environmentstate) and [`LabelControl`](target-node-labelcontrol) nodes create the full "ExperimentMetadata" control panel.

The example below shows the "ExperimentMetadata" `GroupWorkflow` used to construct a control panel for a single foraging patch.

:::workflow
![ExperimentMetadataWorkflow](../../workflows/miniAeon/experimentMetadata.bonsai)
:::

#### EnvironmentSubjectState
<!-- TODO / TOUNDERSTAND -->

(target-groupworkflow-cameraselector)=
### CameraSelector
The "CameraSelector" `GroupWorkflow` creates a simple image visualiser using a custom `StreamSelector` node connected to `SubscribeSubject`s carrying images from each of the cameras and/or other informative images, e.g. a heatmap constructed from [tracked subject positions](target-module-subject-tracking). 

The `StreamSelector` has a single property, "SelectedStream" which enables switching between these images for display. 
This property is externalised to the highest level of the workflow, meaning it is accessible via the [`ExperimentProperties`](target-node-experimentproperties) node. 
This enables the user to select and switch to specific cameras or images during acquisition. 

:::{seealso}
The full control panel example used in Aeon, with three foraging patches and cameras focused on the foraging sites, at [`aeon_experiments/social0.4.0`](aeon-experiments-github:blob/social0.4.0/workflows/social/Extensions/ControlPanel.bonsai).
:::

:::{toctree}
:maxdepth: 1
:hidden:
:glob:

control_panel/*
:::