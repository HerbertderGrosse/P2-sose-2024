# Hinweise für den Versuch: "Spezifische Wärmekapazität" 

##  Spezifischen Wärmekapazität

Die spezifische Wärmekapazität eines Stoffs $X$ ist definiert als
$$
\begin{equation*}
c_{X} = \frac{1}{m_{X}}\frac{\partial Q}{\partial T},
\end{equation*}
$$
wobei $m_{X}$ der Masse von $X$, $\partial Q$ der Änderung der Wärmemenge und $\partial T$ der Änderung der Temperatur entsprechen. Für einen Festkörper oder eine Flüssigkeit gehen Wärmeänderungen, solange Sie nicht zur Änderung des Aggregatzustands führen, in sehr guter Näherung vollständig in Änderungen der inneren Energie $\mathrm{d} U$ und damit in eine Erhöhung der Temperatur $\mathrm{d} T$ über. 

### Prinzip der Messung

Bei diesem Versuch sollen Sie $c_{\mathrm{M}}$ für verschiedene Metalle M, wie z.B. Aluminium mit Hilfe des bekannten Werts $c_{\mathrm{H_{2}O}}=4.1815\ \mathrm{kJ/(kg\,K)}$ von Wasser bestimmen. Hierzu bringen Sie M, mit der Temperatur $T_{\mathrm{M}}$ und der Masse $m_{\mathrm{M}}$ in ein Wärmebad aus Wasser, mit der bekannten Temperatur $T_{\mathrm{H_{2}O}}\neq T_{\mathrm{M}}$ und Masse $m_{\mathrm{H_{2}O}}$ und bestimmen die Mischtemperatur $T_{\mathrm{Mix}}$, die sich nach einiger Zeit einstellt. Dies geschieht durch den Übergang von Wärme $\partial Q$ von einem zum anderen Material. 
$$
\begin{equation*}
\begin{split}
&c_{\mathrm{H_{2}O}}\,m_{\mathrm{H_{2}O}}\left(T_{\mathrm{H_{2}O}}-T_{\mathrm{Mix}}\right) = c_{\mathrm{M}}\,m_{\mathrm{M}}\left(T_{\mathrm{M}}-T_{\mathrm{Mix}}\right) \\
&\\
&c_{\mathrm{M}} = c_{\mathrm{H_{2}O}}\frac{m_{\mathrm{H_{2}O}}\left(T_{\mathrm{H_{2}O}}-T_{\mathrm{Mix}}\right)}{m_{\mathrm{M}}\left(T_{\mathrm{M}}-T_{\mathrm{Mix}}\right)} \\
\end{split}
\end{equation*}
$$
**Eine wichtige Voraussetzung dieser Messung ist, dass kein weiterer Wärmeaustausch mit der Umgebung stattfindet!** 

## Spezifische Wärmekapazität als Funktion der Temperatur

### Prinzip der Messung

Für diese Messung kühlen Sie einen Aluminium-Hohlzylinder in einem Wärmebad von flüssigem Stickstoff auf möglichst tiefe Temperaturen ab. Daraufhin führen Sie dem Hohlzylinder durch eine Heizspule mit der Leistung $P_{\mathrm{Heiz}}$ in festen Zeitintervallen $\mathrm{dt}$ kontrolliert Wärme $\delta Q = P_{\mathrm{Heiz}}\,\mathrm{d}t$ zu. Da dabei keine Arbeit verrichtet wird ($\delta W=0$) geht $\delta Q$ vollständig in innere Energie ($\mathrm{d}U$) über:

$$
\begin{equation*}
P_{\mathrm{H}}\,\mathrm{d}t = \delta Q = \mathrm{d}U = c_{\mathrm{Al}}(T)\,m_{\mathrm{Al}}\,\mathrm{d} T.
\end{equation*}
$$
Daraus ergibt sich 

$$
\begin{equation}
\begin{split}
&c_{\mathrm{Al}}(T) = \frac{P_{\mathrm{H}}}{m_{\mathrm{Al}}\, \dot{T}^{(0)}(T)};\\ 
&\\
&\text{mit:}\\
&\\
&\dot{T}^{(0)}(T) = \lim\limits_{\Delta t\to0}\left(\frac{\Delta T}{\Delta t}\right).\\ 
\end{split}
\end{equation}
$$


### Hinweise zur Durchführung:

Bei der Durchführung wird über $\approx 3\,\mathrm{h}$ in einem festen Intervall von $\Delta t = 10\,\mathrm{s}$ ein Wert aufgezeichnet. Sie sollten deutlich über $100$ Datenpunkte erhalten und können $\dot{T}$ ruhig durch einen Differenzenquotienten benachbarter Messpunkte approximieren. Bestimmen Sie diesen als Funktion von $T$, $\dot{T}(T)$. 

Bei der Auswertung sollten Sie berücksichtigen, dass dem System auch aus der Umgebung Wärme zugeführt wird, die in den gleichen Zeitintervallen zu einer Temperaturänderung $\Delta T_{\mathrm{U}}$ des Hohlzylinders führt. Durch die Ihnen zur Verfügung gestellte Nullmessung können Sie $\dot{T}_{\mathrm{U}}(T)$ bestimmen und $\dot{T}(T)$ in Gleichung (1) entsprechend korrigieren:

```math
\begin{equation*}
\dot{T}(T) = \lim\limits_{\Delta t\to0}\left(\frac{\Delta T - \Delta T_{\mathrm{U}}}{\Delta t}\right) = \dot{T}^{(0)}(T) - \dot{T}_{\mathrm{U}}(T).
\end{equation*}
```



