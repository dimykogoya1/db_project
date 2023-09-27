from django.db import models

from django.forms import ModelForm
from django.contrib.auth.models import User


#Institution Information
class InstitutionInformation(models.Model):
    name = models.CharField(max_length=40)
    location_name = models.CharField(max_length=150)
    address.models.models.CharField(_("address"), max_length=150)
    city = models.CharField(_("city"), max_length=150, default="Providence")
    state = USStateField(_("state"), default="RI")
    zip_code = models.CharField(_("zip code"), max_length=50, default="43760")
class ContactPerson(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(default='', max_length=30)
    email = models.EmailField()

class Title(models.Model):
    director = models.CharField(max_length=50)
    treasury = models.CharField(max_length=50)
    director_assistant = models.CharField(max_length=50)
    officer = models.CharField(max_length=50)
    maintenance = models.CharField(max_length=50)

class HomeAddress(models.Model):
    address_1 = models.CharField(_("address"), max_length=255)
    address_2 = models.CharField(_("address"), max_length=255, blank=True)
    city = models.CharField(_("city"), max_length=150, default="Providence")
    state = USStateField(_("state"), default="RI")
    zip_code = models.CharField(_("zip code"), max_length=50, default="43760")
    
class StaffAndKeyPersonnel(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    work_phone = models.CharField(max_length=20)
    work_email = models.EmailField()
    
    home_address_line_1 = models.CharField(max_length=255)
    home_address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=50)
    
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    cell_phone = models.CharField(max_length=20, blank=True, null=True)
    pager_number = models.CharField(max_length=20, blank=True, null=True)
    home_email = models.EmailField(blank=True, null=True)
def __str__(self):
        return f"{self.first_name} {self.last_name}"
   # see the reference here for the choices >https://docs.djangoproject.com/en/4.2/ref/models/fields/
from django.db import models

class Reporter(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name

# Define the DisasterPlanResponsibility model
class DisasterPlanResponsibility(models.Model):
    RESPONSIBILITY_CHOICES = [
        ('Gathering collections information', 'Gathering collections information'),
        ('Preparing a staff list', 'Preparing a staff list'),
        ('Assessing risks', 'Assessing risks'),
        ('Devising opening and closing procedures', 'Devising opening and closing procedures'),
        ('Devising a preventive maintenance checklist', 'Devising a preventive maintenance checklist'),
        ('Determining salvage priorities', 'Determining salvage priorities'),
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
class InstitutionMaterials(models.Model):
    archival_materials = models.BooleanField(default=False)
    art_on_paper = models.BooleanField(default=False)
    audio_recordings_cd = models.BooleanField(default=False)
    audio_recordings_album = models.BooleanField(default=False)
    audio_recordings_tapes = models.BooleanField(default=False)
    books_rare = models.BooleanField(default=False)
    books_general_collection = models.BooleanField(default=False)
    dvds = models.BooleanField(default=False)
    computer_disks_magnetic = models.BooleanField(default=False)
    computer_tapes_magnetic = models.BooleanField(default=False)
    computer_cd_roms = models.BooleanField(default=False)
    film_motion_picture = models.BooleanField(default=False)
    manuscripts = models.BooleanField(default=False)
    maps_and_plans = models.BooleanField(default=False)
    microfiche = models.BooleanField(default=False)
    microfilm = models.BooleanField(default=False)
    natural_history_materials = models.BooleanField(default=False)
    negatives_polyester = models.BooleanField(default=False)
    negatives_acetate = models.BooleanField(default=False)
    negatives_nitrate = models.BooleanField(default=False)
    negatives_glass_plate = models.BooleanField(default=False)
    newspapers = models.BooleanField(default=False)
    objects_furniture_sculpture = models.BooleanField(default=False)
    organic_material = models.BooleanField(default=False)
    paintings = models.BooleanField(default=False)
    parchment_vellum_manuscripts = models.BooleanField(default=False)
    photographic_prints_bw = models.BooleanField(default=False)
    photographic_prints_color = models.BooleanField(default=False)
    photographs_cased = models.BooleanField(default=False)
    posters = models.BooleanField(default=False)
    scrapbooks = models.BooleanField(default=False)
    serials = models.BooleanField(default=False)
    textiles = models.BooleanField(default=False)
    transparencies_color = models.BooleanField(default=False)
    videocassettes = models.BooleanField(default=False)
    other = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Institution Materials

# Define the choices for the risk levels
RISK_CHOICES = (
    (1, 'Must be addressed'),
    (2, 'Should be addressed'),
    (3, 'Could be addressed'),
    (4, 'Not applicable/no action needed'),
)

# Common fields for risk assessments
class RiskAssessment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    other = models.TextField(blank=True, verbose_name='Other Comments')

    class Meta:
        abstract = True

# Building Systems Procedures Risk Assessment
class BuildingSystemsProceduresRisk(RiskAssessment):
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

    def __str__(self):
        return f'Building Systems Procedures Risk Assessment for {self.user.username}'

# Climate Control Risk Assessment
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

class OpeningProceduresChecklist(models.Model):
    RESPONSIBLE_CHOICES = [
        ('Primary', 'Primary'),
        ('Backup', 'Backup'),
    ]

    # Checklist items
    unusual_activity = models.BooleanField(default=False, verbose_name='No signs of unusual or off-hours activity')
    no_water_leakage = models.BooleanField(default=False, verbose_name='No evidence of water leakage (walls, ceilings, floors, storage areas)')
    no_unusual_smells_sounds = models.BooleanField(default=False, verbose_name='No unusual smells or sounds')
    no_change_in_temperature = models.BooleanField(default=False, verbose_name='No apparent major change in temperature overnight')
    no_change_in_humidity = models.BooleanField(default=False, verbose_name='No apparent major change in relative humidity overnight')
    no_appliances_plugged_in = models.BooleanField(default=False, verbose_name='No small appliances left plugged in overnight')
    lights_working = models.BooleanField(default=False, verbose_name='Lights are working (including emergency lighting)')
    doorbells_buzzers_intercom_working = models.BooleanField(default=False, verbose_name='Doorbells, buzzers, intercom are working')
    windows_locked_fire_doors_closed = models.BooleanField(default=False, verbose_name='Windows locked and fire doors closed')
    security_system_disarmed = models.BooleanField(default=False, verbose_name='Security system is disarmed as required')
    sinks_toilets_working = models.BooleanField(default=False, verbose_name='Sinks and toilets in working order')
    hvac_operating_properly = models.BooleanField(default=False, verbose_name='HVAC is operating properly')
    pumps_operating_properly = models.BooleanField(default=False, verbose_name='Pumps are operating properly')
    other_equipment = models.CharField(max_length=150, blank=True, verbose_name='Other equipment operating properly')
    known_problem_areas_checked = models.TextField(blank=True, verbose_name='Known problem areas checked')
    other_notes = models.TextField(blank=True, verbose_name='Other Notes')

    # Responsible staff
    responsible_staff = models.CharField(max_length=50, choices=RESPONSIBLE_CHOICES, default='Primary')

    def __str__(self):
        return 'Opening Procedures Checklist'

    class Meta:
        verbose_name_plural = 'Opening Procedures Checklist'

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
    day_of_week = models.CharField(max_length=50, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return f'Opening Staff Schedule for {self.get_day_of_week_display()}'

    class Meta:
        verbose_name_plural = 'Opening Staff Schedule'

class FacilitiesInformation(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name of Responsible Person/Department/Company')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=150, blank=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='ZIP Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return 'Facilities Information'

    class Meta:
        verbose_name_plural = 'Facilities Information'

class EmergencyShutOff(models.Model):
    facility_info = models.ForeignKey(FacilitiesInformation, on_delete=models.CASCADE, verbose_name='Facilities Information')
    shut_off_type = models.CharField(max_length=150, verbose_name='Emergency Shut-Off Type')
    location = models.TextField(verbose_name='Location Description')
    procedures = models.TextField(verbose_name='Procedures')

    def __str__(self):
        return f'Emergency Shut-Off for {self.shut_off_type}'

    class Meta:
        verbose_name_plural = 'Emergency Shut-Offs'

class FireDetectionAndSuppression(models.Model):
    # Fire Alarm Pull Box
    fire_alarm_pull_box = models.CharField(max_length=150, verbose_name='Fire Alarm Pull Box Number/Name')
    fire_alarm_pull_box_location = models.TextField(verbose_name='Location Description')

    # Fire Extinguishers
    FIRE_EXTINGUISHER_TYPES = [
        ('ABC', 'ABC'),
        ('Water', 'Water'),
        ('CO2', 'CO2'),
        ('Mist', 'Mist'),
    ]
    fire_extinguisher_type = models.CharField(max_length=50, choices=FIRE_EXTINGUISHER_TYPES, verbose_name='Type of Fire Extinguisher')
    fire_extinguisher_location = models.TextField(verbose_name='Location Description')
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection')

    # Smoke and Heat Detectors
    smoke_heat_detector_type = models.CharField(max_length=150, verbose_name='Type of Detector')
    smoke_heat_detector_location = models.TextField(verbose_name='Location Description')

    # Monitoring and Service
    last_inspection_maintenance_date = models.DateField(verbose_name='Date of Last Inspection/Maintenance')
    last_system_test_date = models.DateField(verbose_name='Date System Was Last Tested')
    monitoring_procedures = models.TextField(verbose_name='Description of Monitoring Procedures')

    def __str__(self):
        return f'Fire Detection and Suppression Information for {self.fire_alarm_pull_box}'

    class Meta:
        verbose_name_plural = 'Fire Detection and Suppression'

class SmokeHeatDetectionMonitoringAgency(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=150, blank=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='ZIP Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return 'Smoke and Heat Detection System Monitoring Agency'

    class Meta:
        verbose_name_plural = 'Smoke and Heat Detection System Monitoring Agencies'

class SmokeHeatDetectionServiceCompany(models.Model):
         name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=150, blank=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='ZIP Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return 'Smoke and Heat Detection System Service Company'

    class Meta:
        verbose_name_plural = 'Smoke and Heat Detection System Service Companies'

class SprinklerSystem(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location')
    description = models.TextField(verbose_name='Description/Type of Sprinkler System')
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection')
    last_flush_date = models.DateField(verbose_name='Date System Was Last Flushed')
    monitoring_procedures = models.TextField(verbose_name='Description of Monitoring Procedures')

    def __str__(self):
        return 'Sprinkler System Information'

    class Meta:
        verbose_name_plural = 'Sprinkler Systems'

class SprinklerSystemMonitoringAgency(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=150, blank=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='ZIP Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return 'Sprinkler System Monitoring Agency'

    class Meta:
        verbose_name_plural = 'Sprinkler System Monitoring Agencies'
class SprinklerSystemServiceCompany(models.Model):
         name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address Line 1')
    address2 = models.CharField(max_length=150, blank=True, verbose_name='Address Line 2')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='ZIP Code')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

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

class GaseousFireSuppressionSystem(models.Model):
    location = models.CharField(max_length=150, verbose_name='Location')
    suppression_system_type = models.CharField(max_length=150, verbose_name='Description/Type of Suppression System')
    age_of_system = models.PositiveIntegerField(verbose_name='Age of System', null=True, blank=True)
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection', null=True, blank=True)
    evacuation_plan_description = models.TextField(verbose_name='Description of Emergency Evacuation Plans', blank=True)
    
    # Monitoring and Service Information
    monitoring_procedures = models.TextField(verbose_name='Monitoring Procedures', blank=True)
    
    # Monitoring Agency
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
    
    # Service Company
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

class SecuritySystemMonitoringAgency(models.Model):
    security_system = models.ForeignKey(SecuritySystem, on_delete=models.CASCADE, related_name='monitoring_agencies')
    organization = models.CharField(max_length=150, verbose_name='Organization/Department')
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
        return f'Monitoring Agency for Security System at {self.security_system.location}'

class SecuritySystemServiceCompany(models.Model):
    security_system = models.ForeignKey(SecuritySystem, on_delete=models.CASCADE, related_name='service_companies')
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
        return f'Service Company for Security System at {self.security_system.location}

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

class HeatingSystemServiceCompany(models.Model):
    heating_system = models.ForeignKey(HeatingSystem, on_delete=models.CASCADE, related_name='service_companies')
    organization = models.CharField(max_length=150, verbose_name='Organization/Department')
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
        return f'Service Company for Heating System at {self.heating_system.location}'

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

class CoolingSystemServiceCompany(models.Model):
    cooling_system = models.ForeignKey(CoolingSystem, on_delete=models.CASCADE, related_name='service_companies')
    organization = models.CharField(max_length=150, verbose_name='Organization/Department')
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
        return f'Service Company for Cooling System at {self.cooling_system.location}'

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
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return self.name

class RegionalBuddyOrganization(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return self.name

# Create a reusable Contact model
class Contact(models.Model):
    name = models.CharField(max_length=150)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    after_hours_phone = models.CharField(max_length=15, blank=True)
    pager = models.CharField(max_length=15, blank=True)

    class Meta:
        abstract = True

# Create a model for IT Department
class ITDepartment(Contact):
    department_name = models.CharField(max_length=150)

# Create a model for Remote Storage Site
class RemoteStorageSite(Contact):
    account_number = models.CharField(max_length=50)
    backup_procedures = models.TextField()

# Create a model for Internet Service Provider
class InternetServiceProvider(Contact):
    account_number = models.CharField(max_length=50)
    restoration_procedures = models.TextField()

# Create a model for Web Site Host
class WebSiteHost(Contact):
    account_number = models.CharField(max_length=50)
    restoration_procedures = models.TextField()

# Create a model for Online Subscription Service
class OnlineSubscriptionService(Contact):
    account_number = models.CharField(max_length=50)
    restoration_procedures = models.TextField()

# Create a model for Regional Online Catalog/Network
class RegionalNetwork(Contact):
    regional_network_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=50)
    network_procedures = models.TextField()
from django.db import models

# Create a model for Software
class Software(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name of software package')
    supplier_and_version = models.CharField(max_length=150, verbose_name='Supplier and version')
    computers_installed_on = models.TextField(verbose_name='Computer(s) on which software is installed')
    registration_number = models.CharField(max_length=50, verbose_name='Registration number', blank=True)
    help_line_telephone_number = models.CharField(max_length=15, verbose_name='Help-line telephone number', blank=True)
    location_of_backup_copy = models.CharField(max_length=150, verbose_name='Location of backup copy', blank=True)
    insurance_coverage = models.CharField(max_length=150, verbose_name='Insurance Coverage', blank=True)

    def __str__(self):
        return self.name

# Create a model for Computer Hardware
class ComputerHardware(models.Model):
    make_and_model = models.CharField(max_length=150, verbose_name='Make and model')
    serial_number = models.CharField(max_length=50, verbose_name='Serial number', blank=True)
    location_of_equipment = models.CharField(max_length=150, verbose_name='Location of equipment', blank=True)
    vendor = models.CharField(max_length=150, verbose_name='Vendor')
    vendor_help_line_number = models.CharField(max_length=15, verbose_name='Vendor help line number', blank=True)
    drives_and_configuration = models.TextField(verbose_name='Drives and configuration', blank=True)
    insurance_coverage = models.CharField(max_length=150, verbose_name='Insurance Coverage', blank=True)

    def __str__(self):
        return self.make_and_model

# Create a model for Data Backup
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

# Create a model for Data Restoration
class DataRestoration(models.Model):
    staff_person_knows_how_to_restore = models.ForeignKey('DisasterResponseTeamMember', on_delete=models.CASCADE, related_name='data_restoration_staff', verbose_name='Staff Person')
    outside_person_or_organization_assist_restore = models.CharField(max_length=150, verbose_name='Name/Organization', blank=True)
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

    def __str__(self):
        return f'{self.staff_person_knows_how_to_restore.name} - {self.outside_person_or_organization_assist_restore}'

# Create a model for Software and Hardware Reconfiguration
class Reconfiguration(models.Model):
    staff_person_within_institution = models.ForeignKey('DisasterResponseTeamMember', on_delete=models.CASCADE, related_name='reconfiguration_staff', verbose_name='Staff Person')
    outside_person_or_organization_assist_reconfigure = models.CharField(max_length=150, verbose_name='Name/Organization', blank=True)
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

    def __str__(self):
        return f'{self.staff_person_within_institution.name} - {self.outside_person_or_organization_assist_reconfigure}'

# Create a model for Relocation of Computer Operations
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

# Create a model to represent the priority of administrative records
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

# Create a model to represent the priority of bibliographic records
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

# Create a model to represent departments and their priorities
class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name='Department Name')
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')

    def __str__(self):
        return self.name

# Create a model to represent collections and their priorities within departments
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


class InsuranceCarrier(models.Model):
    name = models.CharField(max_length=150, verbose_name='Company/Organization')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell phone', blank=True)
    after_hours_phone = models.CharField(max_length=15, verbose_name='After hours phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)

    def __str__(self):
        return self.name

class InsuranceAgent(models.Model):
    name = models.CharField(max_length=150, verbose_name='Company/Organization')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=50, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell phone', blank=True)
    after_hours_phone = models.CharField(max_length=15, verbose_name='After hours phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    frequency_of_review = models.CharField(max_length=150, verbose_name='Frequency of review and updating of this policy')
    person_responsible_for_review = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Person responsible for reviewing and updating this policy')

    def __str__(self):
        return self.name

class BusinessInterruptionInsurance(models.Model):
    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    inception_date = models.DateField(verbose_name='Policy Inception Date')
    expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    coverage_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Business Interruption Insurance Provided')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)
    
    # Insurance carrier information
    carrier_company = models.CharField(max_length=150, verbose_name='Company/Organization')
    carrier_contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    carrier_address1 = models.CharField(max_length=150, verbose_name='Address1')
    carrier_address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    carrier_city = models.CharField(max_length=50, verbose_name='City')
    carrier_state = models.CharField(max_length=2, verbose_name='State')
    carrier_zip = models.CharField(max_length=50, verbose_name='Zip')
    carrier_phone = models.CharField(max_length=15, verbose_name='Phone')
    carrier_cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    carrier_after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    carrier_pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    
    # Insurance agent or broker information
    agent_company = models.CharField(max_length=150, verbose_name='Company/Organization')
    agent_contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    agent_address1 = models.CharField(max_length=150, verbose_name='Address1')
    agent_address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    agent_city = models.CharField(max_length=50, verbose_name='City')
    agent_state = models.CharField(max_length=2, verbose_name='State')
    agent_zip = models.CharField(max_length=50, verbose_name='Zip')
    agent_phone = models.CharField(max_length=15, verbose_name='Phone')
    agent_cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    agent_after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    agent_pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    
    review_frequency = models.CharField(max_length=50, verbose_name='Frequency of Review and Updating of this Policy')
    responsible_person = models.CharField(max_length=150, verbose_name='Person Responsible for Reviewing and Updating this Policy', choices=YOUR_CHOICES)

    def __str__(self):
        return f'Policy Number: {self.policy_number}'

class ExtraExpensesInsurance(models.Model):
    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    inception_date = models.DateField(verbose_name='Policy Inception Date')
    expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    coverage_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Extra Expenses Insurance Provided')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)
    
    # Insurance carrier information
    carrier_company = models.CharField(max_length=150, verbose_name='Company/Organization')
    carrier_contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    carrier_address1 = models.CharField(max_length=150, verbose_name='Address1')
    carrier_address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    carrier_city = models.CharField(max_length=50, verbose_name='City')
    carrier_state = models.CharField(max_length=2, verbose_name='State')
    carrier_zip = models.CharField(max_length=50, verbose_name='Zip')
    carrier_phone = models.CharField(max_length=15, verbose_name='Phone')
    carrier_cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    carrier_after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    carrier_pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    
    # Insurance agent or broker information
    agent_company = models.CharField(max_length=150, verbose_name='Company/Organization')
    agent_contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    agent_address1 = models.CharField(max_length=150, verbose_name='Address1')
    agent_address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    agent_city = models.CharField(max_length=50, verbose_name='City')
    agent_state = models.CharField(max_length=2, verbose_name='State')
    agent_zip = models.CharField(max_length=50, verbose_name='Zip')
    agent_phone = models.CharField(max_length=15, verbose_name='Phone')
    agent_cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    agent_after_hours_phone = models.CharField(max_length=15, verbose_name='After Hours Phone', blank=True)
    agent_pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    
    review_frequency = models.CharField(max_length=50, verbose_name='Frequency of Review and Updating of this Policy')
    responsible_person = models.CharField(max_length=150, verbose_name='Person Responsible for Reviewing and Updating this Policy', choices=YOUR_CHOICES)

    def __str__(self):
        return f'Policy Number: {self.policy_number}'

class SpecialCollectionsInsurance(models.Model):
    office_department = models.CharField(max_length=150, verbose_name='Office/Department in Charge of Self-Insurance')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zip_code = models.CharField(max_length=50, verbose_name='Zip')
    work_phone = models.CharField(max_length=15, verbose_name='Work Phone')
    home_phone = models.CharField(max_length=15, verbose_name='Home Phone', blank=True)
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)

    def __str__(self):
        return f'Office/Department: {self.office_department} - Contact Person: {self.contact_person}'

class InsuranceCoverage(models.Model):
    funds_for_recovery = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Funds Available for Salvage, Repair, and/or Replacement of Collections (in dollars)')
    collections_appraised = models.TextField(verbose_name='Collections Appraised for Insurance Purposes')
    date_of_last_appraisal = models.DateField(verbose_name='Date of Last Appraisal')
    person_conducting_appraisal = models.CharField(max_length=150, verbose_name='Person Conducting Appraisal')
    person_responsible_for_evaluation = models.CharField(max_length=150, verbose_name='Person Responsible for Periodic Evaluation of Funds')
    frequency_of_evaluation = models.CharField(max_length=50, verbose_name='Frequency of Evaluation and Increase of Funds Set Aside for Self-Insurance')
    procedures_in_case_of_damage = models.TextField(verbose_name='Procedures in Case of Damage or Loss')
    documentation_required = models.TextField(verbose_name='Documentation Required to Prove Loss')

    def __str__(self):
        return f'Funds Available: ${self.funds_for_recovery}'

class EvacuationProcedure(models.Model):
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for Clearing Area')
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1')
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2')
    evacuation_procedures = models.TextField(verbose_name='Procedures for Evacuating the Building, Including Disabled Personnel or Patrons')

    def __str__(self):
        return f'Evacuation Area: {self.area_or_floor}'

class StaffVisitorLog(models.Model):
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for List')
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1')
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2')

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
    location = models.CharField(max_length=300, verbose_name='Location')
    space_available = models.CharField(max_length=150, verbose_name='Space Available')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After-Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')

    def __str__(self):
        return f'{self.location_type} - {self.location}'

class FireDepartmentInfo(models.Model):
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection by Fire Marshal')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Fire Department')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    in_house_liaison = models.CharField(max_length=150, verbose_name='In-house Liaison to Fire Department')
    backup_liaison = models.CharField(max_length=150, verbose_name='Backup Liaison')
    last_in_house_review_date = models.DateField(verbose_name='Date of Last In-house Review of Collection Priorities')
    last_on_site_review_date = models.DateField(verbose_name='Date of Last On-site Review with Fire Department Personnel')

    def __str__(self):
        return f'Fire Department Information'

class PoliceDepartmentInfo(models.Model):
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Police Department')
    title = models.CharField(max_length=50, verbose_name='Title')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    in_house_liaison = models.CharField(max_length=150, verbose_name='In-house Liaison to Police Department')
    backup_liaison = models.CharField(max_length=150, verbose_name='Backup Liaison')
    last_on_site_review_date = models.DateField(verbose_name='Date of Last On-site Review with Police Department Personnel')

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

    class Meta:
        verbose_name_plural = 'Emergency Services'
# maintanance utilities  this is last updated need to clear up the codes






