# Hinweise für den Versuch Gammaspektroskopie

## Versuchsdurchführung

#### Aufgabe 1.2: Effekt der Steuerparameter an der Röhre

Steuerparameter an der Röhre sind $\vartheta$, $U_{1}$, $U_{2}$, $U_{3}$. In **Abbildung 5** ist gezeigt, welche Effekte die einzelnen Steuerparameter haben sollten:

<img src="../figures/OptimierungFranckHertz.png" width="800" style="zoom:80%;"/>

**Abbildung 5**: (Effekt der Steuerparameter $\vartheta$, $U_{1}$ und $U_{3}$)

---

Auf der $x$-Achse sind jeweils ansteigende Werte von $U_{2}$ gezeigt. Steigt $I_{A}$ mit nunehmenden Werten von $U_{2}$ sprunghaft an (siehe **Abbildung (a)**) kommt es zur Gasentladung. Dieser Vorgang ist i.a. von fahlblauem Leuchten der Röhre begleitet. Sie sollten eine unkontrollierte Gasentladung unbedingt vermeiden, um die Röhre nicht zu beschädigen. Schalten Sie in diesem Fall $U_{2}$ sofort ab und erhöhen Sie dann $\vartheta$, um die freie Weglänge der Elektronen zu reduzieren. 

Das Raumladungsgitter G2 befindet sich dicht hinter K. Durch $U_{1}$ kommt es zwischen K und G1 daher zu hohen elektrischen Feldern, deren Funktion es ist die Raumladungswolke um K abzusaugen, so dass weitere Elektronen aus K nachrücken können. Die Spannung $U_{1}$ reguliert damit effektiv den Elektronenstrom durch die Röhre und die Steigung von $I_{A}$ als Funktion von $U_{2}$.  In **Abbildung 5 (b)** geht $I_{A}$ bereits weit vor Erreichen des Maximalwertes von $U_{2}$ (auf der $x$-Achse) in die Sättigung der Messanordnung, $U_{1}$ sollte nach unten geregelt werden. In **Abbildung 5 (c)** sollte $U_{1}$ nach oben geregelt werden. Bleibt der Verlauf von $I_{A}$ selbst bei maximaler Einstellung von $U_{1}\approx 5\hspace{0.05cm}\mathrm{V}$ flach regeln Sie $\vartheta$ nach unten, um die mittlere freie Weglänge der Elektronen auf dem Weg durch die Röhre zu erhöhen. 

Die Höhe von $U_{3}$ reguliert die Ausprägung der beobachteten Minima und Maxima. Gleichzeitig wird $I_{A}$ für steigende Werte von $U_{3}$ reduziert. Ohne besondere Optimierung von $U_{3}$ könnte $I_{A}$, bei geeigneter Einstellung von $U_{1}$ so aussehen, wie in **Abbildung 5 (d)** gezeigt. Von **Abbildung 5 (d)** zu **(f)** gelangen Sie, indem Sie vorsichtig abwechselnd $U_{1}$ und $U_{3}$ erhöhen. Von **Abbildung 5 (e)** zu **(f)** gelangrn Sie, indem Sie vorsichtig abwechselnd $U_{1}$ und $U_{3}$ reduzieren.  

**Nehmen Sie sich ausreichend Zeit das Wechselspiel der Steuerparameter zu studieren. Protokollieren Sie schließlich die Einstellungen, zu den entsprechenden Darstellungen gewissenhaft.**

### Aufgabe 2: Charakterisierung der Röhre

#### Aufgabe 2.1: Bestimmung der Spannungsdifferenz $\Delta U_{B}$ und der effektiven Kontaktspannung $U_{\mathrm{th.}}$

Einen schematischen Verlauf von $I_{A}$ als Funktion von $U_{B}$ ist in **Abbildung 2** hier gezeigt. Die Differenzen $\Delta U_{B}$ lassen sich sowohl aus den Maxima, als auch aus den Minima des Verlaufs bestimmen. Im Versuch sollten Sie bis zu fünf Maxima bestimmen können. 

Tragen Sie in einem ersten Diagramm D1 zunächst $I_{A}$ gegen $U_{1}+U_{2}$ auf. Das erste Maximum der Verteilung $U_{B}^{(1)}$ liegt bei einem Wert von $U_{1}+U_{2}$ der größer ist als $\Delta U_{B}$, danach sollten alle weiteren Maxima den gleichen Abstand $\Delta U_{B}$ zueinander aufweisen. Nach Gleichung **(1)** hier entspricht der Differenzbetrag zwischen $U_{B}^{(1)}$ und $\Delta U_{B}$ der effektiven Kontaktspannung $U_{\mathrm{th.}}$. Sie können zur gleichzeitigen Bestimmung von $\Delta U_{B}$ und $U_{th.}$ dann z.B. wie folgt vorgehen: 

- Bestimmen Sie die Lage, der $N$ Maxima aus Ihrer Messung mit entsprechender Unsicherheit, z.B. aus der Anpassung einer Normalverteilung auf einer geeignet gewählten Untergrundfunktion. 

- Tragen Sie daraufhin in einem zweiten Diagramm D2 die Indizes der Maxima ($i=1\ldots N$) auf der $x$-Achse gegen die Lagen des $i$ Maxima auf der $y$-Achse auf. An D2 können Sie ein Modell der Form

  ```math
  \begin{equation*}
  U_{B}^{(i)}(\Delta U_{B}, U_{\mathrm{th.}}) = \Delta U_{B}\cdot i + U_{\mathrm{th.}}
  \end{equation*}
  ```

   anpassen, aus dem Sie $\Delta U_{B}$ und $U_{\mathrm{th.}}$ gleichzeitig bestimmen können. Für die Anpassung mit Hilfe eines XYFits aus dem Programmpaket kafe2 können Sie den Indizes auf der $x$-Achse eine sehr kleine Unsicherheit von $10^{-3}$ zuordnen.  

Kalibrieren Sie für Ihre Auswertung mit Hilfe von $U_{\mathrm{th.}}$ die $x$-Achsen aller aufgenommenen Diagramme entsprechend auf $U_{B}$. 

#### Aufgabe 2.2: Verlauf des Anodenstroms $I_{\mathrm{G2}}$

Das Schottky-Langmuirschen [Raumladungsgesetz](https://de.wikipedia.org/wiki/Raumladungsgesetz) gilt streng genommen nur für evakuierte Dioden. Die Spannung $U_{3}$ ist für diese Aufgabe irrelevant. Regeln Sie daher sowohl $U_{1}$ als auch $U_{3}$ auf Null. 

Bestimmen Sie $I_{\mathrm{G2}}$ für eine geeignet hohe Anzahl, mindestens aber für 10 verschiedene Werte von $U_{2}$. Nehmen Sie sowohl für $I_{\mathrm{G2}}$ als auch für $U_{2}$ geeignete Unsicherheiten an.

Passen Sie an den resultierenden Kurvenverlauf ein Modell der Form

```math
\begin{equation*}
I_{\mathrm{G2}}(\kappa,\,) = \kappa\,\left(U_{2}+U_{\mathrm{th.}}\right)^{\gamma}
\end{equation*}
```

an, wobei $\kappa$, $U_{\mathrm{th.}}$ und $\gamma$ freie Parameter der Anpassung sind. Geben Sie in Ihrer Auswertung den auf die Anzahl der Freiheitsgrade normierten $\chi^{2}$-Wert oder den $p$-Wert der Anpassung an. Innerhalb der resultierenden Unsicherheiten sollte $U_{\mathrm{th.}}$ mit dem aus **Aufgabe 2.1** ermittelten Wert und $\gamma$ mit dem Wert 3/2 übereinstimmen.  

### Aufgabe 3: Höhere Anregungen von $\mathrm{Hg}$

#### Aufgabe 3.1: Beobachtung höherer Anregungen von $\mathrm{Hg}$

Beim Betrieb der Röhre, wie für **Aufgabe 2** kommt es kaum zu Anregungen höherer Energiezustände, weil die Elektronen zwischen den unelastischen Stößen nicht genug kinetische Energie aufnehmen können. Um dies zu erreichen müssen Sie die Röhre in einem anderen Modus betreiben. 

- Legen Sie hierzu G1 und G2 auf das gleiche Potential $U_{2}$. In einer solchen Konfiguration verwenden Sie G1 als Anode und den Raum zwischen G1 und G2 als spannungsfreien **Driftraum**. 
- Senken Sie außerdem ggf. $\vartheta$, um $\lambda$ zu erhöhen. Durch den geringen Abstand zwischen K und G1 ist die Stoßwahrscheinlichkeit dort gering. 
- Im Driftraum ist sie durch die längere Driftstrecke erhöht.  
- Die beobachtbaren Strukturen sollten sich durch ganzzahlige Linearkombinationen der am häufigsten stattfinden Übergänge mit den niedrigsten Energieüberträgen ($`6^{1}\mathrm{S}_{0}\to 6^{3}\mathrm{P}_{1}`$ und $`6^{1}\mathrm{S}_{0}\to 6^{1}\mathrm{P}_{1}`$) erklären lassen. 

#### Aufgabe 3.2: Ionisierungsenergie von $\mathrm{Hg}$

- Für diese Aufgabe besteht das Ziel darin eine kontrollierte Gasentladung einzuleiten.   
- Nehmen Sie $I_{\mathrm{G2}}$ als Funktion von $U_{2}$ auf. Tun Sie dies, per Hand in geeigneten Schritten, um mindestens 10 Messpunkte zwischen $U_{2}=0$ und $30\hspace{0.05cm}\mathrm{V}$ zu erhalten. 
- Zusätzlich können Sie ggf. $\vartheta$ reduzieren, um $\lambda$ weiter zu erhöhen.
- Sobald Ionisation einsetzt sollten Sie einen deutlichen Anstieg in $I_{\mathrm{G2}}$ feststellen.
- Passen Sie ein geeignetes Modell an die Daten an, um den Punkt des Anstiegs mit entsprechender Unsicherheit abzuschätzen. Dies erreichen Sie z.B. durch die Anpassung zweier Geraden. Lassen Sie dabei den Übergangsbereich aus, da Sie dort aufgrund von Auflösungseffekten keinen linearen Verlauf erwarten. Sie können den Schnittpunkt der beiden Geraden als Abschätzung für die Ionisierungsenergie von $\mathrm{Hg}$ verwenden. Schätzen Sie die Unsicherheiten für diese Art der Bestimmung geeignet ab. 

### Aufgabe 4: Bestimmung der mittleren Energie für die Anregung von $\mathrm{Ne}$ durch Elektronenstoß

- Bei den vorherrschenden Anregungen handelt es sich um eine Gruppe von Niveaus, die in einem etwa $0,5\hspace{0.05cm}\mathrm{eV}$ breiten Energiebereich liegen. Das zugehörige emittierte Licht ist rot. Wenn Sie die Beschleunigungsspannung erhöhen, sollten Sie die Verlagerung und die Vermehrung von Leuchtschichten im Stoßraum beobachten können. 
- Für diesen Versuchsteil benutzen Sie eine spezielle Röhre mit indirekter Kathodenheizung, planparalleler Elektrodenanordnung und $\mathrm{Ne}$-Füllung. Die Kontaktspannung zwischen der $\mathrm{BaO}$-Kathode und der Metallanode mindert die angelegte Spannung um etwa $2,5\,\mathrm{V}$. Die Schaltung entspricht der der Franck-Hertz-$\mathrm{Hg}$-Röhre. 
- Die Franck-Hertz-$\mathrm{Ne}$-Röhre ist nur einmal vorhanden, Sie müssen sie also mit den anderen Gruppen gemeinsam benutzen. Weil die Schaltung bereits fertig aufgebaut ist und Wartezeiten für das Aufheizen oder Abkühlen in diesem Fall entfallen, benötigen Sie aber nur wenig Zeit für diese Aufgabe. 
- Die Röhre sollte nicht in der für **Aufgabe 3** modifizierten Schaltung betrieben werden.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Franck_Hertz_Versuch)
