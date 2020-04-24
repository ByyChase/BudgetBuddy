from flask import Flask
from controllers import controllers

if __name__ == "__main__":
    controllers.start_webserver(__name__)