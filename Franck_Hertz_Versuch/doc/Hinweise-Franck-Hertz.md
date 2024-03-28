# Hinweise für den Franck-Hertz-Versuch

## Aufbau und Schaltung der Röhre

Eine Skizze der Tetrode, wie sie für den Franck-Hertz-Versuch im P2 verwendet wird in **Abbildung 1** gezeigt:

<img src="../figures/FranckHertzSkizze.png" width="1000" style="zoom:100%;"/>

**Abbildung 1**: (Schematische Darstellung der Franck-Hertz-Tetrode, wie sie im P2 verwendet wird (oben). Im unteren Teil der Abbildung ist der Aufbau der tatsächlichen Röhre zu sehen)

---

Auf der linken Seite der Zeichnung im oberen Teil der Abbildung befindet sich eine Glühkathode K mit dem Widerstand $R_{\mathrm{K}}$, die mit der Spannung $U_{\mathrm{K}}$ versorgt wird. Im Abstand von ${\approx}0.5\,\mathrm{mm}$ zu K befindet sich ein *grobmaschiges* **Raumladungsgitter G1** (auch [Steuergitter](https://de.wikipedia.org/wiki/Steuergitter) genannt), dessen Funktion es ist, die freien Elektronen aus der Raumladung die K umgibt auf das Beschleunigungsgitter G2 zu lenken. Zwischen K und G1 liegt die Spannung $U_{1}$ an. Das *feinmaschige* **Beschleunigungsgitter G2** (auch [Schirmgitter](https://de.wikipedia.org/wiki/Schirmgitter) genannt) befindet sich im Abstand von $d{\approx}6\,\mathrm{mm}$ von K und fungiert als Anode. Zwischen G1 und G2 liegt die Spannung $U_{2}$ an. Gemeinsam mit der zunächst unbekannten  [Kontakt-](https://de.wikipedia.org/wiki/Volta-Spannung) und [Thermospannung](https://de.wikipedia.org/wiki/Thermoelektrizit%C3%A4t) $U_{\mathrm{th.}}$ zwischen K und G2 ergibt sich die Beschleunigungsspannung zu
$$
\begin{equation*}
U_{B} = U_{\mathrm{th.}}+U_{1}+U_{2}.
\end{equation*}
$$
In wiederum geringem Abstand zu G2 befindet sich eine **Auffängerelektrode A.** Zwischen G2 und A befindet sich die Gegenspannung $U_{3}$. 

## Bahn der ausgelösten Elektronen

Aus K treten Elektronen thermisch aus und werden auf G1 zu beschleunigt. Wegen des geringen Abstands zwischen K und G1 kommt es hier nur selten zu Stößen der Elektronen mit den $\mathrm{Hg}$-Atomen. Während einige Elektronen auf G1 aufschlagen und so über den Strom $I_{\mathrm{G1}}$ zu K zurückgeführt werden, durchdringen die meisten Elektronen die *groben* Maschen von G1 und werden auf G2 zu beschleunigt. Auf diesem deutlich längeren Weg kommt es, abhängig von $U_{2}$ sowohl zu **elastischen** als auch zu **unelastischen** Stößen der Elektronen mit den $\mathrm{Hg}$-Atomen. Die meisten Elektronen treffen daraufhin auf G2 auf und erzeugen dort einen messbaren **Anodenstrom** $I_{\mathrm{G2}}$. Einige Elektronen treten jedoch durch die feinen Maschen von G2 und werden daraufhin durch das elektrische Feld zwischen G2 und A abgebremst. Je nach Konfiguration aus $U_{1}$, $U_{2}$ und $U_{3}$ werden die Elektronen wieder zu G2 zurück beschleunigt, oder sie erreichen A. Dort können sie mit Hilfe eines Operationsverstärkers über den Spannungsabfall ($U_{\mathrm{A}}$) an einem hochohmigen Widerstand als sehr geringer **Auffängerstrom** $I_{\mathrm{A}}$ nachgewiesen werden. Unter [diesem Link](https://www.kippenbergs.de/mint-franckhertz) können Sie eine Simulation des Wegs der Elektronen durch eine etwas einfachere Franck-Hertz-[Triode](https://de.wikipedia.org/wiki/Elektronenr%C3%B6hre#Triode) beobachten. 

## Anodenstrom $I_{\mathrm{G2}}$

Für eine aus einer Glühkathode (z.B. K) und einer Anode (z.B. G2) bestehende, evakuierte Diode, für die der Anodenstrom $I_{\mathrm{G2}}$ durch Raumladungseffekte bei K dominiert wird gilt die Strom-Spannung-Abhängigkeit des Schottky-Langmuirschen [Raumladungsgesetzes](https://de.wikipedia.org/wiki/Raumladungsgesetz)
$$
\begin{equation}
I_{\mathrm{G2}}(U_{B}) = \kappa\, U_{B}^{3/2},
\end{equation}
$$
wobei man $\kappa$ als Raumladungskonstante oder [Perveanz](https://de.wikipedia.org/wiki/Perveanz) bezeichnet. Dabei hängt $\kappa$ nur von der Geometrie der Anordnung und nicht von der Emissionsfähigkeit der Kathode ab. Den in Gleichung **(1)** dargestellten Zusammenhang bezeichnet man auch als [Neilsche Parabel](https://de.wikipedia.org/wiki/Neilsche_Parabel).

Für die Anordnung der im Versuch verwendeten Tetrode kann der Zusammenhang aus Gleichung **(1)** durch die folgenden Besonderheiten modifiziert werden: 

- Zusätzlich zu G2 liegt G1 auf einem relativ zu K nicht verschwindenden Potential und beeinflusst damit die Geometrie der elektrischen Feldlinien und damit der Röhre. 
- Die Tetrode ist nicht evakuiert, sondern mit $\mathrm{Hg}$-Dampf geringer Dichte befüllt, der die Bewegung der Elektronen hämt. 

## Auffängerstrom $I_{A}$

Nur wenige Elektronen treten durch die engen Maschen von G2. Zusätzlich ist die Bewegung der durch die Maschen tretenden Elektronen aufgrund der Streuung an den Atomen des $\mathrm{Hg}$-Dampfs diffus und nur der zum Gegenfeld anti-parallel ausgerichtete Teil der Geschwindigkeit trägt dazu bei $U_{3}$ zu überwinden. Daher gilt i.a. $I_{A}\ll I_{\mathrm{G2}}$. Der Verlauf von $I_{A}$ als Funktion der Beschleunigungsspannung $U_{B}$ ist in **Abbildung 2** schematisch dargestellt:

<img src="../figures/FranckHertzVerlauf.png" width="800" style="zoom:80%;"/>

**Abbildung 2**: (Schematischer Verlauf des Auffängerstroms $I_{A}$ als Funktion der Beschleunigungsspannung $U_{B}$)

---

$I_{A}$ steigt zunächst, wie $I_{\mathrm{G2}}$, mit zunehmender Spannung $U_{B}$ an. In periodischen Abständen $\Delta U_{B}$ kommt es jedoch zu charakteristischen Einbrüchen, die auf **unelastische** Stöße der Elektronen im $\mathrm{Hg}$-Dampf zurückzuführen sind, bei denen die Elektronen so viel ihrer kinetischen Energie verlieren, dass sie $U_{3}$ anschließend nicht mehr überwinden können. Dass $I_{A}$ in diesem Fall nicht auf 0 zurückfällt ist dadurch zu erklären, dass nicht alle Elektronen mit Atomen des $\mathrm{Hg}$-Dampf unelastisch stoßen. Der erste Einbruch in **Abbildung 2** zeigt den Wert von $U_{B}$ an, ab dem die kinetische Energie $E_{\mathrm{kin}}^{(\mathrm{e})}$ der Elektronen zum ersten mal ausreicht, um das Energieniveau mit dem niedrigsten Energieübertrag in einem $\mathrm{Hg}$-Atom anzuregen. Beim zweiten Einbruch reicht die daraufhin auf dem Weg nach G2 wieder aufgenommene Energie aus, um erneut $\mathrm{Hg}$-Atome anzuregen. 

## Mittlere freie Weglänge und Energieverlust der Elektronen

Einer der entscheidenden Faktoren des Versuchs ist die Wahrscheinlichkeit mit der ein freies Elektron auf seinem Weg mit einem $\mathrm{Hg}$-Atom stößt. Diese wird durch die [mittlere freie Weglänge](https://de.wikipedia.org/wiki/Mittlere_freie_Wegl%C3%A4nge) charakterisiert, die wie folgt von der Dichte $n$ der $\mathrm{Hg}$-Atome in der Tetrode und vom Wirkungsquerschnitt $\sigma$ für die Streuung eines Elektrons mit einem $\mathrm{Hg}$-Atom abhängt
$$
\begin{equation*}
\lambda = \frac{1}{n\,\sigma}
\end{equation*}
$$

### Wirkungsquerschnitt

Der Wirkungsquerschnitt $\sigma$ kann durch die geometrische Ausdehnung des $\mathrm{Hg}$-Atoms abgeschätzt werden: 
$$
\begin{equation*}
\sigma= \pi\,R^{2};\qquad R=\sqrt[3]{\frac{3}{4\pi}V};
\qquad V= \frac{M_{m}(\mathrm{Hg})\,f}{N_{A}\,\rho_{\mathrm{fl}}},
\end{equation*}
$$
wobei $`N_{A}`$ der [Avogradro-Konstanten](https://de.wikipedia.org/wiki/Avogadro-Konstante),  $`M_{m}(\mathrm{Hg})`$ der [molaren Masse](https://de.wikipedia.org/wiki/Molare_Masse), $`\rho_{\mathrm{fl}}`$ der Dichte von flüssigem $\mathrm{Hg}$ und $f\approx0.74$ dem Füllfaktor der [dichtesten Kugelpackung](https://de.wikipedia.org/wiki/Dichteste_Kugelpackung) entsprechen. Daraus ergibt sich ein Wert von 
$$
\begin{equation*}
\sigma\approx 8\times10^{-16}\,\mathrm{cm}
^{-2}\end{equation*}
$$

### Teilchendichte

Die Teilchendichte $n$ kann, unter der Annahme, dass sich das System im thermischen Gleichgewicht befindet, mit Hilfe der [idealen Gasgleichung](https://de.wikipedia.org/wiki/Thermische_Zustandsgleichung_idealer_Gase) abgeschätzt werden: 
$$
\begin{equation*}
N\,k\,T = p_{\mathrm{Hg}}\,V;\qquad n=\frac{N}{V} = \frac{p_{\mathrm{Hg}}}{k\,T},
\end{equation*}
$$
wobei $k$ der [Boltzmann-Konstanten](https://de.wikipedia.org/wiki/Boltzmann-Konstante), $N$ der Teilchenzahl, $p_{\mathrm{Hg}}$ dem [Sättigungsdampfdruck](https://de.wikipedia.org/wiki/S%C3%A4ttigungsdampfdruck) von $\mathrm{Hg}$, $V$ dem Volumen und $T$ der Temperatur entsprechen. Die Annahme eines thermischen Gleichgewichts impliziert, dass der $\mathrm{Hg}$-Dampf homogen in der Röhre verteilt ist. Eine Parametrisierung von $p_{\mathrm{Hg}}$ ist in **Abbildung 3** oben gezeigt. 

<img src="../figures/Energieverlust.png" width="800" style="zoom:80%;"/>

**Abbildung 3**: (Verlauf (oben) des Sättigungsdampfdrucks für $\mathrm{Hg}$, (Mitte) der daraus abgeschätzten mittleren freien Weglänge $\lambda$ der Elektronen in $\mathrm{Hg}$-Dampf, sowie (unten) des mittleren Energieverlusts von Elektronen nach Durchlaufen einer Strecke von $6\,\mathrm{mm}$ in $\mathrm{Hg}$-Dampf, jeweils als Funktion der Temperatur)

---

Sie folgt in sehr guter Näherung der Form 
$$
\begin{equation*}
p(T)[\mathrm{mbar}] = 1.324\times 10^{8}\,\exp\left(-\frac{7345.25}{T[\mathrm{K}]}\right),
\end{equation*}
$$
wobei $T$ in $\mathrm{K}$ in die Formel einzusetzen ist, um den Druck in $\mathrm{mbar}$ zu erhalten. Der sich daraus ergebende Verlauf von $\lambda$ ist in **Abbildung 3** (Mitte) gezeigt. Er kann durch die Temperatur des Heizofens verhältnismäßig leicht kontrolliert werden. Beim Betrieb der Röhre zwischen 120 und $200^{\circ}\,\mathrm{C}$ gilt $\lambda\lesssim0.2\ldots 0.02\,\mathrm{mm}$.  

### Energieverlust beim elastischen Stoß

Beim elastischen Stoß sind die kinetische Energie, sowie die Summe aller Impulse im Anfangs- und Endzustand erhalten. Es handelt sich um einen Zwei-Körper-Stoß, der sich im Rahmen der klassischen Mechanik leicht berechnen lässt.  

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
in sehr guter Näherung als ruhend angenommen werden. Ebenso gilt  $m_{\mathrm{Hg}}\gg m_{\mathrm{e}}$, weshalb wir ebenfalls annehmen dürfen, dass das Ruhesystem des Stoßes dem Laborsystem entspricht. In diesem Fall beträgt der maximale Energieübertrag des Elektrons ans $\mathrm{Hg}$-Atom 
$$
\begin{equation*}
\Delta E_{\mathrm{kin}}^{(\mathrm{e})} = E_{\mathrm{kin}}^{(\mathrm{e})}\,\frac{2\,m_{\mathrm{e}}}{m_{\mathrm{Hg}}}\left(1-\cos\theta\right),
\end{equation*}
$$
wobei $m_{\mathrm{e}}$ der Masse des Elektrons und $\theta$ dem Streuwinkel entsprechen. Gemittelt über alle Streuwinkel ergibt sich also ein sehr geringer relativer Energieübertrag von
$$
\begin{equation*}
\frac{\Delta E_{\mathrm{kin}}^{(\mathrm{e})}}{E_{\mathrm{kin}}^{(\mathrm{e})}} = \frac{2\,m_{\mathrm{e}}}{m_{\mathrm{Hg}}}\approx 5.4\times10^{-6}.
\end{equation*}
$$
Andererseits kann das sehr viel leichtere Elektron bei jedem Stoß sehr stark abgelenkt werden, was einen im Vergleich zu einem geraden Weg deutlich längeren Diffusionsweg durch die Tetrode zur Folge hat, bei dem es, je nach $n$, häufig zu Stößen kommen kann. Eine entsprechende Näherungsrechnung dieses Diffusionsprozesses für die dem Versuch zugrunde liegende Geometrie führt auf einen totalen mittleren Energieverlust von 
$$
\begin{equation*}
\Delta E_{\mathrm{kin}}^{(\mathrm{e})}\approx\frac{1}{3}\left(\frac{d}{\lambda}\right)^{2}\frac{2\,m_{\mathrm{e}}}{m_{\mathrm{Hg}}}\, e\,U_{B}.
\end{equation*}
$$
Der Verlauf des relativen Energieverlusts des Elektrons als Funktion der Temperatur im thermischen Gleichgewicht in $\mathrm{Hg}$-Dampf ist in **Abbildung 3** (unten) gezeigt. Er liegt für $T\lesssim175^{\circ}\,\mathrm{C}$ bei unter 1%, steigt jenseits davon jedoch deutlich an.

Wir halten zusammenfassend fest, dass der Energieverlust der Elektronen durch elastische Stöße für Temperaturen von $T\lesssim175^{\circ}\,\mathrm{C}$ verhältnismäßig gering ist. 

### Energieverlust beim unelastischen Stoß

Beim unelastischen Stoß entspricht die kinetische Energie der Stoßpartner nach dem Stoß nicht der kinetischen Energie im Anfangszustand. Die "fehlende" Energie wird in Form von inneren Anregungszuständen des $\mathrm{Hg}$-Atoms aufgenommen. Ein wesentlicher Ausgang des Franck-Hertz-Versuchs ist, dass diese Anregungszustände quantisiert vorliegen.

[Quecksilber](https://www.periodensystem.info/elemente/quecksilber/) hat die Ordnungszahl $Z=80$. In neutralem Zustand ist seine Hülle mit 80 Elektronen besetzt. Die Elektronenkonfiguration lautet: 
$$
\begin{equation*}
\mathrm{[Xe]\,4\,f^{14}\,5\,d^{10}\,6\,s^{2}},
\end{equation*}
$$
d.h. die N-Schale (für die Hauptquantenzahl $n=4$) ist mit 60 Elektronen voll besetzt (Edelgaskonfiguration von $\mathrm{Xe}$), die O-Schale (für $n=5$) hat die Konfiguration $\mathrm{5\,s^{2}\,5\,p^{6}\,5\,d^{10}}$, das $\mathrm{5\,f^{0}}$ Orbital ist unbesetzt und das $\mathrm{6\,s^{2}}$ Orbital mit zwei Elektronen besetzt. 

Im [$6^{1}\mathrm{S}_{0}$-Grundzustand](https://de.wikipedia.org/wiki/Termsymbol) des Atoms sind Gesamtbahndrehimpuls, sowie Gesamtspin der Elektronen Null. In angeregten Zuständen befindet sich ein Elektron (selten Fällen auch zwei oder mehr) in einem Zustand, der zu anderen anderen Quantenzahlen führt. Ein verkürztes Termschema der Energieniveaus in $\mathrm{Hg}$ ist in **Abbildung 4** gezeigt:

<img src="../figures/TermschemaHg.png" width="800" style="zoom:80%;"/>

**Abbildung 4**: (Verkürztes Termschema von $\mathrm{Hg}$ (Werte aus [NIST Atomic Spectra Database](https://www.nist.gov/pml/atomic-spectra-database)))

---

Der $6^{1}\mathrm{S}_{0}$-Grundzustand befindet sich unten links im Bild, schräg verlaufende Linien entsprechen [erlaubten optische Übergängen](https://de.wikipedia.org/wiki/Auswahlregel) zwischen verschiedenen Anregungsniveaus. Für einige optisch erlaubte Übergänge sind auch die Wellenlängen des abgestrahlten Lichts angegeben. Optisch verbotene Übergänge ergeben sich, wenn die Erhaltung des Drehimpulses beim Übergang nur durch Multipolstrahlung höherer Ordnung gewährleistet ist. Da es für Elektronstöße keine solchen Auswahlregeln gibt sind in diesem Fall prinzipiell alle Übergänge erlaubt. Tatsächlich sind aus dem gleichen Grund der Drehimpulserhaltung, auch in diesem Fall optisch verbotene Übergänge i.a. seltener. Die Wahrscheinlichkeit, mit der ein Übergang bei Anregung stattfindet wird durch den Wirkungsquerschnitt beschrieben, den man in diesem Fall auch als [Anregungsfunktion](https://de.wikipedia.org/wiki/Wirkungsquerschnitt) bezeichnet. Dieser ist unterhalb der für die Anregung notwendigen Energie 0 und steigt darüber mehr oder weniger steil an. Im Praktikum beobachtbar sind die Übergänge: 

- $6^{1}\mathrm{S}_{0}\to 6^{3}\mathrm{P}_{0}$ mit einer Energiedifferenz von $4.66\,\mathrm{eV}$ (optisch verboten); die Anregungsfunktion steigt steil, jedoch auf einen kleinen Wert an.
- $6^{1}\mathrm{S}_{0}\to 6^{3}\mathrm{P}_{1}$ mit einer Energiedifferenz von $4.86\,\mathrm{eV}$ (optisch erlaubt); die Anregungsfunktion steigt steil, auf einen großen Wert an.
- $6^{1}\mathrm{S}_{0}\to 6^{3}\mathrm{P}_{2}$ mit einer Energiedifferenz von $5.46\,\mathrm{eV}$ (optisch verboten); die Anregungsfunktion steigt steil, jedoch auf einen kleinen Wert an.
- $6^{1}\mathrm{S}_{0}\to 6^{1}\mathrm{P}_{1}$ mit einer Energiedifferenz von $6.70\,\mathrm{eV}$ (optisch erlaubt); die Anregungsfunktion steigt flach, auf einen großen Wert an.

Nach einer Anregung durch Elektronenstoß kehrt das Atom spontan wieder in den Grundzustand zurück. Bei optisch erlaubten Übergängen erfolgt dieser Übergang in Bruchteilen von Mikrosekunden, unter Emission von Licht, bei optisch verbotenen Übergängen geschieht dies durch erneute Anregung durch  Elektronenstoß in ein höheres Energieniveau mit erlaubtem Übergang oder
durch Stöße mit der Gefäßwand. Der zuletzt genannte Vorgang läuft erheblich langsamer ab. Beim Franck-Hertz-Versuch mit $\mathrm{Hg}$ liegen ohne Ionisierung die alle Wellenlängen des emittierten Lichts im UV-Bereich. Sie sind im Praktikum also nicht zu beobachten.

## Ionisation 

Die Ionisationsenergie (für die einfache Ionisation) von $\mathrm{Hg}$ beträgt $10.44\,\mathrm{eV}$. Für das Auftreten von Ionisierung gibt es im Experiment typische Kennzeichen: 

- Im Gasraum treten positive Ionen auf, diese die Raumladung in der Nähe von K herabsetzen und dadurch jenseits Ionisierungsenergie einen steileren Anstieg von $I_{\mathrm{G2}}$ bewirken. 

- Sie treten auch im Raum zwischen G2 und A auf und bewirken dort einen Strom $I_{A}$ **mit gegenüber den Elektronenstrom umgekehrten Vorzeichen**. 

- Das Zünden einer Gasentladung ist von deutlichem Leuchten begleitet, das spektroskopisch beobachtet werden kann. Bei der Rekombination der Ionen mit Elektronen kommen stufenweise alle möglichen Übergänge bis in den Grundzustand vor. Am deutlichsten sind die folgenden Emissionslinien sichtbar: 

  - $\lambda=404,66\,\mathrm{nm}$ (violett): $7^{3}\mathrm{S}_{1}\to6^{3}\mathrm{P}_{0}$; 
  - $\lambda=407,78\,\mathrm{nm}$ (violett): $7^{1}\mathrm{S}_{0}\to6^{3}\mathrm{P}_{1}$;
  - $\lambda=434,75\,\mathrm{nm}$ (violett): $7^{1}\mathrm{D}_{1}\to6^{1}\mathrm{P}_{1}$;  
  - $\lambda=491,61\,\mathrm{nm}$ (blau): $6^{1}\mathrm{P}_{1}\to 8^{1}\mathrm{S}_{0}$;
  - $\lambda=546,08\,\mathrm{nm}$ (grün): $7^{3}\mathrm{S}_{1}\to6^{3}\mathrm{P}_{2}$;
  - $\lambda=579,07\,\mathrm{nm}$ (gelb): $6^{1}\mathrm{D}_{2}\to6^{1}\mathrm{P}_{1}$.

  Die fahlblaue Farbe des ohne Spektroskop beobachteten Leuchtens ist das Ergebnis der additiven Mischung aus all den einzelnen Linien.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch)
