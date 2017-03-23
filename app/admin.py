from django.contrib import admin
from .models import Criterion, Candidate, Evaluation

admin.site.register(Candidate)
admin.site.register(Criterion)
admin.site.register(Evaluation)