from django.contrib import admin
import main.models as am
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display =('id', 'username', 'email', 'image')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(am.AppUser, UserAdmin)
admin.site.register(am.Review, ReviewAdmin)

