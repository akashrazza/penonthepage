from django.db import models

# Create your models here.
class firstapp(models.Model):
    choice=(('Poetry','Poetry'),('Technology','Technology'),('Politics','Politics'),('photography','photography'))
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateTimeField(auto_created=True)
    about=models.TextField()
    image=models.ImageField(upload_to='./media')
    category=models.CharField(choices=choice,max_length=100)
    views=models.IntegerField(max_length=20)

class comment(models.Model):
    post_id=models.ForeignKey(firstapp,on_delete=models.CASCADE)
    comment=models.TextField()
    name=models.CharField(max_length=100)

