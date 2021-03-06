import logging

import azure.functions as func
from ..flask_api import app

# rewrite URL:s to Azure function mount point (you can configure this in host.json and function.json)
from werkzeug.middleware.dispatcher import DispatcherMiddleware
app.config["APPLICATION_ROOT"] = "/api/sensor"     # Flask app configuration so it knows correct endpoint urls
application = DispatcherMiddleware(None, {
    '/api/sensor': app,
})

# Wrap the Flask app as WSGI application
def main(req: func.HttpRequest, context: func.Context, message: func.Out[str]) -> func.HttpResponse:
    app.config['AZURE_TABLE'] = message
    return func.WsgiMiddleware(application).handle(req, context)
