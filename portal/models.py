from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class TagElement(models.Model):
    text = models.CharField(max_length=15)

    def __str__(self):
        return self.text


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    interests = models.ManyToManyField(TagElement)

    def __str__(self):
        return self.username.username


class Project(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public_desc = models.TextField(max_length=2000)
    private_desc = models.TextField(max_length=5000)
    repo = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='members_set')
    tags = models.ManyToManyField(TagElement)

    def __str__(self):
        return self.name


class JoinRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approver_set')
    status = models.IntegerField()

    def __str__(self):
        return self.project.name+" "+self.requester.username



