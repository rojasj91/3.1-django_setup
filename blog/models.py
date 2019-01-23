"""In line 15 for the description of the Photo,
Dan put a null=True in () only because he made a change to the file that we don not have to make.
Therefore do not add the null=True
model.Model is pulling a specific Model from the models folder.

"""


from django.db import models


class Album(models.Model):
    pass


class Photo(models.Model):
    title = models.CharField(max_length=255)
    picture = models.URLField()
    description = models.TextField(null=True)


kepler = Photo()
oz = Photo()

photos = [kepler, oz]
