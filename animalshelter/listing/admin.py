## Zander B. Wells <zbwells@protonmail.com>
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

from django.contrib import admin
from .models import *

# Place to register models:
admin.site.register(Animal)
admin.site.register(AnimalDetail)
admin.site.register(Picture)
