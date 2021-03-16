bms_thresholds = {'temperature': {'min': 0, 'max': 45}, 'soc': {'min': 20, 'max': 80},
                  'charging_rate': {'min': 0, 'max': 0.8}}

bms_system_languages = {'en': 'BMS System configured with English',
                        'de':'BMS-System auf Englisch konfiguriert'}

bms_system_temperature_unit = {'C': 'Celcius',
                        'F':'Fahrenheit'}

bms_system_temperature_unit_notification = {'en': 'BMS Temperature measurement unit is set to ',
                        'de':'Die BMS-Temperaturmesseinheit ist auf eingestellt '}

bms_input_param_status = {'en':['UNKNOWN PARAMETER','INVALID PARAMETER VALUE'],
                          'de':['UNBEKANNTER PARAMETER','UNGÜLTIGER PARAMETERWERT']}

bms_console_output_messages = {'en':['OVERLIMIT', 'UNDERLIMIT', 'All Parameters are OK','BMS Operating in Unsafe Condition:'],
                                'de':['ÜBER DEM LIMIT','UNTERBEGRENZUNG', 'Alle Parameter sind in Ordnung','BMS arbeitet in unsicherem Zustand:']}

bms_hazard_warning_message = {'en': '!!! WARNING !!!','de': '!!! WARNUNG !!!'}

bms_controller_flags = {'low':1,'high':0}

bms_controller_output_messages ={
                                'en': {'temperature':['Turn ON BMS Cooler', 'Turn ON BMS Heater'],
                                        'soc':['CUT OFF BMS Charging','SWITCH BMS TO POWER SAVING MODE'],
                                        'charging_rate':['Decrease Charging Current','Increase Charging Current']},
                                 'de': {'temperature': ['Schalten Sie den BMS-Kühler ein', 'Schalten Sie die BMS-Heizung ein'],
                                        'soc': ['BMS-Aufladung abschalten', 'Schalten Sie BMS in den Energiesparmodus'],
                                        'charging_rate': ['Ladestrom verringern', 'Ladestrom erhöhen']}
                                 }





