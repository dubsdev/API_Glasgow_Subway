import flask
from flask import Flask, request, jsonify 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

stations = [{'Name': 'bridge street', 'Location': 'Bridge Street'}, {'Name': 'ibrox', 'Location': 'Copland Road'}, {'Name': 'buchanan street', 'Location': 'Buchanan Street'}]


class Index(Resource):
    def get(self):
        return "Awrite there"

class All_Stations(Resource):
    def get(self):
        return jsonify(stations)

    def post(self):

        req_data=  request.get_json()

        print(type(req_data))
       
        new_station = {'Name': req_data['Name'], 'Location': req_data['Location']}

        stations.append(new_station)

        output = jsonify(req_data)
        output.status_code = 200
        
        return f"New station {req_data['Name']} has been added."




class Single_Station(Resource):
    def get(self, station):

        result = []

        for s in stations: 
            if station == s['Name']:
                result.append(s)
        
        #if result == []:
        #    return (f'No Station exists with name {station}')
        
        return jsonify(result)



# Add resources
api.add_resource(Index, '/')
api.add_resource(All_Stations, '/api/v1/stations')
api.add_resource(Single_Station, '/api/v1/stations/<string:station>')


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

