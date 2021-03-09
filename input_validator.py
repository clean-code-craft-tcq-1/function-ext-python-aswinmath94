bms_parameters =['temperature','soc','charging_rate']
from bms_constants import bms_input_param_status
import bms_system_configurator


def bms_parameter_name_validation(status_report):
    for param_name in status_report.keys():
        if param_name not in bms_parameters:
            return bms_input_param_status[bms_system_configurator.system_language][0]
    return 'OK'

def bms_parameter_value_validation(status_report):
    for param_value in status_report.values():
        param_value_type = type(param_value)
        if param_value_type not in [int,float]:
            return bms_input_param_status[bms_system_configurator.system_language][1]
    return 'OK'

