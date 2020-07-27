from django.contrib import admin
from .models import UpcomingEvent,NextBigEvent,slide,LatestSermon,donation,address,phone_number,Email,Ministries,pastors,video,CustomerInfo,prayer,breadcrumb
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin




class LatestSermonadmin(admin.ModelAdmin):
    list_display=('title','date')
    list_filter=('date',)

class donators(admin.ModelAdmin):
    list_display=('firstname','lastname','email','phonenumber','state','amount')

class donationrole(admin.ModelAdmin):
    list_display=('For_What','brief_description')

class bigevent(admin.ModelAdmin):
    list_display=('event','date')

class pastortable(admin.ModelAdmin):
    list_display=('name','role')

class comingevent(admin.ModelAdmin):
    list_display=('description','month','location','time')
    list_filter=('month',)

class videotable(admin.ModelAdmin):
    list_display=('title','date_posted','author')
    list_filter=('date_posted',)

class bread(admin.ModelAdmin):
    list_display=('title','text')
   

# Register your models.  
admin.site.register(UpcomingEvent,comingevent)
admin.site.register(NextBigEvent,bigevent)
# admin.site.register(slide)
# admin.site.register(LatestSermon,LatestSermonadmin)
admin.site.register(donation,donationrole)
admin.site.register(address)
admin.site.register(phone_number)
admin.site.register(Email)
# admin.site.register(Ministries)
# admin.site.register(pastors,pastortable)
#admin.site.register(video,videotable)
admin.site.register(CustomerInfo,donators)
# admin.site.register(prayer)
# admin.site.register(breadcrumb, bread)




@admin.register(prayer)
class prayeradmin(ImportExportModelAdmin):
    pass
@admin.register(Ministries)
class prayeradmin(ImportExportModelAdmin):
    pass
@admin.register(pastors)
class prayeradmin(ImportExportModelAdmin):
    pass
@admin.register(breadcrumb)
class prayeradmin(ImportExportModelAdmin):
    pass
@admin.register(LatestSermon)
class prayeradmin(ImportExportModelAdmin):
    pass
@admin.register(slide)
class prayeradmin(ImportExportModelAdmin):
    pass
#unregister models
admin.site.unregister(Group)



admin.site.site_header = "Army Of Jesus Christ Admin Panel"