(target-node-buttonsource)=
# ButtonSource
The `ButtonSource (Aeon.Environment)` node creates a single labelled button in its visualiser and produces an observable sequence of `Harp.Timestamped<string>` when the button is pressed. 
This sequence is typically cast to a shared `Subject`, with subscriptions elsewhere in the workflow that determine how the button's press affect control, acquisition, or experiment logic.