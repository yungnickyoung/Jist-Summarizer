from summa.summarizer import summarize
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/summarize', methods = ['POST'])
def summarizeArticle():
	req_data = request.get_json()

	app.logger.info('Domain: ' + req_data['domain'])
	summary = summarize(req_data['full_text'], ratio = 0.1)

	app.logger.info(summary)

	response = { 'summary': summary }
	return jsonify(response), 200

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=80)
