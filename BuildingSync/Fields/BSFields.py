''' Could add this on: audit, site, commercial facility, measure, report, emission, time_series, all_resource_total, scenario, lighting_system '''
def user_defined_field(): 
  fields = [
    'FieldName',
    'FieldValue'
  ]
  return fields

''' Site '''
def site():
  #with ID attr
  fields = [
    'PremisesName', 
    'PremisesNotes',
    'PremisesIdentifiers', # Add via method
    'OccupancyClassification',
    'Address', # Add via method
    'ClimateZoneType', #ASHRAE, EnergyStar, CaliforniaTitle24, IECC, BuildingAmerica, CBECS, DOE, Other.  Each with additional CimateZone element.  Takes in a dictionary.
    'eGridRegionCode',
    'WeatherDataStationID', 
    'WeatherStationName', 
    'WeatherStationCategory',
    'Longitude', #with Source attr
    'Latitude', #with Source attr
    'FloorAreas', # Add via method
    'Ownership',
    'OwnershipStatus',
    'PrimaryContactID', #with IDref attr
    'CommercialFacilities', #Each CommercialFacility (with ID attr) added via method
    'UserDefinedFields' #Each UserDefinedField with FieldName, FieldValue

  ]
  return fields

''' Site SubElements '''
def premises_identifier():  #Could add this on a site or in a commercial facility
  fields = [
    'IdentifierLabel',
    'IdentifierCustomName',
    'IdentifierValue'
  ]
  return fields

def address():
  fields = [
    'StreetAddressDetail', #Simplified: StreetAddress, StreetAdditionalInfo; Complex: StreetNumberPrefix, StreetNumberNumeric-with Source attr, StreetNumberSuffix, StreetDirPrefix, StreetName, StreetAdditionalInfo, StreetSuffix, StreetSuffixModifier,
                           #StreetDirSuffix, SubaddressType, SubaddressIdentifier
    'City',
    'State',
    'PostalCode',
    'PostalCodePlus4',
    'County'
  ]
  return fields

def floor_area(): #Could add this on a site or in a commercial facility
  fields = [
    'FloorAreaType',
    'FloorAreaCustomName',
    'FloorAreaValue' #with Source attr
  ]
  return fields

def commercial_facility():
  fields = [
    'PremisesName',
    'PremisesNotes',
    'PremisesIdentifiers', #Add via method
    'OccupancyClassification',
    'OccupancyLevels', #Add via method
    'SpatialUnits', #Add via method
    'Ownership',
    'OwnershipStatus',
    'PrimaryContactID', #with IDref attr
    'NAICSCode',
    'PubliclySubsidized', 
    'FederalBuilding', #dict with Agency, DepartmentRegion, 
    'PortfolioManager', #dict with PMBenchmarkDate, BuildingProfileStatus, FederalSustainabilityChecklistCompletionPercentage-with Source attr,
    'NumberOfBusinesses', #with Source attr
    'FloorAreas', #Add via method
    'AspectRatio', #with Source attr
    'Perimeter', #with Source attr
    'HeightDistribution', 
    'HorizontalSurroundings', 
    'VerticalSurroundings', 
    'Assessment', #with AssessmentProgram, AssessmentLevel, AssessmentValue, AssessmentYear, AssessmentVersion
    'YearOfConstruction', 
    'YearOccupied',
    'YearOfLastEnergyAudit',
    'RetrocommissioningDate', 
    'YearOfLatestRetrofit', 
    'YearOfLastMajorRemodel', 
    'PercentOccupiedByOwner', #with Source attr
    'OperatorType',
    'Subsections', #Add via method
    'UserDefinedFields' #Add via method 
  ]
  return fields  

def occupancy_level():
  fields = [
    'OccupantType', 
    'OccupantQuantityType', 
    'OccupantQuantity' #with Source attr
  ]
  return fields

def spatial_unit():
  fields = [
    'SpatialUnitType', 
    'NumberOfUnits', #with Source attr
    'UnitDensity' #with Source attr
  ]  
  return fields

''' Measure '''
def measure():
  #with ID attr
  fields = [
    'TypeOfMeasure' #dict with Replacement, ModificationRetrocommissioning, Addition, Removal, and their respective elements.
    'SystemCategoryAffected',
    'PremisesAffected', #Add via method #TODO:FIX IT!
    'TechnologyCategories', #Add via method
    'MeasureScaleOfApplication', 
    'LongDescription', 
    'MeasureSavingsAnalysis', #Add via method
    'MVCost', #with Source attr 
    'MVOption'
    'UsefulLife', #with Source attr
    'MeasureFirstCost',  #with Source attr
    'CapitalReplacementCost',  #with Source attr
    'ResidualValue',  #with Source attr
    'Recommended', 
    'StartDate',
    'EndDate',
    'ImplementationStatus',
    'DiscardReason',
    'UserDefinedFields' #Add via method
  ]
  return fields

def premises_affected():  #with IDref
  fields = [
    'MeasureCoverage', #with Source attr
  ]
  return fields

def technology_category(): #TODO: this is a weird one.  Must add technology category name element too.  measure_names are in an array
  fields = [
    'measure_name'
  ]
  return fields

def measure_savings_analysis():
  fields = [
    'MeasureRank', #with Source attr
    'ReferenceCase', #with IDref attr
    'CalculationMethod', #with Simulated, Measured, Estimated, or Other element (as dict)
    'AnnualSavingsSiteEnergy' #with Source attr
    'AnnualSavingsSourceEnergy', #with Source attr
    'AnnualSavingsCost', #with Source attr
    'AnnualSavingsByFuels', #Add via method
    'SummerPeakElectricityReduction', #with Source attr
    'WinterPeakElectricityReduction', #with Source attr
    'AnnualDemandSavingsCost', #with Source attr
    'AnnualWaterSavings', #with Source attr
    'AnnualWaterCostSavings', #with Source attr
    'AnnualOMCostSavings', #with Source attr
    'AnnualOtherCostSavings', #with Source attr
    'EquipmentDisposalAndSalvageCosts', #with Source attr
    'FundingFromIncentives', #with Source attr
    'FundingFromTaxCredits', #with Source attr
    'NPVofTaxImplications', #with Source attr
    'CostEffectivenessScreeningMethod', #with Source attr
    'SimplePayback', #with Source attr
    'NetPresentValue', #with Source attr
    'InternalRateOfReturn' #with Source attr
  ]
  return fields  

def annual_savings_by_fuel():
 fields = [
  'EnergySource',
  'ResourceUnits',
  'AnnualSavingsNativeUnits' #with Source attr
 ]
 return fields  

def report():
  fields = [
    'Scenarios', #Add via method
    'AuditDate',
    'ASHRAEAuditLevel',
    'RetrocommissioningAudit',
    'AuditCost', #with Source attr
    'DiscountFactor', #with Source attr
    'AnalysisPeriod', #with Source attr
    'GasPriceEscalationRate', #with Source attr
    'ElectricityPriceEscalationRate', #with Source attr
    'WaterPriceEscalationRate', #with Source attr
    'OtherEscalationRates', #Add via method
    'InflationRate', #with Source attr
    'Qualifications', #Add via method
    'AuditExemption',
    'AuditorContactID', #with IDref
    'UserDefinedFields' #Add via method
  ]
  return fields 

def scenario():
 # with ID attr
 fields = [
  'ScenarioName',
  'TemporalStatus',
  'Normalization',
  'ScenarioType', #TODO: what to do with this?  dict
  'WeatherType', #with one of Normalized, AdjustedToYear, Actual, Other with respective sub elements (as dict) 
  'ResourceUses', #Add via method
  'TimeSeriesData', #Add via method
  'AllResourcesTotal',
  'AnnualHeatingDegreeDays', #with Source attr
  'AnnualCoolingDegreeDays', #with Source attr
  'HDDBaseTemperature', #with Source attr
  'CDDBaseTemperature', #with Source attr
  'LinkedPremises', #TODO: FIX THIS
  'UserDefinedFields' #Add via method
 ]
 return fields 

def other_escalation_rate():
  #with Source attr
  fields = [
    'EnergyResource',
    'EscalationRate'
  ]
  return fields

def qualification():
  fields = [
    'AuditorQualification',
    'AuditorQualificationNumber',
    'AuditorQualificationState',
    'CertificationExpirationDate',
    'CertifiedAuditTeamMemberContactID', #with IDref
    'AuditTeamMemberCertificationType'
  ]
  return fields  

def resource_use():
  #with ID attr
  fields = [
    'EnergyResource', 
    'ResourceBoundary',
    'WaterResource',
    'ResourceUnits',
    'PercentResource',
    'SharedResourceSystem',
    'EndUse',
    'PercentEndUse',
    'AnnualFuelUseNativeUnits', #with Source attr
    'AnnualFuelUseConsistentUnits', #with Source attr
    'FuelUseIntensity', #with Source attr
    'Utilities', #Add via method
    'Emissions' #Add via method
  ]
  return fields

def utility():
  fields = [
    'RateSchedules', #Add via method
    'MeteringConfiguration',
    'TypeOfResourceMeter',
    'FuelInterruptibility',
    'UtilityName',
    'PowerPlant',
    'UtilityMeterNumber', #TODO: fix this
    'UtilityAccountNumber',
    'UtilityBillPayer',
    'ElectricDistributionUtility',
    'SourceSiteRatio' #with Source attr
  ]
  return fields  

def rate_schedule():
  #with ID attr
  fields = [
    'RateStructureName',
    'TypeOfRateStructure', #with one of FlatRate, TimeOfUseRate, TieredRate, Other, Unknown with respective sub-elements (as dict)
    'RateStructureSector',
    'ReferenceForRateStruture',
    'RateStructureEffectiveDate',
    'RateStructureEndDate',
    'ReactivePowerCharge', #with Source attr
    'MinimumPowerFactorWithoutPenalty', #with Source attr
    'FixedMonthlyCharge', #with Source attr
    'NetMetering', #with AverageMarginalSellRate (that has a Source attr)
    'AverageMarginalCostRate'
  ]
  return fields

def emission():
  fields = [
    'EmissionBoundary',
    'EmissionsType',
    'EmissionsFactor', #with Source attr
    'EmissionsFactorSource', #TODO: fix?
    'GHGEmissions', #with Source attr
    'AvoidedEmissions', #with Source attr
    'UseDefinedFields' #Add via method
  ]
  return fields

def time_series():
  #with ID attr
  fields = [
    'ReadingType',
    'TimeSeriesReadingQuantity',
    'StartTimeStamp',
    'EndTimeStamp',
    'IntervalFrequency',
    'IntervalReading', #with Source attr
    'Phase',
    'EnergyFlowDirection',
    'HeatingDegreeDays', #with Source attr
    'CoolingDegreeDays', #with Source attr
    'HDDBaseTemperature', #with Source attr
    'CDDBaseTemperature', #with Source attr
    'ResourceUseID', #with IDref attr
    'UserDefinedFields' #Add via method
  ]
  return fields  

def all_resource_total():
  #with ID attr
  fields = [
    'EndUse',
    'TemporalStatus',
    'ResourceBoundary',
    'SiteEnergyUse', #with Source attr
    'SiteEnergyUseIntensity', #with Source attr
    'SourceEnergyUse', #with Source attr
    'SourceEnergyUseIntensity', #with Source attr
    'EnergyCost', #with Source attr
    'OnsiteRenewableSystemElectricityExported', #with Source attr
    'ElectricitySourcedFromOnsiteRenewableSystems' #with Source attr
    'SummerPeak', #with Source attr
    'WinterPeak', #with Source attr
    'WaterResource',
    'WaterUse', #with Source attr
    'WaterIntensity', #with Source attr
    'WaterCost', #with Source attr
    'WasteWaterVolume', #with Source attr
    'UserDefinedFields' #Add via method


  ]
  return fields  

def lighting_system():
  #with ID attr
  #with Status attr
  fields = [
    'LampType', #with one of the lamptypes and respective fields (as dict)
    'BallastType',
    'InputVoltage',
    'InstallationType',
    'LightingDirection',
    'LightingControlTypeOccupancy',
    'LightingControlTypeTimer',
    'DimmingCapability', #as dict
    'DaylightingControlSteps', #with Source attr
    'PercentPremisesServed', #with Source attr
    'InstalledPower', #with Source attr
    'LampPower', #with Source attr
    'NumberOfLampsPerLuminaire', #with Source attr
    'NumberOfLampsPerBallast', #with Source attr
    'NumberOfBallastsPerLuminaire', #with Source attr
    'NumberOfLuminaires', #with Source attr
    'OutsideLighting',
    'ReflectorType',
    'LightingEfficacy', #with Source attr
    'WorkPlaneHeight', #with Source attr
    'LuminaireHeight', #with Source attr
    'FixtureSpacing', #with Source attr
    'RatedLampLife', #with Source attr
    'ControlTechnology',
    'ThirdPartyCertification',
    'PrimaryFuel',
    'YearInstalled',
    'YearOfManufacture',
    'Manufacturer',
    'ModelNumber',
    'Location',
    'LinkedPremises', #TODO: FIX THIS
    'UserDefinedFields', #Add via Method
    'Quantity'
  ]
  return fields
