Feature
=======
* Decorator based task
* auto route and import
* ONLY support mongodb

Getting Started
=====================
Include pyramid_celery either by setting your includes in your .ini,
or by calling config.include('pyramid_celery').

``` python
    pyramid.includes = pyramid_celery
```
This will register all the functions decerotated with @task.

Then do scan to activate celery broker in myapp/__init__.py:
``` python
    config.scan()
```

Now you can either use class based:

``` python
from pyramid_celery import task

@task(name='add')
def add(self, x, y):
    print x+y
```

to define route of a task, do

``` python
from pyramid_celery import Task
class RemoteTask(Task):
	queue = 'remote'

@RemoteTask()
def mult(self, x, y):
    return x*y
```

Configuration
=====================
All standard celery configuration options will work. Check out http://ask.github.com/celery/configuration.html

Demo
=====================
Not supported currently
