from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'duration', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)



from django.contrib import admin
from .models import Coursedetails, CourseTechnology


class CourseTechnologyInline(admin.TabularInline):
    model = CourseTechnology
    extra = 1


@admin.register(Coursedetails)
class CoursedetailsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [CourseTechnologyInline]


from django.contrib import admin
from .models import PaymentMethod

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("title", "method_type", "is_active")
    list_filter = ("method_type", "is_active")