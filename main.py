from summa.summarizer import summarize
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/summarize/')
def summarizeArticle():

	#print(request.data.decode("unicode-escape"))
	summary = summarize(request.data.decode("unicode-escape"))
	app.logger.info("Processing article %s", summary)
	return "200"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
