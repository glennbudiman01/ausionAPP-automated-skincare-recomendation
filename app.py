import mysql.connector
from flask import Flask, render_template, request
import joblib
import numpy as np
from tensorflow.keras.utils import load_img
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import img_to_array

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/img/photo/'

mydb = mysql.connector.connect(
    host="sql6.freemysqlhosting.net",
    user="sql6499952",
    password="5dZWzhjMWv",
    database="sql6499952"
)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template("index.html")

    elif request.method == 'POST':
        model1 = load_model('./model development/ausion.h5', compile=False)
        model2 = joblib.load("./model development/stacking-model.pkl")

        a = request.form.get('optradio')
        a = int(a)

        b = request.form.get('umur')
        b = int(b)

        img = request.files['photo']
        img_path = app.config['UPLOAD_FOLDER']+img.filename
        img.save(img_path)
        image = load_img(img_path, target_size=(224, 224))
        x = img_to_array(image)
        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model1.predict(images, batch_size=10)
        classes = np.argmax(classes, axis=1)
        if classes == 0:
            classes = 2
        elif classes == 1:
            classes = 0
        else:
            classes = 1

        features = [[a, b, classes]]
        result = model2.predict(features)
        label = {
            '0': 'normal-jerawat',
            '1': 'normal-komedo',
            '2': 'normal-bopeng',
            '3': 'berminyak-jerawat',
            '4': 'berminyak-komedo',
            '5': 'berminyak-bopeng',
            '6': 'kering-jerawat',
            '7': 'kering-komedo',
            '8': 'kering-bopeng',
            '9': 'kombinasi-jerawat',
            '10': 'kombinasi-komedo',
            '11': 'kombinasi-bopeng',
            '12': 'sensitif-jerawat',
            '13': 'sensitif-komedo',
            '14': 'sensitif-bopeng',
        }
        result = label[str(result[0])]

        if result == "normal-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'normal-jerawat' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "jerawat"

        elif result == "normal-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'normal-poribesar' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "Pori - pori besar"

        elif result == "normal-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'normal-komedo' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "Komedo"

        elif result == "normal-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'normal-bopeng' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "Bopeng"

        elif result == "berminyak-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'berminyak-jerawat' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Jerawat"

        elif result == "berminyak-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'berminyak-poribesar' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Pori - pori besar"

        elif result == "berminyak-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'berminyak-komedo' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Komedo"

        elif result == "berminyak-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'berminyak-bopeng' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Bopeng"

        elif result == "kering-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kering-jerawat' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Jerawat"

        elif result == "kering-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kering-poribesar' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Pori - pori besar"

        elif result == "kering-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kering-komedo' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Komedo"

        elif result == "kering-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kering-bopeng' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Bopeng"

        elif result == "kombinasi-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kombinasi-jerawat' ")
            data = cursor.fetchall()
            kulit = "Kombinasi"
            masalah = "Jerawat"

        elif result == "kombinasi-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kombinasi-poribesar' ")
            data = cursor.fetchall()
            kulit = "Kombinasi"
            masalah = "Pori - pori besar"

        elif result == "kombinasi-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kombinasi-komedo' ")
            data = cursor.fetchall()
            kulit = "Kombinasi"
            masalah = "Komedo"

        elif result == "kombinasi-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'kombinasi-bopeng' ")
            data = cursor.fetchall()

        elif result == "sensitif-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'sensitif-jerawat' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Jerawat"

        elif result == "sensitif-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'sensitif-poribesar' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Pori - pori besar"

        elif result == "sensitif-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'sensitif-komedo' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Komedo"

        else:
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM produkdb WHERE label = 'sensitif-bopeng' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Bopeng"

        return render_template('predict.html', data=data, result=result, kulit=kulit, masalah=masalah)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
