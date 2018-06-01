from flask import Flask, render_template, redirect, url_for
from forms import SearchForm
import requests
import json
import unicodedata

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', name=form.username.data))
    return render_template('search.html', form=form)

@app.route('/search/<name>')
def search(name):
    info = requests.get('http://localhost:5000/search/'+name)
    info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    info = json.loads(info)
    return render_template('show.html', info=info)

@app.route('/hello/<name>')
def hello(name):
    info = requests.get('http://localhost:5000/hello/'+name)
    return info.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
