"""
Problema 1: Regresión Lineal — Inversión en Publicidad vs Unidades Vendidas
Departamento de Marketing | 100 meses de datos históricos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# ── 1. CARGAR Y PROCESAR DATOS ────────────────────────────────────────────────
df = pd.read_csv("/mnt/user-data/uploads/PublicidadVentas.csv")
df.columns = df.columns.str.strip()

print("=" * 60)
print("  PROBLEMA 1 — PUBLICIDAD vs VENTAS")
print("=" * 60)
print(f"\n📂 Datos cargados: {len(df)} registros")
print(f"\n{df.describe().round(2)}\n")

X = df[["Inversion"]].values
y = df["Ventas"].values

# ── 2. AJUSTAR MODELO DE REGRESIÓN LINEAL ─────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

pendiente   = modelo.coef_[0]
intercepto  = modelo.intercept_
y_pred      = modelo.predict(X_test)

# ── 3. MÉTRICAS DE CALIDAD ────────────────────────────────────────────────────
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2  = r2_score(y_test, y_pred)
r2_train = modelo.score(X_train, y_train)

print("─" * 60)
print("  PARÁMETROS DEL MODELO")
print("─" * 60)
print(f"  Ecuación  : Ventas = {pendiente:.2f} × Inversión + {intercepto:.2f}")
print(f"  Pendiente : {pendiente:.4f}  (unidades vendidas por cada $1k invertido)")
print(f"  Intercepto: {intercepto:.4f}")
print()
print("─" * 60)
print("  MÉTRICAS DE EVALUACIÓN")
print("─" * 60)
print(f"  MSE  (test) : {mse:.2f}")
print(f"  RMSE (test) : {rmse:.2f}")
print(f"  R²   (test) : {r2:.4f}  →  {r2*100:.1f}% de varianza explicada")
print(f"  R²   (train): {r2_train:.4f}")

# ── 4. FUNCIÓN DE PREDICCIÓN ──────────────────────────────────────────────────
def estimar_ventas(inversion_miles: float) -> float:
    """
    Estima las unidades vendidas dado un nivel de inversión publicitaria.

    Parámetros
    ----------
    inversion_miles : float
        Inversión en publicidad digital en miles de dólares.

    Retorna
    -------
    float
        Unidades vendidas estimadas.
    """
    prediccion = modelo.predict([[inversion_miles]])[0]
    return prediccion

print()
print("─" * 60)
print("  PREDICCIONES DE EJEMPLO")
print("─" * 60)
for inv in [2.0, 3.5, 5.0, 7.5, 10.0]:
    print(f"  Inversión ${inv:.1f}k  →  {estimar_ventas(inv):,.0f} unidades vendidas")

# ── 5. VISUALIZACIÓN PROFESIONAL ─────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")

fig = plt.figure(figsize=(14, 9))
fig.patch.set_facecolor("#0f1117")
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)

COLOR_PUNTOS   = "#4fc3f7"
COLOR_LINEA    = "#ff6b6b"
COLOR_RESIDUAL = "#a5d6a7"
COLOR_FONDO    = "#1a1d27"
COLOR_TEXTO    = "#e0e0e0"
COLOR_SUBTEXTO = "#9e9e9e"

# ── Panel principal: dispersión + línea de regresión ─────────────────────────
ax1 = fig.add_subplot(gs[:, 0])
ax1.set_facecolor(COLOR_FONDO)

x_line = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
y_line = modelo.predict(x_line)

ax1.scatter(X, y, color=COLOR_PUNTOS, alpha=0.65, s=55,
            edgecolors="white", linewidths=0.4, zorder=3, label="Datos reales")
ax1.plot(x_line, y_line, color=COLOR_LINEA, linewidth=2.5,
         label="Línea de regresión", zorder=4)

# Banda de confianza visual (±1 RMSE)
ax1.fill_between(x_line.ravel(), y_line - rmse, y_line + rmse,
                 color=COLOR_LINEA, alpha=0.12, label=f"±1 RMSE ({rmse:.1f})")

ecuacion = (f"Ventas = {pendiente:.2f}·Inversión"
            f" {'+ ' if intercepto >= 0 else '– '}{abs(intercepto):.2f}")
ax1.text(0.04, 0.93, ecuacion, transform=ax1.transAxes,
         fontsize=11, color=COLOR_LINEA, fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#1a1d27",
                   edgecolor=COLOR_LINEA, alpha=0.8))
ax1.text(0.04, 0.83, f"R² = {r2:.4f}", transform=ax1.transAxes,
         fontsize=10, color=COLOR_TEXTO,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="#1a1d27",
                   edgecolor="#555", alpha=0.8))

ax1.set_xlabel("Inversión en Publicidad (miles USD)", color=COLOR_TEXTO, fontsize=11)
ax1.set_ylabel("Unidades Vendidas", color=COLOR_TEXTO, fontsize=11)
ax1.set_title("Inversión Publicitaria vs Unidades Vendidas", color=COLOR_TEXTO,
              fontsize=13, fontweight="bold", pad=14)
ax1.tick_params(colors=COLOR_SUBTEXTO)
ax1.spines[:].set_color("#333")
leg = ax1.legend(facecolor=COLOR_FONDO, edgecolor="#555",
                 labelcolor=COLOR_TEXTO, fontsize=9)

# ── Panel superior derecho: residuos ─────────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor(COLOR_FONDO)

y_pred_all = modelo.predict(X)
residuos   = y - y_pred_all

ax2.scatter(y_pred_all, residuos, color=COLOR_RESIDUAL, alpha=0.6,
            s=40, edgecolors="white", linewidths=0.3)
ax2.axhline(0, color=COLOR_LINEA, linewidth=1.5, linestyle="--")
ax2.set_xlabel("Valores predichos", color=COLOR_TEXTO, fontsize=9)
ax2.set_ylabel("Residuos", color=COLOR_TEXTO, fontsize=9)
ax2.set_title("Gráfico de Residuos", color=COLOR_TEXTO, fontsize=11,
              fontweight="bold", pad=10)
ax2.tick_params(colors=COLOR_SUBTEXTO, labelsize=8)
ax2.spines[:].set_color("#333")

# ── Panel inferior derecho: predicciones interactivas ─────────────────────────
ax3 = fig.add_subplot(gs[1, 1])
ax3.set_facecolor(COLOR_FONDO)

inversiones  = [2.0, 3.5, 5.0, 7.5, 10.0]
predicciones = [estimar_ventas(i) for i in inversiones]
colores_barra = plt.cm.cool(np.linspace(0.2, 0.9, len(inversiones)))

bars = ax3.bar([f"${i}k" for i in inversiones], predicciones,
               color=colores_barra, edgecolor="white", linewidth=0.5, zorder=3)
for bar, val in zip(bars, predicciones):
    ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
             f"{val:,.0f}", ha="center", va="bottom",
             color=COLOR_TEXTO, fontsize=8, fontweight="bold")

ax3.set_xlabel("Inversión en Publicidad", color=COLOR_TEXTO, fontsize=9)
ax3.set_ylabel("Unidades Estimadas", color=COLOR_TEXTO, fontsize=9)
ax3.set_title("Predicciones por Nivel de Inversión", color=COLOR_TEXTO,
              fontsize=11, fontweight="bold", pad=10)
ax3.tick_params(colors=COLOR_SUBTEXTO, labelsize=8)
ax3.spines[:].set_color("#333")

# Título general
fig.suptitle("Análisis de Regresión Lineal — Marketing Digital",
             color=COLOR_TEXTO, fontsize=16, fontweight="bold", y=0.98)

plt.savefig("/mnt/user-data/outputs/problema1_publicidad_ventas.png",
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.show()
print("\n✅ Gráfico guardado: problema1_publicidad_ventas.png")
