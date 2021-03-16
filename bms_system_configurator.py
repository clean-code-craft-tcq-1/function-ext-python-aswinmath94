from bms_constants import bms_system_languages
from bms_constants import bms_system_temperature_unit
from bms_constants import bms_system_temperature_unit_notification

def set_bms_system_language(language):
    global system_language
    if language in bms_system_languages:
        system_language = language
        print(bms_system_languages[system_language])
        return 1
    else:
        return 0


def set_bms_temperature_unit(temp_unit):
    global system_temp_unit
    if temp_unit in bms_system_temperature_unit:
        system_temp_unit = temp_unit
        print(bms_system_temperature_unit_notification[system_language],bms_system_temperature_unit[temp_unit])
        return 1
    else:
        return 0