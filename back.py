
from flask import Flask, jsonify, request,make_response
from flask_cors import CORS, cross_origin
import requests
import json
from json import loads

app= Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)


@app.route('/info',methods=["GET"])
def get_info():
	request_data= requests.get("http://186.105.225.86:8983/solr/busqueda2/select?q=*:*&fq=grade:3&fq=subject:historia")
	request_data=request_data.json()
			
	return jsonify(request_data)



if __name__ == '__main__':
	app.run(debug=True, port=4000)