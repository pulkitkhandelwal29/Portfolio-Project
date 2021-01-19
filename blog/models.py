from django.db import models

#Steps:-

#Create a Blog model
class Blog(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date (publish date)
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    # image
    image= models.ImageField(upload_to = 'images/')


#Add the Blog App to the settings (in the settings.py, under INSTALLED_APPS section)

#Create a migration(python manage.py makemigrations)
#Migrate(python manage.py migrate)
#These above steps need to be done in terminal


#Add to the admin
#The model has to be registered in the admin.py file of the particular model
