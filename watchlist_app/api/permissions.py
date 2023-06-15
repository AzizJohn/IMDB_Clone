from rest_framework import permissions


class AdminOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
        # # admin_permission=super().has_permission(request, view)  # one way of defining if we using IsAdmin instead of BasePermission
        # admin_permission = bool(request.user and request.user.is_staff)
        # return request.method == 'GET' or admin_permission

    # <----second way oy defining this permission---->
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.review_user == request.user
