# views.py
from django.shortcuts import render
from django.http import HttpResponse
import pickle
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')




# ... (previous code)
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Initialize the OneHotEncoder
onehot_encoder = OneHotEncoder(handle_unknown='ignore')

def loan_prediction(request):
    if request.method == 'GET':
        # Retrieve input values from the form
        Age_cat = request.GET.get('n1')
        Sex = request.GET.get('n2')
        Job = request.GET.get('n3')
        Housing = request.GET.get('n4')
        Saving = request.GET.get('n5')
        Checking = request.GET.get('n6')
        Credit = float(request.GET.get('n7'))
        Duration = int(request.GET.get('n8'))
        Purpose = request.GET.get('n9')

        # Create a dictionary to map categorical values to numerical labels
        label_mapping = {
            'Senior': 0, 'Student': 1, 'Adult': 2, 'Young': 3,
            'male': 0, 'female': 1,
            'Unskilled & Non-resident': 0, 'Unskilled & Resident': 1, 'Skilled': 2, 'Highly Skilled': 3,
            'own': 0, 'free': 1, 'rent': 2,
            'moderate': 0, 'nan': 1, 'little': 2, 'quite rich': 3, 'rich': 4,
            'little': 0, 'moderate': 1, 'nan': 2, 'rich': 3,
            'radio/TV': 0, 'education': 1, 'furniture/equipment': 2, 'car': 3, 'business': 4, 'domestic appliances': 5,
            'repairs': 6, 'vacation/others': 7
        }

        # Map categorical values to numerical labels
        Age_cat_label = label_mapping[Age_cat]
        Sex_label = label_mapping[Sex]
        Job_label = label_mapping[Job]
        Housing_label = label_mapping[Housing]
        Saving_label = label_mapping[Saving]
        Checking_label = label_mapping[Checking]
        Purpose_label = label_mapping[Purpose]

        # Create a dataframe with the input data
        input_data = pd.DataFrame([[Age_cat_label, Sex_label, Job_label, Housing_label, Saving_label,
                                     Checking_label, Credit, Duration, Purpose_label]],
                                   columns=['Age_cat', 'Sex', 'Job', 'Housing', 'Saving',
                                            'Checking', 'Credit', 'Duration', 'Purpose'])

        # Fit and transform using OneHotEncoder
        input_data_encoded = onehot_encoder.fit_transform(
            input_data[['Age_cat', 'Sex', 'Job', 'Housing', 'Saving', 'Checking', 'Purpose']]).toarray()

        # Combine the one-hot encoded features with the remaining numerical features
        input_data_encoded = np.concatenate(
            [input_data_encoded, input_data[['Credit', 'Duration']].values], axis=1)

        # Ensure the number of features matches what the model expects
     

        # Load the saved model
        with open('Notebook/model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        # Perform prediction using the input values
        prediction = model.predict(input_data_encoded)

        # Display the result
        result = 'Approved' if prediction[0] == 0 else 'Rejected'
        return render(request, 'predict.html', {'result': result})
    




        

   
