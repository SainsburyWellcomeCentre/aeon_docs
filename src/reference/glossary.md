(target-glossary)=
# Glossary

This glossary provides definitions for terms used throughout the project documentation.

:::{glossary}

Aeon
    A very long, indefinite period of time. [^1]

Session
    For experiment 0.1, the event over the time period when an animal is placed in the nesting cage until the time the animal is removed from the nesting cage.

Trial
    For experiment 0.1, the event over the time period when an animal starts moving the wheel on a patch until the time a pellet is delivered. Every experiment 0.1 {term}`session` ends on incompleted trials.

Acquisition Epoch
    The event over the time period when the acquistion computer is on and acquiring data until it is stopped. For experiment 0.1 there are multiple acquisition runs due to Bonsai/Windows being restarted.

Acquisition Chunk Duration
    The time duration over which datastream files are written out. For experiment 0.1, data streams were written out in files of 1 hour chunk durations.

Acquisition Chunk
    The event (i.e. all data) over a particular {term}`acquisition chunk duration`.

Acquisition Slice Duration
    The minimum time resolution a user can get from an initial query of a Datajoint table (the timebin size of BLOB and QC data stored in Datajoint tables). For experiment 0.1 this was 10 minutes.

Acquisition Slice
    The event (i.e. all data) over a particular {term}`acquisition slice duration`.

Task Protocol
    An integer number and associated string describing a unique behavioural task run in Project Aeon. For experiment 0.1, there were 8 unique behavioural tasks run.

:::

[^1]: https://en.wikipedia.org/wiki/Aeon