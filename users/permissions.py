from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario puede realizar la accion (GET, POST, PUT, DELETE) que quiere realizar sobre la vista <view>
        """
        # from users.api import UserDetailAPI # lo importa aqui para evitar el error de dependencia ciclica

        # if request.method == 'POST':
        #     return True
        #
        # if request.user.is_authenticated and (
        #         request.method != 'GET' or request.user.is_superuser # or isinstance(view, UserDetailAPI)
        # ):
        #     return True

        if view.action == 'create':
            return True

        if request.user.is_authenticated and view.action in ['retrieve', 'update', 'destroy']:
            return True

        if view.action == 'list' and request.user.is_superuser:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario puede realizar la accion sobre el objeto <obj>
        Un usuario puede borrar o actualizar un usuario, si es superusuario o si es el mismo
        """
        return request.user.is_superuser or request.user == obj