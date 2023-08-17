from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'index.html')

def getPredictions(pclass, sex, age):
    model = pickle.load(open('ml_model1.sav', 'rb'))
    scaled = pickle.load(open('scaler1.sav', 'rb'))

    prediction = model.predict(scaled.transform([
        [pclass, sex, age]
    ]))
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def result(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
   

    result = getPredictions(pclass, sex, age)

    return render(request, 'result.html', {'result': result})
