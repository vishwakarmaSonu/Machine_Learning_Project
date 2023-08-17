from django.shortcuts import render

from joblib import load
model = load('./saveModel/model.joblib')

def predictor(request):
    if request.method == 'POST':
        sonu = request.POST['sonu']
        kk = float(sonu)
      
        y_pred = model.predict([[kk]])
        # if y_pred[0] == 0:
        #     y_pred = 'Setosa'
        # elif y_pred[0] == 1:
        #     y_pred = 'Verscicolor'
        # else:
        #     y_pred = 'Virginica'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')
