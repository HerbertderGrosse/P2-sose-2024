# Hinweise für den Franck-Hertz-Versuch

## Aufbau der Röhre und Bahn der Elektronen

### Aufbau der Franck-Hertz-Röhre

Die Skizze einer Tetrode, wie wir sie für den Franck-Hertz-Versuch im P2 verwenden ist in **Abbildung 1** gezeigt:

<img src="../figures/FranckHertzSkizze.png" width="1000" style="zoom:100%;"/>

**Abbildung 1**: (Schematische Darstellung einer Franck-Hertz-Tetrode, wie sie im P2 verwendet wird (oben). Im unteren Teil der Abbildung ist der Aufbau der tatsächlich Röhre zu sehen)

---

Auf der linken Seite der Zeichnung im oberen Teil der Abbildung befindet sich eine Glühkathode K mit dem Widerstand $R_{\mathrm{K}}$, die mit der Spannung $U_{\mathrm{K}}$ versorgt wird. Im Abstand von ${\approx}0.5\,\mathrm{mm}$ zu K  befindet sich ein *grobmaschiges* **Raumladungsgitter G1** (auch [Steuergitter](https://de.wikipedia.org/wiki/Steuergitter) genannt), dessen Funktion es ist, die freien Elektronen der K umgebenden Raumladung auf das Beschleunigungsgitter G2 zu lenken. Zwischen K und G1 liegt die Spannung $U_{1}$ an. Das *feinmaschige* **Beschleunigungsgitter G2** (auch [Schirmgitter](https://de.wikipedia.org/wiki/Schirmgitter) genannt) befindet sich im Abstand von $d{\approx}6\,\mathrm{mm}$ von K und fungiert als Anode. Zwischen G1 und G2 liegt die Beschleunigungsspannung $U_{2}$ an. In wiederum geringem Abstand zu G2 befindet sich eine **Auffängerelektrode A.** Zwischen G2 und A befindet sich die Gegenspannung $U_{3}$. 

### Qualitative Bahn der ausgelösten Elektronen

Aus K treten Elektronen thermisch aus und werden auf G1 zu beschleunigt. Wegen des geringen Abstands zwischen K und G1 kommt es hier nur selten zu Stößen der Elektronen mit den $\mathrm{Hg}$-Atomen. Während einige Elektronen auf G1 aufschlagen und so zu K zurückgeführt werden, durchdringen die meisten die *groben* Maschen von G1 und werden auf G2 zu beschleunigt. Auf diesem deutlich längeren Weg kommt es, abhängig von $U_{2}$ sowohl zu **elastischen** als auch zu **unelastischen** Stößen der Elektronen mit den $\mathrm{Hg}$-Atomen. Die meisten Elektronen treffen daraufhin auf G2 auf und erzeugen dort einen messbaren **Anodenstrom** $I$. Einige Elektronen treten jedoch auch durch die feinen Maschen von G2 und werden daraufhin durch das elektrische Feld zwischen G2 und A abgebremst. Je nach Konfiguration aus $U_{1}$, $U_{2}$ und $U_{3}$ werden die Elektronen wieder zu G2 zurück beschleunigt, oder sie erreichen A. Dort können sie mit Hilfe eines Operationsverstärkers über den Spannungsabfall ($U_{\mathrm{A}}$) an einem hochohmigen Widerstand als sehr geringer **Auffängerstrom** $I_{\mathrm{A}}$ nachgewiesen werden. Unter [diesem Link](https://www.kippenbergs.de/mint-franckhertz) können Sie eine Simulation des Wegs der Elektronen durch eine etwas einfachere Franck-Hertz-[Triode](https://de.wikipedia.org/wiki/Elektronenr%C3%B6hre#Triode) beobachten. 

### Mittlere freie Weglänge und Energieverlust der Elektronen

Einer der entscheidenden Faktoren dieses Versuchs ist die Wahrscheinlichkeit mit der ein freies Elektron auf seinem Weg mit einem $\mathrm{Hg}$-Atom stößt. Diese wird durch die [mittlere freie Weglänge](https://de.wikipedia.org/wiki/Mittlere_freie_Wegl%C3%A4nge) charakterisiert, die wie folgt von der Dichte $n$ der $\mathrm{Hg}$-Atome in der Tetrode und vom Wirkungsquerschnitt $\sigma$ für die Streuung eines Elektrons mit einem $\mathrm{Hg}$-Atom abhängt
$$
\begin{equation*}
\lambda = \frac{1}{n\,\sigma}
\end{equation*}
$$

#### Wirkungsquerschnitt

Der Wirkungsquerschnitt $\sigma$ kann durch die geometrische Ausdehnung des $\mathrm{Hg}$-Atoms abgeschätzt werden: 
$$
\begin{equation*}
\sigma= \pi\,R^{2};\qquad R=\sqrt[\leftroot{5}\uproot{0}\scriptstyle 3]{\frac{3}{4\pi}V};
\qquad V= \frac{M_{m}(\mathrm{Hg})\,f}{N_{A}\,\rho_{\mathrm{fl}}},
\end{equation*}
$$
wobei $N_{A}$ der [Avogradro-Konstanten](https://de.wikipedia.org/wiki/Avogadro-Konstante),  $M_{m}(\mathrm{Hg})$ der [molaren Masse](https://de.wikipedia.org/wiki/Molare_Masse), $\rho_{\mathrm{fl}}$ der Dichte von flüssigem $\mathrm{Hg}$ und $f\approx0.74$ dem Füllfaktor der [dichtesten Kugelpackung](https://de.wikipedia.org/wiki/Dichteste_Kugelpackung) entsprechen. Daraus ergibt sich ein Wert von 
$$
\begin{equation*}
\sigma\approx 8\times10^{-16}\,\mathrm{cm}
^{-2}\end{equation*}
$$

#### Teilchendichte

Die Teilchendichte $n$ kann, unter der Annahme, dass sich das System im thermischen Gleichgewicht befindet, mit Hilfe der [idealen Gasgleichung](https://de.wikipedia.org/wiki/Thermische_Zustandsgleichung_idealer_Gase) abgeschätzt werden: 
$$
\begin{equation*}
N\,k\,T = p_{\mathrm{Hg}}\,V;\qquad n=\frac{N}{V} = \frac{p_{\mathrm{Hg}}}{k\,T},
\end{equation*}
$$
wobei $k$ der [Boltzmann-Konstanten](https://de.wikipedia.org/wiki/Boltzmann-Konstante), $N$ der Teilchenzahl, $p_{\mathrm{Hg}}$ dem [Sättigungsdampfdruck](https://de.wikipedia.org/wiki/S%C3%A4ttigungsdampfdruck) von $\mathrm{Hg}$, $V$ dem Volumen und $T$ der Temperatur entsprechen. Eine Parametrisierung des Sättigungsdampfdrucks ist in **Abbildung 2** oben gezeigt. 

<img src="../figures/Energieverlust.png" width="1000" style="zoom:100%;" />

**Abbildung 2**: (Verlauf (oben) des Sättigungsdampfdrucks für $\mathrm{Hg}$, (Mitte) der daraus abgeschätzten mittleren freien Weglänge $\lambda$ der Elektronen in $\mathrm{Hg}$-Dampf im thermischen Gleichgewicht, sowie (unten) des mittleren Energieverlusts von Elektronen nach Durchlaufen einer Strecke von $6\,\mathrm{mm}$ in $\mathrm{Hg}$-Dampf im thermischen Gleichgewicht, jeweils als Funktion der Temperatur)

---

Sie folgt in sehr guter Näherung der Form 
$$
\begin{equation*}
p(T) = 1.324\times 10^{8}\,\exp\left(-\frac{7345.25}{T[\mathrm{K}]}\right)\,\mathrm{mbar},
\end{equation*}
$$
wobei $T$ in $\mathrm{K}$ in die Formel einzusetzen ist, um den Druck in $\mathrm{mbar}$ zu erhalten. Der sich daraus ergebende Verlauf von $\lambda$ ist in **Abbildung 2** (Mitte) gezeigt. Er ist durch die Temperatur des Heizofens verhältnismäßig leicht kontrollierbar. Beim Betrieb der Röhre zwischen 120 und $200^{\circ}\,\mathrm{C}$ gilt $\lambda\lesssim0.2\ldots 0.02\,\mathrm{mm}$.  

#### Energieverlust

Beim elastischen Stoß sind die Gesamtenergie, sowie die Summe aller Impulse im Anfangs- und Endzustand erhalten. Es handelt sich um einen Stoß zweier Körper, der sich im Rahmen der klassischen Mechanik leicht berechnen lässt.  

Die Geschwindigkeit eines Elektrons nach Durchlaufen einer Beschleunigungsspannung von $U=1\,\mathrm{V}$ beträgt: 
$$
\begin{equation*}
E_{\mathrm{kin}}^{\mathrm{(e)}} = \frac{1}{2}m_{\mathrm{e}}v^{2} = e\,U;\qquad v=\sqrt{\frac{2\,e\,U}{m_{\mathrm{e}}}}\approx600000\,\mathrm{m/s}.
\end{equation*}
$$
Im Vergleich dazu kann das $\mathrm{Hg}$-Atom mit einer, bei $T\approx500\,\mathrm{K}$, abgeschätzten mittleren Geschwindigkeit von 
$$
\begin{equation*}
E_{\mathrm{kin}}^{(\mathrm{Hg})} = \frac{1}{2}m_{\mathrm{Hg}}\overline{v^{2}} = \frac{3}{2}k\,T;\qquad \overline{v}=\sqrt{\frac{3\,k\,T}{m_{\mathrm{Hg}}}}\approx 250\,\mathrm{m/s}
\end{equation*}
$$
in sehr guter Näherung als ruhend angenommen werden. Ebenso gilt  $m_{\mathrm{Hg}}\gg m_{\mathrm{e}}$. In diesem Fall entspricht das Ruhesystem des Stoßes ebenfalls in sehr guter Näherung dem Laborsystem und der maximale Energieübertrag eines Elektrons ans $\mathrm{Hg}$-Atom bei einem einzelnen, elastischen Stoß beträgt: 
$$
\begin{equation*}
\Delta E = E\,\frac{2\,m_{\mathrm{e}}}{m_{\mathrm{Hg}}}\left(1-\cos\theta\right),
\end{equation*}
$$
wobei $E$ der Energie des einlaufenden Elektrons, $m_{\mathrm{e}}$ der Masse des Elektrons und $\theta$ dem Streuwinkel entsprechen. Gemittelt über alle Streuwinkel ergibt sich ein relativer Energieübertrag von
$$
\begin{equation*}
\frac{\Delta E}{E} = \frac{2\,m_{\mathrm{e}}}{m_{\mathrm{Hg}}}\approx 5.4\times10^{-6},
\end{equation*}
$$
der Energieübertrag eines einzelnen elastischen Stoßes ist also sehr gering. Andererseits kann das sehr viel leichtere Elektron bei jedem Stoß stark abgelenkt werden, was einen deutlich längeren Diffusionsweg durch die Tetrode zur Folge hat, bei dem es, je nach $n$, häufig zu Stößen kommen kann. Eine entsprechende Näherungsrechnung dieses Diffusionsprozesses für die dem Versuch zugrunde liegenden Geometrie führt auf einen totalen mittleren Energieverlust von 
$$
\begin{equation*}
\Delta E\approx\frac{1}{3}\left(\frac{d}{\lambda}\right)^{2}\frac{2\,m_{\mathrm{e}}}{m_{\mathrm{Hg}}}\, e\,U,
\end{equation*}
$$
wobei $U$ der Beschleunigungsspannung und $d\approx6\,\mathrm{mm}$ dem Abstand zwischen K und G2 entsprechen. Der Verlauf des relativen Energieverlusts des Elektrons als Funktion der Temperatur im thermischen Gleichgewicht in $\mathrm{Hg}$-Dampf ist in **Abbildung 2** (unten) gezeigt. Er liegt für $T\lesssim175^{\circ}\,\mathrm{C}$ bei er unter 1%, steigt jenseits davon jedoch deutlich an.

Wir halten zusammenfassend fest, dass der Energieverlust der Elektronen durch elastische Stöße für Temperaturen von $T\lesssim175^{\circ}\,\mathrm{C}$ verhältnismäßig gering ist. 

#### Auffängerstrom

Nur wenige Elektronen treten durch die engen Maschen des Beschleunigungsgitters. Zusätzlich ist die Bewegung der durch die Maschen tretenden Elektronen diffus und nur der zum Gegenfeld anti-parallel ausgerichtete Teil der Geschwindigkeit trägt dazu bei die Gegenspannung zu überwinden. Daher gilt i.a. $I_{A}\ll I$. 

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch)
