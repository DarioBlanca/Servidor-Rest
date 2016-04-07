from rest_framework.decorators import api_view, permission_classes
from rest_framework import views
from django.contrib.auth.models import User
from api.models import RegistroIPs, TablaIntermedia
from rest_framework import status
from api.serializers import TablaIntermediaSerializer, ConexionesSerializer
from django.contrib.auth import authenticate,login as Login,logout as Logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import MySQLdb

class Conexiones(object):
	def __init__(self, nombreUsuario, ippublica, ipprivada, created=None):
		self.nombreUsuario = nombreUsuario
		self.ippublica = ippublica
		self.ipprivada = ipprivada


@permission_classes((IsAuthenticated, ))
def DevolverTabla(user, ips):
	lalala = TablaIntermedia.objects.all().filter(estado= True).exclude(usuario= user, ips=ips)
	db = MySQLdb.connect("localhost", "root", "root", "servidor")
	cursor = db.cursor()
	consulta = "select au.username, ar.ippublica, ar.ipprivada from api_tablaintermedia ap inner join auth_user au on au.id = ap.usuario_id inner join api_registroips ar on ar.id = ap.ips_id where ap.estado = true"
	cursor.execute(consulta)
	resultado = cursor.fetchall()
	nuevaLista = []
	for elemento in resultado:
		if user.username != elemento[0]:
			roberto = Conexiones(nombreUsuario=elemento[0], ippublica= elemento[1], ipprivada=elemento[2])
			nuevaLista.append(roberto)
	serializado = ConexionesSerializer(nuevaLista, many=True)

	instancia = TablaIntermedia(usuario=user, ips=ips)
	instancia.save()
	return serializado.data



@permission_classes((IsAuthenticated, ))
def AltaIPs(ipPublica, ipPrivada):
	tablaIPs = RegistroIPs.objects.all()
	try:
		resultado = RegistroIPs.objects.get(ippublica= ipPublica, ipprivada= ipPrivada)
		return resultado
	except:
		nuevaRelacion = RegistroIPs(ippublica= ipPublica, ipprivada= ipPrivada)
		nuevaRelacion.save()
		return nuevaRelacion


#Dar de baja con una IP dada.
#	(Un usuario registrado nota la desconexion de otro, por lo cual envia un mensaje con la IP del correspondiente cliente
#	 avisando a este servidor que dicha IP fue dada de baja).
	# -> Cambiar estado en tabla intermedia
@csrf_exempt
@permission_classes((IsAuthenticated, ))
def desconexion(request):
	ipsRegistro = RegistroIPs()
	ipsRegistro.ippublica = request.POST['ippublica']
	ipsRegistro.ipprivada = request.POST['ipprivada']
	try:
		registro = TablaIntermedia.objects.get(ips= ipsRegistro)
		registro.estado = False
		registro.save()
		return Response(status= status.HTTP_204_NO_CONTENT)
	except:
		print "Se intento conectar " + registro.usuario + " y fallo."
	return Response(status= status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def conexion(request):
	usuario = request.data['usuario']
	password = request.data['password']
	ipPublica = request.data['ippublica']
	ipPrivada = request.data['ipprivada']

	user = authenticate(username=usuario, password=password)
	if user is not None:
		Login(request, user)
		IPs = AltaIPs(ipPublica, ipPrivada)
		if IPs:
			serializado = DevolverTabla(user, IPs)
			return Response(serializado, status= status.HTTP_200_OK)

	print "Se esta intentando conectar el usuario " + request.data['usuario'] + " pero hay datos invalidos"
	return Response(status= status.HTTP_403_FORBIDDEN)






#Para testeo
#	
#	Alta n1 (no recibe ningun dato)
# 	Alta n2 (debe recibir como usuario conectado n1)
#	Alta n3 (debe recibir como usuarios conectados n1,n2)
#	Baja n1
#	Alta n4 (debe recibir como usuarios conectados n2,n3)










