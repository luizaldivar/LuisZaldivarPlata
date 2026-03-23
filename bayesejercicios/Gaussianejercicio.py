"""
Proyecto: Clasificación de Riesgo Crediticio
Modelo: Gaussian Naive Bayes
Autor: Luis 
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# =============================================================================
# PARTE 1: CARGA Y LIMPIEZA
# =============================================================================
df = pd.read_csv("credit_risk_dataset.csv")

# Rellenar valores nulos con 0 (Personas sin experiencia o tasa no definida)
df['person_emp_length'] = df['person_emp_length'].fillna(0)
df['loan_int_rate'] = df['loan_int_rate'].fillna(0)

# Convertir datos categóricos a numéricos usando LabelEncoder individual
le_home = LabelEncoder()
le_intent = LabelEncoder()
le_grade = LabelEncoder()
le_default = LabelEncoder()

df['person_home_ownership'] = le_home.fit_transform(df['person_home_ownership'])
df['loan_intent'] = le_intent.fit_transform(df['loan_intent'])
df['loan_grade'] = le_grade.fit_transform(df['loan_grade'])
df['cb_person_default_on_file'] = le_default.fit_transform(df['cb_person_default_on_file'])

# =============================================================================
# PARTE 2: EXPLORACIÓN
# =============================================================================
pd.set_option('display.max_columns', 12)
print("--- Descripción Estadística ---")
print(df.describe())
print("\n--- Información General ---")
df.info()

# =============================================================================
# PARTE 3: IDENTIFICACIÓN DE VARIABLES X, Y
# =============================================================================
columnas_x = [
    'person_age', 'person_income', 'person_home_ownership', 'person_emp_length',
    'loan_intent', 'loan_grade', 'loan_amnt', 'loan_int_rate',
    'loan_percent_income', 'cb_person_default_on_file', 'cb_person_cred_hist_length'
]

X = df[columnas_x]
y = df['loan_status']

# =============================================================================
# PARTE 4: DIVISIÓN TRAIN, TEST
# =============================================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# =============================================================================
# PARTE 5: MODELO GAUSSIANNB
# =============================================================================
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# =============================================================================
# PARTE 6: PREDICCIÓN
# =============================================================================
y_pred = modelo.predict(X_test)

# =============================================================================
# PARTE 7: EVALUACIÓN
# =============================================================================
precision = accuracy_score(y_test, y_pred)
matriz = confusion_matrix(y_test, y_pred)

print(f"\nAccuracy (Precisión): {precision:.4f}")
print("\nMatriz de Confusión:")
print(matriz)

# =============================================================================
# PARTE 8: PRUEBA Y REFLEXIÓN
# =============================================================================
nuevo_cliente = [[
    25,                                    # person_age
    50000,                                 # person_income
    le_home.transform(['RENT'])[0],        # person_home_ownership
    4,                                     # person_emp_length
    le_intent.transform(['PERSONAL'])[0],  # loan_intent
    le_grade.transform(['B'])[0],          # loan_grade
    10000,                                 # loan_amnt
    11.5,                                  # loan_int_rate
    0.20,                                  # loan_percent_income
    le_default.transform(['N'])[0],        # cb_person_default_on_file
    5                                      # cb_person_cred_hist_length
]]

pred_riesgo = modelo.predict(nuevo_cliente)

print("\n--- Resultado de la Prueba ---")
if pred_riesgo < 1:
    print("Credito aceptado, buen cliente")
else:
    print("Cliente de alto riesgo")

# --- Respuestas a la Reflexión ---
# ¿Por qué GaussianNB
#R: Debido al tipo de datos que estamos manejando, nos interesa un analisis numerico a diferencia del nominal que se centraba unicamente en palabras,
#¿Qué variable crees que más influye?
#R: La tasa de interes es la que mas influye, un alta tasa es equivalente a una mayor facilidad a que el cliente sea deudor