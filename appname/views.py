# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from django.shortcuts import render

def index(request):
    # Load the dataset into a pandas dataframe
    df = pd.read_csv('default_of_credit_card_clients.csv',encoding='ISO-8859-1', on_bad_lines='skip',lineterminator='\n')

    # Split the data into training and testing sets
    
X = df.drop('Y\r', axis=1) # Remove the target variable
y = df['Y\r'] # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the logistic regression model
    clf = LogisticRegression(C=0.1)

clf.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = clf.predict(X_test)

    # Calculate the accuracy and confusion matrix
    y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)

    
    # Pass the results to the template
    context = {
        'accuracy': accuracy,
        'confusion': confusion,
    }
    return render(request, 'index.html', context)
