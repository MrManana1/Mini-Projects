from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        text_to_translate = request.form['text_to_translate']
        target_language = request.form['target_language']
        source_language = request.form['source_language']

        translator = Translator()
        translated = translator.translate(text_to_translate, dest=target_language, src=source_language)

        return render_template('index.html', languages=LANGUAGES, original=text_to_translate,
                               source_language=source_language, translated=translated.text, target_language=target_language)

    except Exception as e:
        return render_template('index.html', languages=LANGUAGES, error=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
