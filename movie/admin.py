from django.contrib import admin
from users.models import CustomUser
from movie.models import Timestamps, PendingTimestamps

admin.site.register(CustomUser)
admin.site.register(Timestamps)
admin.site.register(PendingTimestamps)
