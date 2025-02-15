from flask import Flask, request, jsonify
from flask_cors import CORS  
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)  

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    src_lang = data.get('src_lang')
    dest_lang = data.get('dest_lang')

    if not text or not src_lang or not dest_lang:
        return jsonify({"error": "Text, source language, and destination language are required"}), 400

    try:
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        return jsonify({"translated_text": translated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run()
