from django.contrib import admin
from gestor.models import Liga
from gestor.models import Partidos
from gestor.models import Arbitros
from gestor.models import Equipos
from gestor.models import DirectorT
from gestor.models import Jugador
from gestor.models import Goles
from gestor.models import Junta_directiva
from gestor.models import Presidente
from gestor.models import Tesorero
from gestor.models import Secretario
from gestor.models import Vocal

# Register your models here.

admin.site.register(Liga)
admin.site.register(Partidos)
admin.site.register(Arbitros)
admin.site.register(DirectorT)
admin.site.register(Jugador)
admin.site.register(Goles)
admin.site.register(Junta_directiva)
admin.site.register(Presidente)
admin.site.register(Tesorero)
admin.site.register(Secretario)
admin.site.register(Vocal)
admin.site.register(Equipos)