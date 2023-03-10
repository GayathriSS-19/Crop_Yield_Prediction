import pickle
# from Crop_Yield_prediction_Model import predict_yield as py, final_model
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return render_template('first.html')


@app.route('/result', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        form = request.form
        area = float(form['area'])
        item = int(form['item'])
        year = int(form['year'])
        rainfall = float(form['rainfall'])
        #  gender = form['gender']
        pesticides = float(form['pesticides'])
        temp = float(form['temp'])
        p = []
        p += [area, item, year, rainfall, pesticides, temp]
        # result = py([p], final_)
        final_model = pickle.load(open("data.pickle", "rb"))
        result = final_model.predict([p])
        return render_template('index.html', res=str(result))
    return render_template('index.html', res="Fill the details and Click Submit")


# app.run()
