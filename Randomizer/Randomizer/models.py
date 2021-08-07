from django.db import models

class UserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    hashcode = models.CharField(max_length=200)


    def __repr__(self):
        return "<User: {} {} {}>".format(self.first_name, self.last_name, self.hashcode)

class UserDataModel(models.Model):
    # current user
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # clicked items separated by commas
    clicked_item = models.TextField(max_length=600)
    # clicked time dates separated by commas
    clicked_date = models.TextField(max_length=600)