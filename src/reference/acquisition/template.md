(target-module-device-name)=
# [Template] Device Name

A brief description of the device functionality and usage, and nodes involved. 

## Nodes
### Device node 
A brief description of what the node does.

#### Inputs
#### Outputs
A sequence of `<type>` with the following attributes. 
| Attribute name     | Type                           | Description                      |
|--------------------|--------------------------------|----------------------------------|
| **Attr1**          | `Type`                         | Description of Attr1             |
| **Attr2**          | `Type`                         | Description of Attr2             |

#### Properties
##### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Property1** | Description of Property1                                  |
| **Property2** | Description of Property2                                  |

##### Other option category or function
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **Option1**   | Description of Option1                        |
| **Option2**   | Description of Option2                        |

##### Subjects
An overview of the events and commands available or published to `Subject`s

###### Device event subjects
`HarpMessage` events emitted to a `Subject`

| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **Event1**        | `Type`      | Description of Event1         |
| **Event2**        | `Type`      | Description of Event2         |

###### Other output subjects
Other subjects published or updated by the node, usually ater some processing

| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **Output1**       | `Type`        | Description of Output1                                                                          |
| **Output2**       | `Type`        | Description of Output2                                                                          |

###### Device command subjects
Existing subjects published outside of the node, but used for input / trigger

| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **Command1**      | `Type`        | Description of Command1                                                                         |
| **Command2**      | `Type`        | Description of Command2                                                                         |

#### Usage
Instructions for creating and configuring the main device node. Add necessary sub-components and configurations.

![InsertWorkflow](path/to/workflow.svg)

## GUI
Description of any user interface components and visualisers.

## Logging
Information on logging functionalities, nodes involved, and schemas for recorded data.

**Data schema**

| Register name         | Access | Address | Type    | Mask type          | Description                                   |
|-----------------------|--------|---------|---------|--------------------|-----------------------------------------------|
| **Register1**         | Access | Address | `Type`  | Mask               | Description of Register1                      |
| **Register2**         | Access | Address | `Type`  | Mask               | Description of Register2                      |

(For not virtual harp devices) a full list of the available registers for the `device name` see the corresponding [device.yml](link-to-harprepo-device.yml)

## State persistence
Information on state recovery or persistence requirements, if applicable.

## Alerts
Explanation of any alert configurations and links to guides or further configuration steps.