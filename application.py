from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello from Samriddhi's HW7 Elastic Beanstalk Application! CodePipeline deployment successful!"

if __name__ == "__main__":
    application.run()
