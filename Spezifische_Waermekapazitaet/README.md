# Hinweise für den Versuch: "Spezifische Wärmekapazität" 

## Hinweise zum Ablauf

Dieser Versuch wird **nicht von allen Studierenden**, sondern nur von den Gruppen 1–20 durchgeführt. Die Vorbesprechung des Versuchs findet an jedem Praktikumstag zwischen 13:30–14:00 statt.

##  Aufgabe 1: Spezifische Wärmekapazität

### Prinzip der Messung

Bei diesem Versuch sollen Sie die spezifische Wärmekapazität eines Metalls, wie z.B. Aluminium mit Hilfe der bekannten spezifischen Wärmekapazität von Wasser ($c_{\mathrm{H_{2}O}}=4,18\,\mathrm{kJ/(kg\,K)}$) bestimmen. die spezifische Wärmekapazität ist definiert als

```math
\begin{equation*}
c = \frac{1}{m}\frac{\partial Q}{\partial T},
\end{equation*}
```

wobei $m$ der Masse des zu untersuchenden Materials, $\partial Q$ der Änderung der Wärmemenge und $\partial T$ der Änderung der Temperatur entsprechen.

Hierzu bringen Sie das gegebene Metall ($\mathrm{M}$, mit der Temperatur $T_{\mathrm{M}}$ und Masse $m_{\mathrm{M}}$) in ein Wärmebad aus Wasser (mit der Temperatur $T_{\mathrm{H_{2}O}}\neq T_{\mathrm{M}}$ und Masse $m_{\mathrm{H_{2}O}}$) und warten, bis sich eine Mischtemperatur $T_{\mathrm{Mix}}$ einstellt. Die Temperatur $T_{\mathrm{Mix}}$ stellt sich durch den Übergang von Wärme $\partial Q$ von einem zum anderen Material ein. 
```math
\begin{equation*}
\begin{split}
&c_{\mathrm{H_{2}O}}\,m_{\mathrm{H_{2}O}}\left(T_{\mathrm{H_{2}O}}-T_{\mathrm{Mix}}\right) = c_{\mathrm{M}}\,m_{\mathrm{M}}\left(T_{\mathrm{M}}-T_{\mathrm{Mix}}\right) \\
&\\
&c_{\mathrm{M}} = c_{\mathrm{H_{2}O}}\frac{m_{\mathrm{H_{2}O}}\left(T_{\mathrm{H_{2}O}}-T_{\mathrm{Mix}}\right)}{m_{\mathrm{M}}\left(T_{\mathrm{M}}-T_{\mathrm{Mix}}\right)} \\
\end{split}
\end{equation*}
```

Eine wichtige Voraussetzung dieser Messung ist, dass kein weiterer Wärmeaustausch mit der Umgebung stattfindet. 

---

## Aufgabe 2: Spezifische Wärmekapazität als Funktion der Temperatur

### Prinzip der Messung

Da dem Aluminium-Hohlzylinder durch die Heizspule Wärme ($\Delta Q$) zugeführt, jedoch keine Arbeit verrichtet wird geht $\Delta Q$ vollständig in innere Energie ($\Delta U$) über:

```math
\begin{equation*}
P_{\mathrm{H}}\,\Delta t = \Delta Q = \Delta U = c_{\mathrm{Al}}(T)\,m_{\mathrm{Al}}\,\Delta T,
\end{equation*}
```

wobei $P_{\mathrm{H}}$ der Heizleistung der Spule, $m_{\mathrm{Al}}$ der Masse des Hohlzylinders und $\Delta T$ der Temperaturänderung im Zeitintervall $\Delta t$ entsprechen. Daraus ergibt sich 

```math
c_{\mathrm{Al}}(T) = \frac{P_{\mathrm{H}}}{m_{\mathrm{Al}}\, \dot{T}^{(0)}(T)}; \qquad \text{mit: }\dot{T}^{(0)}(T) = \lim\limits_{\Delta t\to0}\left(\frac{\Delta T}{\Delta t}\right). \qquad\text{(1)}
```

### Hinweise zur Durchführung:

Bei der Durchführung wird über $\approx 3\,\mathrm{h}$ in einem festen Intervall von $\Delta t = 10\,\mathrm{s}$ ein Wert aufgezeichnet. Sie sollten deutlich über $100$ Datenpunkte erhalten und können $\dot{T}$ ruhig durch einen Differenzenquotienten benachbarter Messpunkte approximieren. Bestimmen Sie diesen als Funktion von $T$, $\dot{T}(T)$. 

Bei der Auswertung sollten Sie berücksichtigen, dass dem System auch aus der Umgebung Wärme zugeführt wird, die in den gleichen Zeitintervallen zu einer Temperaturänderung $\Delta T_{\mathrm{U}}$ des Hohlzylinders führt. Durch die Ihnen zur Verfügung gestellte Nullmessung können Sie $\dot{T}_{\mathrm{U}}(T)$ bestimmen und $\dot{T}(T)$ in Gleichung (1) entsprechend korrigieren:

```math
\begin{equation*}
\dot{T}(T) = \lim\limits_{\Delta t\to0}\left(\frac{\Delta T - \Delta T_{\mathrm{U}}}{\Delta t}\right) = \dot{T}^{(0)}(T) - \dot{T}_{\mathrm{U}}(T).
\end{equation*}
```



