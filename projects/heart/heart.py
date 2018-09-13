import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, SGDClassifier
import evaluation
import classifier


if __name__ == '__main__':
    include = list(range(1, 15)) # excludes original index
    data = pd.read_csv("../../data/heart.csv", usecols=include, sep=",")
    data = data.dropna(axis=0, how='any').reset_index(drop=True) # drop missing values & reset index
    """ --------------------------------------------------------------------
    Data Pre-Processing
    -------------------------------------------------------------------- """
    numerical = ["Age", "RestBP", "Chol", "Fbs", "RestECG", "MaxHR", "ExAng", "Oldpeak", "Slope", "Ca"]
    categorical = ["Sex", "ChestPain", "Thal", "AHD"]
    data["AHD"] = 1.0 * (data["AHD"] == 'Yes') # target variable
    # re-encode categorical variable ChestPain
    ChestPain_cat = data['ChestPain']
    ChestPain_encoded, ChestPain_categories = ChestPain_cat.factorize()
    encoder = OneHotEncoder()
    ChestPain_cat_1hot = encoder.fit_transform(ChestPain_encoded.reshape(-1, 1))
    ChestPain_cat_1hot = pd.DataFrame(ChestPain_cat_1hot.toarray())
    ChestPain_cat_1hot = ChestPain_cat_1hot.rename(columns={0: 'typical', 1: 'asymptomatic',
                                                            2: 'nonanginal', 3: 'nontypical'})

    # re-encode categorical variable Thal
    Thal_cat = data['Thal']
    Thal_encoded, Thal_categories = Thal_cat.factorize()
    Thal_cat_1hot = encoder.fit_transform(Thal_encoded.reshape(-1, 1))
    Thal_cat_1hot = pd.DataFrame(Thal_cat_1hot.toarray())
    Thal_cat_1hot = Thal_cat_1hot.rename(columns= {0: 'normal', 1: 'reversable', 2: 'fixed'})

    """ --------------------------------------------------------------------
    concatenate and split data 
    -------------------------------------------------------------------- """
    data_X = pd.concat([data[numerical], data["Sex"], ChestPain_cat_1hot, Thal_cat_1hot], axis=1)
    data_y = data["AHD"]
    X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.2, random_state=11)

    """ --------------------------------------------------------------------
    fit model with LogisticRegression, make prediction, compute score 
    -------------------------------------------------------------------- """
    logisticRegr = LogisticRegression()
    classifier.fit(logisticRegr, X_train, y_train)
    y_prediction, prediction_probability = classifier.predict(logisticRegr, X_test)

    evaluation.print_measurements(y_test, y_prediction)

    """ --------------------------------------------------------------------
    fit model with SGDClassifier, make prediction, compute measurements  

    SGDC = SGDClassifier()
    classifier.fit(SGDC, X_train, y_train)
    y_prediction, prediction_probability = classifier.predict(SGDC, X_test)

    evaluation.print_measurements(y_test, y_prediction)
    -------------------------------------------------------------------- """
