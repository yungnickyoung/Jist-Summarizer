from summa.summarizer import summarize
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

## /summarize -- POST
# Required body data: 
#   - article_text
# 
# Returns:
#   - 200: If article text was successfully summarized
#   - 400: If request data is missing or invalid
#   - 500: If problem occurred during summarization
@app.route('/summarize', methods = ['POST'])
def summarizeArticle():
    requestData = request.get_json()

    # Validate required data
    try:
        articleText = requestData['article_text']
    except KeyError as kerr:
        abort(Response(status=400, response="400: Error(400): Missing or invalid data provided: {}".format(str(kerr))))

    try:
        summary = summarize(articleText, ratio = 0.1)
    except Exception as e:
        abort(Response(status=500, response="500: Error (500): " + str(e)))

    data = { 'summary': summary }
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)