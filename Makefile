start:
	gunicorn -w 4 --reload  --reload-extra-file ./recepies -b localhost:5000 "recepies:create_app()"

prod:
	gunicorn -w 4 "app:app"