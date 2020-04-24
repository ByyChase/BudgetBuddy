from flask import Flask, render_template, request, session, redirect, g, flash
import os

__flask_app__ = None

def setup_flask(app_name):
    app=Flask(app_name, template_folder="views", static_url_path="/static", static_folder="views/static")

    if app.debug:
        app.secret_key = b'\x87\xcd\xac&\x17\xd4\xb4]\xff|\x89\xc52\xfd}\xa6!\x99\xa6\x82\x19\xe2\x91Jp(\xf9\x0fAq\xd5\xc6'
    else:
        k = os.environb.get(b"FLASK_SECRET_KEY")
        if not k:
            raise EnvironmentError("FLASK_SECRET_KEY must be set for production environment")
        else:
            app.secret_key = k
    
    return app

def start_webserver(app_name):
    app = setup_flask(app_name)
    app.run(debug=True)