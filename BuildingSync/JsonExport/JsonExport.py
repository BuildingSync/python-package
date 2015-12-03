import json
import collections

def export(data, filename):

  ''' export from buildingsync xml to birds json format'''
  ''' expecting 1 of each (Audit, Site, Facility, etc). Use first one '''
  jsondict = collections.OrderedDict()


  ''' apiVersion '''
  audit = {}
  if 'Audits' in data and 'Audit' in data['Audits'][0]:
    audit = data['Audits'][0]['Audit']

    if 'UserDefinedFields' in audit:
      for udf in audit['UserDefinedFields']:
        if udf['UserDefinedField']['FieldName'] == 'ApiVersion':
          jsondict['apiVersion'] = udf['UserDefinedField']['FieldValue']
          break

  ''' building (site & facility) '''
  site = collections.OrderedDict()
  facility = collections.OrderedDict()
  if 'Sites' in audit and 'Site' in audit['Sites'][0]:
    site = audit['Sites'][0]['Site']
    if 'Facilities' in site and 'Facility' in site['Facilities'][0]:
      facility = site['Facilities'][0]['Facility']

  jsondict['building'] = {}
  if 'Classification' in facility:
    jsondict['building']['category'] = facility['Classification']
  if 'OccupancyClassification' in facility:
    jsondict['building']['type'] = facility['OccupancyClassification']
  
  ''' location '''
  jsondict['location'] = collections.OrderedDict()
  if 'Address' in site:
    
    if 'State' in site['Address']:
      jsondict['location']['state'] = site['Address']['State']
    if 'City' in site['Address']:
      jsondict['location']['city'] = site['Address']['City']
    if 'city' in jsondict['location'] and 'state' in jsondict['location']:
      jsondict['location']['stateCity'] = jsondict['location']['state'] + jsondict['location']['city']
    if 'County' in site['Address']:
      jsondict['location']['county'] = site['Address']['County']


  ''' number of floors: FloorsAboveGrade + FloorsBelowGrade'''
  num_floors = 0
  if 'FloorsAboveGrade' in facility:
    num_floors = facility['FloorsAboveGrade']
  if 'FloorsBelowGrade' in facility:
    num_floors = num_floors + facility['FloorsBelowGrade']
  if num_floors != 0 and ('FloorsAboveGrade' in facility or 'FloorsBelowGrade' in facility):
    ''' only add if one of the values existed '''
    jsondict['numberOfFloors'] = num_floors

  ''' Conditioned Floor Areas '''
  if 'FloorAreas' in facility:
    jsondict['conditionedFloorAreas'] = []
    tempAreas = {}
    for fa in facility['FloorAreas']:
      if fa['FloorArea']['FloorAreaType'] == 'Conditioned':
        ''' sum up by story '''
        if str(fa['FloorArea']['Story']) in tempAreas:
          tempAreas[str(fa['FloorArea']['Story'])] = tempAreas[str(fa['FloorArea']['Story'])] + fa['FloorArea']['FloorAreaValue']
        else:
          tempAreas[str(fa['FloorArea']['Story'])] = fa['FloorArea']['FloorAreaValue']  

    ''' now go through tempAreas and assign '''
    for key in tempAreas:
      record = collections.OrderedDict()
      record['floor'] = key
      record['area']  = tempAreas[key]
      jsondict['conditionedFloorAreas'].append(record)

  ''' Exterior Wall Areas '''
  if 'Subsections' in facility:
    jsondict['exteriorWallAreas'] = []
    tempAreas = {}
    for sub in facility['Subsections']:
      current_story = sub['Subsection']['Story']
      area = 0
      if 'Sides' in sub['Subsection']:
        for side in sub['Subsection']['Sides']:
          if 'WallArea' in side['Side']['WallID']:
            area = area + side['Side']['WallID']['WallArea']
      ''' add to area (don't overwrite) '''
      if str(current_story) in tempAreas:
        tempAreas[str(current_story)] = tempAreas[str(current_story)] + area 
      else:
        tempAreas[str(current_story)] = area
    
    ''' now go through tempAreas and assign '''
    for key in tempAreas:
      record = collections.OrderedDict()
      record['floor'] = key
      record['area'] = tempAreas[key]
      jsondict['exteriorWallAreas'].append(record)


  print 'JSON DICT:'
  print jsondict

  ''' write json to file '''      
  if filename.find('.json') == -1:
    filename = filename + '.json' 
  with open(filename, 'w') as outfile:
    json.dump(jsondict, outfile)
  