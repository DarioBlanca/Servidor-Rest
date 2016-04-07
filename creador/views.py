from rest_framework.decorators import api_view#, permission_classes
from django.contrib.auth import authenticate, login as Login
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.authentication import get_authorization_header
#from django.contrib.auth.decorators import permission_required
#from rest_framework.permissions import IsAdminUser
#from django.contrib.auth.decorators import user_passes_test
#from rest_framework.permissions import IsAuthenticated


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



@api_view(['POST',])
def login(request):
	usuario = request.data['usuario']
	password = request.data['password']
	try:	
		user = authenticate(username= usuario, password= password)
	except:
		return Response(status= status.HTTP_401_UNAUTHORIZED)
	if user is not None:
		if user.is_superuser:
			token = Token.objects.get(user_id=user.id)
			data = {"Authorization": str(token)}
			return JSONResponse(data)

	return Response(status= status.HTTP_403_FORBIDDEN)

#Login(request, user)

#@api_view(['POST'])
#@user_passes_test(lambda u: u.is_superuser)
#@permission_required('is_superuser')
#@permission_classes((IsAuthenticated,))
def addUsuario(request):
	header = get_authorization_header(request).split()

    if not auth or auth[0].lower() != b'token':
    	print "Error"
    else:
    	try:
    		token = Token.objects.get(key=claveToken)
    	except DoesNotExist:
    		return Response(status= status.HTTP_403_FORBIDDEN)
    	
    	if token.user_id == 1:
    		#Es el superusuario, por lo cual sale todo piola
			usuario = request.POST['username']
			password = request.POST['password']
			usuario = User.objects.create_user(usuario, "emailtrucho@gmail.com", password)
			usuario.save()
			return Response(status= status.HTTP_201_CREATED)
		return Response(status= status.HTTP_401_UNAUTHORIZED)
	return Response(status= status.HTTP_404_NOT_FOUND)





#from rest_framework.authtoken.models import Token

#token = Token.objects.create(user=...)
#print token.key

