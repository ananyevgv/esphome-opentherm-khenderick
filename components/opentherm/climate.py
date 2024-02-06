from symbol import import_as_name
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, sensor
from esphome import pins, core
from esphome.const import (
    CONF_ID,
)
from esphome.core import coroutine_with_priority
from esphome.cpp_generator import RawExpression
import logging

from . import opentherm_component_schema, set_hotwater_climate, set_heatingwater_climate

DEPENDENCIES = ["opentherm"]

_LOGGER = logging.getLogger(__name__)

CONF_CH_WATER = "ch_water"
CONF_CH2_WATER = "ch_water"
CONF_DHW_WATER = "dhw_water"

opentherm_ns = cg.esphome_ns.namespace("opentherm")
OpenThermClimate = opentherm_ns.class_("OpenthermClimate", climate.Climate, cg.Component)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.Optional(CONF_CH_WATER): climate.CLIMATE_SCHEMA.extend(
                {
                    cv.GenerateID(): cv.declare_id(OpenThermClimate),
                }
            ).extend(opentherm_component_schema())
            .extend(cv.COMPONENT_SCHEMA),
            cv.Optional(CONF_CH2_WATER): climate.CLIMATE_SCHEMA.extend(
                {
                    cv.GenerateID(): cv.declare_id(OpenThermClimate),
                }
            ).extend(opentherm_component_schema())
            .extend(cv.COMPONENT_SCHEMA),
            cv.Optional(CONF_DHW_WATER): climate.CLIMATE_SCHEMA.extend(
                {
                    cv.GenerateID(): cv.declare_id(OpenThermClimate),
                }
            ).extend(opentherm_component_schema())
            .extend(cv.COMPONENT_SCHEMA),
        }
    )
    .extend(opentherm_component_schema())
    .extend(cv.COMPONENT_SCHEMA)
)


@coroutine_with_priority(1.0)
async def to_code(config):

    _LOGGER.info("to_code: %s", config)


    if CONF_CH_WATER in config:
        hotwater_climate = cg.new_Pvariable(config[CONF_CH_WATER][CONF_ID])
        await cg.register_component(chwater_climate, config[CONF_CH_WATER])
        await climate.register_climate(chwater_climate, config[CONF_CH_WATER])
        await set_chwater_climate(chwater_climate, config[CONF_CH_WATER])
    if CONF_CH2_WATER in config:
        hotwater_climate = cg.new_Pvariable(config[CONF_CH2_WATER][CONF_ID])
        await cg.register_component(ch2water_climate, config[CONF_CH2_WATER])
        await climate.register_climate(ch2water_climate, config[CONF_CH2_WATER])
        await set_ch2water_climate(ch2water_climate, config[CONF_CH2_WATER])
    
    if CONF_DHW_WATER in config:
        heatingwater_climate = cg.new_Pvariable(config[CONF_DHW_WATER][CONF_ID])
        await cg.register_component(dhwwater_climate, config[CONF_DHW_WATER])
        await climate.register_climate(dhwwater_climate, config[CONF_DHW_WATER])
        await set_dhw_climate(dhwwater_climate, config[CONF_DHW_WATER])
