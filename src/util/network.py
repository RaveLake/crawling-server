

def get_local_domain():
    try:
        localhost = 'host.docker.internal'
        if localhost != '':
            return localhost
    except:
        return "127.0.0.1"
