from flask import Flask ,render_template,url_for,request
import joblib

random_forest = joblib.load('./models/randomforest.lb')
app = Flask(__name__)

@app.route('/')  # url 
def home():
    return render_template('home.html')


@app.route('/project')   #http://127.0.0.1:5000/project
def project():
    return render_template('project.html')


@app.route('/predict',methods=['GET','POST'])     #http://127.0.0.1:5000/predict
def predict():
    if request.method =="POST":
        region = request.form['region']
        children =int (request.form['children'])
        health = int(request.form['health'])
        smoker =int (request.form['smoker'])
        gender =int (request.form['gender'])
        bmi =int (request.form['bmi'])
        age = int(request.form['age'])
        region_northeast =0
        region_northwest=0
        region_southeast=0
        region_southwest=0
        if region =='se':
            region_southeast=1
        elif region =='sw':
            region_southwest=1
        elif region =='ne':
            region_northeast=1
        else:
            region_northwest=1




        unseen_data =[[age,gender,bmi,children,smoker,health,region_northeast,region_northwest,region_southeast,region_southwest]]

        prediction = random_forest.predict(unseen_data)[0]
        print(prediction)


        return str(prediction)
        

if __name__ == "__main__":
    app.run(debug=True)