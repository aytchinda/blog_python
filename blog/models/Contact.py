from django.db import models

class Contact(models.Model):
    
    civility = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    file = models.FileField(upload_to='contacts/%Y/%m/%d', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Subject :" + self.subject