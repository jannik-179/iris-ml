# Iris Flower Classification App

This is a web application for classifying Iris flowers based on their features (sepal and petal length and width). The application consists of an Angular frontend and a FastAPI backend utilizing a K-Nearest Neighbors (KNN) machine learning model.

## Features

*   Input fields for sepal and petal measurements in cm.
*   Predicts the Iris species (Iris-setosa, Iris-versicolor, Iris-virginica) upon button click.
*   Displays the prediction along with a corresponding image of the flower.
*   The KNN model is trained using the well-known Iris dataset from the UCI Machine Learning Repository.

## Project Structure

```
.
├── iris-backend/      # FastAPI Backend Code
│   ├── main.py
│   └── requirements.txt
├── iris-frontend/     # Angular Frontend Code
│   ├── public/
│   │   └── img/  # Flower images here
│   ├── src/
│   ├── angular.json
│   └── package.json
└── README.md     # This file (in the root directory)
```

## Setup and Running the Application

Follow these steps to run the application locally.

### Prerequisites

*   [Git](https://git-scm.com/)
*   [Python](https://www.python.org/) (Version 3.8 or higher recommended)
*   [Node.js and npm](https://nodejs.org/) (npm is installed with Node.js)
*   [Angular CLI](https://angular.io/cli): `npm install -g @angular/cli`

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/jannik-179/iris-ml
    cd iris-ml
    ```

2.  **Backend Setup:**
    *   Navigate to the backend directory:
        ```bash
        cd iris-backend
        ```
    *   (Recommended) Create and activate a virtual environment:
        ```bash
        # For Linux/macOS
        python3 -m venv venv  # Or python -m venv venv
        source venv/bin/activate

        # For Windows (cmd)
        python -m venv venv
        venv\Scripts\activate.bat

        # For Windows (PowerShell)
        python -m venv venv
        venv\Scripts\Activate.ps1
        ```
    *   Install the Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Start the FastAPI server (while in the `backend` directory):
        ```bash
        uvicorn main:app --reload
        ```
        The server will run by default at `http://127.0.0.1:8000`. The model will be trained on startup.

3.  **Frontend Setup:**
    *   Open a **new terminal window**.
    *   Navigate to the frontend directory:
        ```bash
        cd iris-frontend
        ```
    *   Install the Node.js dependencies:
        ```bash
        npm install
        ```
    *   **Images:** The images (`Iris-setosa.png`, `Iris-versicolor.png`, `Iris-virginica.png`) should already be present in the `frontend/public/img/` directory (based on your `git status` output). Please verify they are there.
    *   Start the Angular development server (while in the `frontend` directory):
        ```bash
        ng serve
        ```
        The server will run by default at `http://localhost:4200`.

4.  **Open the Application:**
    Open your web browser and navigate to `http://localhost:4200`.

## API Endpoint

The backend provides the following endpoint:

*   `POST /predict`: Accepts JSON data with the four features and returns the predicted species.
    *   Request Body Example: `{"sepal_l": 5.1, "sepal_w": 3.5, "petal_l": 1.4, "petal_w": 0.2}`
    *   Response Body Example: `{"prediction": "Iris-setosa"}`
