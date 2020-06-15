from django.db import models
from django.core import validators


# Opcoes de escolha do Event.level
LEVEL_CHOICES = [
    ("CRITICAL", "CRITICAL"),
    ("DEBUG", "DEBUG"),
    ("ERROR", "ERROR"),
    ("WARNING", "WARNING"),
    ("INFO", "INFO")
]


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateField(auto_now=True)
    email = models.CharField(max_length=254, validators=[validators.validate_email])
    password = models.CharField(max_length=50, validators=[validators.MinLengthValidator(8)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'api_user'


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.CharField(max_length=39, validators=[validators.validate_ipv4_address])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'api_agent'


class Event(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_event'


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'api_group'


class GroupUser(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'api_groupuser'
