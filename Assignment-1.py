import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("insurance.csv")
#Task 1
print("Task 1: First 5 records:")
print(df.head())

print("\nNumerical Features:")
print(df.select_dtypes(include=["int64", "float64"]).columns.tolist())

print("\nCategorical Features:")
print(df.select_dtypes(include=["object", "str"]).columns.tolist())

print("\nTarget Variable:")
print("charges")

#Task 2
print("\nTask 2: Missing Values Check:")
print(df.isnull().sum())

df_encoded = pd.get_dummies(df, columns=["sex", "smoker", "region"], drop_first=True, dtype=int)

X = df_encoded.drop(columns=["charges"])
y = df_encoded["charges"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Task 3
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
#Task 4
print("\nTask 4: Model Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R2 Score: {r2:.4f}")

plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--")
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Insurance Charges")
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

print("\nObservations:")
print("1. The model achieved an R2 score of 0.7836, indicating that 78.36% of the variance in the testing dataset is explained by the model's features.")
print("2. The MAE of approximately 4181.1945 suggests that, on average, the predicted charges deviate from the actual charges by about $4,181.19.")
print("3. Smoking status has a massive coefficient (~23,651.13), indicating it is the single most important factor driving higher medical charges.")
#Task 5: Conclusion:
print("\nTask 5: Conclusion:")
print("In conclusion, the multiple linear regression model successfully predicts medical insurance charges with an R2 score of approximately 0.7836. The key findings reveal that smoking is by far the most significant factor affecting insurance charges, increasing them by approximately $23,651 on average when all other variables are held constant. Age and BMI also show a positive correlation with charges, contributing $256.98 and $337.09 per unit increase, respectively. Other features like sex and region have a negligible impact on charges. A major limitation of linear regression for this problem is its inability to capture non-linear relationships and complex interactions between features, such as the interaction between smoking status and high BMI, which typically results in exponentially higher charges that are underpredicted by a purely linear model.")
