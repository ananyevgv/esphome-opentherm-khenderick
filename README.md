# What does this implement?

This component provides support for opentherm devices such as:
* [DIYLess](https://diyless.com/)' Master OpenTherm Shield
* [Ihor Melnyk](http://ihormelnyk.com/opentherm_adapter)' OpenTherm adapter

Those are typically connected to an ESP8266 or ESP32

The functional aspect (OpenTherm communications) is heavily based on [ihormelnyk/opentherm_library](https://github.com/ihormelnyk/opentherm_library).

The goal of this component is not to provide a full-blown climate device, but rather expose a
bunch of OpenTherm data and functionality. To make use of this data and functionality is up to the user. 
This could be by - for example - using the exposed enities in ESPHome/HA automations or by using the 
exposed entities in other components (e.g. a combination of [PID Climate](https://esphome.io/components/climate/pid.html)
and a few [Template Outputs](https://esphome.io/components/output/template.html))

As this is my first component, I'm also looking for constructive criticism on how to enhance this
component where needed.

## Note

This component is currently also in an [open PR to esphome](https://github.com/esphome/esphome/pull/3921),
but has currently a low chance of acceptance since it uses a ~32ms delay in `loop()`. This should be
rewritten to work async.

Feel free to help me out and open a PR with improvements.

## Example entry for `config.yaml`:

Note that the connected boiler might not support all sensors. If warnings are reported about unknown messages
it usually means that the related sensor isn't supported. In that case, just remove that sensor from the config.

```yaml
external_components:
  source: github://khenderick/esphome-opentherm
  components: [opentherm]

opentherm:
  read_pin: 21
  write_pin: 22

sensor:
  - platform: opentherm
    ch_min_temperature:
      name: "CH minimum temperature"
    ch_max_temperature:
      name: "CH maximum temperature"
    dhw_min_temperature:
      name: "DHW minimum temperature"
    dhw_max_temperature:
      name: "DHW maximum temperature"
    dhw_flow_rate:
      name: "DHW flow rate"
    pressure:
      name: "pressure"
    modulation:
      name: "modulation"
    dhw_temperature:
      name: "DHW temperature"
    dhw_2_temperature:
      name: "DHW 2 temperature"
    boiler_temperature:
      name: "boiler temperature"
    boiler_2_temperature:
      name: "boiler 2 temperature"
    return_temperature:
      name: "return temperature"
    outside_temperature:
      name: "outside temperature"
    exhaust_temperature:
      name: "exhaust temperature"
    oem_error_code:
      name: "OEM error code"
    oem_diagnostic_code:
      name: "OEM diagnostic code"
    burner_starts:
      name: "burner starts"
    burner_ops_hours:
      name: "burner operation hours"
    ch_pump_starts:
      name: "CH pump starts"
    ch_pump_ops_hours:
      name: "CH pump operation hours"
    dhw_pump_valve_starts:
      name: "DHW pump/valve starts"
    dhw_pump_valve_ops_hours:
      name: "DHW pump/valve operation hours"
    dhw_burner_starts:
      name: "DHW burner starts"
    dhw_burner_ops_hours:
      name: "DHW burner operation hours"
    boiler_member_id:
      name: "Boiler member ID"

binary_sensor:
  - platform: opentherm
    ch_active:
      name: "CH active"
    ch_2_active:
      name: "CH 2 active"
    dhw_active:
      name: "DHW active"
    flame_active:
      name: "flame active"
    fault:
      name: "fault"
    diagnostic:
      name: "diagnostic"
    service_request:
      name: "service request"
    lockout_reset:
      name: "lockout reset"
    water_pressure_fault:
      name: "water pressure fault"
    gas_flame_fault:
      name: "gas/flame fault"
    air_pressure_fault:
      name: "air pressure fault"
    water_over_temperature_fault:
      name: "water over temperature fault"
    dhw_present:
      name: "DHW present (= true, not present = false)"
    modulating:
      name: "boiler uses modulation (= true, on/off = false)"
    cooling_supported:
      name: "cooling supported (= true, unsupported = false)"
    dhw_storage_tank:
      name: "DHW storage tank (= true, instantaneous/unsupported = false)"
    device_lowoff_pump_control:
      name: "device low-off/pump control allowed (= true, not allowed = false)"
    ch_2_present:
      name: "CH 2 present (= true, not present = false)"
    otc_ratio_max:
      name: "otc ratio max"
    otc_ratio_min:
      name: "otc ratio min"

switch:
  - platform: opentherm
    ch_enabled:
      name: "CH enabled"
    ch_2_enabled:
      name: "CH 2 enabled"
    dhw_enabled:
      name: "DHW enabled"
    otc_active:
      name: "OTC active"

number:
  - platform: opentherm
    ch_setpoint_temperature:
      name: "CH setpoint temperature"
      min_value: 20.0
      max_value: 45.0
      step: 0.5
      restore_value: true
    ch_2_setpoint_temperature:
      name: "CH 2 setpoint temperature"
      min_value: 20.0
      max_value: 45.0
      step: 0.5
      restore_value: true
    dhw_setpoint_temperature:
      name: "DHW setpoint temperature"
      min_value: 38.0
      max_value: 60.0
      step: 0.5
      restore_value: true
    max_ch_setpoint_temperature:
      name: "Max CH setpoint temperature"
      min_value: 0.0
      max_value: 100.0
      step: 0.5
      restore_value: true
    max_modulation:
      name: "Max modulation level"
      min_value: 0.0
      max_value: 100.0
      step: 0.5
      restore_value: true
    otc_set_ratio:
      name: "${last_name} OTC set ratio"
      step: 1
      min_value: 0.0
      max_value: 60.0
      restore_value: true

button:
  - platform: opentherm
    boiler_lo_reset:
      name: "Boiler lock-out reset"
    ch_water_filling:
      name: "CH water filling"
```
