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
    id_num = models.IntegerField("ID Number")
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
    estimated_age = models.IntegerField(default=0)

    image = models.FileField(upload_to="uploads/%Y/%m/", default="")
    notes = models.TextField(blank=True)

    visible_on_website = models.BooleanField("Display on website?", default=True)

    def __str__(self):
        return self.name

'''
This model is to hold extra details for 
animals which might be included in the listing.
'''

class AnimalDetail(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    pregnant = models.BooleanField("Pregnant?")
    microchips = models.BooleanField("Microchipped?")
    good_with_people = models.BooleanField("Good with people?")
    good_with_same_species = models.BooleanField("Good with others of the same species?")
    bite_history = models.BooleanField("Bite history?")
    surrendered_by_owner = models.BooleanField("Surrendered by owner?")
    housebroken = models.BooleanField("Housebroken?")

    reason_for_surrender = models.TextField(
       "If surrendered by owner, why? (Optional)", 
        blank=True
    )
        
    condition_of_teeth = models.TextField(
        "Condition of teeth (Optional)", 
        blank=True
    )
    
    condition_of_skin = models.TextField(
        "Obvious issues or abnormalities? (Optional)", 
        blank=True
    )

    def __str__(self):
        return self.animal.name + ": Details"
    
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
        return self.animal.name + ": " + self.image_desc
    
