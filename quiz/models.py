from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Quizzes(models.Model):
    title = models.CharField(max_length=255, default=_("New Quiz"))
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    
class Questions(models.Model):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )
    
    TYPE = (
        (0, _('Multiple Choice')),
    )
    
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.CASCADE)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_('Type of Questions'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    difficulty = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_('Difficulty')
    )
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))
    is_active = models.BooleanField(default=False, verbose_name=_('Active Status'))
    
    def __str__(self):
        return self.title
    
    
class Answer(models.Model):
    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))
    is_right = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer_text
    