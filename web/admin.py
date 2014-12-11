from django.contrib import admin

from models import *

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('topic','responsible',)
    filter_horizontal = ('users',)
    def get_readonly_fields(self, request, obj=None):
        # only superuser can edit channel responsible
        if request.user.is_superuser:
            return self.readonly_fields
        # if not superuser, responsible will always be itself
        return self.readonly_fields + ('responsible',)
    def save_model(self, request, obj, form, change):
        # superuser can modify responsible
        if request.user.is_superuser:
            obj.save
            return
        # normal users cannot modify channel owner (only themselves)
        fsuser = request.user.fsuser
        obj.responsible = fsuser
        obj.save()
    # admin list
    def queryset(self, request):
        qs = super(ChannelAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(responsible=request.user.fsuser)
        

admin.site.register( FSUser )
admin.site.register( Penalty )
admin.site.register( Post )
admin.site.register( Like )
admin.site.register( Dislike )
admin.site.register( Complaint )
admin.site.register( Channel, ChannelAdmin )
admin.site.register( Comment )

