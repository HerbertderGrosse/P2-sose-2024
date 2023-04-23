# Hinweise für den Versuch Vakuum

 

## Aufgabe 2: Saugvermögen der DSP

### Prinzip der Messung

Den Volumendurchfluss (Volumenstrom)

```math
\frac{\mathrm{d}V}{\mathrm{d}t} = \dot{V}\equiv S
```

durch die Ansaugöffnung einer Pumpe bezeichnet man als **Saugvermögen**. Je nach Druck ($p$) und Temperatur ($T$) eines Gases verändert sich die Stoffmenge ($n$) des geförderten Gases bei gleichem Volumendurchfluss.

Die Menge eines Gases kann man durch seine Masse $m$ abschätzen. Bei Gasen gebräuchlicher ist jedoch die Angabe durch das Produkt $p\,V$, das nach der idealen Gasgleichung 

```math
\begin{equation*}
\begin{split}
& p\,V = n\,R\,T = \frac{m}{M_{M}}R\,T; \\
&\\
&m = \frac{p\,V}{R\,T}M_{M},
\end{split}
\end{equation*}
```

bei bekannter Temperatur zur Massenangabe äquivalent ist. Dabei entspricht $M_{M}$ der [molaren Masse](https://de.wikipedia.org/wiki/Molare_Masse) der Gasmoleküle. Für eine Pumpe ist neben dem Volumen- der **Massenfluss**

```math
\frac{\mathrm{d}m}{\mathrm{d}t} = \dot{m}\equiv q_{m}
```

von Relevanz, der entsprechend auch als **$pV$-Durchfluss**

```math
q_{pV} = \frac{\mathrm{d}(p\,V)}{\mathrm{dt}}
```

angegeben wird. Beachten Sie dass $q_{pV}$ zwar zu $q_{m}$ äquivalent, aber nicht damit identisch ist, der $pV$-Durchfluss trägt z.B. die Einheit einer Leistung.   

Die **Saugleistung** einer Pumpe wird entweder durch $q_{m}$ oder $q_{pV}$ an der Ansaugöffnung angegeben. Bei konstantem Druck $p$ gilt der einfache Zusammenhang 

```math
q_{pV} = \left.\frac{\mathrm{d}(p\,V)}{\mathrm{d}t}\right|_{p=const.} = p\frac{\mathrm{d}V}{\mathrm{d}t} = p\,S
```

Der Begriff der Saugleistung darf nicht mit dem Saugvermögen verwechselt werden. Die Saugleistung gibt die tatsächlich pro Zeiteinheit von der Pumpe abtransportierte Gasmenge an; das Saugvermögen ist die von der Pumpe pro Zeiteinheit *zur Verfügung gestellte* (maximale) "Transportkapazität". 

Wenn wir beim Saugvorgang von einer adiabatischen Zustandsänderung ($\delta Q=0$) ausgehen gilt: 

```math
\begin{equation*}
\begin{split}
\delta Q &= \mathrm{d}(p\,V) = 0;\\
&\\
&= p\,\mathrm{d}V  + V\,\mathrm{d}p \\
&\\
&= p\,S\,\mathrm{d}t  + V\,\mathrm{d}p;\\
&\\
\frac{\mathrm{d}p}{p} &= -\frac{S}{V}\mathrm{d}t,
\end{split}
\end{equation*}
```

wobei $V$ dem Volumen der evakuierten Apparatur entspricht. Für eine Pumpe, die ein Gas aus einer Apparatur hinreichend großen Volumens $V$, ohne weiteren Wärmeaustausch absaugt, würde man also einen exponentiellen Verlauf des Drucks 

```math
\begin{equation*}
\begin{split}
&\ln\left(\frac{p}{p_{0}}\right) = -\frac{S}{V}\left(t-t_{0}\right)\\
&\\
&p(t) = p_{0}\,\exp\left(-\frac{S}{V}\left(t-t_{0}\right)\right)
\end{split}
\end{equation*}
```

erwarten, wobei $p_{0}$ dem Anfangs- (z.B. Umgebungs-)druck zum Zeitpunkt $t_{0}$ zu Beginn des Pumpvorgangs entspricht. 

Für Ihre Messungen nutzen Sie diese Beziehung aus, um $S$ aus dem Verlauf von $\ln(p/p_{0})$ als Funktion von $\Delta t = (t - t_{0})$ abzuschätzen. 

### Hinweise zur Durchführung

Im Experiment messen Sie die *Saugleistung*, die vom Druck in der Apparatur abhängt, möglichst nah an der Ansaugöffnung. Sie steigt während die Pumpe anläuft an, nimmt einen nahezu konstanten Wert an, sobald sie der maximalen Absaugkapazität —und damit dem Saugvermögen der Pumpe— entspricht und fällt wieder ab, sobald andere Größen, wie z.B. Lecks in der Apparatur oder Ausgasungen von Schmiermitteln den Druck im erzeugten Vakuum dominieren.  

## Aufgabe 3: Strömungsleitwert eines dünnen Metallrohrs

### Prinzip der Messung

Der $pV$-Durchfluss durch ein beliebiges Leitungselement ist durch den Zusammenhang

```math
q_{pV} = L\left(p_{2}-p_{1}\right)
```

gegeben, wobei $p_{1}$ dem Druck vor und $p_{2}$ dem Druck hinter dem Leitungselement entsprechen. Den Proportionalitätsfaktor $L$ bezeichnet man als **Strömungsleitwert**. Der Kehrwert von $L$ wird als Strömungswiderstand bezeichnet. 

Eine Pumpe schließt nur selten direkt an die zu evakuierende Apparatur an. Ist dies nicht der Fall ist das Saugvermögen der Pumpe durch den Gesamtleitwert der verbindenden Leitungselemente reduziert. 

Nimmt man an, dass sich die Temperatur des Gases während des Durchflusses durch das Leitungselement nicht wesentlich ändert, dass also der $pV$-Durchfluss durch das Leitungselement konstant ist so erhält man für das effektive Saugvermögen $S_{\mathrm{eff}}$ hinter dem Leitungselement den Zusammenhang 

```math
\begin{equation*}
\begin{split}
&q_{pV} = p_{1}\,S = p_{2}\,S_{\mathrm{eff}};\\
&\\
&S_{\mathrm{eff}} = \frac{p_{1}}{p_{2}}\,S.
\end{split}
\end{equation*}
```

Für $S_{\mathrm{eff}}$ folgt also:

```math
\begin{equation*}
\begin{split}
&L = \frac{q_{pV}}{p_{2}-p_{1}} = \frac{p_{1}}{p_{2}-p_{1}}S = \frac{p_{2}}{p_{2}-p_{1}}S_{\mathrm{eff}};\\
&\\
&\frac{p_{2}}{p_{1}} = \frac{S}{L}+1;\\
&\\
&\frac{S_{\mathrm{eff}}}{L} = \left(1-\frac{p_{1}}{p_{2}}\right) = \left(1-\frac{L}{S+L}\right) = \frac{S}{S+L}; \\
&\\
&\left(S+L\right)\,S_{\mathrm{eff}} = S\,L;
&\\
&\\
&\frac{S+L}{S\,L} = \frac{1}{S_{\mathrm{eff}}} \\
&\\
&\frac{1}{L} + \frac{1}{S} = \frac{1}{S_{\mathrm{eff}}} \\
&\\
&S_{\mathrm{eff}} = \left(\frac{1}{L} + \frac{1}{S}\right)^{-1}
\end{split}
\end{equation*}
```

### Hinweise zur Durchführung

Den Verlauf von $\ln\left(p/p_{0}\right)(t)$ bei T1 nehmen Sie hier als Konsistenzmessung relativ zu Aufgabe 2. Beachten Sie, dass Sie die Apparatur in der Zwischenzeit belüftet, geöffnet und wieder geschlossen haben. 

Beachten Sie für Ihre Diskussion der Druckverläufe bei T1 und T2 Abb. 1.1 im dem Dokument [Grundlagen der Vakuumtechnik](https://git.scc.kit.edu/etp-lehre/p2-for-students/-/blob/main/Vakuum/VakuumGrundlagen.pdf). Sie können für den Vergleich mit der Erwartung die Gleichungen (1.28) aus dem Dokument [Grundlagen der Vakuumtechnik](https://git.scc.kit.edu/etp-lehre/p2-for-students/-/blob/main/Vakuum/VakuumGrundlagen.pdf) verwenden.  





 



