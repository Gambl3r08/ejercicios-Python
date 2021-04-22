import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': 'b3ca26ec78a64948b4086d3f074390d0'}
connection.request('GET', '/v2/competitions/DED', None, headers )
response = json.loads(connection.getresponse().read().decode())

print(response)