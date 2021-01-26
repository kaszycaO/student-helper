from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Components)
admin.site.register(Thresholds)
admin.site.register(Modyfication)
admin.site.register(CourseGroup)
admin.site.register(Goals)
admin.site.register(Files)
admin.site.register(Prediction)
admin.site.register(Events)
admin.site.register(Description)
admin.site.register(Marks)
admin.site.register(CourseEvents)
