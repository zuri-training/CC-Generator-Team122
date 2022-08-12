from django.db import models
from django.contrib.auth.models import User, auth 





class Card(models.Model):
    card = models.ImageField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
class Tutorial(models.Model):
    tutorial = models.CharField(max_length = 500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
class TutorialPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now= True)
    
    def _str_(self):
     return str(self.user) + '.' + str(self.value)

class CardPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now= True)

    def _str_(self):
     return str(self.user) + '.' + str(self.post) + '.' + str(self.value)
    
    class Meta:
        unique_together = ("user", "card", "value")
        unique_together = ("user", "value")
