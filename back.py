
from flask import Flask, jsonify, request,make_response
from flask_cors import CORS, cross_origin
import requests
import json
from json import loads

app= Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)


@app.route('/historiaTercero',methods=["GET"])
def get_historia_tercero():
	request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:3&fq=subject:historia&rows=10")
	request_data=request_data.json()
	print( jsonify(request_data) )		
	return jsonify(request_data)

@app.route('/historiaCuarto',methods=["GET"])
def get_historia_cuarto():
	request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:4&fq=subject:historia&rows=10")
	request_data=request_data.json()
	print( jsonify(request_data) )	
			
	return jsonify(request_data)


@app.route('/matematicaTercero',methods=["GET"])
def get_matematica_tercero():
	request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:3&fq=subject:matematica&rows=10")
	request_data=request_data.json()
			
	return jsonify(request_data)

@app.route('/matematicaCuarto',methods=["GET"])
def get_matematica_cuarto():
	request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:4&fq=subject:matematica&rows=10")
	request_data=request_data.json()
			
	return jsonify(request_data)



@app.route('/historia/<int:curso>',methods=["GET"])
def get_historia_tercero2(curso):
	if( curso == 3):
		request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:3&fq=subject:historia&rows=10")
	elif(curso == 4):		
		request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:4&fq=subject:historia&rows=10")
	else:
		request_data={}
	request_data=request_data.json()
			
	return jsonify(request_data)

	
@app.route('/historia-consulta',methods=['POST'])
def get_historia_query():
	print(request.json)
	curso=4
	if( curso == 3):
		request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:3&fq=subject:historia&rows=10")
	elif(curso == 4):		
		request_data= requests.get("http://host.nekmis.xyz:8983/solr/busqueda2/select?q=*:*&fq=grade:4&fq=subject:historia&rows=10")
	else:
		request_data={}
	request_data=request_data.json()
			
	return jsonify(request_data)

if __name__ == '__main__':
	app.run(debug=True, port=4000)