from flask import Flask, request

app = Flask(__name__)

"""__name__  represents the name of the application package and it is used by Flask to identify resources"""


@app.route('/')
def name_of_app():
    return 'The value of __name__ is {}'.format(__name__) #main


#GET Method url - /health returns health of application
@app.route('/health', methods=['GET'])
def health():
    return 'Server is up and running'











"""run the application using port 5000"""
app.run(port=5000)













