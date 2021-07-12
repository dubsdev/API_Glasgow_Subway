import flask
from flask import Flask, request, jsonify 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

stations = [{'Name': 'bridge street', 'Location': 'Bridge Street'}, {'Name': 'ibrox', 'Location': 'Govan'}]


class Index(Resource):
    def get(self):
        return "Awrite there"

class All_Stations(Resource):
    def get(self):
        return jsonify(stations)

class Single_Station(Resource):
    def get(self, station):

        result = []

        for s in stations: 
            if station == s['Name']:
                result.append(s)
        
        return jsonify(result)



api.add_resource(Index, '/')
api.add_resource(All_Stations, '/api/v1/stations/all')
api.add_resource(Single_Station, '/api/v1/stations/<string:station>')

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

