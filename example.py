from BuildingSync.BuildingSync import *

bs = BuildingSync()

bs.add_audit('audit_id_1')
kwargs = {'FieldName': 'ApiVersion', 'FieldValue': '1.0 draft'}
bs.add_user_defined_field('Audit', 'audit_id_1', **kwargs)

bs.add_site('audit_id_1', 'site_id_1')
kwargs = {'City' : 'Anchorage', 'State' : 'AK', 'County': 'Anchorage'}
bs.add_address('audit_id_1', 'site_id_1', **kwargs)

kwargs = {'Classification': 'Residential', 'OccupancyClassification' : 'Single-Family', 'FloorsAboveGrade' : 3, 'FloorsBelowGrade' : 1}
bs.add_facility('audit_id_1', 'site_id_1', 'facility_id_1', **kwargs)

''' add floor area (to facility) '''
kwargs1 = {'FloorAreaType' : 'Conditioned', 'FloorAreaValue' : 100, 'Story' : 1}
kwargs2 = {'FloorAreaType' : 'Conditioned', 'FloorAreaValue' : 100, 'Story' : 1}
kwargs3 = {'FloorAreaType' : 'Unconditioned', 'FloorAreaValue' : 100, 'Story' : 2}
kwargs4 = {'FloorAreaType' : 'Conditioned', 'FloorAreaValue' : 100, 'Story' : 2}
bs.add_floor_area('Facility', 'audit_id_1', 'site_id_1', 'facility_id_1', **kwargs1)
bs.add_floor_area('Facility', 'audit_id_1', 'site_id_1', 'facility_id_1', **kwargs2)
bs.add_floor_area('Facility', 'audit_id_1', 'site_id_1', 'facility_id_1', **kwargs3)
bs.add_floor_area('Facility', 'audit_id_1', 'site_id_1', 'facility_id_1', **kwargs4)

''' add Exterior Wall Areas '''
kwargs = {'Story' : 1}
bs.add_subsection('audit_id_1', 'site_id_1', 'facility_id_1', 'subsection_id_1', **kwargs)
kwargs1 = {'WallID': {'@IDref': 'wall_id_1', 'WallArea' : 100}}
kwargs2 = {'WallID': {'@IDref': 'wall_id_2', 'WallArea' : 200}}

bs.add_side('audit_id_1', 'site_id_1', 'facility_id_1', 'subsection_id_1', **kwargs1)
bs.add_side('audit_id_1', 'site_id_1', 'facility_id_1', 'subsection_id_1', **kwargs2)
bs.add_side('audit_id_1', 'site_id_1', 'facility_id_1', 'subsection_id_1', **kwargs1)
bs.add_side('audit_id_1', 'site_id_1', 'facility_id_1', 'subsection_id_1', **kwargs2)


bs.export_json('test.json')


#bs.add_site('audit_id_1', 'site_id_1', 'Primary School Site')
#bs.add_measure('audit_id_1', 'measure_id_1', 'Lighting', 'Entire facility', 'Replace incandescent exit signs with LEDs', 0, 5, 39054, 0, 'true', 'Recommended')

#calc_method = {'Simulated' : {'SoftwareProgramUsed' : 'EnergyPlus' , 'SoftwareProgramVersion' : '6.0'}}
#bs.add_measure_savings_analysis('audit_id_1', 'measure_id_1', 1, calc_method, 109, 11451, 0, 0, 8150, 0,0,0,0,0, 'Net Present Value', 2, 246836)

#bs.add_report('audit_id_1', '2015-10-07', 'Level 2: Energy Survey and Analysis', 'true', 1000, 0.15, 20, 0.05, 0.05, 0.05, 0.03)

#scenario_type = {'CurrentBuilding' : {'CalculationMethod' : {'Simulated' : None}}}
#weather_type = {'Normalized' : {'WeatherDataSource' : 'TMY3'}}
#bs.add_report_scenario('audit_id_1', 'scenario_id_1', 'Baseline', 'Pre Retrofit', 'Weather Normalized', scenario_type, weather_type)
#bs.add_report_resource_use('audit_id_1', 'scenario_id_1', 'resource_use_id_1', 'Natural Gas', 'Site', 'therms', 1, 'Whole Building', 1, 120000, 12000, 0.569)
#bs.add_report_timeseries('audit_id_1', 'scenario_id_1', 'timeseries_id_1', 'Total', 'Energy', '2014-01-01T01:00:00', '2014-12-31T24:00:00', 'Annually',
#	2000000, 6311, 842, 'BaseElec1')
#bs.add_report_all_resource_total('audit_id_1' , 'scenario_id_1', 'all_resource_total_id_1', 'Whole Building', 'Baseline', 21713000, 103, 43426000, 206, 900000, 1000, 500, 100, 0.000474, 10000)


#bs.export_xml('test.xml')

#print 'THIS ONE!!'
#bs.print_to_file('test1.txt')

#bs2 = BuildingSync()
#bs2.import_xml('/Users/kflemin/Projects/NIST/example-buildingsync.xml')

#bs2.export_xml('example-exported.xml')
#print 'THIS ONE TOO!!'
#bs2.print_to_file('test2.txt')
#bs2.validate()