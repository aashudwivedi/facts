schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
    },
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True,
        'unique': True
    },
}


DOMAIN = {
    'people': {
        'item_title': 'person',
        'additional_lookup': {
            'url': 'regex("[\W]+")',
            'field': 'username',
        },

        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST'],

        'schema': schema
    }
}

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

URL_PREFIX = 'api'
XML = False

# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
# MONGO_DBNAME = 'apitest'