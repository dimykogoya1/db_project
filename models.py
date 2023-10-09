from django.db import models

from django.forms import ModelForm
from django.contrib.auth.models import User


#Institution Information
class Institution(models.Model):
    name = models.CharField(max_length=40)
    code= models.CharField(max_length=3)
    address=models.ForeignKey("Addresse", on_delete=models.CASCADE, related_name="institution")
    
    class Meta:
        ordering = ['name','code']
        
    def __str__(self):
        return self.name
class address(models.Model):
    street=models.CharField("address"), (max_length=50)
    city=models.ForeignKey("city", on_delete=models.CASCADE, related_name"address")
    zip_code=models.CharField(_("Zip_code"), max_length=10)

class meta:
    ordering =['street', 'zip_code']
        def __str__(self):
          return f"{self.street} {self.city.name}, {self.city.state} {self.zip_code}"
      
class City(models.Model):
    name = models.CharField(_("name"), max_length=100)
    state = USStateField(_("state"), default="RI")
    
    class Meta:
        unique_together = ['name', 'state']
        ordering = ['name']
        
    def __str__(self):
             return self.name
       
class Position(models.Model):
    name = models.CharField(max_length=50,unique=True)
    class Meta:
        ordering=['name']
        
    def __str__(self):
        return self.name
    
class contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.ForeignKey("position", on_delete=models.CASCADE, related_name="contact")
    phone = models.CharField(default='', max_length=30)
    email = models.EmailField()
      
      
    def __str__(self):
        return self.name
        return f"{self.first_name} {self.last_name}
        
class Reporter(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
class TaskResponsibilities(models.Model):
TASK_CHOICES = [
    ('GCI', 'Collection Information'),
    ('PSL', 'Preparing a staff list'),
    ('AR', 'Assessing Risk'),
    ('OCP', 'Opening clossing Procedurse'),
    ('DSP', 'Determining Salvage Priorities'),
    ('PMC', 'Preventive Maintenace Check List'),
    ('IAI', 'Collection Insurance and Acccounting Information'),
    ('FPP', 'Facilitaiting Information and Preparing Floor Plans'),
    ('CIE', 'collection Information Local Emergency'),
    ('GIS', 'Gathering Internal Supplies'),
    ('DEP', 'Devising Emergency Response and Evacuation Procedures'),
    ('IPC', 'Identifying Potential Command center'),
    ('PEC', 'Preparing Emergency Call List'),
    ('IPT', 'Identifying Potential Volunteers'),
    ('CST', 'Coordinating Staff Training'),
    ('CSD', 'Coordinating Staff Distribution'),
    ('PCK', 'Preparing communication PR Kit'),
    ('CBI', 'Communicating with Bank or Financial Institutions'),
    ('MBI', 'Maintaining Budy Institutions'),
    ('IT', 'Information Technology'),
]
  def
# Define the DisasterPlanResponsibility model
class DisasterPlanResponsibility(models.Model):
    RESPONSIBILITY_CHOICES = [
        
        ('Collecting insurance and accounting information', 'Collecting insurance and accounting information'),
        ('Collecting facilities information and preparing floor plans', 'Collecting facilities information and preparing floor plans'),
        ('Collecting information about local emergency services', 'Collecting information about local emergency services'),
        ('Gathering internal supplies', 'Gathering internal supplies'),
        ('Collecting information about external supplies', 'Collecting information about external supplies'),
        ('Devising emergency response and evacuation procedures', 'Devising emergency response and evacuation procedures'),
        ('Preparing an emergency call list', 'Preparing an emergency call list'),
        ('Identifying a potential command center and/or alternative storage or drying space', 'Identifying a potential command center and/or alternative storage or drying space'),
        ('Identifying potential volunteers and/or workers', 'Identifying potential volunteers and/or workers'),
        ('Coordinating staff training', 'Coordinating staff training'),
        ('Coordinating distribution, review, and updating of the plan', 'Coordinating distribution, review, and updating of the plan'),
        ('Preparing communications and PR kit', 'Preparing communications and PR kit'),
        ('Communicating with bank or financial institution', 'Communicating with bank or financial institution'),
        ('Maintaining relationships with "buddy" institutions', 'Maintaining relationships with "buddy" institutions'),
        ('Information Technology', 'Information Technology'),
    ]

    responsibility = models.CharField(max_length=300, choices=RESPONSIBILITY_CHOICES)
    description = models.TextField()
    responsible_team_member = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.responsibility

# boolean https://docs.djangoproject.com/en/4.2/ref/models/fields/
RISK_CHOICES = (
    (1, 'Must be addressed'),
    (2, 'Should be addressed'),
    (3, 'Could be addressed'),
    (4, 'Not applicable/no action needed'),
)

# Base class for all material types
class BaseMaterial(models.Model):
    name = models.CharField(max_length=50)
    risk_level = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Risk Level')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

# Specific material types
class ArchivalMaterial(BaseMaterial):
    pass

class ArtOnPaper(BaseMaterial):
    pass

class AudioRecordingsCD(BaseMaterial):
    pass

class AudioRecordingsAlbum(BaseMaterial):
    pass

class InstitutionMaterials(models.Model):

    archival_materials = models.ForeignKey(ArchivalMaterial, on_delete=models.CASCADE, related_name='institution_archival', null=True, blank=True)
    art_on_paper = models.ForeignKey(ArtOnPaper, on_delete=models.CASCADE, related_name='institution_art_on_paper', null=True, blank=True)
    audio_recordings_cd = models.ForeignKey(AudioRecordingsCD, on_delete=models.CASCADE, related_name='institution_audio_cd', null=True, blank=True)
    audio_recordings_album = models.ForeignKey(AudioRecordingsAlbum, on_delete=models.CASCADE, related_name='institution_audio_album', null=True, blank=True)

    def __str__(self):
        return "Institution Materials"

# Common fields for risk assessments
class RiskAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    other = models.TextField(blank=True, verbose_name='Other Comments')

    class Meta:
        abstract = True

# Define the choices for the risk levels
RISK_CHOICES = (
    (1, 'Must be addressed'),
    (2, 'Should be addressed'),
    (3, 'Could be addressed'),
    (4, 'Not applicable/no action needed'),
)

class BuildingSystemsProcedures(models.Model):
    roof = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Roof')
    sky_lights = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Sky Lights')
    gutters_down_spouts = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Gutters/Downspouts')
    internal_roof_drains = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Internal Roof Drains')
    other_drain_problem = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Other Drain Problem')
    foundation = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Foundation')
    wet_basement = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Wet Basement')
    sump_pump_problems = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Sump Pump Problems')
    bathroom_kitchens_nearby_collections = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Bathroom/Kitchens Nearby Collections')
    water_pipes_running_collection_areas = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Water Pipes Running in Collection Areas')
    water_bearing_hvac_equipment = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Water-Bearing HVAC Equipment')
    water_detection_systems = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Water Detection Systems')
    mold_infestation_water_damage = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Mold Infestation/Water Damage')
    collections_stored_on_the_floor = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Collections Stored on the Floor')
    collections_stored_in_the_basement = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Collections Stored in the Basement')
    collections_stored_in_the_attic = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Collections Stored in the Attic')

    class Meta:
        abstract = True 

class BuildingSystemsProceduresRisk(BuildingSystemsProceduresBase):
    def __str__(self):
        return f'Building Systems Procedures Risk Assessment for {self.user.username}'
        
        
class ClimateControlRisk(RiskAssessment):
    heating_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Heating System')
    cooling_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Cooling System')
    humidification_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Humidification System')
    air_circulation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Air Circulation')
    building_closed_in_winter = models.IntegerField(choices=RISK_CHOICES, verbose_name='Building Closed in Winter')
    temperature_extremes = models.IntegerField(choices=RISK_CHOICES, verbose_name='Temperature Extremes')
    humidity_extremes = models.IntegerField(choices=RISK_CHOICES, verbose_name='Humidity Extremes')
    mold_infestation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Mold Infestation')
    collections_in_uncontrolled_areas = models.IntegerField(choices=RISK_CHOICES, verbose_name='Collections in Uncontrolled Areas')

    def __str__(self):
        return f'Climate Control Risk Assessment for {self.user.username}'

# Security Risk Assessment
class SecurityRisk(RiskAssessment):
    automated_security_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Automated Security System')
    staffing_for_special_collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Staffing for Special Collections')
    written_policies_procedures = models.IntegerField(choices=RISK_CHOICES, verbose_name='Written Policies/Procedures for Security')
    supervision_of_researchers = models.IntegerField(choices=RISK_CHOICES, verbose_name='Supervision of Researchers')
    researcher_identification_procedures = models.IntegerField(choices=RISK_CHOICES, verbose_name='Researcher Identification Procedures')
    vandalism_of_collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Vandalism of Collections')
    theft_of_collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Theft of Collections')
    
     
    def __str__(self):
        return f'Security Risk Assessment for {self.user.username}'
# Housekeeping/Pests Risk Assessment
class HousekeepingPestsRisk(RiskAssessment):
    pest_infestation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Pest Infestation')
    housekeeping_activities = models.IntegerField(choices=RISK_CHOICES, verbose_name='Housekeeping Activities')
    written_policies_procedures = models.IntegerField(choices=RISK_CHOICES, verbose_name='Written Policies/Procedures for Housekeeping')
    visible_dust_dirt = models.IntegerField(choices=RISK_CHOICES, verbose_name='Visible Dust and Dirt in Collections Storage Areas')
    garbage_removal = models.IntegerField(choices=RISK_CHOICES, verbose_name='Garbage Removal')
    special_event_cleanup = models.IntegerField(choices=RISK_CHOICES, verbose_name='Special Event Cleanup')
    food_and_drink_policy = models.IntegerField(choices=RISK_CHOICES, verbose_name='Food and Drink Policy')
    cleaning_of_collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Cleaning of Collections')
    
    
    def __str__(self):
        return f'Housekeeping/Pests Risk Assessment for {self.user.username}'
# Storage Risk Assessment
class StorageRisk(RiskAssessment):
    anchor_shelving = models.IntegerField(choices=RISK_CHOICES, verbose_name='Anchor Shelving to the Wall/Floor/Ceiling')
    brace_shelving = models.IntegerField(choices=RISK_CHOICES, verbose_name='Brace Shelving (to earthquake standards if needed)')
    shelve_books_snugly = models.IntegerField(choices=RISK_CHOICES, verbose_name='Shelve Books Snugly (Minimizes Water Damage)')
    enclose_archival_collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Enclose Archival Collections in Boxes')
    store_valuable_collections_away_from_windows = models.IntegerField(choices=RISK_CHOICES, verbose_name='Store Valuable Collections Away from Windows')
    raise_shelving = models.IntegerField(choices=RISK_CHOICES, verbose_name='Raise Shelving 4-6 Inches Off the Floor')
    
    
    def __str__(self):
        return f'Storage Risk Assessment for {self.user.username}'
# Personnel Risk Assessment
class PersonnelRisk(RiskAssessment):
    staff_training_emergency_procedures = models.IntegerField(choices=RISK_CHOICES, verbose_name='Staff Training - Emergency Procedures')
    staff_training_security_procedures = models.IntegerField(choices=RISK_CHOICES, verbose_name='Staff Training - Security Procedures')
    security_staff_training_recognizing_hazards = models.IntegerField(choices=RISK_CHOICES, verbose_name='Security Staff Training - Recognizing Hazards')
    security_staff_response_to_alar



class DailyPreventiveMaintenanceTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    clean_restrooms = models.BooleanField(default=False)
    stack_maintenance = models.BooleanField(default=False)
    empty_garbage = models.BooleanField(default=False)
    shovel_snow = models.BooleanField(default=False)
    vacuum_floors = models.BooleanField(default=False)
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    def __str__(self):
        return f'Daily Preventive Maintenance Tasks for {self.user.username} on {self.task_date}'

class WeeklyPreventiveMaintenanceTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    check_emergency_numbers = models.BooleanField(default=False)
    security_system_operable = models.BooleanField(default=False)
    emergency_lights_operable = models.BooleanField(default=False)
    emergency_power_operable = models.BooleanField(default=False)
    alarm_panels_operable = models.BooleanField(default=False)
    keys_accounted_for = models.BooleanField(default=False)
    flashlights_present = models.BooleanField(default=False)
    battery_powered_radio_operable = models.BooleanField(default=False) 
    check_pest_traps = models.BooleanField(default=False)
    change_hygrothermograph_chart = models.BooleanField(default=False)
    download_data_logger = models.BooleanField(default=False)
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    def __str__(self):
        return f'Weekly Preventive Maintenance Tasks for {self.user.username} on {self.task_date}'

class SeasonalPreventiveMaintenanceTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    check_caulking = models.BooleanField(default=False)
    clean_gutters = models.BooleanField(default=False)
    check_clean_storm_drains = models.BooleanField(default=False)
    winterize_grounds = models.BooleanField(default=False)
    seasonal_heating_cooling_check = models.BooleanField(default=False)
    spring_planting_maintenance = models.BooleanField(default=False)
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    def __str__(self):
        return f'Seasonal Preventive Maintenance Tasks for {self.user.username} on {self.task_date}'       

class BiannualPreventiveMaintenanceTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    hold_fire_drill = models.BooleanField(default=False)
    inspect_roof_drainage = models.BooleanField(default=False)
    inspect_windows_skylights = models.BooleanField(default=False)
    inspect_building_foundation = models.BooleanField(default=False)
    inspect_fire_detection_system = models.BooleanField(default=False)
    inspect_fire_suppression_system = models.BooleanField(default=False)
    inspect_security_system = models.BooleanField(default=False)
    general_inspection = models.BooleanField(default=False)
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    def __str__(self):
        return f'Biannual Preventive Maintenance Tasks for {self.user.username} on {self.task_date}'

class AnnualPreventiveMaintenanceTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    check_update_insurance_building_equipment = models.BooleanField(default=False)
    check_update_insurance_collections = models.BooleanField(default=False)
    revise_building_maintenance_budget = models.BooleanField(default=False)
    pump_septic_system = models.BooleanField(default=False)
    arrange_inspection_by_fire_marshal = models.BooleanField(default=False)
    flush_fire_suppression_system = models.BooleanField(default=False)
    arrange_inspection_fire_extinguishers = models.BooleanField(default=False)
    arrange_inspection_elevators = models.BooleanField(default=False)
    inspect_electrical_system = models.BooleanField(default=False)
    inspect_plumbing_system = models.BooleanField(default=False)
    update_service_contracts = models.BooleanField(default=False)
    update_building_plans_drawings = models.BooleanField(default=False)
    inventory_collections = models.BooleanField(default=False)
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    def __str__(self):
        return f'Annual Preventive Maintenance Tasks for {self.user.username} on {self.task_date}'

class ClosingStaffSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    primary_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='primary_closing_staff')
    backup_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backup_closing_staff')
    day_of_week = models.CharField(max_length=50, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return f'Closing Staff Schedule for {self.get_day_of_week_display()}'

    class Meta:
        verbose_name_plural = 'Closing Staff Schedule'
        
class Question(models.Model):
  CATEGORY_CHOICES = [
      ('OP', 'Operating Procedures'),
      ('CP', 'Closing Procedures'),
  ]
  
  text = models.TextField(_("text"))
  category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
  
  def __str__(self):
      return self.text


class Questionaire(models.Model): #responsabilities
  institution = models.models.ForeignKey("Institution", verbose_name=_(""), on_delete=models.CASCADE, related_name="tasks")
  question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="qs")
  primary = models.ForeignKey("Contact", on_delete=models.CASCADE, related_name="primary_responsabilities")
  backup = models.ForeignKey("Contact", on_delete=models.CASCADE, related_name="secondary_responsabilities")
  
  def __str__(self):
    return self.question.text
    
class Tasks(models.Model):
  institution = models.models.ForeignKey("Institution", verbose_name=_(""), on_delete=models.CASCADE, related_name="tasks")
  question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="qs")
  answer = models.BooleanField(_("answer"))
  items =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='Operating procedure', null=True, blank=True)
  def __str__(self):
      return self.name
  
class OpeningStaffSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    primary_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='primary_opening_staff', null=True, blank=True)
    backup_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backup_opening_staff', null=True, blank=True)
    day_of_week = models.CharField(max_length=100, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return f'Opening Staff Schedule for {self.get_day_of_week_display()}'

    class Meta:
        verbose_name_plural = 'Opening Staff Schedule'
    
class FacilitiesInfo(modes.Mode):
        name = models.ForeignKey("Location", on_delete=models.CASCADE)
        street = models.CharField(max_length=50)
        zip_code =models.CharField(max_length=50)
    
        class Meta:
             ordering = ['name']
         def __str__(self):
            return f"{self.name}"
class Contact(models.Model):
        phone = models.CharField(max_length=15, verbose_name='Phone')
        after_hours = models.CharField(max_length=15, verbose_name='After Hours Phone')
        pager = models.CharField(max_length=15, verbose_name='Pager')
        email = models.EmailField(max_length=150, verbose_name='Email')
        
        def __str__(self):
            return self.name
        
class Address(models.Model):
        street = models.CharField(_("address"), max_length=150)
        city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="addresses")
        zip_code = models.CharField(_("zip_code"), max_length=10)

    class Meta:
        ordering = ['street', 'zip_code']

    def __str__(self):
        return f"{self.street} {self.city.name}, {self.city.state} {self.zip_code}"

class EmergencyShutOff(models.Model):
    facility_info = models.ForeignKey(FacilitiesInformation, on_delete=models.CASCADE, verbose_name='Facilities Information')
    shut_off_type = models.CharField(max_length=300, verbose_name='Emergency Shut-Off Type')
    location = models.TextField(verbose_name='Location Description')
    procedures = models.TextField(verbose_name='Procedures')

    def __str__(self):
        return f'Emergency Shut-Off for {self.shut_off_type}'

    class Meta:
        verbose_name_plural = 'Emergency Shut-Offs'

class FireDetectionAndSuppression(models.Model):
  
    fire_alarm_pull_box = models.CharField(max_length=255, verbose_name='Fire Alarm Pull Box Number/Name')
    fire_alarm_pull_box_location = models.TextField(verbose_name='Location Description')

    # Fire Extinguishers
    FIRE_EXTINGUISHER_TYPES = [
        ('ABC', 'ABC'),
        ('Water', 'Water'),
        ('CO2', 'CO2'),
        ('Mist', 'Mist'),
    ]
    fire_extinguisher_type = models.CharField(max_length=200, choices=FIRE_EXTINGUISHER_TYPES, verbose_name='Type of Fire Extinguisher')
    fire_extinguisher_location = models.TextField(verbose_name='Location Description')
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection')

    # Smoke and Heat Detectors
    smoke_heat_detector_type = models.CharField(max_length=300, verbose_name='Type of Detector')
    smoke_heat_detector_location = models.TextField(verbose_name='Location Description')

    # Monitoring and Service
    last_inspection_maintenance_date = models.DateField(verbose_name='Date of Last Inspection/Maintenance')
    last_system_test_date = models.DateField(verbose_name='Date System Was Last Tested')
    monitoring_procedures = models.TextField(verbose_name='Description of Monitoring Procedures')

    def __str__(self):
        return f'Fire Detection and Suppression Information for {self.fire_alarm_pull_box}'

    class Meta:
        verbose_name_plural = 'Fire Detection and Suppression'
        
#create parent class, subclass, child class-baseCompany
class CompanyBase(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person') # foregnkey needed
    address = models.ManyToManyField("Address", related_name='comnpanies')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=20, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    class Meta:
        abstract = True
# repeated attributes 
  # 
class SmokeHeatDetectionMonitoringAgency(CompanyBase):
    monitoring_service_type = models.CharField(max_length=100, verbose_name='Monitoring Service Type')
    

    def __str__(self):
        return 'Smoke and Heat Detection System Monitoring Agency'

    class Meta:
        verbose_name_plural = 'Smoke and Heat Detection System Monitoring Agencies'

class SmokeHeatDetectionServiceCompany(CompanyBase):
    service_type = models.CharField(max_length=100, verbose_name='Service Type')

    def __str__(self):
        return 'Smoke and Heat Detection System Service Company'

    class Meta:
        verbose_name_plural = 'Smoke and Heat Detection System Service Companies'

class SprinklerSystemMonitoringAgency(CompanyBase):
    monitoring_type = models.CharField(max_length=100, verbose_name='Monitoring Type')

    def __str__(self):
        return 'Sprinkler System Monitoring Agency'

    class Meta:
        verbose_name_plural = 'Sprinkler System Monitoring Agencies'

class SprinklerSystemServiceCompany(CompanyBase):
    service_type = models.CharField(max_length=100, verbose_name='Service Type')

    def __str__(self):
        return 'Sprinkler System Service Company'

    class Meta:
        verbose_name_plural = 'Sprinkler System Service Companies'

class GaseousFireSuppressionSystem(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location')
    suppression_system_type = models.CharField(max_length=150, verbose_name='Description/Type of Suppression System')
    age_of_system = models.PositiveIntegerField(verbose_name='Age of System', null=True, blank=True)
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection', null=True, blank=True)
    evacuation_plan_description = models.TextField(verbose_name='Description of Emergency Evacuation Plans', blank=True)

    def __str__(self):
        return f'Gaseous Fire Suppression System at {self.location}'

    class Meta:
        verbose_name_plural = 'Gaseous Fire Suppression Systems'


    #Monitoring and Service Information
    monitoring_procedures = models.TextField(verbose_name='Monitoring Procedures', blank=True)
    
    #Monitoring Agency
    monitoring_agency_name = models.CharField(max_length=150, verbose_name='Monitoring Agency Name', blank=True)
    monitoring_contact_person = models.CharField(max_length=150, verbose_name='Contact Person', blank=True)
    monitoring_address1 = models.CharField(max_length=150, verbose_name='Address 1', blank=True)
    monitoring_address2 = models.CharField(max_length=150, verbose_name='Address 2', blank=True)
    monitoring_city = models.CharField(max_length=50, verbose_name='City', blank=True)
    monitoring_state = models.CharField(max_length=2, verbose_name='State', blank=True)
    monitoring_zip = models.CharField(max_length=50, verbose_name='Zip', blank=True)
    monitoring_phone = models.CharField(max_length=20, verbose_name='Phone', blank=True)
    monitoring_after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone', blank=True)
    monitoring_pager = models.CharField(max_length=20, verbose_name='Pager', blank=True)
    monitoring_email = models.EmailField(max_length=150, verbose_name='Email', blank=True)
    
    
    #Service Company
    service_company_name = models.CharField(max_length=150, verbose_name='Service Company Name', blank=True)
    service_contact_person = models.CharField(max_length=150, verbose_name='Contact Person', blank=True)
    service_address1 = models.CharField(max_length=150, verbose_name='Address 1', blank=True)
    service_address2 = models.CharField(max_length=150, verbose_name='Address 2', blank=True)
    service_city = models.CharField(max_length=50, verbose_name='City', blank=True)
    service_state = models.CharField(max_length=2, verbose_name='State', blank=True)
    service_zip = models.CharField(max_length=50, verbose_name='Zip', blank=True)
    service_phone = models.CharField(max_length=20, verbose_name='Phone', blank=True)
    service_after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone', blank=True)
    service_pager = models.CharField(max_length=20, verbose_name='Pager', blank=True)
    service_email = models.EmailField(max_length=150, verbose_name='Email', blank=True)

    def __str__(self):
        return f'Gaseous Fire Suppression System at {self.location}'

    class Meta:
        verbose_name_plural = 'Gaseous Fire Suppression Systems'
        
class MonitoringAgency(models.Model):
        suppression_system_type = models.CharField(max_length=150, verbose_name='Description/Type of Suppression System')
        age_of_system = models.PositiveIntegerField(verbose_name='Age of System', null=True, blank=True)
        last_inspection_date = models.DateField(verbose_name='Date of Last Inspection', null=True, blank=True)
        evacuation_plan_description = models.TextField(verbose_name='Description of Emergency Evacuation Plans', blank=True)
                        
        class meta:
             ordering =['monitoring agency']
             def __str__(self):
                     return f'Gaseous Fire Suppression System at {self.location}'
             
class WaterDetector(models.Model):
    detector_type = models.CharField(max_length=150, verbose_name='Type of Water Detector')
    location = models.CharField(max_length=150, verbose_name='Location')
    
    # Monitoring and Service Information
    monitoring_procedures = models.TextField(verbose_name='Monitoring Procedures', blank=True)

    def __str__(self):
        return f'Water Detector at {self.location}'

    class Meta:
        verbose_name_plural = 'Water Detectors'

class WaterDetector(models.Model):
    detector_type = models.CharField(max_length=150, verbose_name='Type of Water Detector')
    location = models.CharField(max_length=150, verbose_name='Location')


    # Monitoring and Service Information
    monitoring_procedures = models.TextField(
        verbose_name='Description of Monitoring Procedures',
        blank=True
    )

    def __str__(self):
        return f'Water Detector at {self.location}'

class WaterDetectorMonitoringAgency(models.Model):
    water_detector = models.ForeignKey(WaterDetector, on_delete=models.CASCADE, related_name='monitoring_agencies')
    name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=150, verbose_name='City')
    state = models.CharField(max_length=150, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return f'Monitoring Agency for Water Detector at {self.water_detector.location}'

class SecuritySystem(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location')
    security_type = models.CharField(max_length=150, verbose_name='Type of Security')

    # Monitoring and Service Information
    last_inspection_date = models.DateField(
        verbose_name='Date of Last Inspection of Automated Security System',
        null=True, blank=True
    )
    access_code_location = models.CharField(
        max_length=150,
        verbose_name='Location of Access Codes for Automated Security System',
        blank=True
    )
    monitoring_procedures = models.TextField(
        verbose_name='Description of Monitoring Procedures for Automated Security System',
        blank=True
    )

    def __str__(self):
        return f'Security System at {self.location}'

from django.db import models

class SecuritySystemBase(models.Model):
    security_system = models.ForeignKey(SecuritySystem, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=150, verbose_name='City')
    state = models.CharField(max_length=150, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)

    class Meta:
        abstract = True

class SecuritySystemMonitoringAgency(SecuritySystemBase):
    organization = models.CharField(max_length=150, verbose_name='Organization/Department')

    def __str__(self):
        return f'Monitoring Agency for Security System at {self.security_system.location}'

class SecuritySystemServiceCompany(SecuritySystemBase):
    name = models.CharField(max_length=150, verbose_name='Name')

    def __str__(self):
        return f'Service Company for Security System at {self.security_system.location}'


class StaffMember(models.Model):
    name = models.CharField(max_length=150, verbose_name='Staff Member Name')
    access_type = models.CharField(max_length=150, verbose_name='Type of Access')
    areas_accessed = models.TextField(
        verbose_name='Areas to Which Person Has Access',
        help_text='List the areas or rooms this staff member has access to.'
    )
    access_code_location = models.CharField(
        max_length=150,
        verbose_name='Location of Access Codes for Automated Security System',
        blank=True,
        help_text='Specify where access codes are stored or listed.'
    )
    fire_department_access = models.TextField(
        verbose_name='Fire Department Access Procedure',
        help_text='Explain how the fire department would gain access to the building if necessary.'
    )

    def __str__(self):
        return self.name
    
class HeatingSystem(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location (e.g., rooms or areas)')
    system_description = models.TextField(
        verbose_name='Description of Heating System',
        help_text='Describe the type of heating system, type of fuel, distribution system, and whether it provides humidification.'
    )
    operating_procedures = models.TextField(
        verbose_name='Procedures for Operating the System',
        help_text='Explain how to change the settings or operate the heating system.'
    )

    # Monitoring and Service Information
    last_inspection_date = models.DateField(
        verbose_name='Date of Last Inspection and Maintenance of the Heating System',
        null=True, blank=True
    )

    def __str__(self):
        return f'Heating System at {self.location}'
        
class HeatingCompany(modes.Models):
    name = models.ForegnKeyField(max_length=50, on_delete=models.CASCADE, related_name=" heating serverice company ")
    street = models.CharField(max_length=50)
    city = models.ForeignKey(Max_length=100, on_delete=models.CASCADE related_name='city')
    state = models.CharField(max_length=150, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
      
   class Meta:
     odering =['name']
    def __str__(self):
        return self.name
class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    
    class Meta:
      unique_together = ['name', 'phone']
        ordering = ['name']
    def __str__(self):
        return self.name
class Address(modesl.Model)
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.models.ForeignKey("City", on_delete=models.CASCADE)(max_length=100, related_name='city')
    state = models.CharField(max_length=150, verbose_name='State')
    
    class Meta:
      ordering = ['name']
    def __str__(self):
        return self.name

class CoolingSystem(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location (e.g., rooms or areas)')
    system_description = models.TextField(
        verbose_name='Description of Cooling System',
        help_text='Describe the type of cooling system, such as central air conditioning, window units, or heat pumps.'
    )
    operating_procedures = models.TextField(
        verbose_name='Procedures for Operating the System',
        help_text='Explain how to change the settings or operate the cooling system.'
    )

    # Monitoring and Service Information
    last_inspection_date = models.DateField(
        verbose_name='Date of Last Inspection and Maintenance of the Cooling System',
        null=True, blank=True
    )

    def __str__(self):
        return f'Cooling System at {self.location}'

class CoolingSystem(models.Model)
    name = models.CharField(max_length=50,verbose_name="organization name")
    location =models.CharField(_("places"), max_length=50)
    city = models.ForeignKey("city" on_delete=models.CASCADE)
    
    class Meta:
      ordering=['name']
      def __str__(self):
        return self.name
class Location(models.Model):
    contact = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=150, verbose_name='City')
    state = models.CharField(max_length=150, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    
      class Meta:
        unique_together = ['name','city']
        ordering = ['name']
        
    def __str__(self):
        return self.name

class DisasterResponseTeamMember(models.Model):
    ROLE_CHOICES = (
        ('Primary', 'Primary'),
        ('Backup #1', 'Backup #1'),
        ('Backup #2', 'Backup #2'),
    )

    name = models.CharField(max_length=150, verbose_name='Name')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role')
    contact_phone = models.CharField(max_length=15, verbose_name='Phone')
    contact_cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    contact_after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    contact_email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return f'{self.name} - {self.role}'

class DisasterTeamResponsibility(models.Model):
    RESPONSIBILITY_CHOICES = (
        ('Disaster Team Leader', 'Disaster Team Leader'),
        ('Administrator/Supplies Coordinator', 'Administrator/Supplies Coordinator'),
        ('Collections Recovery Specialist', 'Collections Recovery Specialist'),
        ('Subject Specialist/Department Head', 'Subject Specialist/Department Head'),
        ('Work Crew Coordinator', 'Work Crew Coordinator'),
        ('Technology Coordinator', 'Technology Coordinator'),
        ('Building Recovery Coordinator', 'Building Recovery Coordinator'),
        ('Security Coordinator', 'Security Coordinator'),
        ('Public Relations Coordinator', 'Public Relations Coordinator'),
        ('Documentation Coordinator', 'Documentation Coordinator'),
    )

    responsibility = models.CharField(max_length=50, choices=RESPONSIBILITY_CHOICES, verbose_name='Responsibility')
    team_member = models.ForeignKey(DisasterResponseTeamMember, on_delete=models.CASCADE, related_name='responsibilities')

    def __str__(self):
        return f'{self.get_responsibility_display()} - {self.team_member.name}'

class LocalBuddyOrganization(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True) a model for Data Backup
class DataBackup(models.Model):
    DATA_TYPE_CHOICES = (
        ('Collection Records', 'Collection Records'),
        ('In-house Databases', 'In-house Databases'),
        ('Financial Information', 'Financial Information'),
        ('Digital Collections', 'Digital Collections'),
    )

    type_of_data = models.CharField(max_length=150, choices=DATA_TYPE_CHOICES, verbose_name='Type of data')
    location_of_data = models.CharField(max_length=150, verbose_name='Location of Data')
    person_responsible_for_backup = models.ForeignKey('DisasterResponseTeamMember', on_delete=models.CASCADE, related_name='data_backups')
    on_site_location_of_backup = models.CharField(max_length=150, verbose_name='On-site location of backup', blank=True)
    off_site_location_of_backup = models.CharField(max_length=150, verbose_name='Off-site location of backup', blank=True)
    frequency_of_backup = models.CharField(max_length=50, verbose_name='Frequency of backup', blank=True)

    def __str__(self):
        return f'{self.type_of_data} - {self.location_of_data}'

# Create a parent class with common fields
class CommonFields(models.Model):
    staff_person = models.ForeignKey('DisasterResponseTeamMember', on_delete=models.CASCADE, verbose_name='Staff Person')
    outside_person_or_organization = models.CharField(max_length=150, verbose_name='Name/Organization', blank=True)
    title_or_contact = models.CharField(max_length=150, verbose_name='Title/Contact', blank=True)
    address1 = models.CharField(max_length=150, verbose_name='Address1', blank=True)
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=150, verbose_name='City', blank=True)
    state = models.CharField(max_length=150, verbose_name='State', blank=True)
    zip_code = models.CharField(max_length=50, verbose_name='Zip', blank=True)
    phone = models.CharField(max_length=15, verbose_name='Phone', blank=True)
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    email = models.EmailField(max_length=150, verbose_name='Email', blank=True)

    class Meta:
        abstract = True

class DataRestoration(CommonFields):
    def __str__(self):
        return f'{self.staff_person.name} - {self.outside_person_or_organization}'

class Reconfiguration(CommonFields):
    def __str__(self):
        return f'{self.staff_person.name} - {self.outside_person_or_organization}'

class ComputerOperationRelocation(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location')
    contact_person = models.CharField(max_length=150, verbose_name='Contact person')
    phone = models.CharField(max_length=15, verbose_name='Phone', blank=True)
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    procedures = models.TextField(verbose_name='Procedures', blank=True)

    def __str__(self):
        return self.location

class EmergencyRemoteAccess(models.Model):
    telephone_voice_mail = models.TextField(verbose_name='Telephone/Voice Mail', blank=True)
    email = models.TextField(verbose_name='Email', blank=True)
    intranet = models.TextField(verbose_name='Intranet', blank=True)
    library_website = models.TextField(verbose_name='Library Website', blank=True)
    regional_library_network = models.TextField(verbose_name='Regional Library Network', blank=True)
    local_online_catalog = models.TextField(verbose_name='Local Online Catalog', blank=True)
    online_subscription_services = models.TextField(verbose_name='Online Subscription Services', blank=True)
    other = models.TextField(verbose_name='Other', blank=True)

    def __str__(self):
        return 'Emergency Remote Access'

# Create a single instance of the EmergencyRemoteAccess model to store the procedures
EmergencyRemoteAccess.objects.create(
    telephone_voice_mail='Include procedures for switching fax and phone numbers to the remote site.',
    email='Specify how staff can access email remotely.',
    intranet='Detail how staff can access the intranet remotely.',
    library_website='Explain how the library website can be accessed from an alternate site.',
    regional_library_network='Provide information on accessing the regional library network remotely.',
    local_online_catalog='Describe how to access the local online catalog from an alternate location.',
    online_subscription_services='Instructions for accessing online subscription services in an emergency.',
    other='Any other procedures or services related to emergency remote access.'
)

# a model to represent the priority of administrative records
class AdministrativeRecord(models.Model):
    PRIORITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    priority_ranking = models.PositiveIntegerField(choices=PRIORITY_CHOICES, verbose_name='Priority Ranking')
    record_type = models.CharField(max_length=150, verbose_name='Type of Record Group')
    location = models.CharField(max_length=300, verbose_name='Location of Records')

    def __str__(self):
        return f'Priority {self.priority_ranking} - {self.record_type}'

#a model to represent the priority of bibliographic records
class BibliographicRecord(models.Model):
    PRIORITY_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    priority_ranking = models.PositiveIntegerField(choices=PRIORITY_CHOICES, verbose_name='Priority Ranking')
    record_type = models.CharField(max_length=150, verbose_name='Type of Record Group')
    location = models.CharField(max_length=300, verbose_name='Location of Records')

    def __str__(self):
        return f'Priority {self.priority_ranking} - {self.record_type}'
        
        
class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name='Department Name')
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')

    def __str__(self):
        return self.name

#  a model to represent collections and their priorities within departments
class Collection(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=150, verbose_name='Collection Name')
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name='Department Name')
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')

    def __str__(self):
        return self.name

class Collection(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=150, verbose_name='Collection Name')
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')
    location = models.CharField(max_length=300, verbose_name='Location (include floor and specific location)')

    def __str__(self):
        return self.name

class OverallSalvagePriority(models.Model):
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')
    material_or_equipment = models.CharField(max_length=150, verbose_name='Material or Equipment')
    location = models.CharField(max_length=300, verbose_name='Location (include floor and specific location)')

    def __str__(self):
        return self.material_or_equipment

class BuildingPlan(models.Model):
    name = models.CharField(max_length=150, verbose_name='Plan Name')
    description = models.TextField(verbose_name='Plan Description')
    color_code = models.CharField(max_length=20, verbose_name='Color Code')

    def __str__(self):
        return self.name

class InsuranceInformation(models.Model):
    BUILDING = 'Building'
    MACHINERY = 'Machinery'
    EQUIPMENT = 'Equipment'

    PROPERTY_CHOICES = [
        (BUILDING, 'Building'),
        (MACHINERY, 'Machinery'),
        (EQUIPMENT, 'Equipment'),
    ]

    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    policy_inception_date = models.DateField(verbose_name='Policy Inception Date')
    policy_expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    property_covered = models.CharField(max_length=20, choices=PROPERTY_CHOICES, verbose_name='Property Covered')
    amount_of_coverage = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Coverage')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)

    def __str__(self):
        return f'Policy: {self.policy_number}, Property: {self.get_property_covered_display()}'


class InsuranceCompany(models.Model):
    name = models.CharField(_("company"), max_length=50)
    ddress1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    street = models.CharField(max_length=50, verbose_name='City')
    
    class Meta:
      ordering =['name']
      def __str__(self):
          return self.name
class Contact(models.Model):
    city=models.ForeignKey(max_length=150, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, verbose_name='Phone', blank=True)
    pager = models.CharField(max_length=30, verbose_name='Pager', blank=True)
    email = models.EmailField(max_length=150, verbose_name='Email', blank=True)
    
    class Metad:
      ordering = ['name','state', 'city']
    def __str__(self):
        return self.name
    
    
    

class Inventory(models.Model):
    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    inception_date = models.DateField(verbose_name='Policy Inception Date')
    expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    coverage_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Business Interruption Insurance Provided')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)
    frequency_of_review = models.CharField(max_length=150, verbose_name='Frequency of review and updating of this policy')
    person_responsible_for_review = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Person responsible for reviewing and updating this policy')

    class Meta:
        ordering = ['policy_number']

    def __str__(self):
        return self.policy_number

class ExpensesInsurance(models.Model):
    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    inception_date = models.DateField(verbose_name='Policy Inception Date')
    expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    coverage_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Extra Expenses Insurance Provided')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)

    class Meta:
        unique_together = ['policy_number', 'inception_date', 'expiration_date']

    def __str__(self):
        return self.policy_number

class Address(models.Model):
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    zip_code = models.CharField(max_length=50, verbose_name='Zip')
    state = models.CharField(max_length=2, verbose_name='State')

    class Meta:
        ordering = ['city']

    def __str__(self):
        return f'{self.address1}, {self.city}, {self.state} {self.zip_code}'

class ContactInfo(models.Model):
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    email = models.EmailField(max_length=254, verbose_name='Email')

    def __str__(self):
        return self.email

class DepartmentInsurance(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        ##
# list of Insurance Inventories 
FREQUENCY_CHOICES = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annually', 'Annually'),
)

RESPONSIBILITY_CHOICES = (
    ('person_1', 'Person 1'),
    ('person_2', 'Person 2'),
    ('backup_1', 'Backup #1'),
    ('backup_2', 'Backup #2'),
)

class InsuranceCoverage(models.Model):
    funds = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Funds Available for Salvage, Repair, and/or Replacement of Collections (in dollars)')
    collections= models.TextField(verbose_name='Collections Appraised for Insurance Purposes')
    date_of_last = models.DateField(verbose_name='Date of Last Appraisal')
    onducting = models.CharField(max_length=150, verbose_name='Person Conducting Appraisal')
    responsible = models.CharField(max_length=150, verbose_name='Person Responsible for Periodic Evaluation of Funds', choices=RESPONSIBILITY_CHOICES)
    frequency = models.CharField(max_length=50, verbose_name='Frequency of Evaluation and Increase of Funds Set Aside for Self-Insurance', choices=FREQUENCY_CHOICES)
    procedures = models.TextField(verbose_name='Procedures in Case of Damage or Loss')
    documentation = models.TextField(verbose_name='Documentation Required to Prove Loss')

    def __str__(self):
        return f'Funds Available: ${self.funds_for_recovery}'

class EvacuationProcedure(models.Model):
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for Clearing Area', choices=RESPONSIBILITY_CHOICES)
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1', choices=RESPONSIBILITY_CHOICES)
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2', choices=RESPONSIBILITY_CHOICES)
    evacuation_procedures = models.TextField(verbose_name='Procedures for Evacuating the Building, Including Disabled Personnel or Patrons')

    def __str__(self):
        return f'Evacuation Area: {self.area_or_floor}'

class StaffVisitorLog(models.Model):
    area_or_floor = models.CharField(max_length=300, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for List', choices=RESPONSIBILITY_CHOICES)
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1', choices=RESPONSIBILITY_CHOICES)
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2', choices=RESPONSIBILITY_CHOICES)

    def __str__(self):
        return f'Staff/Visitor Log for {self.area_or_floor}'

class AssemblyArea(models.Model):
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    staff_member_in_charge = models.CharField(max_length=150, verbose_name='Staff Member in Charge of Head Count')
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1')
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2')
    location = models.CharField(max_length=300, verbose_name='Location')

    def __str__(self):
        return f'Assembly Area: {self.area_or_floor}'

class EmergencyCallList(models.Model):
    staff_member = models.CharField(max_length=150, verbose_name='Staff Member')
    estimated_response_time = models.CharField(max_length=50, verbose_name='Estimated Response Time')
    position_on_call_list = models.PositiveIntegerField(verbose_name='Position on Call List')

    def __str__(self):
        return self.staff_member


class CommandCenter(models.Model):
    command_center_location = models.CharField(max_length=300, verbose_name='Command Center Location')
    alternate_location_1 = models.CharField(max_length=300, verbose_name='Alternate Location #1')
    alternate_location_2 = models.CharField(max_length=300, verbose_name='Alternate Location #2 (Off-site)')

    def __str__(self):
        return f'Command Center: {self.command_center_location}'

class CollectionStorageLocation(models.Model):
    LOCATION_CHOICES = (
        ('Within Building/Institution', 'Within Building/Institution'),
        ('Off-Site', 'Off-Site'),
    )

    location_type = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name='Location Type')
    location = models.CharField(max_length=300, verbose_name='Location')
    space_available = models.CharField(max_length=150, verbose_name='Space Available')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After-Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')

    def __str__(self):
        return f'{self.location_type} - {self.location}'

class DryingSpace(models.Model):
    LOCATION_CHOICES = (
        ('Within Building/Institution', 'Within Building/Institution'),
        ('Off-Site', 'Off-Site'),
    )

    location_type = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name='Location Type')
    location = models.CharField(max_length=150, verbose_name='Location')
    space_available = models.CharField(max_length=150, verbose_name='Space Available')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After-Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')

    def __str__(self):
        return f'{self.location_type} - {self.location}'
class Department(models.Model):
    name = models.CharField(max_length=50)
    backup = models.CharField(max_length=50, verbose_name="backup liason")
    data = models.DateField(auto_now=False, auto_now_add=False)
    review_date=models.DateField(auto_now=False, auto_now_add=False,verbose_name='Date of Last In-house Review of Collection Priorities')
    
class Fire



class Police


class EmergencyM

class localEmergency
    
    
    
class FireDepartmentInfo(models.Model):
    
    inspection_date = models.DateField(verbose_name='Date of Last Inspection by Fire Marshal')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Fire Department')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    in_house = models.CharField(max_length=150, verbose_name='In-house Liaison to Fire Department')
    backup= models.CharField(max_length=150, verbose_name='Backup Liaison')
    date = models.DateField(verbose_name='Date of Last In-house Review of Collection Priorities')
    review_date = models.DateField(verbose_name='Date of Last On-site Review with Fire Department Personnel')

    def __str__(self):
        return f'Fire Department Information'

class PoliceDepartmentInfo(models.Model):
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Police Department')
    title = models.CharField(max_length=50, verbose_name='Title')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    in_house = models.CharField(max_length=150, verbose_name='In-house Liaison to Police Department')
    backup= models.CharField(max_length=150, verbose_name='Backup Liaison')
    last_date = models.DateField(verbose_name='Date of Last On-site Review with Police Department Personnel')

    def __str__(self):
        return f'Police Department Information'

class EmergencyManagementAgency(models.Model):
    name = models.CharField(max_length=150, verbose_name='Agency Name')
    address1 = models.CharField(max_length=150, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    fax = models.CharField(max_length=15, verbose_name='Fax')
    website = models.URLField(max_length=300, verbose_name='Website')

    def __str__(self):
        return self.name

class LocalEmergencyManagement(models.Model):
    agency_name = models.CharField(max_length=150, verbose_name='Local Emergency Management Agency')
    contact_persons = models.TextField(verbose_name='Contact Person(s)')
    titles = models.TextField(verbose_name='Title(s)')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    in_house_liaison = models.CharField(max_length=150, verbose_name='In-house Liaison to Local Emergency Management Agencies')
    backup_liaison = models.CharField(max_length=150, verbose_name='Backup Liaison')
    last_on_site_review_date = models.DateField(verbose_name='Date of Last On-site Review with Emergency Management Personnel')
    procedures_description = models.TextField(verbose_name='Description of Applicable Local Procedures for Managing Disasters')

    def __str__(self):
        return f'Local Emergency Management Agency: {self.agency_name}'

class EmergencyServices(models.Model):
    ambulance_name = models.CharField(max_length=150, verbose_name='Ambulance Name')
    ambulance_phone = models.CharField(max_length=15, verbose_name='Ambulance Phone')
    is_911_available = models.BooleanField(default=False, verbose_name='Are 911 services available?')
    in_house_security_name = models.CharField(max_length=150, verbose_name='In-house Security Name')
    in_house_security_phone = models.CharField(max_length=15, verbose_name='In-house Security Phone')
    in_house_security_after_hours_phone = models.CharField(max_length=15, verbose_name='In-house Security After-hours Phone')
    in_house_security_cell_phone = models.CharField(max_length=15, verbose_name='In-house Security Cell Phone')
    security_monitoring_name = models.CharField(max_length=150F, verbose_name='Security Monitoring Company Name')
    security_monitoring_phone = models.CharField(max_length=15, verbose_name='Security Monitoring Company Phone')
    security_monitoring_after_hours_phone = models.CharField(max_length=15, verbose_name='Security Monitoring Company After-hours Phone')
    security_monitoring_cell_phone = models.CharField(max_length=15, verbose_name='Security Monitoring Company Cell Phone')
    other_name = models.CharField(max_length=150, verbose_name='Other Name')
    other_phone = models.CharField(max_length=15, verbose_name='Other Phone')
    other_after_hours_phone = models.CharField(max_length=15, verbose_name='Other After-hours Phone')
    other_cell_phone = models.CharField(max_length=15, verbose_name='Other Cell Phone')
    
    def __str__(self):
        return f'Emergency Services for {self.ambulance_name}'
class Organization(models.Model):
  MAINTENACE_CHOICES = (
      ("maintanace", "Maintanace")
      ("utilities", "Utilities")
      ("facilities", "Facilities")
      ("janitorial", "Janitorial")
      ("electrician", "Electrician")
      ("plumber","Plumber")
  )
    maintanance = models.CharField(_("Maintenance"), max_length=50, choices=MAINTENANCE_CHOICES)
    unilities = models.CharField(_("Utilities"), max_length=50, choices=MAINTENANCE_CHOICES)
    Facilities = models.CharField(_("Facilities"), max_length=50, choices=MAINTENANCE_CHOICES)
    Genitorial_services = models.CharField(_("Janitorial Services"), max_length=50, choices=MAINTENANCE_CHOICES)
    Electrician = models.CharField(_("Electrician"), max_length=50, choices=MAINTENANCE_CHOICES)
    plumber = models.CharField(_("Plumber"), max_length=50, choices=MAINTENANCE_CHOICES)

    class Meta:
          ordering = ['maintanace']
          
    def __str__(self):
        return f"Organization {self.id}"
        
class City(models.Model):
    state = models.CharField(_("state"), max_length=50)
    city = models.CharField(_("city"), max_length=50,)
    zi_code = models.CharField(max_length=50)
    
    class Meta:
         unique_together = ['city', 'state']
            ordering = ['city']
    def __str__(self):
             return self.city
             
class Address(models.Model):
    address1 = models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.ForeignKey("city", verbose_name=_("city"), on_delete=models.CASCADE)
  
    class Meta: 
        ordering = ['city']
            def __str__(self):
                return self.city.ity
class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(default='', max_length=30)
    email = models.EmailField()
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email =models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self f"{self.first_name} {self. last_name}"
    
class ServiceOrganization(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name of the organization")
    contact_person = models.CharField(max_length=20, verbose_name="Contact person")
    address1 = models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2', blank=True)
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='Cell phone number')
    pager_phone = models.CharField(max_length=30, verbose_name='Pager Phone')
    pager_email = models.EmailField(max_length=100, verbose_name='Email address')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class LockSmith(ServiceOrganization):
    def __str__(self):
        return f"Locksmith: {self.name}"

class Carpenter(ServiceOrganization):
    def __str__(self):
        return f"Carpenter: {self.name}"

class Exterminator(ServiceOrganization):
    def __str__(self):
        return f"Exterminator: {self.name}"

class ComputerEmergency(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class LegalAdvisor(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class ArchitectBuilder(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
        
class GasCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class OilCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class ElectricCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class WaterUtilityCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class TelephoneCampanyCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class ElevatorCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class SprinklerSeriviceCompany(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class HeatingSystemService(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class CoolingSystemService(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class SecuritySystemService(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
class Other(models.Model)
    name=models.CharField(max_length=150, verbose="name of the organization")
    contact_person=models.CharField(max_length=20,verbose="contact person")
    address1=models.CharField(max_length=150, verbose_name="Organization address")
    address2 = models.CharField(max_length=150, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip Code')
    phone = models.CharField(max_length=30, verbose_name='Phone')
    cell_phone_number = models.CharField(max_length=30, verbose_name='cell ephon number')
    pager_phone = models.CharField(max_length=30, verbose_name='pager Phone')
    pager_email = models.EmailField(max_length=100)(max_length=30, verbose_name='email address')
    
    def __str__(self):
        return self.name
        
    


