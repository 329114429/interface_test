from urllib import request
from django.http import JsonResponse
from django.shortcuts import redirect

# 需要登录才能访问的资源
LOGIN_REQUIRED_URLS = {
    '/praise/', '/criticize/', '/excel/', '/teachers_data/'
}


def check_login_middleware(get_resp):
    def wrapper(request, *args, **kwargs):
        # 请求的资源在上面的集合中
        if request.path in LOGIN_REQUIRED_URLS:
            if 'userid' not in request.session:
                if request.is_ajax():
                    return JsonResponse({
                        'code': 10003,
                        'hint': '请登录',
                    })
                else:
                    backurl = request.get_full_path()
                    # 非ajax请求重定向登录页面
                    return redirect(f'/login/?backurl={backurl}')
        return get_resp(request, *args, **kwargs)

    return wrapper
