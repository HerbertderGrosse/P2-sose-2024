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

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch)
