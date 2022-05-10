from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(func):
    def wrapper_func(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect('curls')
        else:
            return func(req, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper_func(req, *args, **kwargs):
            
            group = None
            if req.user.groups.exists():
                group = req.user.groups.all()[0].name
                
            if group in allowed_roles:
                return func(req, *args, **kwargs)
            else:
                return HttpResponse('You are no authorized to view this page')
        return wrapper_func
    return decorator


def adminonly(func):
    def wrapper_func(req, *args, **kwargs):
        group = None
        if req.user.groups.exists():
            group = req.user.groups.all()[0].name
            
        if group == 'Customer':
            return redirect('curls')
        
        if group == 'Business':
            return func(req, *args, **kwargs)
    
    return wrapper_func