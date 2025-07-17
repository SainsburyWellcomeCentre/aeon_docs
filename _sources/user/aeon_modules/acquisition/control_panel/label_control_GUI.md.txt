(target-node-labelcontrol)=
# LabelControl
The `LabelControl (Aeon.Environment)` node creates a text box visualiser and populates it with the string representation of its input sequence. 
This can be used to display various experimental parameters and states in a custom visualiser and control panel. 

![LabelControlGUI](../../../../images/label_control.svg){align=center}

In Aeon, this node is used to display the current environmental and experimental parameters, including:
- The name of the chosen environment YAML file that defines the experimental logic and parameters, e.g. "EnvironmentRandom".
- Information about the current experimental block, including the block number, number of delivered pellets, threshold and timeout parameters.
- Information about all foraging patches in the habitat, including the current depletion rate, delta, and threshold.