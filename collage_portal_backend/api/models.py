from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from django.template.defaultfilters import truncatechars

# from phonenumber_field.modelfields import PhoneNumberField



fs = FileSystemStorage(location=settings.MEDIA_ROOT)




# university model

# class University(models.Model):
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)


# Collage model
class College(models.Model):
    name = models.CharField(max_length=60, db_index=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    state = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    accreditation_status = models.CharField(max_length=100, null=True, blank=True)
    establishment_date = models.DateField(null=True, blank=True)
    institution_type = models.CharField(max_length=50, null=True, blank=True)
    affiliation = models.CharField(max_length=100, null=True, blank=True)
    campus_facilities = models.TextField(null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='college_images/', null=True, blank=True)
    # has_virtual_tour = models.BooleanField(default=False)
    # has_video_tour = models.BooleanField(default=False)
    virtual_tour_link = models.URLField(max_length=100, null=True, blank=True)
    # virtual_360_tour_link = models.URLField(max_length=100, null=True, blank=True)  # Field for virtual 360 tour link
    virtual_360_tour = models.ImageField(upload_to='virtual_tours/', null=True, blank=True)
    # ratings = models.ForeignKey('Review', on_delete=models.CASCADE)
    # this is committed for later use
    # university = models.ForeignKey(University, on_delete=models.
    # CASCADE)
    course = models.ForeignKey
    
    class Meta:
        verbose_name_plural = "Colleges"
        ordering = ['name']  # Ordering by name

    def __str__(self):
        return self.name

#Specialization Model
class Specialization(models.Model):
    # college = models.ForeignKey(College, on_delete=models.CASCADE)
    # course = models.ForeignKey('Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    # duration = models.DurationField()
    total_avg_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    # faculty = models.ManyToManyField('Faculty', related_name='specialization_reverse')
    curriculum = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    career_opportunities = models.TextField(blank=True, null=True)
    research_areas = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Specializations"
        ordering = ['name']

    def __str__(self):
        return self.name

    


# Course model
class Course(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    code = models.CharField(max_length=50)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        null=True,
        blank=True, #need to check this one
    )
    description = models.CharField(max_length=1000, null=True, blank=True)
    duration = models.DurationField()
    eligibility = models.TextField(null=True, blank=True)
    total_avg_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # departments = models.ManyToManyField('Department', related_name='courses_reverse')
    
    
    

    

# #  Faculty model
# class Faculty(models.Model):
#     name = models.CharField(max_length=70)
#     designation = models.CharField(max_length=70)
#     specialization = models.CharField(max_length=30)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=254)
#     departments = models.ManyToManyField('Department', related_name='faculties_reverse')


#     def __str__(self):
#         return self.name
    
    
# Fee model

class Fee(models.Model):
    # college = models.ForeignKey(College, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee = models.IntegerField()
    # currency = models.CharField(max_length=3) 
    fee_structure = models.TextField(max_length= 20, null=True, blank=True)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    tuition_fee_description = models.TextField(null=True, blank=True)
    hostel_fee = models.DecimalField(max_digits=10, decimal_places=2)
    hostel_fee_description = models.TextField(null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    # fee_structure_link = models.URLField(max_length=100, null=True, blank=True)
    # this is committed for later use
    # university = models.ForeignKey(University, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.course.name} Fee"

    

# Department model
class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    # faculty = models.CharField(max_length=60)
    email = models.EmailField(max_length=254, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    head_of_department = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='department_images/', null=True, blank=True)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE) # not appropriate as dept is linked with  collage

# Country model
class Country(models.Model):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)  
    description = models.TextField(blank=True, null=True)
    flag_image = models.ImageField(upload_to='country_flags/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
# # Study Abroad 
# class StudyAbroadOption(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='study_abroad_options')
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     fee = models.IntegerField()
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     specialization = models.ManyToManyField('Specialization', related_name='courses_reverse')
    
#     address = models.CharField(max_length=255)
#     duration = models.DurationField()
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.course} in {self.country.name}"
    
    
    
   # Admission model 
class Admission(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    requirements = models.TextField(blank=True, null=True)
    entrance_exam = models.CharField(max_length=100, null=True, blank=True)
    exam_date = models.DateField(null=True, blank=True)
    admission_link = models.URLField(max_length=200, null=True, blank=True)
    # application_link = models.URLField(max_length=200, blank=True, null=True)
    # application_deadline = models.DateField(blank=True, null=True)
    # admission_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # currency = models.CharField(max_length=3, blank=True, null=True)
    fee_structure = models.ForeignKey(Fee, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Admission for {self.college.name}"    
    
    
    # User Profile model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    preferences = models.JSONField(null=True, blank=True)
    password = models.CharField(max_length=128)  # Field to store hashed password

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.user.set_password(self.password)
        # Save the associated User object
        # self.user.save()
        super().save(*args, **kwargs)  # Call the save method of the superclass

    def __str__(self):
        return self.user.username    

# video tour 
# class VideoTour(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True, null=True)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     video_url = models.URLField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return truncatechars(self.name, 50)

#     def save(self, *args, **kwargs):
#         if not self.name:
#             self.name = f"{self.college.name} - Video Tour"
#             # Optionally, you can slugify the name for a URL-friendly version
#             self.name = slugify(self.name)
#         super().save(*args, **kwargs)



# virtual 360 tour 
# class Virtual360Tour(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True, null=True)
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     tour_media = models.ImageField(upload_to='virtual_tours/', null=True, blank=True)

#     def __str__(self):
#         return truncatechars(self.name, 50)

#     def save(self, *args, **kwargs):
#         if not self.name:
#             self.name = f"{self.college.name} - Virtual Tour"
#             # Optionally, you can slugify the name for a URL-friendly version
#             self.name = slugify(self.name)
#         super().save(*args, **kwargs)



# Form Model
class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    stream = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f'Form by {self.email, self.phone}'
    
# review model
class Review(models.Model):
       college = models.ForeignKey(College, on_delete=models.CASCADE)
       ratings = models.IntegerField()
       remarks = models.TextField() 
       user = models.ForeignKey(User,on_delete=models.CASCADE)
       
       def __str__(self):
        return f'Review by {self.user.username}'
       