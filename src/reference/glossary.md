(target-glossary)=
# Glossary

This glossary provides definitions for terms used throughout the project documentation.

:::{glossary}

Acquisition Chunk
    The event (i.e. all data) over a particular {term}`acquisition chunk duration`.

Acquisition Chunk Duration
    The time duration over which datastream files are written out. For experiment 0.1, datastreams were written out in files of 1 hour chunk durations.

Acquisition Epoch
    The event over the time period when the acquistion computer is on and acquiring data until it is stopped. For experiment 0.1 there are multiple acquisition runs due to Bonsai/Windows being restarted.

Acquisition Slice
    The event (i.e. all data) over a particular {term}`acquisition slice duration`.

Acquisition Slice Duration
    The minimum time resolution a user can get from an initial query of a Datajoint table (the timebin size of BLOB and QC data stored in Datajoint tables). For experiment 0.1 this was 10 minutes.

Aeon
    A very long, indefinite period of time. [^1]

Block
    A specific period of time, typically lasting around 3 hours, during which the reward rate for each `streams.UndergroundFeeder` (food patch) is manipulated to encourage different behaviours in the subjects.

Place
    A specific location subjects can visit within the Aeon habitat, e.g. environment, nest, arena, food patch.

Session
    For experiment 0.1, the event over the time period when an animal is placed in the nesting cage until the time the animal is removed from the nesting cage.

Task Protocol
    An integer number and associated string describing a unique behavioral task run in Project Aeon. For experiment 0.1, there were 8 unique behavioral tasks run.

Trial
    For experiment 0.1, the event over the time period when an animal starts moving the wheel on a patch until the time a pellet is delivered. Every experiment 0.1 {term}`session` ends on incompleted trials.

Visit
    A period of time during which a subject remains at a {term}`place`.
:::

[^1]: https://en.wikipedia.org/wiki/Aeon