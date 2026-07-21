# 🏥 Medical Insurance Cost Prediction using Multiple Linear Regression

**Name:** Taran Ali Ahmed  
**Registration No.:** 23BCE10952  
**Application No.:** IN26009846

---

## 📌 Project Overview

This project develops a **Multiple Linear Regression** model to predict **medical insurance charges** based on customer demographic and health-related attributes. The model is trained using the **Medical Cost Personal Insurance Dataset** and evaluated using standard regression metrics.

---

## 🎯 Objective

The primary objective of this project is to:

- Predict individual medical insurance charges.
- Analyze the impact of different demographic and lifestyle factors on insurance costs.
- Evaluate the effectiveness of Multiple Linear Regression for this prediction task.

---

## 📂 Dataset

**Dataset:** Medical Cost Personal Insurance Dataset

🔗 **Kaggle Link:** https://www.kaggle.com/datasets/mirichoi0218/insurance

### Dataset Features

| Feature | Type | Description |
|---------|------|-------------|
| `age` | Numerical | Age of the insured person |
| `sex` | Categorical | Gender (Male/Female) |
| `bmi` | Numerical | Body Mass Index |
| `children` | Numerical | Number of dependent children |
| `smoker` | Categorical | Smoking status |
| `region` | Categorical | Residential region |
| `charges` | Target Variable | Medical insurance charges |

---

## 🛠️ Technologies & Libraries

- **Python**
- **Pandas** – Data loading and preprocessing
- **NumPy** – Numerical computations
- **Scikit-learn** – Model training and evaluation
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization

---

## ⚙️ Methodology

### 1. Data Exploration

- Loaded the dataset.
- Identified numerical and categorical features.
- Verified that there were **no missing values**.

### 2. Data Preprocessing

- Applied **One-Hot Encoding** to categorical variables:
  - `sex`
  - `smoker`
  - `region`
- Used `drop_first=True` to avoid the dummy variable trap.
- Split the dataset into:
  - **80% Training Data**
  - **20% Testing Data**

### 3. Model Training

- Trained a **Multiple Linear Regression** model using Scikit-learn's `LinearRegression`.

### 4. Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### 5. Visualization

Generated an **Actual vs Predicted Charges** scatter plot to compare predicted insurance charges with actual values.

---

# 📊 Results

## Model Performance

| Metric | Value |
|---------|--------:|
| **Mean Absolute Error (MAE)** | **4181.19** |
| **Mean Squared Error (MSE)** | **33,596,915.85** |
| **R² Score** | **0.7836 (78.36%)** |

The model explains approximately **78.36%** of the variance in medical insurance charges.

---

## 📈 Regression Coefficients

| Feature | Coefficient | Interpretation |
|---------|------------:|----------------|
| **smoker_yes** | **+23,651.13** | Strongest positive impact on insurance charges |
| `children` | +425.28 | Slight increase in charges |
| `bmi` | +337.09 | Higher BMI increases insurance cost |
| `age` | +256.98 | Charges increase with age |
| `sex_male` | -18.59 | Negligible effect |
| `region_northwest` | -370.68 | Minor regional variation |
| `region_southeast` | -657.86 | Minor regional variation |
| `region_southwest` | -809.80 | Minor regional variation |

### 🔍 Key Insight

Smoking status is the **most influential factor**, increasing predicted insurance charges by approximately **$23,651** while holding all other variables constant.

---

# 📉 Actual vs Predicted Charges

<p align="center">
  <img src="https://github.com/user-attachments/assets/97953e85-98d2-43e8-a99c-41331ef067c7" alt="Actual vs Predicted Charges" width="800">
</p>

The scatter plot shows that most predicted values closely follow the actual values, although very high insurance charges tend to be underestimated due to the linear nature of the model.

---

# ✅ Conclusion

The **Multiple Linear Regression** model provides a strong baseline for predicting medical insurance costs, achieving an **R² score of 0.7836**.

### Key Findings

- 🚬 Smoking is the strongest predictor of insurance charges.
- 📈 Insurance costs increase with both **age** and **BMI**.
- 👨‍👩‍👧 The number of dependent children has a modest positive effect.
- 🌍 Gender and region contribute very little to the prediction.

### Limitations

Multiple Linear Regression assumes a linear relationship between variables and therefore cannot effectively capture:

- Non-linear relationships
- Complex feature interactions
- Extreme insurance charges

For example, the interaction between **high BMI** and **smoking** often produces much higher medical costs than a simple linear model can predict.

---

# 🚀 Future Improvements

- Implement Polynomial Regression
- Compare with Decision Tree Regression
- Train a Random Forest Regressor
- Evaluate Gradient Boosting models (XGBoost/CatBoost)
- Perform Hyperparameter Tuning
- Apply Cross-Validation for better generalization

---

# 📚 References

- Medical Cost Personal Insurance Dataset (Kaggle)
- Scikit-learn Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Seaborn Documentation

---

## ⭐ If you found this project helpful, consider giving it a star!
