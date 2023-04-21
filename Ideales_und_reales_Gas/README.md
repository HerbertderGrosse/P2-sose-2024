# Hinweise für den Versuch: "Ideales und reales Gas" 

##  Aufgabe 1: Gasthermometer

### Prinzip der Messung

Der grundsätzliche Aufbau des Gasthermometers und die im weiteren Verlauf verwendeten Bezeichnungen finden Sie in der folgenden Skizze: 

<img src="./figures/GasthermometerSkizze.png" width="500" height="500" style="zoom:60%;" />

Die Temperaturmessung beruht auf der idealen Gasgleichung 
```math
\begin{equation*}
p(V, T) = \frac{n\,R\,T}{V},
\end{equation*}
```

wobei $p$ dem Druck, $V$ dem Volumen, $T$ der Temperatur, $n$ der Stoffmenge des Gases und $R$ der idealen Gaskonstanten entsprechen.

Das Thermometer wird nach dem Prinzip der Druckmessung bei konstantem Volumen verwendet. In diesem Fall gilt $p\propto T$ mit: 
```math
\left.p(T)\right|_{V=const.} = p_{0}\left(1+\alpha\,T\right). \qquad\text{(1)}
```

Die Steigung $\alpha$ wird als **Spannungskoeffizient** bezeichnet. Numerisch ist $\alpha$ zum Volumenausdehnungskoeffizienten des Gases äquivalent. Wenn Sie $T$ auf der Celsius-Skala messen entspricht $p_{0}$ dem Druck bei $0^{\circ}\mathrm{C}$. In diesem Fall verschwindet der Gasdruck $p(T_{0})$ bei einer Temperatur von $T_{0}=-1/\alpha$. Diese Temperatur wird als **absoluter Nullpunkt** bezeichnet.

Zur Messung tauchen Sie den Glaskolben G vollständig in ein [Wärmebad](https://de.wikipedia.org/wiki/W%C3%A4rmebad) ein, dass Sie mit destilliertem Wasser herstellen. Wenn Sie den Druck bei der Siede- ($T_{s}$) und Schmelztemperatur messen erhalten Sie eine Abschätzung $\alpha^{(0)}$ aus der Beziehung: 
```math
\begin{equation*}
\alpha^{(0)} = \frac{p(T_{s}) - p_{0}}{p_{0}\,T_{s}}
\end{equation*}
```

Wenn Sie $\alpha$ genauer bestimmen wollen, sollten Sie einige Effekte beachten, die Ihre Messung verfälschen können:

- G hat eine thermische Ausdehnung.
- G verformt sich unter Druck.
- Luft ist kein ideales Gas.
- Ein Teil des Gases befindet sich (bei Raumtemperatur) außerhalb von G.

Alle Effekte bis auf die thermische Ausdehnung von G sind allerdings sehr klein und können vernachlässigt werden. Einen Korrekturterm für die thermische Ausdehnung von G erhalten Sie aus der folgenden Überlegung: 

Bei $T_{s}$ hat sich das Volumen $V_{\mathrm{G}}$ von G um den Faktor 
```math
\begin{equation*}
\frac{V_{\mathrm{G}}^{\prime}}{V_{\mathrm{G}}} = 1+T_{s}\gamma
\end{equation*}
```

ausgedehnt, wobei Sie den kubischen Ausdehnungskoeffizient von Glas ($\gamma=2,5\times10^{-5}\,\mathrm{K}^{-1}$)  als gegeben voraussetzen können. Nach der idealen Gasgleichung ($p\,V=const.$) ist $p(T_{s})$ um den entsprechenden Faktor zu verringern. Aus Gleichung (1) ergibt sich damit:

```math
\begin{equation*}
p(T_{s}) = \frac{p_{0} + \alpha\,p_{0}\,T_{s}}{1+T_{s}\gamma};
\end{equation*}
```

```math
\begin{equation*}
\begin{split}
\alpha &= \frac{\left(1+T_{s}\gamma\right)\,p(T_{s})-p_{0}}{p_{0}\,T_{s}}; \\
&\alpha = \frac{p(T_{s})-p_{0}}{p_{0}\,T_{s}} + \frac{p(T_{s})}{p_{0}}\gamma = \alpha^{(0)} + \frac{p(T_{s})}{p_{0}}\gamma \\
\end{split}
\end{equation*}
```

```math
\begin{equation*}
\alpha = \frac{p(T_{s})-p_{0}}{p_{0}\,T_{s}} + \frac{p(T_{s})}{p_{0}}\gamma = \alpha^{(0)} + \frac{p(T_{s})}{p_{0}}\gamma
\end{equation*}

```

Beachten Sie außerdem, dass $T_{s}$ vom Umgebungsdruck abhängt. Sie können $T_{s}(p)$ mit Hilfe eines im Versuchsraum vorhandenen Barometers und der ebenfalls vorliegenden Dampfdruckkurve für Wasser bestimmen. Berücksichtigen Sie entsprechende Unsicherheiten in Ihrer Messung.   

### Hinweise zur Durchführung

Schieben Sie das Becherglas vorsichtig von unten her so hoch wie möglich über G. Füllen Sie es dann mit einem Gemisch aus fein zerstoßenem Eis und Wasser, so dass G möglichst ganz bedeckt ist. Rühren Sie die Mischung vorsichtig durch, so dass eine möglichst homogene Temperaturverteilung im Wärmebad entsteht. Schieben Sie, während sich das Gasthermometer abkühlt, R2 bis zum Anschlag nach unten um zu verhindern, dass Quecksilber in G eindringen kann. 

Nach $\approx15\,\mathrm{min}$ sollte die Luft in G die Temperatur des Wärmebads angenommen haben. Regeln Sie das Gasvolumen ein, indem Sie R2 langsam so weit nach oben verschieben, bis die Quecksilberkuppe in R1 die Spitze S gerade berührt. Aus der Höhendifferenz $\Delta h$ der beiden Quecksilberkuppen können Sie $p_{0}$ im Volumen $V$ bestimmen. Vergessen Sie nicht, dass auf die Quecksilberkuppe in R2 noch der äußere Luftdruck wirkt. Um den Druck in $\mathrm{mbar}$ zu erhalten verwenden Sie die Umrechnung: $1\,\mathrm{mm\,Hg} = 1,33322\,\mathrm{mbar}$. 

Bringen Sie danach das Wasserbad auf Siedetemperatur $T_{s}$. Achten Sie auch beim Heizen darauf, dass G immer vollständig mit Wasser bedeckt ist. Bevor Sie $p(T_{s})$ wie oben bestimmen, sollte das Wasser einige Minuten lang sieden.

---

## Aufgabe 2: Adiabatenexponent (nach [Clément-Desormes](https://de.wikipedia.org/wiki/Experiment_von_Cl%C3%A9ment-Desormes))

### Prinzip der Messung

Zustandsänderungen von Gasen, die ohne Wärmeaustausch mit der Umgebung ($\delta Q=0$) stattfinden, bezeichnet man als *adiabatisch*. Sie können mit Hilfe der Adiabatengleichungen
```math
\begin{equation*}
p\,V^{\kappa} = const.;\quad T\,V^{\kappa-1} = const.
\end{equation*}
```

beschrieben werden. 

Das Verfahren von Clément-Desormes zur Bestimmung von $\kappa$ wird mit einer Flasche durchgeführt, die mit dem zu untersuchenden Gas befüllt und einem U-Rohr-Manometer zur Druckmessung verbunden ist. Aus dem Anfangszustand $\left(\begin{array}{ccc}p_{0}& V_{0} & T_{0}\end{array}\right)$ gehen Sie wie folgt vor:

1. Erzeugen Sie mit dem Handblasebalg einen (nicht zu großen) Überdruck $\Delta p_{1}$ in der Flasche. Warten Sie den Temperaturausgleich ab. Das System hat daraufhin den Zustand

   ```math
   \left(\begin{array}{ccc}p_{0}+\Delta p_{1} & V_{0} & T_{0}\end{array}\right).
   ```

2. (**Schritt 2**): Öffnen Sie das Ventil der Flasche kurzzeitig und schließen Sie es unmittelbar wieder, so dass es zu einem Druckausgleich mit der Umgebung durch **adiabatische Expansion** kommen kann. Das System hat daraufhin den Zustand 
   ```math
   \left(\begin{array}{ccc}p_{0} & V_{0}+\Delta V & T_{0}-\Delta T \end{array}\right).
   ```

3. Nach schließen des Ventils ist das Volumen der Luft in der Flasche wieder fest vorgegeben. Aufgrund des Druckausgleichs in Schritt 2 liegt die Temperatur der Luft in der Flasche unterhalb der Umgebungstemperatur. Das System hat somit den Zustand 
   ```math
   \left(\begin{array}{ccc}p_{0} & V_{0} & T_{0}-\Delta T \end{array}\right).
   ```

4. (**Schritt 4**): Durch Temperaturausgleich (nach einer Wartezeit von $\approx10\,\mathrm{s}$) stellt sich aufgrund **isochorer Erwärmung** erneut ein Überdruck ein. Das System hat daraufhin den Zustand 
   ```math
   \left(\begin{array}{ccc}p_{0}+\Delta p_{2} & V_{0} & T_{0} \end{array}\right).
   ```

#### Berechnungen für Schritt 2:

Für die **adiabatische Expansion** in Schritt 2 gilt: 
```math
\begin{equation*}
\begin{split}
&\left(p_{0}+\Delta p_{1}\right)\,V_{0}^{\kappa} = p_{0}\,\left(V_{0}+\Delta V\right)^{\kappa}\\
&\\
&T_{0}\,V_{0}^{\kappa-1} = \left(T_{0}-\Delta T\right)\,\left(V_{0}+\Delta V\right)^{\kappa-1}.\\
\end{split}
\end{equation*}
```

Für kleine Volumenänderungen $\Delta V\ll V_{0}$ gilt die Näherung  

```math
\begin{equation*}
\left(V_{0}+\Delta V\right)^{\kappa}\approx V_{0}^{\kappa}\left(1+\kappa\frac{\Delta V}{V_{0}}\right)
\end{equation*}
```

woraus folgt: 

```math
\begin{split}
&\frac{\Delta p_{1}}{p_{0}} = \kappa \frac{\Delta V}{V_{0}}\\
&\\
&\frac{\Delta T}{T_{0}}\approx\frac{\Delta T}{T_{0}-\Delta T} = \left(\kappa-1\right)\frac{\Delta V}{V_{0}}\qquad\text{(1)}\\
&\\
&\frac{\Delta T}{T_{0}} = \frac{\kappa-1}{\kappa}\frac{\Delta p_{1}}{p_{0}}\\
\end{split}

```

#### Berechnungen für Schritt 4:

Für die **isochore Erwärmung** in Schritt 4 gilt nach der idealen Gasgleichung:

```math
\begin{split}
&\frac{T_{0}-\Delta T}{T_{0}} = \frac{p_{0}}{p_{0}+\Delta p_{2}};\qquad\text{(3)}\\
&\\
&\frac{\Delta T}{T_{0}} = 1-\frac{p_{0}}{p_{0}+\Delta p_{2}}
\approx \frac{\Delta p_{2}}{p_{0}}.\\
\end{split}
```

Dabei wurde der Quotient auf der rechten Seite der Gleichung für $\Delta p_{2}\ll p_{0}$ in einer geometrischen Reihe entwickelt. 

#### Berechnung von $\kappa$ 

Gleichsetzen der Gleichungen (2) und (3) führt auf:

```math
\begin{equation*}
\begin{split}
&\frac{\kappa-1}{\kappa}\Delta p_{1} = \Delta p_{2}; \\
&\kappa = \frac{\Delta p_{1}}{\Delta p_{1} - \Delta p_{2}}
\end{split}
\end{equation*}
```

Für die Barometerkuppen im U-Rohr-Barometer gilt: 

```math
\begin{equation*}
p(h_{i}) = p_{0} + \rho\,g\,h_{i},
\end{equation*}
```

wobei $\rho$ der Dichte der Barometerflüssigkeit und $g$ der Erdbeschleunigung entsprechen, woraus sich direkt die finale Bestimmungsgleichung ergibt: 

```math
\begin{equation*}
\kappa = \frac{h_{1}}{h_{1}-h_{2}}
\end{equation*}
```

### Hinweise zur Durchführung

Erzeugen Sie mit dem Handblasebalg nicht zu viel Überdruck $\Delta p_{1}$, da sonst beim Druckausgleich in Schritt 2 Flüssigkeit aus dem U-Rohr-Manometer austreten kann. Achten Sie darauf, dass sich ein Gleichgewichtszustand einstellt bevor Sie das U-Rohr-Manometer ablesen.  

---

## Aufgabe 3: Adiabatenexponent (Schwingungsmethode)

### Prinzip der Messung

Bei dieser Methode schwingt ein Pfropfen auf einem Luftpolster, das durch den Schwingungsvorgang in nahezu adiabatische Kompression und Expansion versetzt wird. Nach der Adiabatengleichung gilt in diesem Fall: 

```math
\begin{equation*}
p\,V^{\kappa} = const.
\end{equation*}
```

Für differentielle Druck- und Volumenänderungen ergibt sich daraus:

```math
\begin{split}
&\frac{\mathrm{d}p}{\mathrm{d}V} = -const.\,\kappa\,V^{-\kappa-1} \\
&\hphantom{\frac{\mathrm{d}p}{\mathrm{d}V}}= -\kappa\frac{p}{V};\qquad\text{(4)}\\
&\\
&\mathrm{d}p = -\kappa\frac{p}{V}\,\mathrm{d}V\\
\end{split}

```

Aus der Multiplikation von Gleichung (4) mit dem Rohrinnenquerschnitt $A$ ergibt sich die Kraft auf den Pfropfen und eine lineare Schwingungsgleichung für die Bewegung des Pfropfens:

```math
\begin{split}
&\mathrm{d}F = -\kappa\frac{p}{V}A^{2}\,\mathrm{d}x \\
&\\
&m\,\ddot{x} = -\kappa\frac{p}{V}A^{2}\,x,
\end{split}

```

wobei $m$ der Masse des Pfropfens entspricht. An dieser Stelle wird die Näherung vorgenommen, dass sich $p$ und $V$ durch die Bewegung des Pfropfens aus seiner Ruhelage nur geringfügig ändern. Aus Gleichung (5) lässt sich die Periode der Schwingung ableiten zu:

```math
T = 2\pi\sqrt{\frac{m\,V}{\kappa\,p\,A^{2}}},\qquad\text{(6)}
```

woraus sich $\kappa$ bestimmen lässt:

```math
\begin{equation*}
\kappa = \left(\frac{2\pi}{T}\right)^{2}\frac{m\,V}{p\,A^{2}}
\end{equation*}
```

Beachten Sie, das die Variablenbezeichnung $T$ in diesem Versuchsteil eine andere Bedeutung hat als sonst bei diesem Praktikumsversuch. 

### Hinweise zur Durchführung

#### Methode nach Rüchardt:

In diesem Fall erzeugen Sie die Schwingung mit Hilfe einer Stahlkugel als Pfropfen, deren Durchmesser exakt mit dem Innendurchmesser eines Glasrohrs übereinstimmt, so dass sie das Glasrohr nahezu luftdicht verschließt. Das Glasrohr wird mit Hilfe eines durchbohrten Stopfens ebenfalls möglichst luftdicht auf eine der bereitgestellten $10\,\mathrm{l}$-Flaschen aufgesetzt. Bei dieser Anordnung schwingt die Kugel auf einem Luftpolster mit großem Volumen $V$ während $A$ klein ist, $T$ ist daher groß genug, so dass Sie die Schwingung gut beobachten und $T$ gut bestimmen können.  Nehmen Sie für das Volumen dieses Luftkissens $V=10,58\,\mathrm{l}\pm0,3\%$ an.

Bei Glasrohr und Stahlkugel handelt es sich um **Präzisionsanfertigungen, die mit größter Sorgfalt zu behandeln sind!** Damit die Kugel das Glasrohr luftdicht abschließen, sich aber gleichzeitig möglichst reibungsfrei darin bewegen kann müssen die folgenden Bedingungen so gut wie möglich erfüllt sein: 

- Das Glasrohr muss möglichst genau senkrecht stehen.
- Sowohl das Glasrohr, als auch die Stahlkugel müssen äußerst sauber sein. 
- Alle Stopfen müssen luftdicht abschließen.

Reinigen Sie Kugel und Rohrinnenfläche sorgfältig mit einem Lederlappen. Berühren Sie die Kugel nach Möglichkeit niemals mit den Fingern. Sollte dies dennoch geschehen, wiederholen Sie den Reinigungsvorgang.

Setzen Sie das Glasrohr so ein, dass der durchbohrte Stopfen möglichst luftdicht abschließt. Lassen Sie die Kugel aus dem Lederlappen behutsam ins Glasrohr gleiten und bestimmen Sie $T$ aus möglichst vielen, mindestens aber 5 Schwingungen. Wiederholen Sie diesen Vorgang mehrfach, um ein Maß für die Streuung zu erhalten. Um die Kugel nach Beendigung einer Messreihe aus dem Rohr zu entnehmen, kippen Sie die Flasche –so lange die Kugel sich noch in
der Glasröhre befindet– vorsichtig um und lassen Sie die Kugel in die bereitstehende Plastikschale gleiten.

 Diese Messung führen Sie nur für Luft durch.  

#### Methode mit dem Kolbenprober

In diesem Fall ersetzt der Kolbenprober das Glasrohr und die Kugel; $V$ und $T$ sind deutlich kleiner, als bei der Anordnung von Rüchardt , so dass $T$ elektronisch, mit Hilfe eines angebrachten Magneten, einer Induktionsspule um den Kolbenprober und eines Frequenzzählers bestimmt wird. 

Indem Sie die Induktionsspule verschieben können Sie die Werte von $V$ selbst bestimmen. Messen Sie $T$ für Werte zwischen $V=30-80\,\mathrm{ml}$. Die Bestimmung von $\kappa$ erfolgt dann durch geeignete Anpassung des Zusammenhangs aus Gleichung (6) an die gemessenen Wertepaare $\left(\begin{array}{cc}V_{i} & T_{i}\end{array}\right)$.  

Führen Sie diese Messung erst mit Luft und dann mit dem Edelgas Argon durch und überprüfen Sie, ob $\kappa$ mit der Erwartung

```math
\begin{equation*}
\kappa = \frac{f+2}{f}
\end{equation*}
```

aus der [kinetischen Gastheorie](https://de.wikipedia.org/wiki/Kinetische_Gastheorie) übereinstimmt, wobei $f$ der Anzahl der [Freiheitsgrade](https://de.wikipedia.org/wiki/Freiheitsgrad) des untersuchten Gases entspricht. Je nach Gas erwarten Sie die folgenden Werte für $f$:

- Edelgas: $f=3$
- $\mathrm{O_{2}}$, $\mathrm{N_{2}}$: $f=5$
- $\mathrm{CO_{2}}$: $f=7$

---

## Aufgabe 4: Dampfdruckkurve (n-Hexan)

### Prinzip der Messung

Übergänge der einzelnen Phasen "fest", "flüssig", und "gasförmig" eines Stoffes werden mit Hilfe von [Phasendiagrammen](https://de.wikipedia.org/wiki/Phasendiagramm) dargestellt. In einem abgeschlossenen Volumen $V$ gibt es, für eine gegebene Temperatur $T$, jeweils nur einen bestimmten Druck $p(T)$, bei dem zwischen zwei Phasen eines Stoffes ein thermodynamisches Gleichgewicht herrscht. Ein thermodynamisches Gleichgewicht zwischen allen drei Phasen eines Stoffs existiert nur an einem einzigen Punkt im Phasendiagramm, dem Tripelpunkt. 

Bei diesem Versuchsteil beobachten Sie den Phasenübergang zwischen "flüssig" und "gasförmig" von n-Hexan. Das dazugehörige Phasendiagramm heißt Dampfdruckkurve. 

Für einen Carnot-Prozess gilt allgemein:

```math
\begin{equation*}
\frac{\mathrm{d} W}{\mathrm{d}T} = -\frac{Q}{T}
\end{equation*}
```

Mit $\mathrm{d}W = \left(V_{\mathrm{fl}}-V_{\mathrm{d}}\right)\,\mathrm{d}p$ wird daraus die [Clausius-Clapeyron-Gleichung](https://de.wikipedia.org/wiki/Clausius-Clapeyron-Gleichung): 

```math
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{Q}{T\,\left(V_{\mathrm{d}} - V_{\mathrm{fl}}\right)},

```

wobei $V_{\mathrm{fl}}$ dem Volumen der Flüssigkeit und $V_{\mathrm{d}}$ dem Volumen des Dampfs entsprechen. Nach diesem Zusammenhang benötigen Sie die Wärme $Q$, um bei der Temperatur $T$ eine Flüssigkeit mit $V_{\mathrm{fl}}$ in ein Gas mit $V_{\mathrm{d}}$ überzuführen. 

Für die weiteren Betrachtungen machen wir die Annahme $V_{\mathrm{fl}}<<V_{\mathrm{d}}$ und betrachten den Dampf als ideales Gas mit: 

```math
\begin{equation*}
V_{\mathrm{d}} = \frac{n\,R\,T}{p},
\end{equation*}
```

womit Gleichung (7), nach Separation der Variablen, die folgende Form annimmt: 

```math
\begin{split}
&\frac{\mathrm{d}p}{p} = \frac{Q}{n\,R}\,\frac{\mathrm{d}T}{T^{2}} \\
&\\
&p(T) = p_{0}\exp\left(-\frac{Q}{n\,R\,T}\right), \\
\end{split}

```

wobei es sich um die zu erwartende funktionale Form der Dampfdruckkurve handelt.

### Hinweise zur Durchführung

In einem Glaskolben befinden sich (in erster Näherung) nur die Flüssigkeit und der Dampf von $1\,\mathrm{mol}$ n-Hexan. Der Dampfdruck wird mit einem direkt verbundenen Quecksilbermanometer gemessen, dessen Stand Sie mit einem [Kathetometer](https://de.wikipedia.org/wiki/Kathetometer) ablesen können.

Tauchen Sie den Kolben mit dem n-Hexan in ein Wärmebad, dessen Temperatur Sie so langsam verändern müssen, dass die Flüssigkeit und der Dampf an jedem Messpunkt im Gleichgewicht sind. Stellen Sie das Fernrohrokular des Kathetometers auf das Fadenkreuz ein. Während der Messung darf am Fernrohr selbst daraufhin nicht mehr verändert werden. 

Zur Messung des Dampfdrucks bei Raumtemperatur visieren Sie die beiden
Quecksilberkuppen nacheinander an und lesen die jeweilige Höhendifferenz an der Kathetometerskala ab. Den Fokus auf die Kuppen müssen Sie dabei durch Verschieben des ganzen Gestells erreichen. Für die weiteren Druckmessungen genügt es, wenn Sie nur noch eine der beiden Kuppen anvisieren.

Achten Sie darauf, dass zu Beginn des Experiments kein flüssiges n-Hexan außerhalb des Wärmebads niedergeschlagen ist, das Ihre Messung verfälschen würde. Rühren Sie während des Versuches das Wärmebad langsam um, so dass Sie eine möglichst homogene Temperaturverteilung erhalten.

Nehmen Sie zunächst die Dampfdruckkurve bei langsam sinkender Temperatur auf. Geben Sie hierzu Eisstückchen ins Wärmebad. Nehmen Sie dann die Dampfdruckkurve bei langsam steigender Temperatur auf. Gießen Sie hierzu dem Wärmebad destilliertes Wasser zu.

Bestimmen Sie dann durch geeignete Anpassung des Zusammenhangs aus Gleichung ($\ref{eq:Dampfdruck}$) $Q_{\mathrm{M}}$. Wenn Sie für beide Messreihen vergleichbare Werte für $Q_{\mathrm{M}}$ erhalten können Sie davon ausgehen, dass Sie den Gleichgewichtszustand zwischen "flüssig" und "gasförmig" erfolgreich präpariert haben. 
