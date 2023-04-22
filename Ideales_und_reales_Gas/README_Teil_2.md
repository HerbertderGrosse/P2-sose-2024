# Hinweise für den Versuch: "Ideales und reales Gas" 

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
&\hphantom{\frac{\mathrm{d}p}{\mathrm{d}V}}= -\kappa\frac{p}{V};\qquad\text{(4)} \\
&\\
&\mathrm{d}p = -\kappa\frac{p}{V}\,\mathrm{d}V\\
\end{split}

```

Aus der Multiplikation von Gleichung (4) mit dem Rohrinnenquerschnitt $A$ ergibt sich die Kraft auf den Pfropfen und eine lineare Schwingungsgleichung für die Bewegung des Pfropfens:

```math
\begin{split}
&\mathrm{d}F = -\kappa\frac{p}{V}A^{2}\,\mathrm{d}x \\
&\\
&m\,\ddot{x} = -\kappa\frac{p}{V}A^{2}\,x,\qquad\text{(5)} 
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

Indem Sie die Induktionsspule verschieben können Sie die Werte von $V$ selbst bestimmen. Messen Sie $T$ für Werte zwischen $V=30-80\,\mathrm{ml}$. Die Bestimmung von $\kappa$ erfolgt dann durch geeignete Anpassung des Zusammenhangs aus Gleichung (6) an die gemessenen Wertepaare 

```math
\left(\begin{array}{cc}V_{i} & T_{i}\end{array}\right).
```

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
\frac{\mathrm{d}p}{\mathrm{d}T} = \frac{Q}{T\,\left(V_{\mathrm{d}} - V_{\mathrm{fl}}\right)}, \quat\text{(7)}

```

wobei $V_{\mathrm{fl}}$ dem Volumen der Flüssigkeit und $V_{\mathrm{d}}$ dem Volumen des Dampfs entsprechen. Nach diesem Zusammenhang benötigen Sie die Wärme $Q$, um bei der Temperatur $T$ eine Flüssigkeit mit $V_{\mathrm{fl}}$ in ein Gas mit $V_{\mathrm{d}}$ überzuführen. 

Für die weiteren Betrachtungen machen wir die Annahme 

```math
V_{\mathrm{fl}}<<V_{\mathrm{d}}
```

 und betrachten den Dampf als ideales Gas mit: 

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
&p(T) = p_{0}\exp\left(-\frac{Q}{n\,R\,T}\right), \quad\text{(8)}\\
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

Bestimmen Sie dann durch geeignete Anpassung des Zusammenhangs aus Gleichung (8) $Q_{\mathrm{M}}$. Wenn Sie für beide Messreihen vergleichbare Werte für $Q_{\mathrm{M}}$ erhalten können Sie davon ausgehen, dass Sie den Gleichgewichtszustand zwischen "flüssig" und "gasförmig" erfolgreich präpariert haben. 
