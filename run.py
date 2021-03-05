#./env/bin/python
import os


os.system('gunicorn -w 4 --reload -b localhost:5000 "recepies:create_app()"')
