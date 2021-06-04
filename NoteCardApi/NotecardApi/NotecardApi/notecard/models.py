from django.db import models

# Create your models here.
class NoteCard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    collection = models.ForeignKey('Collection', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id



class Collection(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title
