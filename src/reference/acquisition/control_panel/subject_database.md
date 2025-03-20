(target-node-subjectdatabase)=
# SubjectDatabase <!--TODO: Placeholder content-->
The `SubjectDatabase (...)` node ...

## Inputs
## Outputs
A sequence of `<type>` with the following attributes. 
| Attribute name     | Type                           | Description                      |
|--------------------|--------------------------------|----------------------------------|
| **Attr1**          | `Type`                         | Description of Attr1             |
| **Attr2**          | `Type`                         | Description of Attr2             |

## Properties
### General
| Property name | Description                                               |
|---------------|-----------------------------------------------------------|
| **Property1** | Description of Property1                                  |
| **Property2** | Description of Property2                                  |

### Other option category or function
| Property name | Description                                   |
|---------------|-----------------------------------------------|
| **Option1**   | Description of Option1                        |
| **Option2**   | Description of Option2                        |

### Subjects
An overview of the events and commands available or published to `Subject`s

#### Device event subjects
`HarpMessage` events emitted to a `Subject`

| Subject name      | Type        | Description                   |
|-------------------|-------------|-------------------------------|
| **Event1**        | `Type`      | Description of Event1         |
| **Event2**        | `Type`      | Description of Event2         |

#### Other output subjects
Other subjects published or updated by the node, usually ater some processing

| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **Output1**       | `Type`        | Description of Output1                                                                          |
| **Output2**       | `Type`        | Description of Output2                                                                          |

#### Device command subjects
Existing subjects published outside of the node, but used for input / trigger

| Subject name      | Type          | Description                                                                                     |
|-------------------|---------------|-------------------------------------------------------------------------------------------------|
| **Command1**      | `Type`        | Description of Command1                                                                         |
| **Command2**      | `Type`        | Description of Command2                                                                         |

## Usage
Instructions for creating and configuring the main device node. Add necessary sub-components and configurations.

::workflow
![InsertWorkflow](path/to/workflow.bonsai)
:::