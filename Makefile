dev:
	gunicorn -w 4 --reload  --reload-extra-file ./recepies -b localhost:8000 "recepies:create_app()"

prod:
	gunicorn -w 4 "wsgi:app"