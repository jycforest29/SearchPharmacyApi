DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'pharmacy',
        'USER': 'root',
        'OPTIONS':{
            'charset':'utf8',
            'use_unicode':True
        },
        'PASSWORD': 'jycforest',
    }
}
SECRET_KEY = 'django-insecure-hj31_ai4#&t$_jhsc*nqmi^9u1+d=7hhrdl@k8+o#1^8wqt(l%'