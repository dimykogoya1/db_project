from django.db import models
#from django.contrib.auth.models import User
#You are still referencing the user model. The 'user-type' you are creating does not need an account to access the system.
from enum import Enum, auto
#from django.forms import ModelForm
# You are not using Forms yet, at least not under models.


class Institution(models.Model):
    name = models.CharField(max_length=40)
    code= models.CharField(max_length=3)
    address=models.ForeignKey("Address", on_delete=models.CASCADE, related_name="institution")
    
    class Meta:
        ordering = ['name','code']
        
    def __str__(self):
        return self.name
    
class Address(models.Model):
    street=models.CharField(max_length=50, verbose_name="strett Name")
    city=models.ForeignKey("City", on_delete=models.CASCADE, related_name="address") #usually, related name uses the plural of the referenced object.
    zip_code=models.CharField(max_length=10)         #CharField has not attribute "zip_code". 

    class Meta:
        ordering =['street', 'zip_code']
    def __str__(self):
        return f"{self.street} {self.city.name}, {self.city.state} {self.zip_code}"

      
class City(models.Model):
    name = models.CharField("City", max_length=100)
    state = models.CharField(max_length=20, default="RI") #Datefield for a two character Varchar/CharField?
    
    class Meta:
        unique_together = ['name', 'state']
        ordering = ['name']
        
    def __str__(self):
        return self.name
       
class Position(models.Model):
    name = models.CharField(max_length=50,unique=True) #You need to be consistent with your use of spaces. Two between classes, one between definitions. 

    class Meta:
        ordering=['name']
        
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.ForeignKey("Position", on_delete=models.CASCADE, related_name="contact") #Plural
    phone = models.CharField(default='', max_length=30) #Empty defaults are not a good practice
    email = models.EmailField(blank=True, null=True)
      
    def __str__(self):
        #return self.name # There is no name attribute. Were you trying to do something along the lines of 
        return f"{self.first_name} {self.last_name}"
    
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

    name = models.ForeignKey("Responsibility", on_delete=models.CASCADE, related_name="task_responsibility")
    responsibility = models.CharField(max_length=3, choices=TASK_CHOICES)

    class Meta:
        ordering = ['responsibility', 'name']
       
    def __str__(self):
        return f"{self.responsibility.name}"   # get_responsability_display() is a funtion that works under the template (Jinja) not as part of the model.
                                                # Also, you cannot call a function/helper without any reference, there is no attribute get_responsability_display() in the class.
    
RISK_CHOICES = (
    (1, 'Must be addressed'),
    (2, 'Should be addressed'),
    (3, 'Could be addressed'),
    (4, 'Not applicable/no action needed'),
)
class BaseMaterial(models.Model):
    name = models.CharField(max_length=50)
    risk_level = models.IntegerField(choices=RISK_CHOICES, choices=4, verbose_name='Risk Level')     #Again, defaults are a bad practice. Also, if you are adding verbose name to one attribute, you should add them to all.
                                                                                                     #Also, the system automatically converts word_anotherword into Word Anotheword while displaying data through the template.
    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class ClimateControlRisk(models.Model):
    name = models.ForeignKey("Name", on_delete=models.CASCADE, related_name="name")
    heating_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Heating System')
    cooling_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Cooling System')
    humidification_system = models.IntegerField(choices=RISK_CHOICES, verbose_name='Humidification System')
    air_circulation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Air Circulation')
    building_closed = models.IntegerField(choices=RISK_CHOICES, verbose_name='Building Closed in Winter')
    temperature_extremes = models.IntegerField(choices=RISK_CHOICES, verbose_name='Temperature Extremes')
    humidity_extremes = models.IntegerField(choices=RISK_CHOICES, verbose_name='Humidity Extremes')
    mold_infestation = models.IntegerField(choices=RISK_CHOICES, verbose_name='Mold Infestation')
    collections = models.IntegerField(choices=RISK_CHOICES, verbose_name='Collections in Uncontrolled Areas') #This was a good use of verbose name

    class Meta:
        ordering = ['name']
    def __str__(self):
       return f'Climate Control Risk Assessment for {self.name}' #This will retunr an error, as the class has not foreign keys, much less one to the User model (which you should not be using like this anyway.)
  
class RiskLevel(models.TextChoices): # What is the difference between RiskLevel and RISK_CHOICES? (line 125 and line 94)
    MUST_BE_ADDRESSED = '1', 'Must be addressed'
    SHOULD_BE_ADDRESSED = '2', 'Should be addressed'
    COULD_BE_ADDRESSED = '3', 'Could be addressed'
    NOT_APPLICABLE = '4', 'Not applicable/no action needed'
    #Were you trying to create tuples as the values? You can assign X,Z = 1, 2, but not X = 1,2

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
        return f'{self._meta.verbose_name} Risk Assessment for {self.user.username}' #Again, you are referencing a model you are not using.

#While I appreciate the idea of trying to learn more about inheritance and mixins, code between lines 125-151 can be summarized into a single class.
#class RiskAssesmentBase(models.Model):
#    risk_level = models.CharField(max_length=1, choices=RISK_CHOICES)
#
#   class Meta:
#        abstract = True

class SecurityRisk(RiskAssessmentBase, RiskAssessmentMixin): #The following classes did not need the mixin, the choices was enough. Again, you are not providing a reference to the user model.
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    other = models.TextField(blank=True, verbose_name='Other Tasks')

    class Meta:
        abstract = True

    """ def __str__(self):
        return f'{self.get_task_type()} PM Tasks for {self.user.username} on {self.task_date}'

    def get_task_type(self):
        raise NotImplementedError("Subclasses must implement this method") """

class DailyPMTask(BasePMTask): #The following classes have one problem. Are all the daily/weekly/monthly tasks performed/supervised by the same person? (lines 216-287)
    clean_restrooms = models.BooleanField(default=False)
    stack_maintenance = models.BooleanField(default=False)
    empty_garbage = models.BooleanField(default=False)
    shovel_snow = models.BooleanField(default=False)
    vacuum_floors = models.BooleanField(default=False)

    @staticmethod #What is the purpose of this? Daily what? 
    def daily():
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

    primary_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='primary_closing_staff') #Again, you should not use the User model for this case scenario. 
    backup_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backup_closing_staff')
    day_of_week = models.PositiveIntegerField(choices=DAYS_OF_WEEK, unique=True) #You cannot use unique here, otherwise only one person in the whole system would be assigned to a day.

    class Meta:
        verbose_name_plural = 'Closing Staff Schedule'

        def __str__(self):
         return f'Closing Staff Schedule for {self.get_day_of_week_display()}' #Indentation is relevant. Also, you cannot reference the self object without an attribute. That only works as an argument, but
                                                                               # call self.get_day_of... as there is no such attribute. Also, that helper works only with the template.
        
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
    institution = models.ForeignKey("Institution", on_delete=models.CASCADE, related_name="questionnaires")
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="questionnaires") 
    primary = models.CharField(max_length=50, verbose_name="Primary Contact") # Aren't you suppose to reference a model here? Not the User model, but something like Associate or Worker
    backup = models.CharField(max_length=50, verbose_name="Backup Contact") #Same as above.

    def __str__(self):
        return self.question.text #Are you sure that's what you want displayed as the representation of the object?
    
class Tasks(models.Model):
    institution_name = models.ForeignKey("Institution", verbose_name="Institution Name", on_delete=models.CASCADE, related_name="tasks")
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="tasks")
    answer = models.BooleanField() #Are these true/false questions?
    items = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operating_procedures', null=True, blank=True) #Users as items? 

    def __str__(self):
        return str(self.institution_name) #While possible, this looks like an illegal operation that might bring problems. 

  
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
    day_of_week = models.PositiveIntegerField(choices=DAYS_OF_WEEK, unique=True) #Since you already had a days of the week Choices, why the duplicate? Also, it cannot be unique. Reference the previous usage for more details.

    class Meta:
        verbose_name_plural = 'Weekly Opening Staff Schedules'

        def __str__(self):
            return f'Weekly Opening Staff Schedule for {self.get_day_of_week_display()}' #Again, this is not how the display helper works. Also, this is a function of class Meta, not the WeeklyOpening class. Indentation matters.
class FacilitiesInfo(models.Model): # Don't you already have an address model for this? 
    street = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class EmergencyShutOff(models.Model):
    facility_info = models.ForeignKey("FacilitiesInfo", on_delete=models.CASCADE, related_name='emergency_shut_offs')
    shut_off_type = models.CharField(max_length=300, verbose_name='Emergency Shut-Off Type')
    procedures = models.TextField(verbose_name='Procedures')

    class Meta:
        verbose_name_plural = 'Emergency Shut-Offs'

    def __str__(self):
        return f'Emergency Shut-Off for {self.shut_off_type}'




class FireExtinguisherType(models.TextChoices):
    ABC = 'ABC', 'ABC'
    WATER = 'Water', 'Water'
    CO2 = 'CO2', 'CO2'
    MIST = 'Mist', 'Mist' #Again, this is now how tuples work. 

class FireDetection(models.Model):
    fire_alarm_pull_box_number = models.CharField(max_length=255, verbose_name='Fire Alarm Pull Box Number/Name')
    fire_alarm_box_location = models.TextField(verbose_name='Location Description') #How about using a reference to the next model? 

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

class Companies(models.Model): #I would make the name of the class singular, and then add in class Meta the plural option. 
    # Do comapnies need a name?
    heat_detectors = models.CharField(max_length=50)
    smoke_detectors = models.CharField(max_length=50)
    sprinklers = models.CharField(max_length=50, verbose_name='Sprinklers System')
    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name="locations")

    class Meta:
        ordering = ['location']

    def __str__(self):
        return str(self.location)  # Are you sure you want to reference companies by location?

class ServiceType(models.Model):
    date_created = models.DateField()
    date_updated = models.DateField()
    description = models.CharField(max_length=300)
    monitoring_type = models.CharField(max_length=100, verbose_name='Monitoring Type') #No controlled vocabulary for this?

    def __str__(self):
        return f"{self.description} ({self.monitoring_type})"


class Services(models.Model):
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    addresses = models.ManyToManyField("Address", related_name='services_companies')
    phone = models.CharField(max_length=30, verbose_name='Phone Number')
    after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=20, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return str(self.contact_person)

class GasServices(models.Model): #On a second look, it appear this model is a mixture of Service Type and Services? Why are you duplicating efforts?
    service_category = models.CharField(max_length=100) # Service type?
    date_created = models.DateField(blank=True, null=True)
    date_updated = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=250, verbose_name='Emergency Evacuation Plans') #The first four attributes are present in Service Type, maybe use inheritance instead?
    addresses = models.ManyToManyField("Address", related_name='gas_services_addresses')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    after_hours = models.CharField(max_length=20, verbose_name='After Hours Phone')
    pager = models.CharField(max_length=20, verbose_name='Pager')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return f"{self.service_category} {', '.join(map(str, self.addresses.all()))}"

class WaterDetector(models.Model): #You have a Location model and a Street model. You need to define which one you want to use. Consistency is important.
    name = models.CharField(max_length=150, verbose_name="Detector Name")
    location = models.CharField(max_length=50, verbose_name="Location")
    street = models.ForeignKey("Address", related_name="wd_address", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class WaterDetectorCategory(models.Model):
    text = models.CharField(max_length=200, verbose_name="Text")
    detector_type = models.CharField(max_length=150, verbose_name='Type of Water Detector') # No controlled vocabulary for a'type' item?
    water_detector = models.ForeignKey("WaterDetector", verbose_name='Water Detector', on_delete=models.CASCADE, default=1)
    monitoring_procedures = models.TextField(verbose_name='Monitoring Procedures', blank=True)

    def __str__(self):
        return self.text


class State(models.Model):
    name = models.CharField(max_length=150, verbose_name='State Name') #Is this what you are referencing on Address?

    def __str__(self):
        return self.name


class HeatingCompany(models.Model):
    address = models.ForeignKey("Address", on_delete=models.CASCADE, related_name='heating_service_company_address')
    material = models.CharField(max_length=200, blank=True)
    other = models.CharField(max_length=300)

    class Meta:
        ordering = ['material']  

    def __str__(self):
        return str(self.material)


class Name(models.Model): # What is name being used for? It could be great for companies that have more than one function. 
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    
class CoolingSystem(models.Model):
    name = models.CharField(max_length=50, verbose_name="Organization Name")
    city = models.ForeignKey("City", on_delete=models.CASCADE, related_name="city") #Just city, no address?

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name #While I have skipped a few of these, self.name does not always return a string. Using "f" strings is usally the safest bet. 
    
class DisasterTeam(models.Model):
    ROLE_CHOICES = [
        ('Primary', 'Primary'),
        ('Backup 1', 'Backup 1'),
        ('Backup 2', 'Backup 2'),
    ]

    name = models.CharField(max_length=150, verbose_name='Name') #Are you referencing a team member? or the Team? Either wat, this should be a foreign key. 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role')
    contact_phone = models.CharField(max_length=30, verbose_name='Phone') #You could avoid much of the following attributes if you were referencing a person (not from the User model)
    contact_cell_phone = models.CharField(max_length=20, verbose_name='Cell Phone', blank=True)
    contact_after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone', blank=True)
    contact_email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return f'{self.name} - {self.role}'
    
class TeamName(models.Model):
    name = models.CharField(max_length=150, verbose_name='Team Name')

    def __str__(self):
        return self.name

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
    #Are you should the above are the correct relationships? TeamName is a single line, while DisasterTeam is a much more complex object. 

    def __str__(self):
        return f'{self.get_responsibility_display()} - {self.team_member.name}'
    
class DisasterResponseTeamMember(models.Model): #Wait! Another class for team members? 
    ROLE_CHOICES = [
        ('Leader', 'Leader'),
        ('Coordinator', 'Coordinator'),
        ('Member', 'Member'),
    ] #Consistence for readability purposes is also important. You are using different ways to approach the same problem. Stick to one. 

    name = models.CharField(max_length=150, verbose_name='Name')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Role')
    contact_phone = models.CharField(max_length=30, verbose_name='Phone')
    contact_cell_phone = models.CharField(max_length=20, verbose_name='Cell Phone', blank=True)
    contact_after_hours_phone = models.CharField(max_length=20, verbose_name='After Hours Phone', blank=True)
    contact_email = models.EmailField(verbose_name='Email', blank=True)

    def __str__(self):
        return f'{self.name} - {self.role}'

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
    frequency = models.CharField(max_length=50, verbose_name='Frequency of Backup', blank=True) # is this frequency measured as daily, weekly, monthly, etc? If so, it should be a controlled vocabulary (enum)

    def __str__(self):
        return f'{self.type_of_data} - {self.location_of_data}'

class CommonFields(models.Model): #Common fields? As in miscellaneous? Many of the attributes listed below are already present in other classes. 
    staff_person = models.ForeignKey("DisasterResponseTeamMember", on_delete=models.CASCADE, verbose_name='Staff Person')
    outside_organization = models.CharField(max_length=150, verbose_name='Organization', blank=True)
    title_or_contact = models.CharField(max_length=150, verbose_name='Title/Contact', blank=True)
    address1 = models.CharField(max_length=150, verbose_name='Address1', blank=True)
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    zip_code = models.CharField(max_length=50, verbose_name='Zip', blank=True)
    phone = models.CharField(max_length=15, verbose_name='Phone', blank=True)
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone', blank=True)
    pager = models.CharField(max_length=15, verbose_name='Pager', blank=True)
    email = models.EmailField(max_length=150, verbose_name='Email', blank=True)

    class Meta:
        abstract = True

class DataRestoration(CommonFields): #Since this and the following model referer to organizations, wouldn't it be easier to use a foreign key to the company?
    outside_organization = models.CharField(max_length=150, verbose_name='Organization', blank=True)

    def __str__(self):
        return f'{self.staff_person.name} - {self.outside_organization}'

class Reconfiguration(CommonFields):
    outside_organization = models.CharField(max_length=150, verbose_name='Organization', blank=True)

    def __str__(self):
        return f'{self.staff_person.name} - {self.outside_organization}'

class ComputerOperation(models.Model): #How are all of this tasks relate other than they are computer related? 
    OPERATION_CATEGORIES = [
        ('OR', 'Computer Operation Relocation'),
        ('ERA', 'Emergency Remote Access'),
        ('P', 'Procedures'),
        ('LW', 'Library Website'),
    ]

    category = models.CharField(max_length=3, choices=OPERATION_CATEGORIES, verbose_name='Category')
    procedures = models.TextField(verbose_name='Procedures', blank=True)
    computer = models.CharField(max_length=150)
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

    class Meta:
        ordering = ['priority_ranking'] #sort based on priority? 

    def __str__(self):
        return f'{self.get_priority_ranking_display()} - {self.record_type}'

class PriorityMixin(models.Model): #I am not quite sure what you were trying to do here. Is this supposed to be a reference to the previous model?
    priority_ranking = models.PositiveIntegerField(verbose_name='Priority Ranking')

    class Meta:
        abstract = True

class Department(PriorityMixin):
    name = models.CharField(max_length=150, verbose_name='Department Name')

    def __str__(self):
        return self.name

class Collection(PriorityMixin):
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=150, verbose_name='Collection Name') #Again, this model could benefit with some foreign keys in the base mixin model.
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
    name = models.CharField(max_length=500, verbose_name='Plan Name')
    description = models.TextField(verbose_name='Plan Description')
    color_code = models.CharField(max_length=20, verbose_name='Color Code') #Are these color codes referenced elsewhere? Should be limited to a set?

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
    ] #Two different ways to approach a problem in the same model. You need to select one. 

    policy_number = models.CharField(max_length=50, verbose_name='Policy Number')
    policy_inception_date = models.DateField(verbose_name='Policy Inception Date')
    policy_expiration_date = models.DateField(verbose_name='Policy Expiration Date')
    property_covered = models.CharField(max_length=20, choices=PROPERTY_CHOICES, verbose_name='Property Covered') #Probably a reference to the library. 
    amount_of_coverage = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Coverage')
    deductible = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Amount of Deductible', null=True, blank=True)

    def __str__(self):
        return f'Policy: {self.policy_number}, Property: {self.get_property_covered_display()}' 


class InsuranceCompany(models.Model): #Isn't this just a company? 
    address1 = models.CharField(max_length=150, verbose_name='Address1')
    address2 = models.CharField(max_length=150, verbose_name='Address2', blank=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name='City')

    class Meta:
        ordering = ['city'] #Foreign Keys should be use rarely to order the values of a model.

    def __str__(self):
        return self.city
    
class Inventories(models.Model): # Why do inventories have almost the same data as insurance information? 
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

class ExpensesInsurance(models.Model): #Again, very clear some of the same attributes from the previous model. 
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

    policy1 = models.CharField(max_length=50, choices=IC_CHOICES, verbose_name='Policy Information')
    policy2 = models.CharField(max_length=50, choices=IC_CHOICES, verbose_name='Policy Information Business')

    def __str__(self):
        return self.name
      
RESPONSIBILITY_CHOICES = ( #How do you know who's who?
    ('person_1', 'Person 1'),
    ('person_2', 'Person 2'),
    ('backup_1', 'Backup #1'),
    ('backup_2', 'Backup #2'),
)

FREQUENCY_CHOICES = ( #You coyld've use these before. 
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annually', 'Annually'),
)

class InsuranceCoverage(models.Model):
    funds = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Funds Available for Salvage, Repair (in dollars)')
    collections = models.TextField(verbose_name='Collections Appraised') #Should you reference a collection here? Or are they only named once?
    date_of_last = models.DateField(verbose_name='Date of Last Appraisal')
    conducting = models.CharField(max_length=150, verbose_name='Person Conducting Appraisal')
    responsible = models.CharField(max_length=150, verbose_name='Person Responsible', choices=RESPONSIBILITY_CHOICES)
    frequency = models.CharField(max_length=50, verbose_name='Frequency of Evaluation', choices=FREQUENCY_CHOICES)
    procedures = models.TextField(verbose_name='Procedures in Case of Damage or Loss')
    documentation = models.TextField(verbose_name='Documentation Required')

    def __str__(self):
        return f'Funds Available: ${self.funds}' #funds but not what the insurance is covering?

class EvacuationProcedure(models.Model):
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for Clearing Area', choices=RESPONSIBILITY_CHOICES) # Should be referencing a person
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1', choices=RESPONSIBILITY_CHOICES) # Again, should be referencing a person. 
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2', choices=RESPONSIBILITY_CHOICES)
    evacuation_procedures = models.TextField(verbose_name='Evacuation procedure')

    def __str__(self):
        return f'Evacuation Area: {self.area_or_floor}'

class StaffVisitorLog(models.Model): #You should be referencing already existing models here (foreign keys)
    area_or_floor = models.CharField(max_length=300, verbose_name='Area/Floor')
    person_responsible = models.CharField(max_length=150, verbose_name='Person Responsible for List', choices=RESPONSIBILITY_CHOICES)
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1', choices=RESPONSIBILITY_CHOICES)
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2', choices=RESPONSIBILITY_CHOICES)

    def __str__(self):
        return f'Staff/Visitor Log for {self.area_or_floor}'

class AssemblyArea(models.Model): #Same as above. area or floor, backup, and location should be foreign keys. 
    area_or_floor = models.CharField(max_length=150, verbose_name='Area/Floor')
    staff_member_in_charge = models.CharField(max_length=150, verbose_name='Staff Member')
    backup_1 = models.CharField(max_length=150, verbose_name='Backup #1')
    backup_2 = models.CharField(max_length=150, verbose_name='Backup #2')
    location = models.CharField(max_length=300, verbose_name='Location')

    def __str__(self):
        return f'Assembly Area: {self.area_or_floor}'

class EmergencyCallList(models.Model): #Staff member should be a reference to person/associate/worker or similar but not User.
    staff_member = models.CharField(max_length=150, verbose_name='Staff Member')
    estimated_response_time = models.CharField(max_length=50, verbose_name='Estimated Response Time') #Should time be an integer or a float at least? Or maybe two fields? Time and Unit?
    position_on_call_list = models.PositiveIntegerField(verbose_name='Position on Call List')

    def __str__(self):
        return self.staff_member


class CommandCenter(models.Model): #Maybe use the address model to reference content?
    command_center_location = models.CharField(max_length=300, verbose_name='Command Center Location')
    alternate_location_1 = models.CharField(max_length=300, verbose_name='Alternate Location #1')
    alternate_location_2 = models.CharField(max_length=300, verbose_name='Alternate Location #2 (Off-site)')

    def __str__(self):
        return f'Command Center: {self.command_center_location}'

class CollectionStorage(models.Model): #Collection storage but not indicating the collections being stored?
    LOCATION_CHOICES = (
        ('Within Building/Institution', 'Within Building/Institution'),
        ('Off-Site', 'Off-Site'),
    )

    location_type = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name='Location Type')
    location = models.CharField(max_length=300, verbose_name='Location') #reference to a company? Institution? Library?
    space_available = models.CharField(max_length=150, verbose_name='Space Available')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person') #reference
    phone = models.CharField(max_length=15, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After-Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')

    def __str__(self):
        return f'{self.location_type} - {self.location}'

class DryingSpace(models.Model): #Maybe this and the above models could be one and define its purpose as an attribute?
    LOCATION_CHOICES = (
        ('Within Building/', 'Within Building/'),
        ('Off-Site', 'Off-Site'),
    )

    location_type = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name='Location Type')
    space_available = models.CharField(max_length=150, verbose_name='Space Available')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    cell_phone = models.CharField(max_length=15, verbose_name='Cell Phone')
    after_hours_phone = models.CharField(max_length=15, verbose_name='After-Hours Phone')
    pager = models.CharField(max_length=15, verbose_name='Pager')

    def __str__(self):
        return f'{self.location_type} - {self.space_available}'

        
class Organization(models.Model): #This model could use company as reference and determine the role of the company. Much easier.
    CATEGORIES_CHOICES = [
        ('PD', 'Police Department'),
        ('EM', 'Emergency Management'),
        ('LM', 'Local Emergency Management'),
        ('ES', 'Emergency Services'),
    ]
    emergency_services = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, verbose_name='Emergency Services')
    name = models.CharField(max_length=150, verbose_name='Organization Name')
    state = models.CharField(max_length=50, verbose_name='State')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Fire Department')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    cell_phone = models.CharField(max_length=20, verbose_name='Cell Phone')
    fax = models.CharField(max_length=20, verbose_name='Fax')
    website = models.URLField(max_length=300, verbose_name='Website')

    class Meta:
        ordering = ['name', 'state']

    def __str__(self):
        return self.name

class MaterialsService(models.Model): #Similar to the above, it could use a reference to organization with minor changes.
    name = models.CharField(max_length=50, verbose_name="Service")
    backup = models.CharField(max_length=50, verbose_name="Backup Liaison")
    date = models.DateField(auto_now=False, auto_now_add=False)
    review_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date Review of Collection Priorities') #auto_now and auto_now_add are false by default, no need to include them if that's the case.
    inspection_date = models.DateField(verbose_name='Date of Last Inspection by Fire Marshal')
    contact_person = models.CharField(max_length=150, verbose_name='Contact Person within Fire Department') 
  

    def __str__(self):
        return f'{self.name} - {self.organization}'


class NonOrganization(models.Model): #Again, company and role. Also, not all companies do everything. Also, the models is providing maintanance with the role of maitenance. 
                                    # Either that, or a plumber that can work as an electrician. It makes no sense. 
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
     
class OrganizationM(models.Model): #Ok, this could work with some additiona, but it is not referenced. 
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
  





