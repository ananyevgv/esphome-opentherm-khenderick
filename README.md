# What does this implement?

This component provides support for opentherm BAXI NUVOLA-3 B-40 such as:
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



web_server:
  port: 80
  auth:
    username: !secret web_user
    password: !secret web_pass 
```
