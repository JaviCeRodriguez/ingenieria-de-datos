import yaml

__config = None # Para cachear la configuración

def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.load(f, Loader=yaml.FullLoader)
    
    return __config


