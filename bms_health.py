from bms_constants import bms_thresholds
from bms_constants import bms_console_output_messages
import bms_system_configurator
from bms_constants import bms_controller_flags
from bms_constants import bms_hazard_warning_message
from bms_constants import bms_controller_output_messages


def collect_anomalies(anomaly, bms_parameter, bms_parameter_value, bms_parameter_range):
    bms_parameter_value = BMS_temperature_haldler(bms_parameter, bms_parameter_value)
    if bms_parameter_value < bms_parameter_range['min']:
        anomaly.append([bms_parameter, bms_console_output_messages[bms_system_configurator.system_language][1], 'low'])
    elif bms_parameter_value > bms_parameter_range['max']:
        anomaly.append([bms_parameter, bms_console_output_messages[bms_system_configurator.system_language][0], 'high'])


def bms_health_is_ok(status_report):
    anomalies = []
    for bms_parameter in status_report:
        collect_anomalies(anomalies, bms_parameter, status_report[bms_parameter], bms_thresholds[bms_parameter])
    BMS_console_output(anomalies)
    BMS_controller_output(anomalies)
    return anomalies


def BMS_console_output(anomalies):
    if len(anomalies) == 0:
        print(bms_console_output_messages[bms_system_configurator.system_language][2])
    else:
        print('------------------------- {} -------------------------'.format(
            bms_hazard_warning_message[bms_system_configurator.system_language]))
        for parameter in anomalies:
            print(bms_console_output_messages[bms_system_configurator.system_language][3] + '{} -> {}'.format(
                parameter[0], parameter[1]))
        print('-------------------------------------------------------')


def BMS_controller_output(anomalies):
    if len(anomalies) != 0:
        for parameter in anomalies:
            print(bms_controller_output_messages[bms_system_configurator.system_language][parameter[0]][
                      bms_controller_flags[parameter[2]]])


def BMS_temperature_haldler(bms_parameter, bms_parameter_value):
    if bms_parameter == 'temperature':
        return convert_to_celcius(bms_parameter_value)
    else:
        return bms_parameter_value


def convert_to_celcius(bms_parameter_value):
    if bms_system_configurator.system_temp_unit == 'F':
        return (bms_parameter_value - 32) * (5 / 9)
    else:
        return bms_parameter_value
