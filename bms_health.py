from bms_constants import bms_thresholds
from bms_constants import bms_input_param_range_status
import bms_system_configurator


def collect_anomalies(anomaly, bms_parameter, bms_parameter_value, bms_parameter_range):
    bms_parameter_value = BMS_temperature_haldler(bms_parameter,bms_parameter_value)
    if bms_parameter_value < bms_parameter_range['min']:
        anomaly.append([bms_parameter, bms_input_param_range_status[bms_system_configurator.system_language][1]])
    elif bms_parameter_value > bms_parameter_range['max']:
        anomaly.append([bms_parameter, bms_input_param_range_status[bms_system_configurator.system_language][0]])


def bms_health_is_ok(status_report):
    anomalies = []
    for bms_parameter in status_report:
        collect_anomalies(anomalies, bms_parameter, status_report[bms_parameter], bms_thresholds[bms_parameter])
    bms_breach_param(anomalies)
    return anomalies


def bms_breach_param(anomalies):
    if len(anomalies) == 0:
        print(bms_input_param_range_status[bms_system_configurator.system_language][2])
    else:
        for parameter in anomalies:
            print(bms_input_param_range_status[bms_system_configurator.system_language][3] + '{} -> {}'.format(
                parameter[0], parameter[1]))


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
