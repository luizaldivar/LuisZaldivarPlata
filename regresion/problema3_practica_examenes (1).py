"""
Problema 3: Regresión Lineal — Horas de Práctica vs Puntuación en Examen
Instructor de Programación | 150 estudiantes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ── 1. CARGAR Y EXPLORAR DATOS ────────────────────────────────────────────────
df = pd.read_csv("/mnt/user-data/uploads/PracticaExamenes.csv")
df.columns = df.columns.str.strip()

print("=" * 60)
print("  PROBLEMA 3 — HORAS DE PRÁCTICA vs PUNTUACIÓN")
print("=" * 60)
print(f"\n📂 Datos cargados: {len(df)} registros")
print(f"\n{df.describe().round(2)}\n")

X = df["horas"].values
y = df["puntuacion"].values

correlacion = np.corrcoef(X, y)[0, 1]
print(f"  Correlación de Pearson (r): {correlacion:.4f}")
print(f"  Interpretación: {'Fuerte' if abs(correlacion) > 0.7 else 'Moderada' if abs(correlacion) > 0.4 else 'Débil'}"
      f" correlación {'positiva' if correlacion > 0 else 'negativa'}\n")

# ── 2. MODELO DE REGRESIÓN LINEAL SIMPLE ──────────────────────────────────────
X_2d  = X.reshape(-1, 1)
modelo = LinearRegression()
modelo.fit(X_2d, y)

pendiente  = modelo.coef_[0]
intercepto = modelo.intercept_
y_pred     = modelo.predict(X_2d)

# ── 3. ECUACIÓN DE LA RECTA ───────────────────────────────────────────────────
r2   = r2_score(y, y_pred)
mse  = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
n    = len(X)

print("─" * 60)
print("  ECUACIÓN DE LA RECTA DE REGRESIÓN")
print("─" * 60)
print(f"  Puntuación = {pendiente:.4f} × Horas"
      f" {'+ ' if intercepto >= 0 else '– '}{abs(intercepto):.4f}")
print(f"  Pendiente  : {pendiente:.4f}")
print(f"    → Por cada hora adicional de práctica, la puntuación")
print(f"      aumenta en promedio {pendiente:.2f} puntos.")
print(f"  Intercepto : {intercepto:.4f}")
print(f"    → Puntuación base estimada con 0 horas de práctica.")

print()
print("─" * 60)
print("  COEFICIENTE DE DETERMINACIÓN R²")
print("─" * 60)
print(f"  R²   = {r2:.4f}")
print(f"  → El modelo explica el {r2*100:.1f}% de la variabilidad")
print(f"    en las puntuaciones de los estudiantes.")
print(f"  MSE  = {mse:.2f}")
print(f"  RMSE = {rmse:.2f}")

# ── 4. FUNCIÓN DE PREDICCIÓN ──────────────────────────────────────────────────
def predecir_puntuacion(horas: float) -> float:
    """
    Predice la puntuación esperada dado un número de horas de práctica.

    Parámetros
    ----------
    horas : float
        Horas de práctica semanal.

    Retorna
    -------
    float
        Puntuación estimada en el examen (escala 0-100).
    """
    pred = modelo.predict([[horas]])[0]
    return min(max(pred, 0), 100)   # limitar a rango válido

print()
print("─" * 60)
print("  PREDICCIONES DE EJEMPLO")
print("─" * 60)
for h in [2, 5, 8, 12, 15, 20]:
    p = predecir_puntuacion(h)
    print(f"  {h:>3} horas/semana  →  {p:.1f} puntos estimados")

# ── 5. VISUALIZACIÓN PROFESIONAL ─────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")

COLOR_FONDO    = "#0a0e1a"
COLOR_PANEL    = "#131929"
COLOR_PUNTOS   = "#80cbc4"
COLOR_LINEA    = "#f48fb1"
COLOR_BANDA    = "#f48fb1"
COLOR_TEXTO    = "#eceff1"
COLOR_SUBTEXTO = "#78909c"
COLOR_HIST     = "#7986cb"

fig = plt.figure(figsize=(14, 9))
fig.patch.set_facecolor(COLOR_FONDO)
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.50, wspace=0.38)

# ── Panel principal: dispersión + regresión ───────────────────────────────────
ax1 = fig.add_subplot(gs[:, :2])
ax1.set_facecolor(COLOR_PANEL)

x_line = np.linspace(X.min() - 0.5, X.max() + 0.5, 300)
y_line = modelo.predict(x_line.reshape(-1, 1))

ax1.fill_between(x_line, y_line - rmse, y_line + rmse,
                 color=COLOR_BANDA, alpha=0.10, label=f"±1 RMSE ({rmse:.2f} pts)")
ax1.scatter(X, y, color=COLOR_PUNTOS, alpha=0.60, s=50,
            edgecolors="white", linewidths=0.4, zorder=3, label="Estudiantes")
ax1.plot(x_line, y_line, color=COLOR_LINEA, linewidth=2.8,
         label="Regresión lineal", zorder=4)

# Puntos predicción de ejemplo
horas_demo = [5, 10, 15, 20]
for h in horas_demo:
    p = predecir_puntuacion(h)
    ax1.annotate(
        f"{h}h → {p:.0f}pts",
        xy=(h, p), xytext=(h + 0.5, p - 3.5),
        color="#ffe082", fontsize=8, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="#ffe082", lw=1.0),
    )
    ax1.scatter([h], [p], color="#ffe082", s=80, zorder=5,
                edgecolors="white", linewidths=0.8)

ecuacion = (f"Puntuación = {pendiente:.2f}·Horas"
            f" {'+ ' if intercepto >= 0 else '– '}{abs(intercepto):.2f}")
ax1.text(0.04, 0.94, ecuacion, transform=ax1.transAxes,
         fontsize=12, color=COLOR_LINEA, fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.4", facecolor=COLOR_PANEL,
                   edgecolor=COLOR_LINEA, alpha=0.85))
ax1.text(0.04, 0.86, f"R² = {r2:.4f}   |   r = {correlacion:.4f}",
         transform=ax1.transAxes, fontsize=10, color=COLOR_TEXTO,
         bbox=dict(boxstyle="round,pad=0.3", facecolor=COLOR_PANEL,
                   edgecolor="#445", alpha=0.8))

ax1.set_xlabel("Horas de Práctica Semanal", color=COLOR_TEXTO, fontsize=11)
ax1.set_ylabel("Puntuación en Examen (pts)", color=COLOR_TEXTO, fontsize=11)
ax1.set_title("Horas de Práctica vs Puntuación Final\nAnálisis de Regresión Lineal Simple",
              color=COLOR_TEXTO, fontsize=13, fontweight="bold", pad=14)
ax1.tick_params(colors=COLOR_SUBTEXTO)
ax1.spines[:].set_color("#223")
ax1.legend(facecolor=COLOR_PANEL, edgecolor="#445",
           labelcolor=COLOR_TEXTO, fontsize=9)

# ── Panel superior derecho: distribución de residuos ─────────────────────────
ax2 = fig.add_subplot(gs[0, 2])
ax2.set_facecolor(COLOR_PANEL)

residuos = y - y_pred
ax2.hist(residuos, bins=18, color=COLOR_HIST, edgecolor="white",
         linewidth=0.5, alpha=0.85)
ax2.axvline(0, color=COLOR_LINEA, linewidth=1.5, linestyle="--")
ax2.set_xlabel("Residuo", color=COLOR_TEXTO, fontsize=9)
ax2.set_ylabel("Frecuencia", color=COLOR_TEXTO, fontsize=9)
ax2.set_title("Distribución\nde Residuos", color=COLOR_TEXTO,
              fontsize=10, fontweight="bold", pad=8)
ax2.tick_params(colors=COLOR_SUBTEXTO, labelsize=8)
ax2.spines[:].set_color("#223")

# ── Panel inferior derecho: curva de predicción ───────────────────────────────
ax3 = fig.add_subplot(gs[1, 2])
ax3.set_facecolor(COLOR_PANEL)

horas_rng = np.linspace(1, 25, 100)
preds_rng = [predecir_puntuacion(h) for h in horas_rng]

ax3.plot(horas_rng, preds_rng, color=COLOR_LINEA, linewidth=2.2)
ax3.fill_between(horas_rng, preds_rng, alpha=0.15, color=COLOR_LINEA)
ax3.set_xlabel("Horas de Práctica", color=COLOR_TEXTO, fontsize=9)
ax3.set_ylabel("Puntuación Predicha", color=COLOR_TEXTO, fontsize=9)
ax3.set_title("Curva de\nPredicción", color=COLOR_TEXTO,
              fontsize=10, fontweight="bold", pad=8)
ax3.tick_params(colors=COLOR_SUBTEXTO, labelsize=8)
ax3.spines[:].set_color("#223")

fig.suptitle("Análisis de Regresión Lineal — Práctica vs Rendimiento Académico",
             color=COLOR_TEXTO, fontsize=15, fontweight="bold", y=0.98)

plt.savefig("/mnt/user-data/outputs/problema3_practica_examenes.png",
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.show()
print("\n✅ Gráfico guardado: problema3_practica_examenes.png")
