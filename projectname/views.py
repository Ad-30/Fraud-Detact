
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')
with open('model.pkl', 'rb') as file:
    clf = pickle.load(file)
@csrf_exempt
def detect_fraud(request):
    if request.method == 'POST':
        input_data = []
        for i in range(1, 31):
            input_field = request.POST.get(f'input{i}')
            
            if input_field:
                input_data.append(float(input_field))
            else:
                input_data.append(0.0)
        do = pd.DataFrame([input_data],columns=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount'],dtype = float)
        y_pred = clf.predict(do)
        print(y_pred[0])
        return render(request, 'index.html', {'result': y_pred[0]})
#        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
#sdfkjsdfjkjflskdjflksdjlkfjsdlkfjklsdjflksdjflkjsdlkfjdlkjfldskjflsdf;lajsldjlsdjlkdsjflkd
