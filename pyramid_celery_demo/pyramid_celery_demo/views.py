from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from .models import (
    DBSession,
    TaskItem,
)

from pyramid_celery_demo.tasks import (
    DeleteTask,
    add_task
)

import time

@view_config(route_name='index', renderer='pyramid_celery_demo:templates/tasks.mako')
def index(request):
    tasks = DBSession.query(TaskItem).all()
    return {'tasks': tasks }

@view_config(route_name='add_task')
def create_task(request):
    task_val = request.POST['task']
    add_task.delay(task_val)
    time.sleep(1)

    return HTTPFound(request.route_url('index'))

@view_config(route_name='delete_task')
def delete_task(request):
    task_id = request.matchdict['task_id']
    DeleteTask.delay(task_id)
    time.sleep(1)
    return HTTPFound(request.route_url('index'))
