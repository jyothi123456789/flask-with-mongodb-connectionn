from flask import Flask
from flask_restful import Resource,Api

app=Flask("VideoAPI")
api=Api(app)

videos={
    'video1':{'title':'Hello world in python'},
    'video2':{'title':'Flask test run'}
}
class Video(Resource):
    def get(self):
        return "Hello World"

api.add_resource(Video,'/')

if __name__=='__main__':
    app.run()