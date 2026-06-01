from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Activity
from .models import classes
from .models import events
from .models import venues
from .models import sports_classes
from .models import Profile



admin.site.register(Category)
admin.site.register(Activity)
admin.site.register(classes)
admin.site.register(events)
admin.site.register(venues)
admin.site.register(sports_classes)
admin.site.register(Profile)


