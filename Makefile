dev:
	gunicorn -w 4 --reload  --reload-extra-file ./recepies -b localhost:8000 "wsgi:app"

prod:
	gunicorn -w 4 "wsgi:app"