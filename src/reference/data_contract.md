(target-data-schema)=
# Data Schema

**Version**: 0.2.0-draft

## Devices

### VideoController

  * harp data: `<name>_address.bin [HARP]`
    | name       | address | payload   | attributes | description |
    | ---------- | ------- | --------- | ---------- | ----------- |
    | `pwm_enable` | `39` | `uint16` | bitmask | specifies which PWM has been enabled |
    | `pwm1_freq` | `50` | `float32` | frequency | the frequency of PWM1 (max: 1000Hz) |
    | `pwm1_dutycycle` | `51` | `float32` | dutycycle | the duty cycle of PWM1 (max: 100%) |
    | `pwm1_mode` | `55` | `uint8` | mode | should always be 0 (infinite) |
    | `pwm1_trig` | `56` | `uint8` | start_trigger | should always be 0 (software trigger) |
    | `pwm1_conf_event` | `57` | `uint8` | rise_event | should always be 1 (enabled) |
    | `pwm2_freq` | `58` | `float32` | frequency | the frequency of PWM1 (max: 1000Hz) |
    | `pwm2_dutycycle` | `59` | `float32` | dutycycle | the duty cycle of PWM1 (max: 100%) |
    | `pwm2_mode` | `63` | `uint8` | mode | should always be 0 (infinite) |
    | `pwm2_trig` | `64` | `uint8` | start_trigger | should always be 0 (software trigger) |
    | `pwm2_conf_event` | `65` | `uint8` | rise_event | should always be 1 (enabled) |
    | `pwm_start` | `66` | `uint8` | bitmask | specifies which PWM has started |
    | `pwm_stop` | `67` | `uint8` | bitmask | specifies which PWM has stopped |
    | `pwm_rise_event` | `68` | `uint8` | bitmask | specifies which PWM has been triggered |


### VideoSource

  * video frames: `<name>.avi [FMP4 codec]`
  * video metadata: `<name>.csv [CSV]`
    | time      | hw_counter | hw_timestamp |
    | --------- | ---------- | ------------ |
    | `float64` | `int64`    | `int64`      |

  * (optional) harp data: `<name>_address.bin [HARP]`
    | name       | address | payload   | attributes | description |
    | ---------- | ------- | --------- | ---------- | ----------- |
    | `position` | `200`   | `float32` | [x, y, angle, major, minor, area, id] | one entry for each animal, for each frame |
    | `region` | `201`   | `uint8` | area code | one entry for each animal, for each frame |

  * area code map:
    | name     | code |
    | -------- | ---- |
    | none     | 0    |
    | nest     | 1    |
    | corridor | 2    |
    | arena    | 3    |
    | patch1   | 4    |
    | patch2   | 5    |


### AudioSource

  * audio buffers: `<name>.wav [PCM 16-bit mono]`
  * audio metadata: `MISSING`

### PatchController

  * patch state: `<name>_State.csv [CSV]`
    | time      | threshold  | d1        | delta     |
    | --------- | ---------- | ----------| --------- |
    | `float64` | `float64`  | `float64` | `float64` |

  * harp data: `<name>_address.bin [HARP]`
    | name       | address | payload   | attributes | description |
    | ---------- | ------- | --------- | ---------- | ----------- |
    | `beam_break` | `32` | `uint8` | bitmask | the current state of the beam break |
    | `delivery_set` | `35` | `uint8` | bitmask | a pellet delivery has been requested |
    | `delivery_clear` | `36` | `uint8` | bitmask | the pellet delivery pin has been cleared |
    | `expansion_board` | `87` | `uint8` | expansion | the type of board in the expansion port |
    | `encoder_read` | `90` | `uint16` | [angle, intensity] | the current state of the magnetic encoder |
    | `encoder_mode` | `91` | `uint8` | mode | should always be 4 (500Hz) |
    | `dispenser_state` | `200` | `float32` | value | the estimated number of pellets in the dispenser |
    | `delivery_manual` | `201` | `uint8` | event | a manual pellet delivery has been requested |
    | `missed_pellet` | `202` | `uint8` | event | a pellet has been missed |
    | `delivery_retry`  | `203` | `uint8` | bitmask | a pellet delivery command has been retried |

### WeightScale

  * harp data: `<name>_address.bin [HARP]`
    | name       | address | payload   | attributes | description |
    | ---------- | ------- | --------- | ---------- | ----------- |
    | `weight_raw` | `200` | `float32` | [value, stable] | the raw weight samples (g) |
    | `weight_tare` | `201` | `uint8` | event | a tare command has been sent |
    | `weight_filtered` | `202` | `float32` | [value, stable] | filtered weight samples (`stable` is slope of regression) |
    | `weight_baseline` | `203` | `uint8` | event | a baseline has been taken |
    | `weight_subject` | `204` | `float32` | [value, stable] | the stable baselined weight of a subject in the nest (g) |

### ExperimentalMetadata

  * environment state: `<name>_EnvironmentState.csv [CSV]`
    | time      | type                       |
    | --------- | -------------------------- |
    | `float64` | `Maintenance \ Experiment` |

  * subject state: `<name>_SubjectState.csv [CSV]`
    | time      | id         | weight    | event |
    | --------- | ---------- | ----------| ----- |
    | `float64` | `str`      | `float64` | `str` |

  * subject visits: `<name>_SubjectVisits.csv [CSV]`
    | time      | id         | event | area  |
    | --------- | ---------- | ----- | ----- |
    | `float64` | `str`      | `Enter \ Exit` | `str` |

  * message log: `<name>_MessageLog.csv [CSV]`
    | time      | priority   | type      | message   |
    | --------- | ---------- | ----------| --------- |
    | `float64` | `Notification \ Alert`  | `str`     | `TSV str` |