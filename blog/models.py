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


    #Providing formatting for pretty blogs
    def summary(self):
        '''Returns the first 100 characters of the big whole summary '''
        return self.body[:100]

    def pub_date_pretty(self):
        '''Returns the published date in the proper format '''
        return self.pub_date.strftime('%b %e %Y')


    #Also we can change the appearance of name in Admin page like "Blog Project 1" to "title" in the admin page (dashboard)
    #for better remembering
    #By default it is coming like Blog project 1 and that becomes difficult when we want to edit it
    def __str__(self):
        '''__str__ is the name that is stored on admin page '''
        return self.title





#Add the Blog App to the settings (in the settings.py, under INSTALLED_APPS section)

#Create a migration(python manage.py makemigrations)
#Migrate(python manage.py migrate)
#These above steps need to be done in terminal


#Add to the admin
#The model has to be registered in the admin.py file of the particular model
