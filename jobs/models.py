from django.db import models

#models.Model helps in background save our data into the database
#Our job is to create a model that has image and then some text or summary
#Create different properties based on task(for fiels visit documentation)
#upload_to helps to store the image(the path in which directory) whenver the job model will be created

class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=200)
