from unified import unified

if unified.config['DEBUG']:
    unified.debug = True

unified.run(**unified.config['WERKZEUG_OPTS'])
