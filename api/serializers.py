from rest_framework import serializers
from api.models import TablaIntermedia
from django.contrib.auth.models import User


#Se supone que no tengo que serializar los usuarios por que no voy a devolverlos
#class UserSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = User
#		fields = ('id', 'username')

class TablaIntermediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = TablaIntermedia
		fields = ('ips_id', 'usuario')

class ConexionesSerializer(serializers.Serializer):
	nombreUsuario = serializers.CharField(max_length=50)
	ippublica = serializers.CharField(max_length=16)
	ipprivada = serializers.CharField(max_length=16)

