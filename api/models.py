from django.db import models


class Qualification(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    

    CARDIOLOGIST = 'Cardiology'
    DERMATOLOGIST = 'Dermatology'
    ORTHOPEDIST = 'Orthopedics'
    PEDIATRICIAN = 'Pediatrics'
    PSYCHIATRIST = 'Psychiatry'
    SURGEON = 'Surgery'
    NEUROLOGIST = 'Neurology'
    GASTROENTEROLOGIST = 'Gastroenterology'
    ONCOLOGIST = 'Oncology'
    OBSTETRICIAN_GYNECOLOGIST = 'Obstetrics and Gynecology'
    ENDOCRINOLOGIST = 'Endocrinology'
    RADIOLOGIST = 'Radiology'
    OPHTHALMOLOGIST = 'Ophthalmology'
    UROLOGIST = 'Urology'
    OTOLARYNGOLOGIST = 'Otolaryngology'
    INFECTIOUS_DISEASE_SPECIALIST = 'Infectious Disease'

    SPECIALIZATION_CHOICES = [
        (CARDIOLOGIST, 'Cardiology'),
        (DERMATOLOGIST, 'Dermatology'),
        (ORTHOPEDIST, 'Orthopedics'),
        (PEDIATRICIAN, 'Pediatrics'),
        (PSYCHIATRIST, 'Psychiatry'),
        (SURGEON, 'Surgery'),
        (NEUROLOGIST, 'Neurology'),
        (GASTROENTEROLOGIST, 'Gastroenterology'),
        (ONCOLOGIST, 'Oncology'),
        (OBSTETRICIAN_GYNECOLOGIST, 'Obstetrics and Gynecology'),
        (ENDOCRINOLOGIST, 'Endocrinology'),
        (RADIOLOGIST, 'Radiology'),
        (OPHTHALMOLOGIST, 'Ophthalmology'),
        (UROLOGIST, 'Urology'),
        (OTOLARYNGOLOGIST, 'Otolaryngology'),
        (INFECTIOUS_DISEASE_SPECIALIST, 'Infectious Disease'),
    
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES)
    qualifications = models.ForeignKey(Qualification, on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField()
    office_number = models.CharField(max_length=15)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

