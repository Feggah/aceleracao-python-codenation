from django.contrib import admin
from .models import User, Agent, GroupUser, Group, Event
# Register your models here.


admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Group)
admin.site.register(GroupUser)
admin.site.register(Event)
