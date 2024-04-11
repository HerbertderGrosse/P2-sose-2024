# Hinweise für den Versuch Photoeffekt

## Versuchsdurchführung

### Hg-Dampflampe

[Hg](https://de.wikipedia.org/wiki/Quecksilberdampflampe) besitzt u.a. die folgenden für diesen Versuch relevanten diskreten Emissionslinien 

- $\lambda=365.01\, \mathrm{nm}$ (UV);
- $\lambda=404.66\, \mathrm{nm}$ (violett);
- $\lambda=407.78\, \mathrm{nm}$ (violett);
- $\lambda=435.83\, \mathrm{nm}$ (blau);
- $\lambda=491.60\, \mathrm{nm}$ (cyan);
- $\lambda=546.07\, \mathrm{nm}$ (grün);
- $\lambda=576.96\, \mathrm{nm}$ (orange);
- $\lambda=579.07\, \mathrm{nm}$ (orange).

In der Überlagerung ergibt sich eine grünliche Farbe. Einzelne Wellenlängen können mit Hilfe von sechs Fabry-Pero-Farbfiltern weiter ausgewählt werden, die für die folgenden Wellenlängen durchlässig sind:

- $\lambda^{(1)}_{\mathrm{CWL}}=360\, \mathrm{nm}$;
- $\lambda^{(2)}_{\mathrm{CWL}}=400\, \mathrm{nm}$;
- $\lambda^{(3)}_{\mathrm{CWL}}=440\, \mathrm{nm}$;
- $\lambda^{(4)}_{\mathrm{CWL}}=490\, \mathrm{nm}$;
- $\lambda^{(5)}_{\mathrm{CWL}}=540\, \mathrm{nm}$;
- $\lambda^{(6)}_{\mathrm{CWL}}=590\, \mathrm{nm}$.

Die Abkürzung CWL steht dabei für *central wavelength*; es ist die Wellenlänge in der Mitte des Filterbandpasses. Laut Hersteller haben die Filter eine [Halbwertsbreite](https://de.wikipedia.org/wiki/Halbwertsbreite) von $\pm10\, \mathrm{nm}$, aus der Sie die Standardabweichung des eingestrahlten Lichts bestimmen können. Beachten Sie dabei die Umrechnung zwischen Halbwertsbreite und Standardabweichung unter Annahme einer Normalverteilung. 

### Qualitativer Verlauf von Strom, Spannung und $E_{\mathrm{kin}}$ der austretenden Elektronen

Eine Skizze des qualitativen Verlaufs von Strom, Spannung und $E_{\mathrm{kin}}$ der austretenden Elektronen ist in **Abbildung 3** gezeigt: 

<img src="../figures/PhotoeffektKurven.png" width="1000" style="zoom:100%;"/>

**Abbildung 3**: (Qualitativer Verlauf von Strom, Spannung und $E_{\mathrm{kin}}$ der austretenden Elektronen für den äußeren photoelektrischen Effekt)

---

Erst ab einer charakteristischen Frequenz $\nu_{0}$ treten Elektronen aus K aus. Der Verlauf von $E_{\mathrm{kin}}$ als Funktion von $\nu$ ist daraufhin linear. Extrapoliert man den Verlauf bis zum Abszissenschnittpunkt erhält man die Austrittsarbeit der Elektronen aus dem Kathodenmaterial $W_{K}$. Als Funktion einer externen Spannung $U_{o}$ folgt der Photostrom $I_{\mathrm{Ph}}$, abhängig von den Abmessungen der Photozelle, dem [Raumladungsgesetz](https://de.wikipedia.org/wiki/Raumladungsgesetz). Ab einer maximalen Gegenspannung $U_{o}(I_{\mathrm{Ph}}=0)$ kommt $I_{\mathrm{Ph}}$ zum erliegen. In der Praxis kann eine zusätzliche Kontanktspannung $U_{K}$ zwischen A und K auch ohne Lichteinstrahlung zu einem resultierenden Stromfluss führen. Dies führt i.a. zu einer Parallelverschiebung des Verlaufs von $I_{\mathrm{Ph}}$ entlang der $y$-Achse.

### Aufgabe 1.1: Qualitative Beobachtung des äußeren photoelektrischen Effekts

- Eine sich mit der Zeit bildende Oxyschicht kann die Photoemission stark beeinträchtigen. Polieren Sie Zn daher vor Versuchsbeginn sorgfältig. Laden Sie Zn daraufhin mit einer Spannung von ${\approx}\pm2\ \mathrm{kV}$ auf. 

- Zur Demonstration verwenden Sie ein statisches Elektrometer (E). Der Ausschlag von E ist vom Vorzeichen der Ladung unabhängig; er ändert sich nur sehr langsam.

- Nach Beleuchten mit Hg sollten Sie beobachten, dass der Ausschlag von E (ebenfalls langsam) zurückgeht, wenn Sie Zn negativ aufgeladen haben. Er sollte erhalten bleiben, wenn Sie Zn positiv aufgeladen haben. 

- In der Praxis wird sich Zn aufgrund von Wechselwirkungen mit der Umgebung mit zunehmender Zeit immer entladen. Die Halbwertszeit für diesen Vorgang können Sie mit Hilfe einer Messung ohne Lichteinstrahlung abschätzen.

- Wenn Sie Zn negativ aufgeladen haben und eine positive Elektrode (A) in die Nähe von Zn bringen sollten Sie beobachten, dass der Entladevorgang deutlich schneller vonstatten geht.  

- Diskutieren Sie alle Beobachtungen, die Sie bei diesem Versuch machen.  


### Aufgabe 1.2: Charakterisierung des für die folgenden Aufgaben zu verwendeden Elektrometers

Die Ladungesbewegungen, die Sie bei diesem Versuch untersuchen sind i.a. sehr gering (im Bereich von $1-100\ \mathrm{nA}$). 

Spannungemessungen erfolgen direkt (siehe **Abbildung 1** oben [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Photoeffekt/doc/Hinweise-Photoeffekt.md)). Strommessungen erfolgen als Messung einer Spannung $U_{\mathrm{Ph}}$, die über einen bekannten Arbeitswiderstand $R=100\ \mathrm{M\Omega}$ abfällt (siehe **Abbildung 2** unten [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Photoeffekt/doc/Hinweise-Photoeffekt.md)). Hierzu verwenden Sie einen Messverstärker mit sehr hohem Innenwiderstand $R_{i}$. Einen solchen Aufbau bezeichnet man ebenfalls als Elektrometer. Eine Abbildung der Frontfläche der Kontrollbox zur Steuerung des Elektrometers finden Sie [hier]([hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Photoeffekt/figures/IMG_1600.jpg)).  Im Folgenden sollen Sie sich mit dem für alle weiteren Versuche zu verwendenden Elektrometer vertraut machen in dem Sie die folgenden Schritte ausführen: 

#### Nullabgleich

Führen Sie einen Nullabgleich des Elektrometers duch. Sie tun dies, z.B. indem Sie eine Referenzspannung $U_{o}$ anschließen, die entsprechende Taste links am Schaltkasten des Messverstärkers gedrückt halten und die ausgegebene Spannung mit den Potentiometerschrauben zur Grob- und Feinjustierung variieren. Nehmen Sie die Justierung für die Verstärkung $V=100$ vor, damit können Sie den resultierenden Nullabgleich auch für geringere Verstärkungen verwenden. 

#### Bestimmung des Innenwiderstands $R_{i}$

Das Ersatzschaltbild hierzu ist in **Abbildung 4** gezeigt:

<img src="../figures/Innenwiderstand.png" width="1000" style="zoom:100%;"/>

**Abbildung 4**: (Ersatzschaltbild zur Bestimmung von $R_{i}$ des für die weiteren Aufgaben zu verwendenden Elektrometers)

---

Von außen liegt die als bekannt angenommene Spannung $U_{o}$ an. Das Elektrometer ist durch die Schaltung innerhalb des gestrichelten Kastens dargestellt. Nach den [Kirchhoffschen Regeln](https://de.wikipedia.org/wiki/Kirchhoffsche_Regeln) gilt: 
$$
\begin{equation}
\begin{split}
&U_{E}=R_{i}\,I;\qquad U_{o}=(R_{V}+R_{i})\,I;\\
&\\
&U_{E} = U_{o}\,\frac{R_{i}}{R_{V}+R_{i}}\approx U_{o}\left(1-\frac{R_{V}}{R_{i}}\right); \\
%&\\
%&R_{i} = \frac{U_{E}}{U_{0}+U_{E}}\,R_{V}.\\
\end{split}
\end{equation}
$$
Zur Bestimmung von $R_{i}$ können Sie z.B. wie folgt vorgehen: 

- Bestimmen Sie für eine Verstärkung von $V=1$ die gemessene Spannung $U_{E}$ für die zu Verfügung stehenden Vorwiderstände von $R_{V}=0.1,\ 1,\ 10\ \mathrm{G\Omega}$ und tragen Sie die Messpunkte in einem Diagramm geeignet auf. 
- Nehmen Sie $\Delta R_{V}/R_{V}=\pm 10\%$ und $\Delta U_{o}=\pm0.01\ \mathrm{V}$ an. 
- Passen Sie an den Verlauf das Modell aus Gleichung **(1)** an.

**Beachten Sie, dass die maximal ausgegebene Spannung des Verstärkers $\pm10\ \mathrm{V}$ nicht übersteigt. Die $4\ \mathrm{mm}$-Massebuche links unten an der Frontfläche der Kontrollbox liegt auf dem gleichen Potential, wie der BNC-Außenleiter.** 

### Aufgabe 2.1 Spannung $U_{\mathrm{Ph}}$ der Photozelle bei variierender Lichtfrequenz 

Gehen Sie zur Bestimmung von $h$ wie folgt vor: 

- Achten Sie auf eine zentrale und gute Ausleuchtung der Photozelle.

- Schalten Sie dann Schritt für Schritt einen Filter nach dem anderen vor den Lichtschutzkollimator der Photozelle. Die Filter sind aufsteigend in $\lambda_{\mathrm{CWL}}^{(i)}$ montiert. 

- Warten Sie, eine stabile Anzeige von $U_{\mathrm{Ph}}$ am Elektrometer ab. Eine Messung von $U_{\mathrm{Ph}}$ ohne weitere Verstärkung (d.h. mit $V=1$) sollte ohne weiteres möglich sein. Protokollieren Sie den verwendeten Wert von $V$. 

- Nehmen Sie **mindestend drei Messreihen** auf, bestimmen Sie den Messwert $U_{\mathrm{Ph}}^{(i)}$ durch Stichprobenmittelung, und die Unsicherheit $\Delta U_{\mathrm{Ph}}^{(i)}$ aus der Stichprobenvarianz. 

- Stellen Sie die Messpunkte $(U^{(i)}_{\mathrm{Ph}},\ \lambda^{(i)}_{\mathrm{CWR}})$ einschließlich der abgeschätzten Unsicherheiten $(\Delta U^{(i)}_{\mathrm{Ph}},\ \Delta \lambda^{(i)}_{\mathrm{CWR}})$ geeignet dar und passen Sie ein Modell der folgenden Form daran an:

  ```math
  \begin{equation*}
  U_{\mathrm{Ph}}^{(i)} = \frac{c\,h}{e}\frac{1}{\lambda^{(i)}_{\mathrm{CWL}}}+\frac{1}{e}W_{\mathrm{eff}}
  \end{equation*}
  ```

-  Geben Sie Ihr Messergebnis für $h$ und $W_{\mathrm{eff}}$ einschließlich Unsicherheiten an und diskutieren Sie es. Beziehen Sie in diese Diskussion auch den $\chi^{2}$-Wert der Anpassung mit ein. 

- Sowohl [$e=1.602176634\times10^{-19}\ \mathrm{C}$](https://de.wikipedia.org/wiki/Elementarladung) als auch [$c=2.99792458\times10^{8}\ \mathrm{m/s}$](https://de.wikipedia.org/wiki/Lichtgeschwindigkeit) sind SI-Einheiten definierende Naturkonstanten die **ohne Unsicherheiten definiert** sind. Sie können diesen Umstand in Ihrer Anpassung an die Daten berücksichtigen, um $h$ direkt zu bestimmen. 

### Aufgabe 2.2: Photostrom $I_{\mathrm{Ph}}$ als Funktion einer angelegten externen Spannung $U_{o}$ bei variierender Lichtintensität

- Schließen Sie hierzu den Widerstand mit $R=100\ \mathrm{M\Omega}$ parallel zum Messeingang des Elektrometers, wie in **Abbildung 2** unten [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Photoeffekt/doc/Hinweise-Photoeffekt.md) gezeigt. Der Strom berechnet sich dann aus
  ```math
  \begin{equation*}
  I_{\mathrm{Ph}}=\frac{U_{E}}{R\,V},
  \end{equation*}
  ```

  wobei $U_{E}$ die am Gerät ausgegebene Spannung und $V$ der eingestellte Verstärkungsfaktor sind. Zweckmäßige Spannungsintervalle für $U_{o}$ sind z.B.:

  - Von $-3.0\ \mathrm{V}$ bis $-0.5\ \mathrm{V}$ in Schritten von $\Delta U_{o}=0.1\ \mathrm{V}$.
  - Von $-0.5\ \mathrm{V}$ bis $3.0\ \mathrm{V}$ in Schritten von $\Delta U_{o}=0.5\ \mathrm{V}$.
  - Von $3.0\ \mathrm{V}$ bis $9.0\ \mathrm{V}$ in Schritten von $\Delta U_{o}=1.0\ \mathrm{V}$.

- Stellen Sie die Datenpunkte für die **Messung mit und ohne Graufilter** im gleichen Diagramm geeignet dar und passen Sie in einem geeigneten Bereich der Datenpunkte ein Modell an, aus dem Sie $U_{o}(I_{\mathrm{Ph}}=0)$ bestimmen können. Ein solches Modell könnte z.B. so aussehen:
  ```math
  \begin{equation*}
  I_{\mathrm{Ph}}= a\,U_{o} + I_{0},
  \end{equation*}
  ```

  wobei es sich bei $a$ und $I_{0}$ um freie Parameter handelt. 

- Bestimmen Sie die Reduktion der Lichtitensität durch den Graufilter, indem Sie z.B. dem obigen Diagramm ein Panel zufügen, in dem Sie das Verhältnis der gemessenen Werte mit und ohne Graufilter abtragen. Da $I_{\mathrm{Ph}}$ zu Lichtintensität proportional ist ist zu erwarten, dass das Verhältnis $I_{\mathrm{Ph}}^{\mathrm{filter}}/I_{\mathrm{Ph}}$ nicht von $U_{o}$ abhängt. 

- Diskutieren Sie Ihre Ergebnisse einschließlich der $\chi^{2}$-Werte der gewählten Anpassungen und der erhaltenen Unsicherheiten sowohl für die Abschwächung des Graufilters, als auch für den Wert von $U_{o}(I_{\mathrm{Ph}}=0)$. 

### Aufgabe 2.3: Spannung $U_{o}(I_{\mathrm{Ph}}=0)$ bei variierender Lichtfrequenz

Gehen Sie zur Bestimmung von $U_{o}(I_{\mathrm{Ph}}=0)$ nun (wieder bei maximaler Lichtintensität) analog zu **Aufgabe 2.2** vor. 

Passen Sie an die erhaltenen Werte von $U_{o}^{(i)}(I_{\mathrm{Ph}}=0, \lambda_{\mathrm{CWL}}^{(i)})$ ein geeignetes Modell zur Bestimmung von $h$ an und vergleichen Sie das Ergebnis mit dem Ergebnis von Aufgabe **Aufgabe 2.1**. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Photoeffekt)
