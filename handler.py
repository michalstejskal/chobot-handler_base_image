import json

from flask import Flask
import requests
import os
import user_code as user_code

app = Flask(__name__)


@app.route("/")
def hello():
	val = user_code.handle()
	responsse = {'response; '"HELLO WROLD! vraceno z userCode: " + val}
	return json.loads(responsse)


if __name__ == "__main__":
	print("MOCK API SECOND STARTED")
	app.run(debug=True, host="0.0.0.0", port=5000)

