from django.utils.deprecation import MiddlewareMixin
from celery.decorators import task
from .redis import redis_instance


@task
def increase_counter():
    if redis_instance.exists('counter'):
        redis_instance.incr('counter')
    else:
        redis_instance.set('counter', 1)


class CountRequestMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        if not request.path == '/request_count/reset/':
            increase_counter()
        return response