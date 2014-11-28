from django.contrib import admin

from models import *

admin.site.register( FSUser )
admin.site.register( Penalty )
admin.site.register( Post )
admin.site.register( Like )
admin.site.register( Dislike )
admin.site.register( Complaint )
admin.site.register( Channel )

