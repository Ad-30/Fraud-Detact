
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    
#    df = pd.read_csv('default_of_credit_card_clients.csv',encoding='ISO-8859-1', on_bad_lines='skip',lineterminator='\n')
#
#
#
#    X = df.drop('Y\r', axis=1)
#    y = df['Y\r']
#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#    clf = LogisticRegression(C=0.1)
#
#    clf.fit(X_train, y_train)
#
#
#    y_pred = clf.predict(X_test)
#
#
#    y_pred = clf.predict(X_test)
#    accuracy = accuracy_score(y_test, y_pred)
#    confusion = confusion_matrix(y_test, y_pred)
#
#
#
#    context = {
#        'accuracy': accuracy,
#        'confusion': confusion,
#    }
    return render(request, 'index.html')
#def detect_fraud(request):
#        # Load the dataset into a pandas dataframe
#    df = pd.read_csv('default_of_credit_card_clients.csv',encoding='ISO-8859-1', on_bad_lines='skip',lineterminator='\n')
#
#    # Split the data into training and testing sets
#
#    X = df.drop('Y\r', axis=1) # Remove the target variable
#    y = df['Y\r'] # Target variable
#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
#    # Fit the logistic regression model
#    clf = LogisticRegression(C=0.1)
#
#    clf.fit(X_train, y_train)
#
#    # Make predictions on the testing set
#    y_pred = clf.predict(X_test)
#
#    # Calculate the accuracy and confusion matrix
#    y_pred = clf.predict(X_test)
#    accuracy = accuracy_score(y_test, y_pred)
#    confusion = confusion_matrix(y_test, y_pred)
#
#
#    # Pass the results to the template
#    context = {
#        'accuracy': accuracy,
#        'confusion': confusion,
#    }
#    return render(request, 'index.html', context)




from django.http import HttpResponse


from django.views.decorators.csrf import csrf_exempt


df = pd.read_csv('creditcard.csv',encoding='ISO-8859-1', on_bad_lines='skip',lineterminator='\n')

X = df.drop('Class\r', axis=1) # Remove the target variable
y = df['Class\r'] # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=1000)

clf.fit(X_train, y_train)

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
