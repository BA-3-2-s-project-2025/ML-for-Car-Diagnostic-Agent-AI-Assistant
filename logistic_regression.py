import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import seaborn as sns
import joblib
import matplotlib.pyplot as plt

encoder = LabelEncoder()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
np.set_printoptions(threshold=np.inf)

# Load dataset
df = pd.read_csv(r"predictive_maintenance.csv")
df = df.dropna()

# Drop unused columns
df = df.drop(columns=['UDI', 'Product ID'])

# Preprocessing
encoder.fit(df['Type'])  # Change type to numeric values
df['Type'] = encoder.fit_transform(df['Type'])

# Separating input features and target
X = df[["Type", "Air temperature [K]", "Process temperature [K]",
        "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]",
        "Target"]]
X = X.to_numpy()

y = df['Failure Type']

#Min max scaling
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)

model = LogisticRegression(random_state=42, class_weight='balanced',max_iter=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


#Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
#plt.show()


joblib.dump(model, "model") #Create model file
mj = joblib.load('model') #Load model file



def convert(value):
    if value == "H":
        numeric_value = 0
    elif value == "L":
        numeric_value = 1
    elif value == "M":
        numeric_value = 2
    return numeric_value

        

def predict(values):
        return mj.predict([values])



instance = [convert("M"),298.2,308.5,2678,10.7,86,1]

prediction = predict(instance)
print(prediction)

