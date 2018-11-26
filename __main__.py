from index import app
from utils import get_config

if __name__ == "__main__":
    config = get_config('config.json')
    secret_key = config.get('secret_key', None)
    host = config.get('host', None)
    port = config.get('port', None)

    if secret_key:
        app.secret_key = secret_key
        if host is None or port is None:
            app.run()
        else:
            app.run(host=host, port=int(port))
    else:
        print('secret_key is required')