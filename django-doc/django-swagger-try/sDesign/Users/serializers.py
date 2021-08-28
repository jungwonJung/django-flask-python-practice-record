from rest_framework.serializers import ModelSerializer
from Users.models import Sdesgin_Users


class Sdesgin_UsersSerializer(ModelSerializer):

    class Meta:
        model = Sdesgin_Users
        fields = '__all__'
