Here's an updated README file including instructions on how to set up and run the Flask application:

---

# Car Price Prediction

This project aims to develop a machine learning model to predict the price of used cars based on various features. The dataset includes information about different cars sold across various locations in India.

## Project Definition

### Project Overview

**Background Information:**
The used car market has been growing rapidly due to economic considerations and the increasing popularity of online marketplaces. Accurate price prediction is crucial for both sellers and buyers to ensure fair transactions.

**Project Origin:**
This project utilizes machine learning algorithms to predict used car prices based on features like make, model, year of manufacture, mileage, fuel type, transmission, and more.

**Related Data Sets or Input Data:**
The primary dataset includes:
- Name: Name of the car
- Location: Location where the car is being sold
- Year: Year of manufacture
- Kilometers Driven: Total kilometers driven
- Fuel Type: Type of fuel used
- Transmission: Type of transmission
- Owner Type: Ownership type
- Mileage: Mileage of the car
- Engine: Engine capacity
- Power: Power of the car
- Seats: Number of seats in the car
- New Price: New price of the car (if available)
- Price: Price of the used car (target variable)

### Problem Statement

The goal is to build a predictive model that estimates the price of used cars based on given features. The model will help users determine the fair market value of a used car, aiding both sellers and buyers.

### Metrics

To evaluate the model's performance, the R-squared (R²) metric is used. It measures the proportion of variance in the dependent variable (car price) predictable from the independent variables (features).

**Justification for Using R-squared:**
- **Interpretability**: R-squared provides a straightforward interpretation of how well the model explains the variability of the target variable.
- **Benchmark**: It is a common and widely accepted metric for regression problems.
- **Diagnostic**: It helps in diagnosing the model's performance.

## Analysis

### Data Exploration

The dataset contains 14 columns, each representing a feature related to used cars, and consists of several thousand rows.

### Descriptive Statistics

Basic descriptive statistics of the dataset can be found in the analysis section of the code.

### Abnormalities

1. Columns like Mileage, Engine, Power, and New Price include units with values, requiring separation and conversion to numerical data.
2. Mileage units are not uniform due to different fuel types.
3. Some columns contain null values.

### Visualization

Visualizations include distributions of key numerical features and pie charts for categorical variables like fuel types and transmission types.

## Methodology

### Data Preprocessing

1. **Dropping Columns**: The 'New Price' column is dropped due to many null values. Unnamed index columns are also removed.
2. **Handling Missing Values**: Null and duplicate values are dropped.
3. **Removing Specific Fuel Types**: Rows with CNG, LPG, and Electric fuel types are removed.
4. **Removing Units**: Units are removed from Mileage, Engine, and Power columns.
5. **Extracting Brand Name**: The brand name is extracted from the car name.
6. **Encoding Categorical Columns**: Categorical columns are converted to numerical values using Label Encoding.

### Implementation

Two models are trained: Random Forest and XGBoost. Hyperparameter tuning is performed using GridSearchCV to find the best parameters.

## Results

### Model Evaluation and Validation

**1. XGBoost**
- **Parameters**: Learning Rate: 0.1, Max Depth: 6, Number of Estimators: 400
- **Performance**: R2 Score: 0.8958

**2. Random Forest**
- **Parameters**: Max Depth: 20, Min Samples Leaf: 1, Min Samples Split: 2, Number of Estimators: 300
- **Performance**: R2 Score: 0.8864

XGBoost slightly outperforms Random Forest with a higher R2 score.

### Comparison of Results

| Model          | Parameters                                                                 | R2 Score |
|----------------|---------------------------------------------------------------------------|---------|
| XGBoost        | {'learning_rate': 0.1, 'max_depth': 6, 'n_estimators': 400}                | 0.8958  |
| Random Forest  | {'max_depth': 20, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 300} | 0.8864  |

## Conclusion

### Reflection

The project successfully predicts car prices using machine learning models. Key steps include data preprocessing, exploratory data analysis, model building, tuning, and evaluation.

### Improvement

Suggestions for future research:
1. **Advanced Feature Engineering**: Explore sophisticated feature engineering techniques.
2. **Ensemble Methods**: Implement and compare additional ensemble methods.
3. **Deep Learning Approaches**: Investigate deep learning models.
4. **Time-Series Analysis**: Incorporate time-series analysis for a comprehensive understanding of price dynamics.
5. **Feature Importance and Explainability**: Improve model interpretability using techniques like SHAP or LIME.

## Application

### Flask Web Application

A Flask web application has been created to provide an interactive interface for predicting car prices based on user input.


[Ảnh chụp màn hình 2024-07-29 025219](https://github.com/user-attachments/assets/540e3f35-c633-41c1-9de7-68243a73abb0)

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Load the Model**:
   Ensure the trained model (`XGBoost_model.pkl`) is in the project directory.

4. **Run the Flask Application**:
    ```bash
   python app.py
   ```

5. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/` to access the car price prediction application.

### Application Usage

1. **Home Page**:
   The home page displays a form where you can input car details such as name, location, year, kilometers driven, fuel type, transmission, owner type, mileage, engine, power, and seats.

2. **Prediction**:
   After filling out the form, click on the "Predict Price" button. The application will display the predicted price based on the input features.

3. **Past Predictions**:
   The application also displays a list of past predictions for reference.

---

This README provides an overview of the Car Price Prediction project, outlines its purpose, methodology, results, application setup, and usage instructions.
