import time


def fit(model, features, target):
   start = time.time()
   model.fit(features, target)
   end = time.time()

   print(f'Fitting done in {end - start}s.')

   return model


def predict(model, data_X):
   start = time.time()
   y_prediction = model.predict(data_X)
   prediction_probability = model.predict_proba(data_X)
   end = time.time()

   print(f'Predicting done in {end - start}s.')

   return y_prediction, prediction_probability
