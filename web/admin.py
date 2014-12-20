from django.contrib import admin
from models import *


# ChannelAdmin requirements can be checked in issue #12 (create channel view)
# https://github.com/lacetans/faceschool/issues/12
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('topic','responsible',)
    filter_horizontal = ('users',)
    form = DataImport
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        # if not superuser, disable responsible field
        return self.readonly_fields + ('responsible',)
    def save_model(self, request, obj, form, change):
        # superuser can modify channel responsible
        if request.user.is_superuser:
            obj.save
            return
        # force responsible to logged user (when creating channel)
        fsuser = request.user.fsuser
        obj.responsible = fsuser
        obj.save()
    def queryset(self, request):
        qs = super(ChannelAdmin, self).get_queryset(request)
        # superuser can see all channels
        if request.user.is_superuser:
            return qs
        # show only owned channels (teachers)
        return qs.filter(responsible=request.user.fsuser)
        

admin.site.register( FSUser )
admin.site.register( Penalty )
admin.site.register( Post )
admin.site.register( Like )
admin.site.register( Dislike )
admin.site.register( Complaint )
admin.site.register( Channel, ChannelAdmin )
admin.site.register( Comment )

