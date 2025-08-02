# from flask import Flask, render_template, request
# import spacy
# import os

# app = Flask(__name__)
# nlp = spacy.load("en_core_web_sm")

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         job_description = request.form['jd']
#         # Assume some parsing and matching function here
#         result = "Sample result: skills match score 85%"
#         return render_template('index.html', result=result)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request
import spacy
import os

app = Flask(__name__)

# ✅ Ensure the spaCy model is available (auto-download if not)
try:
    nlp = spacy.load("en_core_web_sm")
except:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_description = request.form['jd']
        # Example response – replace this with real logic
        result = "Sample result: skills match score 85%"
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
