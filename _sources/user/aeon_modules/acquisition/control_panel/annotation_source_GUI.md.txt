(target-node-annotationsource)=
# AnnotationSource
The `AnnotationSource (Aeon.Environment)` node is a custom node designed to allow manual text input to be logged as an annotation or sent as an alert.

![AnnotationSourceGUI](../../../../images/annotation_source.svg){align=center}

1. **Text box**: Accepts manual text input to be logged as an annotation or alert.
2. **Annotation**: Button to [log](target-node-formatlogmessage) the text input to the message log at the Notification level.
3. **Alert**: Button to log the text input to the message [log](target-node-formatlogmessage) at the Alert level and [send](target-node-sendalert) the alert.