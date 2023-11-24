from django.contrib import admin
from.models import State,District,Branch,Student,Course
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    filter_vertical = ('courses',)
    exclude = ['created_user']
    list_display=['name','image','project_Type']

class StateAdmin(admin.ModelAdmin):
   
    exclude = ['created_user']
    
admin.site.register(State,StateAdmin)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Student,StudentAdmin)
