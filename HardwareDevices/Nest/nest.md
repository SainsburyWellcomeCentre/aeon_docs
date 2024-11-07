# Nest / weighing scale

## Device Configuration
 Create a `Groupworkflow` called 'Nest'. Inside, place a `WeightScale (Aeon.Acquisition)` node, externalise it's properties and connect to the `WorkflowOutput`:

 ![WeightScale](./Workflows/weightScale.svg)

This node establishes a serial connection to the weighing scale, allowing direct control to read the weight, as well as send tare commands to the scale. The weightScale device node also processes the weight data from the scale to calculate a baseline weight that can be subtracted on a trigger. The node also filters the weight signal with a linear regression filter over a sliding window defined in the [properties](#properties-of-the-node). Finally, a measure of confidence for each of these readings is calculated. These measures are packaged into `Aeon.Environment.WeightMeasurement` class, each composed of the `Harp.Timestamp`, `Value` and the `Confidence` index of the weight measure.

### Direct Inputs and Outputs:

**Inputs** - None

**Outputs** - Stream of `DynamicClass` with the following attributes:

| **Attribute**                 | **Type**       | **Description**                                              |
|-------------------------------|----------------|--------------------------------------------------------------|
| **RawWeight.Value**           | `float`        | Raw weight measurement value from the scale                  |
| **RawWeight.Confidence**      | `float`        | Confidence score for the raw weight measurement              |
| **RawWeight.Timestamp**       | `DateTime`     | Timestamp when the raw weight measurement was recorded       |
| **FilteredWeight.Value**      | `float`        | Filtered weight measurement after smoothing/filtering        |
| **FilteredWeight.Confidence** | `float`        | Confidence score for the filtered weight                     |
| **FilteredWeight.Timestamp**  | `DateTime`     | Timestamp when the filtered weight measurement was recorded  |
| **BaselinedWeight.Value**     | `float`        | Baseline-adjusted weight measurement                         |
| **BaselinedWeight.Confidence**| `float`        | Confidence score for the baselined weight                    |
| **BaselinedWeight.Timestamp** | `DateTime`     | Timestamp for the baselined weight measurement               |

## **Properties of the Node**

### General

| **Property**               | **Description**                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| **PortName**               | Name of the serial port used to communicate with the digital scale                            |
| **FilterWindow**           | Defines the size of the sliding window for linear regression filtering of weight measurements |

### ***Subject names:***
Events and commands from the scale are collected from, and published to `Subjects`, in some cases after some processing. Here you set the names used for these `Subjects` to identify events, commands or datastreams for this device. Device events subects become accessible in the bonsai editor's toolbox anywhere in the workflow using the name set here.

## **Subjects:**
### Device Events Subjects

| **Subject**              | **Type**                    | **Description**                                                              |
|--------------------------|-----------------------------|------------------------------------------------------------------------------|
| **WeightData**           | `Aeon.Environment.WeightMeasurement`| Contains timestamped weight measurements both raw and after filtering and baseline adjustments. Also directly output by the node |
| **TareEvents**           | `Harp.Timestamped`          | Timestamped tare events indicating tare commands sent to the scale |

#### Other Output Subjects

| **Subject**              | **Type**                    | **Description**                                                  |
|--------------------------|-----------------------------|------------------------------------------------------------------|
| **RawWeight**            | `Aeon.Environment.WeightMeasurement`         | Raw weight data directly from the serial input                   |
| **FilteredWeight**       | `Aeon.Environment.WeightMeasurement`         | Filtered weight data based on the configured filter window size  |
| **BaselinedWeight**      | `Aeon.Environment.WeightMeasurement`         | Baseline-adjusted weight data                                    |

### Device Command Subjects

| **Subject**              | **Type**             | **Description**                                                                                |
|--------------------------|----------------------|------------------------------------------------------------------------------------------------|
| **TareCommands**         | `object`             | Input sequence for tare commands, sent to reset the scale’s weight measurement                 |
| **GlobalTrigger**        | `object`             | A global trigger that synchronizes with external events or reset triggers for baseline weight. |
| **BaselineWeightTrigger**| `object`             | Specifies the trigger for resetting the baseline weight                                        |

## GUI

No specific GUI components are defined for this device.

## Logging

Outputs from the nest module are collected and formatted into harp messages using the `Harp.Format` and custom `FormatWeight` nodes to configure the register addresses for each data stream on a virtual harp device, utilising commonly available registers. Logging of this virtual harp device can then be performed as with any harp device using the  [`LogHarpState (Aeon.Acquisition)`](../../Logging/LogHarpState.md) node.  

![logPatchEvents](./Workflows/logWeight.svg)

*Data Schema*:

| Register Name         | Access | Address | Type              | Mask Type / attributes         | Description                                         |
|-----------------------|--------|---------|-------------------|--------------------------------|-----------------------------------------------------|
| **(weight_raw)**         | Event  | 200     | `[double,float,float]` | [Timestamp,Value,Confidence] | Logs raw weight data directly from the scale input |
| **(weight_tare)**        | Write  | 201     | `U8`              |  -                              | Logs each tare command event with a timestamp      |
| **(weight_filtered)**    | Event  | 202     | `[double,float,float]` | [Timestamp,Value,Confidence] | Logs weight data after filtering adjustments       |
| **(weight_baseline)**    | Write  | 203     | `U8`              |  -                              | Logs events with a timestamp when the baseline weight is reset      |

## State Persistence

Weight measurements are not required for environment state persistence

## Alerts

Weight measurements are currently not configured for alerts, though one could configure alert messages to alert the team to, for example, drops in measured weight below a threshold for a given animal.
