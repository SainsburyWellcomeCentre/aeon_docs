# Control Panel
During an AEON experiment, it is important to have a way of monitoring the state of the experiment as well as controlling the hardware devices and parameters of an experiment in real time. 

The `ControlPanel` constructs visualisers and a control panel for a given AEON experiment. These are split into several categories, each implemented in a dedicated `GroupWorkflow` within the `ControlPanel`


:::workflow
![ControlPanelWorkflow](../../../workflows/miniAeon/controlPanel.bonsai)
:::

1. 'PatchActivity', which tracks the state of the feeders on the rig, including the current threshold, rolling and total distance travelled on the wheels of the feeders wheels, information on the number and timing of food pellet deliveries and time since different subjects visited the different patches. 
2. 'SubjectActivity', which constructs additional controls for the environment and exposed properties of the workflow, as well as additional visualiser windows. In Aeon, these additional windows are used to display tracking or pose information and monitoring of light levels in the experiment room. 
3. 'EnvironmentState', which constructs a mashup of a general control panel displaying information and providing control dialogues for the [foraging feeders](../foraging_patch/foraging_patch.md), the environment configuration and manual annotation and alert logs grouped into the 'ExperimentMetadata' `GroupWorkflow`, as well as experimental subjects entered and removed from the arena and subject weight measurements grouped into the 'EnvironmentSubjectState' `GroupWorkflow`
4. 'CameraSelector', which displays a single image visualiser used to view any camera or other `OpenCV.Net.IplImage`, selected from a list of `Subject`s using the 'SubjectActivity' control panel.

Additionally, the `ControlPanel` node enables manual control to start and stop the cameras on the setup through `keyDown` nodes cast to `Subject`s 'StartCameras' and 'StopCameras' that trigger or halt acquisition of camera images by the [`CameraController`](../camera_controller.md). Finally, it defines and splits the timestamped entry and exit events of experimental subjects, defined by the [`SubjectDatabase`](./auxiliary_nodes/subject_database.md) inside 'ExperimentMetadata', and utilised by the `RepeatEverySubject` workflow to begin and end subscription to the attached sequence on entry and exit of an experimental subject.

Visualisers and control panel are displayed when the workflow is run from the editor or the CLI. As with any other visualisers in Bonsai, the visibility, position, size and layout configuration are stored and loaded from the workflow's `.bonsai.layout` file, saved with the workflow. 

These control panels are largely supported and configured using in-built functionality provided by nodes in the `Bonsai.GUI` package, but some visualisers are constructed using custom auxiliary nodes for AEON experiments in the `Aeon.Environment` namespace or as an extension in C#. These include:

- [`ExperimentProperties`](./auxiliary_nodes/experimentProperties.md)
- [`AnnotationSource`](./auxiliary_nodes/annotation_source_GUI.md)
- [`EnvironmentState`](./auxiliary_nodes/environment_state_GUI.md)
- [`LabelControl`](./auxiliary_nodes/label_control_GUI.md)
- [`ButtonSource`](./auxiliary_nodes/button_source_GUI.md)

and the external workflow:
- [`SubjectDatabase`](./auxiliary_nodes/subject_database.md)

## Usage:
### 'PatchActivity'
The 'PatchActivity' `GroupWorkflow` used for Aeon experiments, with three feeders and cameras focused on the foraging sites, can be found inside the `ControlPanel` external workflow of an experimental workflow of the [aeon-experiments](https://github.com/SainsburyWellcomeCentre/aeon_experiments) repo, for example in the tagged `social0.4`. The example below shows an example of the construction of this section of the control panel but for a single feeder, camera and RFID. 

:::workflow
![PatchActivityWorkflow](../../../workflows/miniAeon/patchActivity.bonsai)
:::

### 'SubjectActivity'
The 'SubjectActivity' `GroupWorkflow` used for aeon experiments is shown here. It uses an [`ExperimentProperties'](./auxiliary_nodes/experiment_properties_GUI.md) node to allow online access to exposed properties during an experiment, and a [`ButtonSource (Aeon.Environment)`](./auxiliary_nodes/buttonSource_GUI.md) node to generate a labelled button that reloads an environment file, triggered through a shared `Subject`, here called `ReloadEnvironment`. Additionally, the results of pose tracking modules are subscribed to (`SubjectPoses`) as well as images from a camera that monitors the status of controlled light sources in the room (`CameraLightMonitor`) are subscribed to and arranged in `TableLayoutPanel`s that then construct a full visualiser window.

:::workflow
![PatchActivityWorkflow](../../../workflows/miniAeon/patchActivity.bonsai)
:::

### 'EnvironmentState'
The 'EnvironmentState' control panel or visualiser used for Aeon experiments is constructed as a combination of the output of two `GroupWorkflows`: 'ExperimentMetadata' and 'EnvironmentSubjectState' 

#### ExperimentMetadata

This `GroupWorkflow` constructs a visualiser window enabling control of the basic functions for each of the [foraging patches](../foraging_patch/foraging_patch.md) in the arena, through a [`PatchDispenser`](../foraging_patch/auxiliary_nodes/patch_dispenser.md) node per feeder. 
In addition to controlling the hardware functions of a feeder, this node also constructs a [dispenser control panel](./auxiliary_nodes/patch_dispenser_GUI.md) for a given patch. 

In addition, an [`AnnotationSource`](./auxiliary_nodes/annotation_source_GUI.md), [`EnvironmentState`](./auxiliary_nodes/environment_state_GUI.md) and [`LabelControl`](./auxiliary_nodes/label_control_GUI.md) nodes are used to construct the complete 'ExperimentMetadata' control panel.

In a full AEON experiment, three patches are included, plus a 'dummy' patch. Show here is the functionality of this group for a single patch, as featured in miniAEON:
:::workflow
![ExperimentMetadataWorkflow](../../../workflows/miniAeon/ExperimentMetadata.bonsai)
:::

Finally, the patch dispenser events are parsed into 'Reset' or manual 'Deliver' command `Subject`s which are used by the [`UndergroundFeeder`](../foraging_patch/foraging_patch.md#undergroundfeeder) node to control the behaviour of the feeder hardware.

#### EnvironmentSubjectState

<!-- TODO / TOUNDERSTAND -->

### 'CameraSelector'

Some experimental branches of the aeon-experiments repository, specifically social0.4, include the 'CameraSelector' `GroupWorkflow`. 

The CameraSelector constructs a simple image visualiser using a custom C# `StreamSelector` node connected to `SubscribeSubject`s carrying images from each of the cameras and /or other informative images, e.g. a heatmap constructed from tracking animal positions. 

The `StreamSelector` has a single property, 'SelectedStream' which enables switching between these images for display. This property is externalised to the highest level of the workflow, meaning it is accessible via the [`ExperimentProperties`](./auxiliary_nodes/experiment_properties_GUI.md) node. This enables the user to select and switch to specific cameras or images during acquisition. 