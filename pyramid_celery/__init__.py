from celery import Celery as C
from pymongo import uri_parser

celery = None
Task = None

def config_cellery(settings):
    obj_config = config_celery_for_mongo(settings)
    global celery
    celery = C()
    celery.config_from_object(obj_config)
    global Task
    Task = celery.create_task_cls()

def includeme(config):
    config_cellery(config.registry.settings)

def config_celery_for_mongo(settings):
    db_uri = settings['mongodb.uri'].strip('"\'')
    db_name = settings['celery.dbname'].strip('"\'')
    res = uri_parser.parse_uri(db_uri)
    host, port = res['nodelist'][0]
    modules_to_register = eval(settings['celery.import'])

    celery_config = {
        'CELERY_RESULT_BACKEND' : 'mongodb',
        'BROKER_TRANSPORT'      : 'mongodb',
        'CELERY_IMPORTS': tuple(modules_to_register),
        'BROKER_HOST'   : host,
        'BROKER_PORT'   : port,
        'BROKER_VHOST'  : db_name,
        'CELERY_MONGODB_BACKEND_SETTINGS' : {
            'host': host,
            'port': port,
            'database': db_name
        }
    }
    print celery_config
    return celery_config
