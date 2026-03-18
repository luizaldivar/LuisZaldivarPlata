"""
Problema 2: Regresión Lineal — Edad vs Costo Mensual de Póliza
Aseguradora | 120 clientes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import scipy.stats as stats

# ── 1. CARGAR DATOS ───────────────────────────────────────────────────────────
df = pd.read_csv("/mnt/user-data/uploads/EdadSeguros.csv")
df.columns = df.columns.str.strip()

print("=" * 60)
print("  PROBLEMA 2 — EDAD vs COSTO DE PÓLIZA")
print("=" * 60)
print(f"\n📂 Datos cargados: {len(df)} registros")
print(f"\n{df.describe().round(2)}\n")

X = df["Edad"].values
y = df["Costo"].values
n = len(X)

# ── 2. VERIFICAR RELACIÓN LINEAL (gráfico inicial) ───────────────────────────
# (incluido en el panel de visualización final)

# ── 3. ENTRENAR MODELO Y EXTRAER PARÁMETROS ───────────────────────────────────
X_2d = X.reshape(-1, 1)
modelo = LinearRegression()
modelo.fit(X_2d, y)

pendiente  = modelo.coef_[0]
intercepto = modelo.intercept_
y_pred     = modelo.predict(X_2d)

r2   = r2_score(y, y_pred)
mse  = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print("─" * 60)
print("  PARÁMETROS DEL MODELO")
print("─" * 60)
print(f"  Ecuación  : Costo = {pendiente:.4f} × Edad + {intercepto:.4f}")
print(f"  Pendiente : {pendiente:.4f}  ($ adicionales por año de edad)")
print(f"  Intercepto: {intercepto:.4f}")
print()
print("─" * 60)
print("  MÉTRICAS DE EVALUACIÓN")
print("─" * 60)
print(f"  R²  : {r2:.4f}  →  {r2*100:.1f}% de varianza explicada")
print(f"  MSE : {mse:.2f}")
print(f"  RMSE: {rmse:.2f}")

# ── 4. INTERVALOS DE CONFIANZA ────────────────────────────────────────────────
# IC al 95% usando distribución t
alpha    = 0.05
t_crit   = stats.t.ppf(1 - alpha / 2, df=n - 2)
x_mean   = X.mean()
ss_x     = np.sum((X - x_mean) ** 2)
residuos = y - y_pred
s_e      = np.sqrt(np.sum(residuos ** 2) / (n - 2))   # error estándar residual

def intervalo_confianza(x_nuevo):
    """Calcula predicción e IC 95% para un valor de edad."""
    pred = modelo.predict([[x_nuevo]])[0]
    se_pred = s_e * np.sqrt(1/n + (x_nuevo - x_mean)**2 / ss_x)
    margen   = t_crit * se_pred
    return pred, pred - margen, pred + margen

# ── 5. TABLA PREDICCIONES EDADES CLAVE ────────────────────────────────────────
edades_clave = [30, 40, 50, 60]
print()
print("─" * 60)
print("  PREDICCIONES PARA EDADES CLAVE (IC 95%)")
print("─" * 60)
print(f"  {'Edad':>6} │ {'Costo Est.':>12} │ {'Límite Inf.':>12} │ {'Límite Sup.':>12}")
print(f"  {'─'*6}─┼─{'─'*12}─┼─{'─'*12}─┼─{'─'*12}")
tabla = []
for edad in edades_clave:
    pred, li, ls = intervalo_confianza(edad)
    tabla.append((edad, pred, li, ls))
    print(f"  {edad:>6} │ ${pred:>10.2f} │ ${li:>10.2f} │ ${ls:>10.2f}")

# ── 6. VISUALIZACIÓN PROFESIONAL ─────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")

COLOR_FONDO    = "#0d1b2a"
COLOR_PANEL    = "#1b2838"
COLOR_PUNTOS   = "#64b5f6"
COLOR_LINEA    = "#ffb74d"
COLOR_IC       = "#ef9a9a"
COLOR_TABLA    = "#81c784"
COLOR_TEXTO    = "#eceff1"
COLOR_SUBTEXTO = "#90a4ae"

fig = plt.figure(figsize=(14, 9))
fig.patch.set_facecolor(COLOR_FONDO)
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.38)

# ── Panel principal: datos + regresión + IC ───────────────────────────────────
ax1 = fig.add_subplot(gs[:, 0])
ax1.set_facecolor(COLOR_PANEL)

x_line = np.linspace(X.min() - 1, X.max() + 1, 300)
y_line = modelo.predict(x_line.reshape(-1, 1))

# IC para la línea de regresión
se_line = s_e * np.sqrt(1/n + (x_line - x_mean)**2 / ss_x)
y_low   = y_line - t_crit * se_line
y_high  = y_line + t_crit * se_line

ax1.fill_between(x_line, y_low, y_high, alpha=0.20,
                 color=COLOR_IC, label="IC 95%")
ax1.scatter(X, y, color=COLOR_PUNTOS, alpha=0.65, s=55,
            edgecolors="white", linewidths=0.4, zorder=3, label="Clientes")
ax1.plot(x_line, y_line, color=COLOR_LINEA, linewidth=2.5,
         label="Línea de regresión", zorder=4)

# Marcar edades clave
for edad, pred, li, ls in tabla:
    ax1.axvline(edad, color=COLOR_TABLA, linewidth=0.8, linestyle=":", alpha=0.6)
    ax1.scatter([edad], [pred], color=COLOR_TABLA, s=90, zorder=5,
                edgecolors="white", linewidths=0.8)

ecuacion = (f"Costo = {pendiente:.2f}·Edad"
            f" {'+ ' if intercepto >= 0 else '– '}{abs(intercepto):.2f}")
ax1.text(0.04, 0.94, ecuacion, transform=ax1.transAxes,
         fontsize=11, color=COLOR_LINEA, fontweight="bold",
         bbox=dict(boxstyle="round,pad=0.4", facecolor=COLOR_PANEL,
                   edgecolor=COLOR_LINEA, alpha=0.85))
ax1.text(0.04, 0.84, f"R² = {r2:.4f}", transform=ax1.transAxes,
         fontsize=10, color=COLOR_TEXTO,
         bbox=dict(boxstyle="round,pad=0.3", facecolor=COLOR_PANEL,
                   edgecolor="#555", alpha=0.8))

ax1.set_xlabel("Edad del cliente (años)", color=COLOR_TEXTO, fontsize=11)
ax1.set_ylabel("Costo mensual de póliza (USD)", color=COLOR_TEXTO, fontsize=11)
ax1.set_title("Edad vs Costo Mensual de Póliza\ncon Intervalo de Confianza 95%",
              color=COLOR_TEXTO, fontsize=12, fontweight="bold", pad=14)
ax1.tick_params(colors=COLOR_SUBTEXTO)
ax1.spines[:].set_color("#334")
ax1.legend(facecolor=COLOR_PANEL, edgecolor="#555",
           labelcolor=COLOR_TEXTO, fontsize=9)

# ── Panel superior derecho: residuos ─────────────────────────────────────────
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_facecolor(COLOR_PANEL)

ax2.scatter(y_pred, residuos, color="#ce93d8", alpha=0.65, s=40,
            edgecolors="white", linewidths=0.3)
ax2.axhline(0, color=COLOR_LINEA, linewidth=1.5, linestyle="--")
ax2.set_xlabel("Valores predichos", color=COLOR_TEXTO, fontsize=9)
ax2.set_ylabel("Residuos", color=COLOR_TEXTO, fontsize=9)
ax2.set_title("Gráfico de Residuos", color=COLOR_TEXTO, fontsize=11,
              fontweight="bold", pad=10)
ax2.tick_params(colors=COLOR_SUBTEXTO, labelsize=8)
ax2.spines[:].set_color("#334")

# ── Panel inferior derecho: tabla de edades clave ────────────────────────────
ax3 = fig.add_subplot(gs[1, 1])
ax3.set_facecolor(COLOR_PANEL)
ax3.axis("off")

encabezados = ["Edad", "Costo Est.", "IC Inf.", "IC Sup."]
filas = [[f"{e} años", f"${p:.2f}", f"${li:.2f}", f"${ls:.2f}"]
         for e, p, li, ls in tabla]

tabla_mpl = ax3.table(
    cellText=filas,
    colLabels=encabezados,
    cellLoc="center",
    loc="center",
)
tabla_mpl.auto_set_font_size(False)
tabla_mpl.set_fontsize(9)
tabla_mpl.scale(1.2, 1.8)

for (row, col), cell in tabla_mpl.get_celld().items():
    cell.set_facecolor(COLOR_PANEL if row > 0 else "#263850")
    cell.set_text_props(color=COLOR_TEXTO if row > 0 else COLOR_TABLA,
                        fontweight="bold" if row == 0 else "normal")
    cell.set_edgecolor("#334")

ax3.set_title("Predicciones — Edades Clave", color=COLOR_TEXTO,
              fontsize=11, fontweight="bold", pad=14)

fig.suptitle("Análisis de Regresión Lineal — Costo de Pólizas por Edad",
             color=COLOR_TEXTO, fontsize=16, fontweight="bold", y=0.98)

plt.savefig("/mnt/user-data/outputs/problema2_edad_seguros.png",
            dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.show()
print("\n✅ Gráfico guardado: problema2_edad_seguros.png")
