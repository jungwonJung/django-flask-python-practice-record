from rest_framework.serializers import ModelSerializer
from Users.models import Sdesign_Users


class Sdesgin_UsersSerializer(ModelSerializer):

    class Meta:
        model = Sdesign_Users
        fields = '__all__'