from flask import Flask , request
from flask_restful import Resource , Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {'about' : 'Hello programmer !'}
    def post(self):
        postData = request.get_json()
        return {'You have sent ' : postData}

class Math(Resource):
    def get(self,num):
        return {'num' : num * 10}

api.add_resource(Hello,'/')
api.add_resource(Math,'/math/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
