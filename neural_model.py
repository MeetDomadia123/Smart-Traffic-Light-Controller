import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore
from sklearn.model_selection import train_test_split


# Genrate Synthetic Data

def genrate_dataset(samples=100):
    X=np.random.randint(0,20, size=(samples,4))
    y=np.clip(X.sum(axis=1) * 1.5,5,6)
    return X,y

# Build and train model
def build_and_train_model():
    X,y=genrate_dataset(1000)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

    model =Sequential([
        Dense(16, input_dim=4, activation='relu'),
        Dense(8, activation='relu'),
        Dense(1, activation='linear')
    ])

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
    model.fit(X_train, y_train, epochs=30, batch_size=16, verbose=0)

    print("Model Trained : Sample Evaluation")
    model.evaluate(X_test,y_test,verbose=2)

    return model

# predict green time

def predict_green_time(model, vehical_data):
    input_arr = np.array([list(vehical_data.values())])
    return model.predict(input_arr)[0][0]


if __name__ == "__main__":
    model = build_and_train_model()
    test_data = {'north': 6, 'south': 10, 'east': 4, 'west': 8}
    prediction = predict_green_time(model, test_data)
    print(f"Predicted Green Time for {test_data} = {prediction:.2f} sec")


