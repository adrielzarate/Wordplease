from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer


class UserViewSet(GenericViewSet):

# # class UsersAPI(APIView):
# class UsersAPI(GenericAPIView): # GenericAPIView utilizamos parte de las vistas genericas

    queryset = User.objects.all()
    permission_classes = [UserPermission]

    def get_serializer_class(self):
        return UserSerializer if self.request.method == 'POST' else UserListSerializer

    # def get(self, request):
    def list(self, request):
        """
        Devuelve el listado de usuarios en formato JSON
        :param request: objeto de tipo HttpRequest
        :return: objeto de tipo Response
        """
        # users = User.objects.all()
        # response = []
        # for user in users:
        #     response.append({
        #         'username': user.username,
        #         'first_name': user.first_name,
        #         'last_name': user.last_name
        #     })
        # json.dumps convierte objetos de datos primitivos a json
        # return HttpResponse(json.dumps(response))
        # return Response(response)

        # con many=True le decimos al serializador que no vamos a pasar un unico usuario sino muchos, de una vista de usuarios
        # serializer = UserListSerializer(users, many=True)
        # return Response(serializer.data)

        queryset = self.queryset
        users = self.paginate_queryset(queryset) # paginamos primero queryset (la busqueda a la base de datos)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(users, many=True) # elijo el serializador
        return self.get_paginated_response(serializer.data) # devuelvo la respuesta paginada

    # def post(self, request):
    def create(self, request):
        """
        Crear un usuario y devuelve la informacion del usuario creado
        :param request: objeto de tipo HttpRequest
        :return: objeto Response con datos del usuario creado o 400 con los errores cometidos
        """
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            # new_user = serializer.save(), podriamos usarlo asi por si necesitamos la variable
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class UserDetailAPI(APIView):
# class UserDetailAPI(GenericAPIView):

    permission_classes = [UserPermission]

    # def get(self, request, pk):
    def retrieve(self, request, pk):
        """
        Devuelve el detalle del usuario con pk <pk>
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos devolver
        :return: objeto Response con datos del usuario o 404
        """

        # get_object_or_404 es una funcion que si no encuentra el objeto devuelve automaticamente un 404
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user) # la validaciona  nievel de objeto hace falta hacerl manual. Como esta api fue creada de manera manual, comprueba si hay permiso para ser usado
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # def delete(self, request, pk):
    def destroy(self, request, pk):
        """
        Borra el usuario con pk <pk> si existe
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos borrar
        :return: 204 o 404
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 204 indica que el recurso ha sido borrado

    # def put(self, request, pk):
    def update(self, request, pk):
        """
        Actualiza el usuario con pk <pk> si existe
        :param request: objeto de tipo HttpRequest
        :param pk: pk del usuario que queremos actualizar
        :return: 202 o 404
        """
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)