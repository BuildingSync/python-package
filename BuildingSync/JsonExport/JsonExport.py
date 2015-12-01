import json
import collections

def export(data, filename):

  ''' export json '''
  ''' expecting 1 of each (Audit, Site, Facility, etc). Use first one '''
  jsondict = collections.OrderedDict()

  print 'HI!'
  print data['Audits'][0]['Audit']

  ''' api_version '''
  if 'Audits' in data and 'Audit' in data['Audits'][0]:
    audit = data['Audits'][0]['Audit']

    if 'UserDefinedFields' in audit:
      for udf in audit['UserDefinedFields']:
        if udf['UserDefinedField']['FieldName'] == 'ApiVersion':
          jsondict['api_version'] = udf['UserDefinedField']['FieldValue']
          break




  print jsondict

  ''' write json to file '''      
  if filename.find('.json') == -1:
    filename = filename + '.json' 
  with open(filename, 'w') as outfile:
    json.dump(jsondict, outfile)
  