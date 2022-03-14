from flask import Flask, render_template, request, flash, redirect, url_for
from gaz import getgazprice
import db

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def hello_world():


    """Seulement les users authentifié peuvent voir
    les camions (useless pour clients) """

    with db.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute('SELECT * FROM camions')
            camions = curseur.fetchall()

    return render_template('index.html', camions=camions)


@app.route('/ajout', methods=['GET', 'POST'])
def ajout_camion():

    #TODO: ORM

    """Ajout d'un camion"""
    if request.method == 'POST':
        immatriculation = request.form['immatriculation']
        poids = request.form['poids']
        consomation = request.form['consomation']
        with db.creer_connexion() as conn:
            with conn.get_curseur() as curseur:
                curseur.execute("INSERT INTO camions (immatriculation, poids, consomation) VALUES (%s, %s, %s)", (immatriculation, poids, consomation))
                conn.commit()
                flash("good")

    with db.creer_connexion() as conn:
        with conn.get_curseur() as curseur:
            curseur.execute('SELECT * FROM camions')
            camions1 = curseur.fetchall()

    #return redirect(url_for('/'))
    return render_template('ajoutCamion.html', camions1=camions1)

@app.route('/gazPrices')
def gaz_prix():
    prixGaz = getgazprice.gaz_prices
    return render_template('gazPrices.html', prixGaz=prixGaz)



if __name__ == '__main__':
    app.run()
