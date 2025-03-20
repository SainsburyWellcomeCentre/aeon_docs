(target-module-nest)=
# Nest
The nest module is utilised with a [nest](target-nest) hardware module assembly (consisting of a weighing scale) to provide shelter for animals in the arena and a means to track and measure their weight.

## Nodes
### WeightScale
The `WeightScale (Aeon.Environment)` node establishes a serial connection to the weighing scale in the nest, allowing direct control to read the weight, as well as to send tare commands to the scale. 
The node also processes the weight data from the scale to calculate a baseline weight that can be subtracted on a trigger. 
It also filters the weight signal with a linear regression filter over a sliding window defined in its [properties](#properties). 
Finally, a measure of confidence for each of these readings is calculated. 
<!-- TODO: link to API Reference -->
These measures are packaged into `Aeon.Environment.WeightMeasurement` class, each composed of the "Timestamp" (`double`), "Value" (`float`) and the "Confidence" index (`float`) of the weight measure. 

#### Inputs
None

#### Outputs
Stream of `DynamicClass` with the following attributes:
| Attribute name     | Type                           | Description                      |
|--------------------|--------------------------------|----------------------------------|
| **RawWeight.Value**           | `float`        | Raw weight measurement value from the scale                  |
| **RawWeight.Confidence**      | `float`        | Confidence score for the raw weight measurement              |
| **RawWeight.Timestamp**       | `double`     | Timestamp when the raw weight measurement was recorded       |
| **FilteredWeight.Value**      | `float`        | Filtered weight measurement after smoothing/filtering        |
| **FilteredWeight.Confidence** | `float`        | Confidence score for the filtered weight                     |
| **FilteredWeight.Timestamp**  | `double`     | Timestamp when the filtered weight measurement was recorded  |
| **BaselinedWeight.Value**     | `float`        | Baseline-adjusted weight measurement                         |
| **BaselinedWeight.Confidence**| `float`        | Confidence score for the baselined weight                    |
| **BaselinedWeight.Timestamp** | `double`     | Timestamp for the baselined weight measurement               |

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **PortName**               | Name of the serial port used to communicate with the digital scale                            |
| **FilterWindow**           | Defines the size of the sliding window for linear regression filtering of weight measurements |

##### Subjects
Events and commands from the weighing scale are collected from, and published to `Subject`s, in some cases after some processing. 
Here you set the names used for these `Subject`s to identify events, commands or data streams for this node for a specific nest. 
Each of these subjects becomes accessible in the Bonsai editor's toolbox anywhere in the workflow using the name set here.

###### Device event subjects
<!-- Do we need to specify the type for tare events, i.e. `Harp.Timestamped<type>`? -->
| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **WeightData**           | `Aeon.Environment.WeightMeasurement`| Contains timestamped weight measurements both raw and after filtering and baseline adjustments. Also directly output by the node |
| **TareEvents**           | `Harp.Timestamped`          | Timestamped tare events indicating tare commands sent to the scale |

###### Other output subjects
| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **RawWeight**            | `Aeon.Environment.WeightMeasurement`         | Raw weight data directly from the serial input                   |
| **FilteredWeight**       | `Aeon.Environment.WeightMeasurement`         | Filtered weight data based on the configured filter window size  |
| **BaselinedWeight**      | `Aeon.Environment.WeightMeasurement`         | Baseline-adjusted weight data                                    |

###### Device command subjects
| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **TareCommands**         | `object`             | Input sequence for tare commands, sent to reset the scale’s weight measurement                 |
| **GlobalTrigger**        | `object`             | A global trigger that synchronizes with external events or reset triggers for baseline weight. |
| **BaselineWeightTrigger**| `object`             | Specifies the trigger for resetting the baseline weight                                        |

#### Usage
Create a `Groupworkflow` and give it an appropriate name, e.g. "Nest". 
Inside, place a `WeightScale (Aeon.Environment)` node, externalise all properties, and connect to the `WorkflowOutput`.

:::workflow
![WeightScale](../../workflows/weightScale.bonsai)
:::

## GUI
No specific GUI components are defined for this module.

## Logging
Outputs from the nest module are collected and formatted into Harp messages using the `Harp.Format` and custom `FormatWeight` nodes to configure the register addresses for each data stream on a virtual Harp device, utilising commonly available registers. 
Logging of this virtual Harp device can then be performed as with any Harp device using the [`LogHarpState (Aeon.Acquisition)`](target-node-logharpstate) node.  

:::workflow
![logPatchEvents](../../workflows/logWeight.bonsai)
:::

**Data schema**

| Register name         | Access | Address | Type    | Mask type          | Description                                   |
|-----------------------|--------|---------|---------|--------------------|-----------------------------------------------|
| **(weight_raw)**         | Event  | 200     | `[double,float,float]` | [Timestamp,Value,Confidence] | Logs raw weight data directly from the scale input |
| **(weight_tare)**        | Write  | 201     | `U8`              |  -                              | Logs each tare command event with a timestamp      |
| **(weight_filtered)**    | Event  | 202     | `[double,float,float]` | [Timestamp,Value,Confidence] | Logs weight data after filtering adjustments       |
| **(weight_baseline)**    | Write  | 203     | `U8`              |  -                              | Logs events with a timestamp when the baseline weight is reset      |

## State persistence
Weight measurements are not required for environment state persistence.

## Alerts
Alerts are not currently configured for weight measurements, but could be configured to alert the team to, for example, drops in measured weight below a threshold for a given animal.