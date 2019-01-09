# # Pip imports
# from rest_framework import permissions
# from rest_framework import generics
#
# # App imports
# from ..serializers import SystemSettingsSerializer
# from ..models import SystemSettings
#
#
# class SystemSettingsAPIView(generics.RetrieveAPIView):
#     serializer_class = SystemSettingsSerializer
#     permission_classes = [permissions.AllowAny]
#
#     def get_object(self):
#         return SystemSettings.objects.first()