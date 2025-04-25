from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from contextlib import asynccontextmanager

TEST_SIZE = 0.2
RANDOM_STATE = 42
DEFAULT_K = 7

class IrisFeatures(BaseModel):
    sepal_l: float
    sepal_w: float
    petal_l: float
    petal_w: float

class PredictionResponse(BaseModel):
    prediction: str

model = None
scaler = None
encoder = None
feature_names = None

def initialize_model():
    global model, scaler, encoder, feature_names

    print("Loading and preprocessing data...")
    iris = fetch_ucirepo(id=53)
    X = iris.data.features
    y = iris.data.targets.iloc[:, 0].rename('species')
    print('Dataset downloaded successfully.')

    if X.isnull().sum().sum() > 0:
      print('Missing values detected in features X.')
    else:
      print('No missing values detected in features X.')

    feature_names = X.columns.tolist()

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    X_train, _, y_train, _ = train_test_split(
        X, y_encoded,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y_encoded
    )

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)

    model = KNeighborsClassifier(n_neighbors=DEFAULT_K)
    model.fit(X_train_scaled, y_train)
    print(f'k-NN model trained and ready.')

@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_model()
    yield

app = FastAPI(title="Iris Prediction API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict", response_model=PredictionResponse)
async def predict_iris(features: IrisFeatures):
    if not model or not scaler or not encoder or not feature_names:
        return {"error": "Model or components not initialized"}

    input_data = [features.sepal_l, features.sepal_w, features.petal_l, features.petal_w]
    input_array = np.array(input_data).reshape(1, -1)

    input_df = pd.DataFrame(input_array, columns=feature_names)

    input_scaled = scaler.transform(input_df)

    prediction_encoded = model.predict(input_scaled)
    prediction = encoder.inverse_transform(prediction_encoded)

    return PredictionResponse(prediction=prediction[0])