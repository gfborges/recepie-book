from flask import json
from recepies.error import NotFound
from recepies import app

@app.errorhandler(404)
def handle_404(e: NotFound):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
