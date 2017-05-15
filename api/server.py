import msgpack
import pickle
from flask import Flask, make_response
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin

from retrievers import userInteractionIntel

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['BUNDLE_ERRORS'] = True

@api.representation('application/msgpack')
def output_msgpack(data, code, headers=None):
    '''Makes a Flask response with a msgpack encoded body'''
    resp = make_response(msgpack.packb(data, use_bin_type=True), code)
    resp.headers.extend(headers or {})
    return resp

class AllLastViewBeforeBuy(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser = parser.add_argument('user',type=float, required=True, location='json')
		parser = parser.add_argument('product', type=float, required=True, location='json')  
		parser = parser.add_argument('time_of_action',type=float, required=True, location='json')
		
		args = parser.parse_args(strict=True)

		user = args['user']
		product = args['product']
		time_of_action = args['time_of_action']
		
		retriever = userInteractionIntel()
		lastViewedAt = retriever.getAllLastViewBeforeBuy(user, product, time_of_action)		

		answer = {'at': lastViewedAt[0]}
		return (answer)

class ProductsBought(Resource):
    def get(self):
        retriever = userInteractionIntel()
        productsBought = retriever.getProductsBought()
        answer = {'products_bought': productsBought}
        return (answer)

#ProductsBought
api.add_resource(ProductsBoughtInfo, '/api/productsBought')

#LastViewBeforeBuy
api.add_resource(AllLastViewBeforeBuy, '/api/allLastViewBeforeBuy')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
