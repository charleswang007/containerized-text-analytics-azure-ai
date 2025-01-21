from flask import Flask, request, jsonify, render_template_string
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 3000))

# Read API key and endpoint from environment variables
api_key = os.environ.get("apiKey")
endpoint = os.environ.get("endpoint")

if not api_key or not endpoint:
    raise ValueError("apiKey and endpoint environment variables are required")

credential = AzureKeyCredential(api_key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Container Status</title>
    </head>
    <body>
        <h1>The container is working</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route("/analyze", methods=["POST"])
def analyze():
    documents = request.json.get("documents")

    if not documents or not isinstance(documents, list):
        return jsonify({"error": "Invalid input"}), 400

    try:
        response = client.analyze_sentiment(documents)
        results = [
            {
                "id": doc.id,
                "sentiment": doc.sentiment,
                "confidence_scores": {
                    "positive": doc.confidence_scores.positive,
                    "neutral": doc.confidence_scores.neutral,
                    "negative": doc.confidence_scores.negative
                },
                "sentences": [
                    {
                        "text": sentence.text,
                        "sentiment": sentence.sentiment,
                        "confidence_scores": {
                            "positive": sentence.confidence_scores.positive,
                            "neutral": sentence.confidence_scores.neutral,
                            "negative": sentence.confidence_scores.negative
                        }
                    } for sentence in doc.sentences
                ]
            } for doc in response if not doc.is_error
        ]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
