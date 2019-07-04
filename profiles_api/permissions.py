from rest_framework import permissions



class NoPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class UserViewsPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'PUT' or request.method == 'GET':
            return request.user.id is not None
        return True


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user) and request.user.id
