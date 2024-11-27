## <u>**Patch Dispenser:**</u>

This module keeps track of the number of pellets available to the feeder. It accepts pellet discount notifications triggered by the IR beam break following successful pellet delivery, and discounts these from the total number of pellets, which is itself set manually when loading the feeder hopper.

### **Device configuration**

 Place a `SubscribeSubject` and point it to the 'PelletDelivered' `Subject` for your patch (e.g. 'Patch1PelletDelivered'). Connect this to a `Condition` node that checks the `Value` of the incoming subject. This is a `Boolean` that reports `True` on pellet delivery, and ensures only the rising edge of this signal is counted as a delivery. Finally, connect this to an `Aeon.Foraging.PatchDispenser` node:

![Aeon.Foraging.PatchDispenser](./Workflows/patchDispenser.svg)

## Inputs and Outputs:

**Inputs** - `Harp.Timestamped<bool>`. Events emitted by the `UndergroundFeederModule` indicating pellet delivery. 

**Outputs** - Stream of custom class `Aeon.Foraging.DispenserEventArgs`. Each item emitted consists of a 'Value' (`int`) corresponding to the pellet count following an event, and an 'EventType' (`Aeon.Foraging.DispenserEventType`) describing the reason for the new pellet count, i.e. due to a triggered 'Discount', or 'Reset' or 'Refill' command from the [control panel](../../GUI/controlPanel.md).

## **Properties of the node:**

### ***General:***

| Property Name | Description                                           |
|---------------|-------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module. e.g. 'Patch1' |

### ***Subject names:***
Set the names used for these subjects to identify the events and commands for a dispenser node for a specific feeder.

## <u>Subjects</u>:

| Subject Name          | Type                    | Description                                                         |
|----------------------|-----------------------------------------------------------|
| **ControllerEvents** | `Aeon.Foraging.DispenserEventArgs` | Controller events shared `Subject`, carrying the number of pellets remaining (`int`) and the `EventType`. Also output directly by the node. |
| **DispenserState** |   | Declared `StateRecoverySubject` to store the current number of pellets. |

---