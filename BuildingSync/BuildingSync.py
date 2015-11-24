import xmltodict as xmltodict
import collections
from Fields import BSFields

class BuildingSync:
  def __init__(self):
    ''' Constructor for this class. '''
    ''' Initialize dictionary '''
    self.data = collections.OrderedDict()
    self.data['Audits'] = []

  def find_audit(self, auditID):
    for audit in self.data['Audits']:
      if audit['Audit']['@ID'] == auditID:
        return audit
    return None
  def find_site(self, audit, siteID):
    for site in audit['Audit']['Sites']:
      if site['Site']['@ID'] == siteID:
        return site
    return None
  def find_commercial_facility(self, site, commercialFacilityID):
    for commercial_facility in site['Site']['CommercialFacilities']:
      if commercial_facility['CommercialFacility']['@ID'] == commercialFacilityID:
        return commercial_facility   
    return None
  def find_measure(self, audit, measureID):
    for measure in audit['Audit']['Measures']:
      if measure['Measure']['@ID'] == measureID:
        return measure
    return None
  def find_scenario(self, audit, scenarioID):
    for scenario in audit['Audit']['Report']['Scenarios']:
      if scenario['Scenario']['@ID'] == scenarioID:
        return scenario  
    return None
  def find_timeseries(self, scenario, timeSeriesID):
    for timeseries in scenario['TimeSeriesData']:
      if timeseries['TimeSeries']['@ID'] == timeSeriesID:
        return timeseries      
    return None
  def find_allresourcetotal(self, scenario, allResourceTotalID):
    for allresourcetotal in scenario['AllresourceTotals']:
      if allresourcetotal['AllResourceTotal']['@ID'] == allResourceTotalID:
        return allresourcetotal  
    return None
  def find_resourceuse(self, scenario, resourceUseID):
    for resourceuse in scenario['ResourceUses']:
      if resourceuse['ResourceUse']['@ID'] == resourceUseID:
        return resourceUse
    return None
 def find_emission(self, resourceUse, emissionID):
    for emission in resourceUse['Emissions']:
      if emission['Emission']['@ID'] == emissionID:
        return emission       
    return None

  def find_system(self, audit, systemType, systemID):
    ''' pluralize systemType '''
    systemTypes = systemType + 's'
    for system in audit['Systems'][systemTypes]:
      if system[systemType]['@ID'] == systemID:
        return system
    return None

  def import_xml(self, filename):
    ''' import XML '''
    print 'Import BuildingSync XML'
    f = open(filename, 'r')
    xml_data = f.read()
    f.close()
    self.data = xmltodict.parse(xml_data)

  def export_xml(self, filename):
    ''' export XML '''
    print 'Export BuildingSync to ' + filename
    # make sure filename has 'xml' in it
    if filename.find('.xml') == -1:
      filename = filename + '.xml'
    f = open(filename, 'w')
    f.write(xmltodict.unparse(self.data, pretty=True))
    f.close()

  def set_fields(element, elementType, kwargs):
  
    section = elementType.lower()

    ''' get fields '''
    fields = BSFields.section()

    for name, value in kwargs.items():
      for field in fields:
        if field.lower() == name.lower():
          if elementType == None
            element[field] = value
          else
            element[elementType][field] = value  #check if elementType is defined
          break

    return element

  def find_field(element, kwargs):
    for name, value in kwargs.items():
      if name.lower() == element.lower():
        return value
    return None

  def add_audit(self, auditID):
    ''' add audit '''
    ''' use @ in front of name to indicate an attribute instead of element '''
    new_audit = {'Audit' : {'@ID': auditID, 'Sites': [], 'Systems': [], 'Schedules': [], 'Measures': [], 'Report': ''}}
    self.data['Audits'].append(new_audit)
    #print self.data['Audits']

  def add_site(self, auditID, siteID, **kwargs):
    
    new_site = {'Site' : {'@ID' : siteID}}
    new_site = self.set_fields(new_site, 'Site', kwargs)

    ''' find correct audit '''
    audit = self.find_audit(auditID)
    audit['Audit']['Sites'].append(new_site)
    print self.data['Audits']

  def add_commercial_facility(self, auditID, siteID, commercialFacilityID, **kwargs):
  
    new_commercial_facility = {'CommercialFacility' : {'@ID' : commercialFacilityID}}
    new_commercial_facility = set_fields(new_commercial_facility, 'CommercialFacility', kwargs)

    ''' find correct audit & site '''
    audit = self.find_audit(auditID)
    site = self.find_site(audit, siteID)

    if 'CommercialFacilities' not in site['Site']:
      site['Site']['CommercialFacilities'] = {}

    site['Site']['CommercialFacilities'].append(new_measure)
    print self.data['Audits']


  def add_user_defined_field(self, addTo, auditID, **kwargs):
    ''' User-Defined Fields can be added to many elements '''
    ''' audit, site, commercial facility, measure, report, emission, time_series, all_resource_total, scenario, lighting_system '''
    ''' in this case kwargs will have IDs in it '''
    
    udf = {'UserDefinedField' : {}}
    udf = self.set_fields(udf, 'UserDefinedFields', kwargs)

    audit = self.find_audit(auditID)

    if addTo == 'Audit':
      if 'UserDefinedFields' not in audit['Audit']:
        audit['Audit']['UserDefinedFields'] = {}
      audit['Audit']['UserDefinedFields'].append(udf)
    elif addTo == 'Site':
      siteID = self.find_field('siteID', kwargs)
      # TODO add error checking 
      site = self.find_site(self, audit, siteID)
      if 'UserDefinedFields' not in site['Site']:
        site['Site']['UserDefinedFields'] = {}
      site['Site']['UserDefinedFields'].append(udf)
    elif addTo == 'CommercialFacility':
      commercialFacilityID = self.find_field('commercialFacilityID', kwargs)
      #TODO add error checking
      commercial_facility = self.find_commercial_facility(self, site, commercialFacilityID)
      if 'UserDefinedFields' not in commercial_facility['CommercialFacility']:
        commercial_facility['CommercialFacility']['UserDefinedFields'] = {}
      commercial_facility['CommercialFacility']['UserDefinedFields'].append(udf)
    elif addTo == 'Measure':
      measureID = self.find_field('measureID', kwargs)
      #TODO add error checking
      measure = self.find_measure(audit, measureID)
      if 'UserDefinedFields' not in measure['Measure']:
        measure['Measure']['UserDefinedFields'] = {}
      measure['Measure']['UserDefinedFields'].append(udf)
    elif addTo == 'Report':
      report = audit['Report']
      if 'UserDefinedFields' not in report:
        report['UserDefinedFields'] = {}
      report['UserDefinedFields'].append(udf)
    elif addTo == 'Scenario':  
      scenarioID = self.find_field('scenarioID', kwargs)
      #TODO add error checking
      scenario = self.find_scenario(audit, scenarioID)
     if 'UserDefinedFields' not in scenario['Scenario']:
       scenario['UserDefinedFields'] = {}
     scenario['UserDefinedFields'].append(udf)  
   
    elif addTo == 'TimeSeries':
      scenarioID = self.find_field('scenarioID', kwargs)
      timeSeriesID = self.find_field('timeSeriesID', kwargs)
      #TODO add error checking
      scenario = self.find_scenario(audit, scenarioID)
      timeseries = self.find_timeseries(scenario, timeSeriesID)
      if 'UserDefinedFields' not in timeseries['TimeSeries']:
        timeseries['UserDefinedFields'] = {}
      timeseries['UserDefinedFields'].append(udf)
        
    elif addTo == 'AllResourceTotal':
      scenarioID = self.find_field('scenarioID', kwargs)
      allResourceTotalID = self.find_field('allResourceTotalID', kwargs)
      #TODO add error checking
      scenario = self.find_scenario(audit, scenarioID)
      art = self.find_allresourcetotal(scenario, allResourceTotalID)
      if 'UserDefinedFields' not in art['AllResourceTotal']:
        art['UserDefinedFields'] = {}
      art['UserDefinedFields'].append(udf)
    elif addTo == 'Emission':
      #find report->scenarios->resourceUses->Emissions->EmissionID
      scenarioID = self.find_field('scenarioID', kwargs)
      resourceUseID = self.find_field('resourceUseID', kwargs)
      emissionID = self.find_field('emissionID', kwargs)
      #TODO add error checking
      scenario = self.find_scenario(audit, scenarioID)
      resourceUse = self.find_resourceuse(scenario, resourceUseID)
      emission = self.find_emission(resourceUse, emissionID)
      if 'UserDefinedFields' not in emission['Emission']:
        emission['UserDefinedFields'] = {}
      emission['UserDefinedFields'].append(udf)  

    elif addTo == 'LightingSystem':
      lightingSystemID = self.find_field(lightingSystemID, kwargs)
      #TODO add error checking
      lightingSystem = self.find_system(audit, 'LightingSystem', lightingSystemID)
      if 'UserDefinedFields' not in lightingSystem['LightingSystem']:
        lightingSystem['UserDefinedFields'] = {}
      lightingSystem['UserDefinedFields'].append(udf)


  def add_measure(self, auditID, measureID, **kwargs):

    new_measure = {'Measure' : {'@ID' : measureID}}
    new_measure = self.set_fields(new_measure, 'Measure', kwargs)

    ''' find correct audit '''
    audit = self.find_audit(auditID)
    audit['Audit']['Measures'].append(new_measure)
    print self.data['Audits']

  def add_measure_savings_analysis(self, auditID, measureID, **kwargs):
    ''' add measure savings analysis to an existing measure '''
    measure_savings_analysis = {}
    measure_savings_analysis = set_files(measure_savings_analysis, None, kwargs)

    ''' find correct audit and measure '''
    audit = self.find_audit(auditID)
    measure = self.find_measure(audit, measureID)
    measure['Measure']['MeasureSavingsAnalysis'] = measure_savings_analysis
    #print self.data['Audits']

  def add_report(self, auditID, **kwargs):
    
    report = {}
    report = set_fields(report, None, kwargs)

    audit = self.find_audit(auditID)
    audit['Audit']['Report'] = report
    #print self.data['Audits']

  def add_report_scenario(self, auditID, scenarioID, **kwargs):
    ''' add a scenario for report '''
    scenario = {'Scenario' : {'@ID' : scenarioID}}
    scenario = self.set_fields(scenario, 'Scenario', kwargs)
    
    audit = self.find_audit(auditID)
    if 'Scenarios' not in audit['Audit']['Report']:
      audit['Audit']['Report']['Scenarios'] = {}

    audit['Audit']['Report']['Scenarios'].append(scenario)
    #print self.data['Audits']

  def add_report_resource_use(self, auditID, scenarioID, resourceUseID, **kwargs):

    resource_use = {'ResourceUse' : {'@ID' : resourceUseID}}
    resource_use = self.set_fields(resource_use, 'ResourceUse', kwargs)

    audit = self.find_audit(auditID)
    scenario = self.find_scenario(audit, scenarioID)
    if 'ResourceUses' not in scenario['Scenario']:
      scenario['Scenario']['ResourceUses'] = {}

    scenario['Scenario']['ResourceUses'].append(resource_use)
    #print self.data['Audits']

  def add_report_timeseries(self, auditID, scenarioID, timeseriesID, **kwargs):

    timeseries = {'TimeSeries' : {'@ID' : timeseriesID}} 
    timeseries = self.set_fields(timeseries, 'TimeSeries', kwargs)

    audit = self.find_audit(auditID)
    scenario = self.find_scenario(audit, scenarioID)
    if 'TimeSeriesData' not in scenario['Scenario']:
      scenario['Scenario']['TimeSeriesData'] = {}
    scenario['Scenario']['TimeSeriesData'].append(timeseries)
    #print self.data['Audits']

  def add_report_all_resource_total(self, auditID, scenarioID, allResourceTotalID, **kwargs):

    allresourcetotal = {'AllResourceTotal' : {'@ID' : allResourceTotalID}} 
    allresourcetotal = self.set_fields(allresourcetotal, 'AllResourceTotal', kwargs)

    audit = self.find_audit(auditID)
    scenario = self.find_scenario(audit, scenarioID)
    if 'AllResourceTotals' not in scenario['Scenario']:
      scenario['Scenario']['AllResourceTotals'] = {}
    scenario['Scenario']['AllResourceTotals'].append(allresourcetotal)
    #print self.data['Audits']

  def add_lighting_system(self, auditID, lightingSystemID, **kwargs):

    lighting_power = {'LightingPower': {'@ID' :lightingSystemID}}
    lighting_power = self.set_fields(lighting_power, 'LightingPower', kwargs)

    audit = self.find_audit(auditID)
    audit['Systems']['LightingSystems'].append(lighting_power)



  def print_to_file(self, filename):
    ''' for testing '''
    f = open(filename, 'w')
    f.write(str(self.data))
    f.close()
    #print self.data['Audits']


  def validate(self):
    ''' validate that self.data matches the schema '''
    errors = []
    
    errors += self.validate_sites()
    errors += self.validate_systems()
    errors += self.validate_schedules()
    errors += self.validate_measures()
    errors += self.validate_report()

    print 'there are ' + str(len(errors)) + ' errors'
    print errors


  def validate_sites(self):
    # TODO
    errors = []
    return errors

  def validate_systems(self):
    # TODO
    errors = []
    return errors

  def validate_schedules(self):
    # TODO
    errors = []
    return errors

  def validate_measures(self):
    # TODO
    errors = []
    return errors

  def validate_report(self):
    # TODO
    errors = []
    return errors

# do systems

