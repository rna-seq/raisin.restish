"""
WSGI/PasteDeploy application bootstrap module.
"""
import os
from configobj import ConfigObj
from restish.app import RestishApp
from raisin.resource import root
from raisin.mysqldb import DB


def make_app(global_conf, **app_conf):
    """
    PasteDeploy WSGI application factory. Called by PasteDeploy (or a compatable WSGI application
    host) to create the raisin.restish WSGI application.
    """
    app = RestishApp(root.Root())
    app = setup_environ(app, global_conf, app_conf)
    return app


def setup_environ(app, global_conf, app_conf):
    """
    WSGI application wrapper factory for extending the WSGI environ with application-specific keys.
    """
    # Create any objects that should exist for the lifetime of the application
    # here. Don't forget to actually include them in the environ below!
    print "Settings:"
    for key, value in global_conf.items():
        print " " * 4, key, value

    pickles_cache_path = None
    if global_conf['use_pickles_cache'] == 'True':
        pickles_cache_path = os.path.abspath(global_conf['pickles_cache_path'])
    dbs = {}
    if global_conf['use_sql_database']:
        connections = ConfigObj(os.path.abspath(global_conf['mysql_connections']))
        databases = ConfigObj(os.path.abspath(global_conf['mysql_databases']))
        projects = ConfigObj(os.path.abspath(global_conf['projects']))
        for id, info in projects.items():
            for project in info['projects']:
                dbs[project] = {}
                for db_id, db_name in projects[id]['dbs'].items():
                    connection = connections[databases[db_name]['connection']]
                    db = DB(database=databases[db_name]['db'],
                            host=connection['server'],
                            port=int(connection['port']),
                            user=connection['user'],
                            passwd=connection['password'],)
                    dbs[project][db_id] = db
        parameters = ConfigObj(os.path.abspath(global_conf['parameters']))
        project_parameters = ConfigObj(os.path.abspath(global_conf['project_parameters']))
        parameter_labels = {}
        parameter_columns = {}
        parameter_mapping = {}
        for parameter, info in parameters.items():
            parameter_labels[parameter] = (info['title'], info['type'])
            parameter_columns[parameter] = info['column']
        for project, info in project_parameters.items():
            parameter_mapping[project] = info['parameters']

    def application(environ, start_response):
        # Making the following additional keys available to the environ.
        # They become available to the request like this:
        # request.environ['myvar']
        environ['pickles_cache_path'] = pickles_cache_path
        environ['dbs'] = dbs
        environ['parameter_columns'] = parameter_columns
        environ['parameter_labels'] = parameter_labels
        environ['parameter_mapping'] = parameter_mapping
        return app(environ, start_response)

    return application
