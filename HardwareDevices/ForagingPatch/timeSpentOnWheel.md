## <u>**TimeSpentOnWheel:**</u>

This node monitors the motion of a given foraging wheel and accumulates the total time the subject is actively turning the wheel. In Project Aeon, a `RepeatEveryBlock (Aeon.Acquisition)`(./RepeatEveryBlock.md) node is used here to reset the monitor after a block transition, before passing the result to a `BehaviorSubject` named appropriately.

<!--
:::workflow
![timeSpentOnWheel]($Workflows/timeSpentOnWheel.bonsai)
:::
-->

![timeSpentOnWheel](./Workflows/timeSpentOnWheel.svg) <!-- remove these and replace with bonsai workflow from PR https://github.com/SainsburyWellcomeCentre/aeon_docs/pull/80 -->

![timeSpentOnWheelWorkflow](./Workflows/timeSpentOnWheelWorkflow.svg)

Within the `TimeSpentOnWheel` node, the [`WheelMoving (Aeon.Acquisition)`](./WheelMoving.md) node reports whether the wheel is in motion or not, and accumulates the differences between timestamps emitted by the feeder while the wheel is in motion.

## Inputs and Outputs:

**Inputs** - None

**Outputs** - 

## **Properties of the node:**

### ***General:***

| Property Name | Description                                           |
|---------------|-------------------------------------------------------|
| **Name**      | Set the name to identify this specific dispenser module. e.g. 'Patch1' |

### ***Subject names:***
Set the names used for `Subjects` to identify the relevant events for a pellet monitor for a specific feeder.

## <u>Subjects</u>:

| Property Name         | Description                                              |
|----------------------|-----------------------------------------------------------|
| **** |  |
| ****   |  |