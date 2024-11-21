## <u>**Patch Dispenser:**</u>
![Aeon.Foraging.PatchDispenser](./Workflows/patchDispenser.svg)

This module keeps track of the number of pellets available to the feeder. It accepts pellet discount notifications triggered by the IR beam break following successful pellet delivery, and discounts these from the total number of pellets, which is itself set manually when loading the feeder hopper.

## Inputs and Outputs:

**Inputs** - `Harp.Timestamped<bool>`. Events emitted by the `UndergroundFeederModule` indicating pellet delivery. 

**Outputs** - Stream of custom class `Aeon.Foraging.DispenserEventArgs`. Each item emitted consists of a 'Value' (`int`) corresponding to the pellet count following an event, and an 'EventType' (`Aeon.Foraging.DispenserEventType`) describing the reason for the new pellet count, i.e. due to a 'Discount', 'Reset' or 'Refill' command.

## **Properties of the node:**

### ***General:***

| Property Name | Description                                           |
|---------------|-------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module. e.g. 'Patch1' |

### ***Subject names:***
Set the names used for these subjects to identify the events and commands for a dispenser node for a specific feeder. Each of these subjects is published and become accessible in the bonsai editor's toolbox anywhere in the workflow using this name.

## <u>Subjects</u>:

| Property Name         | Description                                              |
|----------------------|-----------------------------------------------------------|
| **ControllerEvents** | Controller events shared `Subject`. Also output directly by the node. |
| **DispenserState**   | Declared `StateRecoverySubject` to store the dispenser state in th event of workflow failure. |

---