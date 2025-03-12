The `EnvironmentState (Aeon.Environment)` node is a special case of a labelled button, operating similarly to `ButtonSource`, but returning an observable sequence of type `Aeon.Environment.EnvironmentStateMetadata`, which details the name and type of experimental environments or paradigms. The visualiser for this node provides a single, labelled button to toggle between named 'Environment States'. In Aeon this is used to switch between 'Maintenance' and 'Experiment' states.

![EnvironmentStateGUI](../../../../images/Environment_state.svg)

The node itself generates an observable sequence reflecting changes in this state, i.e. when the button is clicked. In Aeon experiments, this state is broadcast through a shared `Subject`.

This is subscribed to in several places in the experiment logic workflow to log state changes with the data, and to effect this state change by altering parameters and logic, and can be readily used to alter hardware behaviour.