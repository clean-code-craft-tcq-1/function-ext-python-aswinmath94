from bms_health import bms_health_is_ok
from input_validator import bms_parameter_name_validation
from input_validator import bms_parameter_value_validation
from bms_system_configurator import set_bms_system_language
from bms_system_configurator import set_bms_temperature_unit

if __name__ == '__main__':

    assert (set_bms_system_language('en') == 1)
    assert (set_bms_system_language('hindi') == 0)
    assert (set_bms_temperature_unit('C') == 1)
    assert (set_bms_temperature_unit('Kelvin') == 0)



    set_bms_system_language('en')
    assert (bms_parameter_name_validation({'bms_temperature': 40, 'soc': 40, 'charging_rate': 0.8}) == 'UNKNOWN PARAMETER')
    assert (bms_parameter_name_validation({'temperature': 40, 'soc': 40, 'charging_rate': 0.6}) == 'OK')
    assert (bms_parameter_value_validation({'temperature': 'nan', 'soc': 40, 'charging_rate': 0.8}) == 'INVALID PARAMETER VALUE')
    assert (bms_parameter_value_validation({'temperature': 40, 'soc': '', 'charging_rate': 0.8}) == 'INVALID PARAMETER VALUE')
    assert (bms_parameter_value_validation({'temperature': 40, 'soc': 40, 'charging_rate': 'unknown'}) == 'INVALID PARAMETER VALUE')
    assert (len(bms_health_is_ok({'temperature': 40, 'soc': 40, 'charging_rate': 0.6})) == 0)
    assert (len(bms_health_is_ok({'temperature': 100, 'soc': 40, 'charging_rate': 0.8})) > 0)
    assert (len(bms_health_is_ok({'temperature': -40, 'soc': 40, 'charging_rate': 0.8})) > 0)

    set_bms_system_language('de')
    assert (bms_parameter_name_validation({'bms_temperature': 40, 'soc': 40, 'charging_rate': 0.8}) == 'UNBEKANNTER PARAMETER')
    assert (bms_parameter_name_validation({'temperature': 40, 'soc': 40, 'charging_rate': 0.6}) == 'OK')
    assert (bms_parameter_value_validation({'temperature': 'nan', 'soc': 40, 'charging_rate': 0.8}) == 'UNGÜLTIGER PARAMETERWERT')
    assert (bms_parameter_value_validation({'temperature': 40, 'soc': '', 'charging_rate': 0.8}) == 'UNGÜLTIGER PARAMETERWERT')
    assert (bms_parameter_value_validation({'temperature': 40, 'soc': 40 , 'charging_rate': 'unknown'}) == 'UNGÜLTIGER PARAMETERWERT')
    assert (bms_parameter_name_validation({'temperature': 40, 'soc': 40, 'charging_rate': 0.6}) == 'OK')
    assert (len(bms_health_is_ok({'temperature': 40, 'soc': 40, 'charging_rate': 0.6})) == 0)
    assert (len(bms_health_is_ok({'temperature': 100, 'soc': 40, 'charging_rate': 0.8})) > 0)
    assert (len(bms_health_is_ok({'temperature': -40, 'soc': 40, 'charging_rate': 0.8})) > 0)

    set_bms_system_language('en')
    set_bms_temperature_unit('C')
    assert (len(bms_health_is_ok({'temperature': 40, 'soc': 40, 'charging_rate': 0.6})) == 0)
    assert (len(bms_health_is_ok({'temperature': 100, 'soc': 40, 'charging_rate': 0.8})) > 0)
    assert (len(bms_health_is_ok({'temperature': -40, 'soc': 40, 'charging_rate': 0.8})) > 0)

    set_bms_system_language('de')
    set_bms_temperature_unit('F')
    assert (len(bms_health_is_ok({'temperature': 40, 'soc': 40, 'charging_rate': 0.6})) == 0)
    assert (len(bms_health_is_ok({'temperature': 100, 'soc': 40, 'charging_rate': 0.8})) == 0)
    assert (len(bms_health_is_ok({'temperature': -40, 'soc': 40, 'charging_rate': 0.8})) > 0)
