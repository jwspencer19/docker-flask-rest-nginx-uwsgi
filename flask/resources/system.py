import socket
from flask_restful import Resource

class AppVersion(Resource):
    def get(self):
        return {'App Version': 3.0}, 200

class HostName(Resource):
    def get(self):
        return {'Host Name': socket.gethostname()}, 200
