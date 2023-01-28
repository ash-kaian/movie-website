from flask import Flask, render_template, request, redirect, url_for
from data import movie_data, movie_details_data
import jyserver.Flask as jsf

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        movie_id = request.form['id']
        return redirect(url_for('movie_id', id=movie_id))
    else:
        return render_template('index.html', popular=movie_data('movie', 'popular'), top_rated=movie_data('movie', 'top_rated'))


@app.route('/<id>')
def movie_id(id):
    return render_template('details.html', id_movie=id, movie_details=movie_details_data('movie', id))


if __name__ == '__main__':
    app.run()
