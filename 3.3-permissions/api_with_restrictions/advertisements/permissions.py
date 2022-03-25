# from rest_framework.permissions import BasePermission


# class IsOwnerOrReadOnly(BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method == "GET":
#             return True
#         return request.user == obj.creator


from rest_framework import permissions

class IsAdminOrIsSelf(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True

        return request.user == obj.creator

class AddToFavorite(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        print('request.user==', request.user)
        print('obj.creator==', obj.creator)
        return request.user != obj.creator