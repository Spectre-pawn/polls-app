from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pollsquestions(models.Model):
    category=models.CharField(max_length=50)
    question=models.CharField(max_length=100)
    option_1=models.CharField(max_length=50,)
    option_2=models.CharField(max_length=50,)
    option_3=models.CharField(max_length=50,)
    option_4=models.CharField(max_length=50,)
    count_opt_1=models.IntegerField(default=0)
    count_opt_2=models.IntegerField(default=0)
    count_opt_3=models.IntegerField(default=0)
    count_opt_4=models.IntegerField(default=0)
    created_by=models.ForeignKey(User,  on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.category
    def total(self):
        return self.count_opt_1+self.count_opt_2+self.count_opt_3 +self.count_opt_4
    def get_polls_by_user(current_user):
	    return Pollsquestions.objects.filter(created_by=current_user).order_by('-pub_date')

class voter(models.Model):
    poll_question=models.ForeignKey(Pollsquestions,  on_delete=models.CASCADE)
    Voter_name=models.ForeignKey(User,  on_delete=models.CASCADE)
    def __str__(self):
        return self.poll_question.question + self.Voter_name.username