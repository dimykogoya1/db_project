from django.db import models
from django.contrib.auth.models import User
from enum import Enum, auto
from django.forms import ModelForm
from django.contrib.auth.models import User


class Institution(models.Model):
    name = models.CharField(max_length=40)
    code= models.CharField(max_length=3)
    address=models.ForeignKey("Addresse", on_delete=models.CASCADE, related_name="institution")
    
    class Meta:
        ordering = ['name','code']
        
    def __str__(self):
        return self.name
    
class Address(models.Model):
    street=models.CharField(max_length=50, verbose_name="strett Name")
    city=models.ForeignKey("City", on_delete=models.CASCADE, related_name="address")
    zip_code=models.CharField("zip_code", max_length=10)

class Meta:
    ordering =['street', 'zip_code']
    def __str__(self):
          return f"{self.street} {self.city.name}, {self.city.state} {self.zip_code}"
      
class City(models.Model):
    name = models.CharField("City", max_length=100)
    state = models.DateField("state", default="RI")
    
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
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.ForeignKey("Position", on_delete=models.CASCADE, related_name="contact")
    phone = models.CharField(default='', max_length=30)
    email = models.EmailField(blank=True, null=True)
      
    def __str__(self):
        return self.name
    
class Reporter(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Responsibilities(models.Model):
    TASK_CHOICES = (
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
    )

    responsibility = models.CharField(max_length=3, choices=TASK_CHOICES)
    def __str__(self):
        return self.get_responsibility_display()
    
RISK_CHOICES = (
    (1, 'Must be addressed'),
    (2, 'Should be addressed'),
    (3, 'Could be addressed'),
    (4, 'Not applicable/no action needed'),
)
class BaseMaterial(models.Model):
    name = models.CharField(max_length=50)
    risk_level = models.IntegerField(choices=RISK_CHOICES, default=4, verbose_name='Risk Level')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class ClimateControlRisk(models.Model):
    heating_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Heating System')
    cooling_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Cooling System')
    humidification_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Humidification System')
    air_circulation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Air Circulation')
    building_closed = models.IntegerField(choices=RISK_CHOICES, verbose_name='Building Closed in Winter')
    temperature_extremes = models.IntegerField(choices=RISK_CHOICES, verbose_name='Temperature Extremes')
    humidity_extremes = models.IntegerField(choices=RISK_CHOICES, verbose_name='Humidity Extremes')
    mold_infestation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Mold Infestation')
    collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Collections in Uncontrolled Areas')

    def __str__(self):
        return f'Climate Control Risk Assessment for {self.user.username}'
  
class RiskLevel(models.TextChoices):
    MUST_BE_ADDRESSED = '1', 'Must be addressed'
    SHOULD_BE_ADDRESSED = '2', 'Should be addressed'
    COULD_BE_ADDRESSED = '3', 'Could be addressed'
    NOT_APPLICABLE = '4', 'Not applicable/no action needed'

class RiskAssessmentBase(models.Model):
    class Meta:
        abstract = True

class RiskAssessment(models.Model):
    risk_level = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Risk Level'
    )

    class Meta:
        abstract = True

class RiskAssessmentMixin(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return f'{self._meta.verbose_name} Risk Assessment for {self.user.username}'

class SecurityRisk(RiskAssessmentBase, RiskAssessmentMixin):
    automated_security_system = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Automated Security System'
    )

class HousekeepingPestsRisk(RiskAssessmentBase, RiskAssessmentMixin):
    pest_infestation = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Pest Infestation'
    )

class StorageRisk(RiskAssessmentBase, RiskAssessmentMixin):
    anchor_shelving = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Anchor Shelving'
    )

class PersonnelRisk(RiskAssessmentBase, RiskAssessmentMixin):
    staff_training_emergency_procedures = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Staff Training'
    )
    staff_training_security_procedures = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Security Procedures'
    )
    security_staff_training_recognizing_hazards = models.CharField(
        max_length=1,
        choices=RiskLevel.choices,
        verbose_name='Recognizing Hazards'
    )

class TaskStatus(Enum):
    NOT_DONE = auto(), 'Not Done'
    DONE = auto(), 'Done'

class BasePMTask(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    task_date = models.DateField()
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.get_task_type()} PM Tasks for {self.user.username} on {self.task_date}'

    def get_task_type(self):
        raise NotImplementedError("Subclasses must implement this method")

class DailyPMTask(BasePMTask):
    clean_restrooms = models.BooleanField(default=False)
    stack_maintenance = models.BooleanField(default=False)
    empty_garbage = models.BooleanField(default=False)
    shovel_snow = models.BooleanField(default=False)
    vacuum_floors = models.BooleanField(default=False)

    def get_task_type(self):
        return 'Daily'

class WeeklyPMTask(BasePMTask):
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
  
    @staticmethod
    def weekly_plan():
        return "weekly"

class SeasonalPMTask(BasePMTask):
    check_caulking = models.BooleanField(default=False)
    clean_gutters = models.BooleanField(default=False)
    check_clean_storm_drains = models.BooleanField(default=False)
    winterize_grounds = models.BooleanField(default=False)
    seasonal_heating_cooling_check = models.BooleanField(default=False)
    spring_planting_maintenance = models.BooleanField(default=False)

    @staticmethod
    def task_type():
        return "Seasonal"

class BiannualPMTask(BasePMTask):
    hold_fire_drill = models.BooleanField(default=False)
    inspect_roof_drainage = models.BooleanField(default=False)
    inspect_windows_skylights = models.BooleanField(default=False)
    inspect_building_foundation = models.BooleanField(default=False)
    inspect_fire_detection_system = models.BooleanField(default=False)
    inspect_fire_suppression_system = models.BooleanField(default=False)
    inspect_security_system = models.BooleanField(default=False)
    general_inspection = models.BooleanField(default=False)

    @staticmethod
    def Bannul_task():
        return "Biannual"

class AnnualPMTask(BasePMTask):
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

    @staticmethod
    def Annual(self):
        return "Annual"
    
class ClosingStaffSchedule(models.Model):
    DAYS_OF_WEEK = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    primary_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='primary_closing_staff')
    backup_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backup_closing_staff')
    day_of_week = models.PositiveIntegerField(choices=DAYS_OF_WEEK, unique=True)

    class Meta:
        verbose_name_plural = 'Closing Staff Schedule'

        def __str__(self):
         return f'Closing Staff Schedule for {self.get_day_of_week_display()}'
        
class Question(models.Model):
  CATEGORY_CHOICES = [
      ('OP', 'Operating Procedures'),
      ('CP', 'Closing Procedures'),
  ]
  
  text = models.TextField(max_length=250, verbose_name="Text")
  category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
  
  def __str__(self):
      return self.text

class Questionaire(models.Model): 
  institution = models.ForeignKey("Institution", on_delete=models.CASCADE, related_name="tasks")
  question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="qs")
  primary = models.ForeignKey("Contact1", on_delete=models.CASCADE, related_name="primary_responsabilities")
  backup = models.ForeignKey("Contact2", on_delete=models.CASCADE, related_name="secondary_responsabilities")
  
  def __str__(self):
    return self.question.text
    
class Tasks(models.Model):
  name = models.ForeignKey("Institution", verbose_name="Institution Name", on_delete=models.CASCADE)
  question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="qs")
  answer = models.BooleanField()
  items =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='Operating procedure', null=True, blank=True)

  def __str__(self):
      return self.name
  
class WeeklyOpening(models.Model):
    DAYS_OF_WEEK = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    primary_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='primary_opening_staff', null=True, blank=True)
    backup_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backup_opening_staff', null=True, blank=True)
    day_of_week = models.PositiveIntegerField(choices=DAYS_OF_WEEK, unique=True)

    class Meta:
        verbose_name_plural = 'Weekly Opening Staff Schedules'

        def __str__(self):
            return f'Weekly Opening Staff Schedule for {self.get_day_of_week_display()}'
    
class FacilitiesInfo(models.Model):
        name = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="Facilitties")
        street = models.CharField(max_length=50)
        zip_code =models.CharField(max_length=50)

        def __str__(self):
            return f"{self.name}"

class EmergencyShutOff(models.Model):
    facility_info = models.ForeignKey("FacilitiesInformation", on_delete=models.CASCADE, verbose_name='Facilities Information')
    shut_off_type = models.CharField(max_length=300, verbose_name='Emergency Shut-Off Type')
    location = models.ForeignKey("location",on_delete=models.CASCADE, verbose_name='Location Description')
    procedures = models.TextField(verbose_name='Procedures')

    class Meta:
        verbose_name_plural = 'Emergency Shut-Offs'

    def __str__(self):
        return f'Emergency Shut-Off for {self.shut_off_type}'


class FireExtinguisherType(models.TextChoices):
    ABC = 'ABC', 'ABC'
    WATER = 'Water', 'Water'
    CO2 = 'CO2', 'CO2'
    MIST = 'Mist', 'Mist'

class FireDetection(models.Model):
    fire_alarm_pull_box_number = models.CharField(max_length=255, verbose_name='Fire Alarm Pull Box Number/Name')
    fire_alarm_box_location = models.TextField(verbose_name='Location Description')

    fire_extinguisher_type = models.CharField(
        max_length=200,
        choices=FireExtinguisherType.choices,
        verbose_name='Type of Fire Extinguisher'
    )
    fire_location_description = models.TextField(verbose_name='Location Description')
    last_inspection_date = models.DateField(verbose_name='Date of Last Inspection')
    heat_detector_type = models.CharField(max_length=300, verbose_name='Type of Detector')
    monitoring_description = models.TextField(max_length=300, verbose_name='Description of Monitoring Procedures')

    def __str__(self):
        return f'Fire Detection and Suppression Information for {self.fire_alarm_pull_box_number}'

    class Meta:
        verbose_name_plural = 'Fire Detection and Suppression Information'
        
class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name="Location Name")

    def __str__(self):
        return self.name

class Companies(models.Model):
    name = models.ForeignKey("Name", verbose_name="Company Name", on_delete=models.CASCADE)
    heat_detectors = models.CharField(max_length=50)
    smoke_detectors = models.CharField(max_length=50)
    sprinklers = models.CharField(max_length=50, verbose_name='Sprinklers System')
    location = models.ForeignKey("Location", verbose_name="Location", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

class ServiceType(models.Model):
    name = models.ForeignKey("Type", verbose_name="Type of Service", on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField()
    description = models.CharField(max_length=300)
    monitoring_type = models.CharField(max_length=100, verbose_name='Monitoring Type')

    def __str__(self):
        return f"{self.name} {self.date_created} {self.description}"

class Services(models.Model):
    name = models.ForeignKey(Companies, verbose_name="Company", on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    addresses = models.ManyToManyField("Address", related_name='companies')
    phone = models.CharField(max_length=30, verbose_name='Phone Number')
    after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=20, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return str(self.name)

class GasCompanies(models.Model):
    name = models.ForeignKey("company",verbose_name="Gas Company", on_delete=models.CASCADE)
    addresses = models.ManyToManyField("Address",related_name="address")
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")
    location = models.ForeignKey(Location, verbose_name="Location", on_delete=models.CASCADE)
    services = models.CharField(max_length=100, verbose_name="Services")

    def __str__(self):
        return str(self.name)

class Services(models.Model):
    name = models.ForeignKey("Services", verbose_name="Service", on_delete=models.CASCADE)
    date_created = models.DateField(blank=True, null=True)
    date_updated = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=250, verbose_name='Emergency Evacuation Plans')
    addresses = models.ManyToManyField(Address, related_name='companies')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    after_hours = models.CharField(max_length=20, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=20, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return f"{self.name} {', '.join(map(str, self.addresses.all()))}"

class WaterDetector(models.Model):
    name = models.ForeignKey("Department", verbose_name="Water Detection", on_delete=models.CASCADE)
    location = models.CharField(max_length=50, verbose_name="Location")
    city = models.ForeignKey("City",on_delete=models.CASCADE, verbose_name="City")
    street = models.ForeignKey(Address, verbose_name="Street Name", on_delete=models.CASCADE)

    def __str__(self):
        return f'Water Detector at {self.location}'

class WaterDetectorCategory(models.Model):
    text = models.CharField(max_length=200, verbose_name="Text")
    detector_type = models.CharField(max_length=150, verbose_name='Type of Water Detector')
    location = models.ForeignKey("Location",verbose_name='Location', on_delete=models.CASCADE)
    monitoring_procedures = models.TextField(verbose_name='Monitoring Procedures', blank=True)

    class Meta:
        ordering = ['text']

    def __str__(self):
        return self.text
    
class State(models.Model):
    name = models.CharField(max_length=150, verbose_name='State Name')

    def __str__(self):
        return self.name


class HeatingCompany(models.Model):
    name = models.ForeignKey("ContactInfo", on_delete=models.CASCADE, related_name="heating_service_company")
    street = models.ForeignKey("Street", on_delete=models.CASCADE,related_name="street_name")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='heating_service_company_address')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)

        
class Name(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class CoolingSystem(models.Model):
    name = models.CharField(max_length=50, verbose_name="Organization Name")
    location = models.ForeignKey("Locations",on_delete=models.CASCADE, verbose_name="Places")
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="city")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class DisasterTeam(models.Model):
    ROLE_CHOICES = [
        ('Primary', 'Primary'),
        ('Backup 1', 'Backup 1'),
        ('Backup 2', 'Backup 2'),
    ]

    name = models.ForeignKey("Name",max_length=150, verbose_name='Name')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role')
    contact_phone = models.CharField(max_length=30, verbose_name='Phone')
    contact_cell_phone = models.CharField(max_length=20, verbose_name='Cell Phone', blank=True)
    contact_after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone', blank=True)
    contact_email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return f'{self.name} - {self.role}'

class TeamResponsibility(models.Model):
    RESPONSIBILITY_CHOICES = [
        (1, 'Disaster Team Leader'),
        (2, 'Administrator/Supplies Coordinator'),
        (3, 'Collections Recovery Specialist'),
        (4, 'Subject Specialist/Department Head'),
        (5, 'Work Crew Coordinator'),
        (6, 'Technology Coordinator'),
        (7, 'Building Recovery Coordinator'),
        (8, 'Security Coordinator'),
        (9, 'Public Relations Coordinator'),
        (10, 'Documentation Coordinator'),
    ]
    name = models.ForeignKey("Name", on_delete=models.CASCADE, related_name='team_responsibilities')
    responsibility = models.IntegerField(choices=RESPONSIBILITY_CHOICES, verbose_name='Responsibility')
    team_member = models.ForeignKey("TeamName", on_delete=models.CASCADE, related_name='team_member_responsibilities')

    def __str__(self):
        return f'{self.get_responsibility_display()} - {self.team_member.name}'
    
class DataBackup(models.Model):
    DATA_TYPE_CHOICES = [
        ('Collection Records', 'Collection Records'),
        ('In-house Databases', 'In-house Databases'),
        ('Financial Information', 'Financial Information'),
        ('Digital Collections', 'Digital Collections'),
    ]

    type_of_data = models.CharField(max_length=150, choices=DATA_TYPE_CHOICES, verbose_name='Type of Data')
    location_of_data = models.CharField(max_length=150, verbose_name='Location of Data')
    person_backup = models.ForeignKey('DisasterResponseTeamMember', on_delete=models.CASCADE, related_name='data_backups')
    on_site_backup = models.CharField(max_length=150, verbose_name='On-site Location of Backup', blank=True)
    off_site_location = models.CharField(max_length=150, verbose_name='Off-site Location of Backup', blank=True)
    frequency = models.CharField(max_length=50, verbose_name='Frequency of Backup', blank=True)

    def __str__(self):
        return f'{self.type_of_data} - {self.location_of_data}'


class CommonFields(models.Model):
    staff_person = models.ForeignKey("DisasterResponseTeamMember", on_delete=models.CASCADE, verbose_name='Staff Person')
    outside_organization = models.CharField(max_length=150, verbose_name='Organization', blank=True)
    title_or_contact = models.CharField(max_length=150, verbose_name='Title/Contact', blank=True)
    address1 = models.CharField(max_length=150, verbose_name='Address1', blank=True)
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.ForeignKey("City", max_length=150, on_delete=models.CASCADE)
    state = models.ForeignKey("State",verbose_name='State', on_delete=models.CASCADE)
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
    
class ComputerOperation(models.Model):
    OPERATION_CATEGORIES = [
        ('OR', 'Computer Operation Relocation'),
        ('ERA', 'Emergency Remote Access'),
        ('P', 'Procedures'),
        ('LW', 'Library Website'),
    ]

    category = models.CharField(max_length=3, choices=OPERATION_CATEGORIES, verbose_name='Category')
    procedures = models.TextField(verbose_name='Procedures', blank=True)
    computer = models.ForeignKey("Computer", verbose_name="Computer", on_delete=models.CASCADE)
    intranet = models.TextField(verbose_name='Intranet', blank=True)
    website = models.TextField(verbose_name='Library Website', blank=True)
    regional_network = models.TextField(verbose_name='Regional Library Network', blank=True)
    online_catalog = models.TextField(verbose_name='Local Online Catalog', blank=True)
    subscription_services = models.TextField(verbose_name='Online Subscription Services', blank=True)
    other = models.TextField(verbose_name='Other', blank=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return f'{self.category} - {self.computer.name}'
    
class AdministrativeRecord(models.Model):
    PRIORITY_CHOICES = (
        (1, 'Priority 1'),
        (2, 'Priority 2'),
        (3, 'Priority 3'),
        (4, 'Priority 4'),
        (5, 'Priority 5'),
    )

    priority_ranking = models.IntegerField(choices=PRIORITY_CHOICES, verbose_name='Priority Ranking')
    record_type = models.CharField(max_length=150, verbose_name='Type of Record Group')
    location = models.ForeignKey("Location",max_length=300, verbose_name='Location of Records')

    class Meta:
        ordering = ['priority_ranking']

    def __str__(self):
        return f'{self.get_priority_ranking_display()} - {self.record_type}'


class PriorityMixin(models.Model):
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')

    class Meta:
        abstract = True

class Department(PriorityMixin):
    name = models.CharField(max_length=150, verbose_name='Department Name')

    def __str__(self):
        return self.name

class Collection(PriorityMixin):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=150, verbose_name='Collection Name')
    location = models.CharField(max_length=300, verbose_name='Location floor')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Collections'

class OverallSalvagePriority(PriorityMixin):
    material_or_equipment = models.CharField(max_length=150, verbose_name='Material or Equipment')
    location = models.CharField(max_length=300, verbose_name='Location Floor')

    def __str__(self):
        return self.material_or_equipment

    class Meta:
        verbose_name_plural = 'Overall Salvage Priorities'

class BuildingPlan(models.Model):
    name = models.ForeignKey("Bulding",on_delete=models.CASCADE, verbose_name='Plan Name')
    description = models.TextField(verbose_name='Plan Description')
    color_code = models.CharField(max_length=20, verbose_name='Color Code')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Building Plans'


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
    name = models.ForeignKey("Company", max_length=50, verbose_name='Company Name')
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name='City')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Inventories(models.Model):
    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    inception_date = models.DateField(verbose_name='Policy Inception Date')
    expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    coverage_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Business')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)
    frequency_of_review = models.CharField(max_length=150, verbose_name='Frequency of review')
    person_responsible_for_review = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Person responsibily')

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

class InsuranceType(models.Model):
    IC_CHOICES = [
        ('IC', 'Insurance Carrier'),
        ('IA', 'Insurance Agency'),
    ]

    policy1 = models.CharField(max_length=50, choices=IC_CHOICES, related_name='policy_information')
    policy2 = models.CharField(max_length=50, choices=IC_CHOICES, related_name='policy_information_business')

    def __str__(self):
        return self.name
     
RESPONSIBILITY_CHOICES = (
    ('person_1', 'Person 1'),
    ('person_2', 'Person 2'),
    ('backup_1', 'Backup #1'),
    ('backup_2', 'Backup #2'),
)

FREQUENCY_CHOICES = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annually', 'Annually'),
)

class InsuranceCoverage(models.Model):
    funds = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Funds Available for Salvage, Repair (in dollars)')
    collections = models.TextField(verbose_name='Collections Appraised')
    date_of_last = models.DateField(verbose_name='Date of Last Appraisal')
    conducting = models.CharField(max_length=150, verbose_name='Person Conducting Appraisal')
    responsible = models.CharField(max_length=150, verbose_name='Person Responsible', choices=RESPONSIBILITY_CHOICES)
    frequency = models.CharField(max_length=50, verbose_name='Frequency of Evaluation', choices=FREQUENCY_CHOICES)
    procedures = models.TextField(verbose_name='Procedures in Case of Damage or Loss')
    documentation = models.TextField(verbose_name='Documentation Required')

    def __str__(self):
        return f'Funds Available: ${self.funds}'

class EvacuationProcedure(models.Model):
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for Clearing Area', choices=RESPONSIBILITY_CHOICES)
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1', choices=RESPONSIBILITY_CHOICES)
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2', choices=RESPONSIBILITY_CHOICES)
    evacuation_procedures = models.TextField(verbose_name='Evacuation procedure')

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
    staff_member_in_charge = models.CharField(max_length=150, verbose_name='Staff Member')
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

class CollectionStorage(models.Model):
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
    location = models.ForeignKey("locations", verbose_name='Location',on_delete=models.CASCADE )
    space_available = models.CharField(max_length=150, verbose_name='Space Available')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After-Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')

    def __str__(self):
        return f'{self.location_type} - {self.location}'
        
class Organiztion(models.Model):
    CATEGORIES_CHOICES = [
        ('PD', 'Police Department'),
        ('EM', 'Emergency Management'),
        ('LM', 'Local Emergency Management'),
        ('ES', 'Egermency Services'), 
    ]
    emergency_services = models.CharField(max_length=50, choices = CATEGORIES_CHOICES, verbose_name = 'emergency services ')
    city = models.ManyToManyField("city", verbose_name="City")
    state = models.CharField("state", max_length=50)
    Zip_code = models.ForeignKey("Zip_code", verbose_name="area code", on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Fire Department')
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    fax = models.CharField(max_length=15, verbose_name='Fax')
    website = models.URLField(max_length=300, verbose_name='Website')

    
    class Meta:
        ordering =['name','city']
    def __str__(self):
        return self.name
        
class Services(models.Model):
    name = models.CharField(max_length=50, related_name="Service")
    backup = models.CharField(max_length=50, verbose_name="backup liason")
    date = models.DateField(auto_now=False, auto_now_add=False)
    review_date = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Date Review of Collection Priorities')
    inspection_date = models.DateField(verbose_name='Date of Last Inspection by Fire Marshal')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Fire Department')
    
    def __str__(self):
        return f'Emergency Services'
        
class NonOrganization(models.Model):
    MAINTENANCE_CHOICES = (
        ("maintenance", "Maintenance"),
        ("utilities", "Utilities"),
        ("facilities", "Facilities"),
        ("janitorial", "Janitorial"),
        ("electrician", "Electrician"),
        ("plumber", "Plumber"),
    )

    maintenance = models.CharField("Maintenance", max_length=50, choices=MAINTENANCE_CHOICES)
    utilities = models.CharField("Utilities", max_length=50, choices=MAINTENANCE_CHOICES)
    facilities = models.CharField("Facilities", max_length=50, choices=MAINTENANCE_CHOICES)
    janitorial_services = models.CharField("Janitorial Services", max_length=50, choices=MAINTENANCE_CHOICES)
    electrician = models.CharField("Electrician", max_length=50, choices=MAINTENANCE_CHOICES)
    plumber = models.CharField("Plumber", max_length=50, choices=MAINTENANCE_CHOICES)

    class Meta:
        ordering = ['maintenance']

    def __str__(self):
        return f"Organization {self.id}"
     
class Organization(models.Model):
    CATEGORIES_CHOICES = [
        ('CE', 'Computer Emergency'),
        ('O', 'Organization'),
        ('CA', 'Legal Advisor'),
        ('AB', 'Architecture Builder'),
        ('GC', 'Gas Company'),
        ('OC', 'Oil Company'),
        ('EC', 'Electric Company'),
        ('WUC', 'Water Utility Company'),
        ('ECO', 'Elevator Company'),
    ]

    name = models.CharField(max_length=100)
    categories = models.CharField(max_length=3, choices=CATEGORIES_CHOICES, verbose_name="Categories")
  
    def __str__(self):
        return self.name
  
  
class Municipality(models.Model):
    state = models.CharField(max_length=50)
    city = models.ForeignKey("City",on_delete=models.CASCADE, related_name="city" )
    zip_code = models.CharField(max_length=50)
    
    class Meta:
        unique_together = ['city', 'state']
        ordering = ['city']

    def __str__(self):
        return f'{self.city}, {self.state}'



