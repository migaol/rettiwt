from rettiwt import create_app
from rettiwt.config import Config, ConfigDebug

app = create_app(Config)

if __name__ == '__main__':
    app.run()