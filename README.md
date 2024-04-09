# Salary Prediction Streamlit App with Decision Tree Model

This is a simple Streamlit web application that predicts salary based on input features using a decision tree model. The app allows users to input various features related to a job candidate and get a salary prediction based on the provided data.

## Features

- Input various job-related features such as years of experience, education level, job type, etc.
- Uses a trained decision tree model to predict salary based on the input features.
- Displays the predicted salary to the user.

## Technologies Used

- Python
- Streamlit
- Scikit-learn (for machine learning model)

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/salary-prediction-streamlit-app.git
   cd salary-prediction-streamlit-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Access the app in your web browser at `http://localhost:8501`.

## Usage

1. Open the Streamlit app in your web browser after running `streamlit run app.py`.
2. Enter the required job-related features in the input fields provided.
3. Click the "Predict Salary" button to see the predicted salary based on the input features.

## Project Structure

```
salary-prediction-streamlit-app/
│
├── app.py             # Main Streamlit application file
├── model.pkl          # Trained decision tree model (pickle file)
├── requirements.txt   # Python dependencies
├── README.md          # Project README file
└── data/              # Directory containing data files (if applicable)
    ├── dataset.csv    # Sample dataset used for training the model
```

## Data

The app uses a dataset containing job-related features and corresponding salary values to train the decision tree model. The `model.pkl` file contains the serialized trained decision tree model for making predictions.

## Contributing

Contributions to this project are welcome! Please feel free to open a pull request or submit an issue if you have any suggestions, feature requests, or bug fixes.

