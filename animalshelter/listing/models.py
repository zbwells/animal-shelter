from django.db import models

## Models for the animal listing


'''
Animal model; contains all of the information for one animal.
Name, ID, Image, Species, Breed, Sex, Weight, 
Estimated Date of Birth, Intake date, Available on, 
Status, and other miscellaneous details.
'''

class Animal(models.Model):
    name = models.CharField(max_length=100)
    id_num = models.IntegerField()
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)

    ## Weight is CharField so that "pounds" or "kilograms" can be appended
    weight = models.CharField(max_length=25)
    
    gender = models.CharField(
        max_length=6, 
        choices=(
            ("Male", "Male"), 
            ("Female", "Female")
        )
    )
    
    intake_date = models.DateField("Intake Date")
    estimated_dob = models.DateField("Estimated Date of Birth")
    
    status = models.CharField(
        max_length=20, 
        choices=(
            ("Available", "Available"), 
            ("Adopted", "Adopted"), 
            ("Unavailable", "Unavailable")
        )
    )

    image = models.FileField(upload_to="uploads/%Y/%m/", default="")
    notes = models.TextField()

    def __str__(self):
        return self.name

'''
Separate model for the image of the animal;
This is so that there can be more than one image listed
for any given animal, if necessary.
'''

class Picture(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/%Y/%m/")
    image_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.image_desc
    
