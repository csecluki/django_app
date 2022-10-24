from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


def ajax_login_required(func):

    def wrapper(*args, **kwargs):
        request_object = get_request_object(args)
        if request_object.user.is_authenticated:
            return func(*args, **kwargs)
        else:
            return JsonResponse(data={'detail': 'Not authorized'}, status=401)

    return wrapper


def ajax_permission_required(permission):

    def decorator(func):

        def wrapper(*args, **kwargs):

            request_object = get_request_object(args)
            if request_object.user.has_perm(permission):
                return func(*args, **kwargs)
            else:
                return JsonResponse(data={'detail': 'Permission denied'}, status=403)

        return wrapper

    return decorator


def get_request_object(request):
    return next(filter(lambda a: isinstance(a, WSGIRequest), request))
