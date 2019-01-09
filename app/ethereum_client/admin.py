# Django imports
from django.contrib import admin

# App imports
from .models import EthVoter
from .models import VoteLog
from .models import VotingDetailsLog


admin.site.register(EthVoter)
admin.site.register(VoteLog)
admin.site.register(VotingDetailsLog)
