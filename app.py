from flask import Flask, render_template, request
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.check_spellings(text)
        corrected_grammar = spell_checker_module.check_grammar(text)
        return render_template("index.html", corrected_text=corrected_text, corrected_grammar=corrected_grammar)

@app.route('/grammar', methods=['POST'])
def grammar():
   if request.method =='POST':
       file= request.files['file']
       readable = file.read().decode('utf-8',errors='ignore')
       corrected_file_text = spell_checker_module.check_spellings(readable)
       corrected_file_grammar = spell_checker_module.check_grammar(readable)
   return render_template("index.html", corrected_text=corrected_file_text, corrected_grammar=corrected_file_grammar)


if __name__ == '__main__':
    app.run(debug=True)
