from summa.summarizer import summarize
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/summarize', methods = ['POST'])
def summarizeArticle():	
	summary = summarize(request.data.decode("unicode-escape"), ratio=.1)
	app.logger.info("Processing article: %s", summary)
	return summary

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
