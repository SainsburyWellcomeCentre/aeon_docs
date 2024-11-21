## <u>**PelletMonitor:**</u>

This node monitors the current state of pellet delivery commands and the beam break. 

![Aeon.Foraging.PelletMonitor](./Workflows/pelletMonitor.svg)
![Aeon.Foraging.PelletMonitorWorkflow](./Workflows/pelletMonitorWorkflow.svg)

## Inputs and Outputs:

**Inputs** - None 

**Outputs** - Sequence of dynamic class events triggered by deliver pellet commands and beam break events, consisting of a Timestamp (`double`) and a Value (`boolean`) that reports the current state. This Value is `True` if when a delivery command has been received, and `False` when a successful beam break is detected. 

## **Properties of the node:**

### ***Subject names:***
Set the names used for `Subjects` to identify the relevant events for a pellet monitor for a specific feeder.

## <u>Subjects</u>:

| Property Name         | Description                                              |
|----------------------|-----------------------------------------------------------|
| **PelletCommand** | The name of the shared `Subject` carrying all events published by the [output expander](https://github.com/harp-tech/device.outputexpander) connected to an [`UndergroundFeeder`](#undergroundfeeder-node). e.g. 'Patch1Events'  |
| **PelletDelivered**   | The name of the shared `Subject` carrying beam break events indicating successful pellet deliveries, e.g. 'Patch1PelletDelivered'. Also published in [`UndergroundFeeder`](#undergroundfeeder-node) |
