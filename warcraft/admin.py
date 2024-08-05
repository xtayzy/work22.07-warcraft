from django.contrib import admin

# Register your models here.

from warcraft.models import Screenshot, About, Cinematic, GameProcess, Location, Music, Characters, Company, Background


admin.site.register(Screenshot)
admin.site.register(About)
admin.site.register(Cinematic)
admin.site.register(GameProcess)
admin.site.register(Location)
admin.site.register(Music)
admin.site.register(Characters)
admin.site.register(Company)
admin.site.register(Background)