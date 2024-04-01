# Hinweise für den Versuch Gammaspektroskopie

## Gammaspektroskopie

### Zufall und Statistik

Bei den Wechselwirkungen einzelner Teilchen mit Materie handelt es sich um probabilistische Vorgänge. Ob ein auf den Detektor auftreffendes Photon $\gamma$ seine gesamte Energie $E_{\gamma}$ im Detektor deponieren, oder ein gestreutes Photon $\gamma'$ den Detektor nach Compton-Streuung wieder verlassen wird ist nicht deterministisch vorhersagbar. All diesen Ereignissen lassen sich jedoch feste und immer gleiche Wahrscheinlichkeiten zuordnen.

Ebenso ist die Entstehung des zu $\gamma$ gehörigen Signals $Q(E_{\gamma})$ mit dem Produkt einer schier unüberschaubar großen Anzahl an Einzelwahrscheinlichkeiten $p_{k}$ verbunden. Diese quantifizieren z.B.

- das Auftreten einzelner Wechselwirkungen hoch-energetischer Photonen mit dem Detektormaterial; 
- die Erzeugung von Ladungsträgern und Szintillationsphotonen im Detektormaterial; 
- das Auftreten von Primärelektronen $e_{i}$ an der PK; 
- die Vervielfachung der $e_{i}$ im SEV, sowie die sich anschließende, weitere, elektronische Signalverstärkung und Übersetzung in Kanäle des MCA. 

Für die folgenden Betrachtungen lassen wir die Vervielfachung der $e_{i}$ im SEV, sowie die sich daran anschließende weitere Signalverarbeitung, auf die wir später zurück kommen werden, zunächst außer Acht.

Die Wahrscheinlichkeit für das Auftreten eines Primärelektrons an der PK folgt, den obigen Überlegungen zufolge, einer uns unbekannten Wahrscheinlichkeitsverteilung 
$$
\begin{equation*}
P_{\omega\in\Omega} = \sum\limits_{\omega\in\Omega}\,\prod\limits_{k\in\omega}p_{k},
\end{equation*}
$$
die wir theoretisch ermitteln könnten, wenn wir allen möglichen Prozessketten $\omega\in\Omega$ folgen würden, die zur Erzeugung eines Primärelektrons an der PK führen können. Diese Annahme ist allerdings wirklich nur theoretischer Natur, da die Anzahl an $\omega$ sehr, wenn nicht gar unendlich groß ist. Wir müssen uns also damit begnügen, dass die Kenntnis von $P_{\omega\in\Omega}$ für uns unerreichbar ist. Wir stellen jedoch fest, dass $P_{\omega\in\Omega}$ für alle $e_{i}$ gleich ist. Weiterhin ordnen wir $P_{\omega\in\Omega}$, zur weiteren Charakterisierung, den Erwartungswert $\mu_{P}$ und die Standardabweichung $\sigma_{P}$ zu. 

Ein wichtiger Schritt in den weiteren Überlegungen ist, dass wir im folgenden nicht die Wahrscheinlichkeit für das konkrete Auftreten $P_{\omega\in\Omega}(e_{i})$ eines bestimmten Primärelektrons $e_{i}$, sondern den Erwartungswert $\mu_{P}$ für das Auftreten eines Primärelektrons im Allgemeinen betrachten. In den folgenden Gleichungen taucht daher zwar der Erwartungswert $\mu_{P}$ auf, es handelt sich dabei aber um den Erwartungswert einer Wahrscheinlichkeit, die selbst ohne weiteres eine Zufallsvariable sein kann.

Das Signal an der PK setzt sich aus $N_{\mathrm{e}}$ Primärelektronen zusammen. Nach dem [Zentralen Grenzwertsatz](https://de.wikipedia.org/wiki/Zentraler_Grenzwertsatz) von Lindeberg-Lévy können wir davon ausgehen, dass die Summe aus $N_{\mathrm{e}}$ Einzelbeiträgen für $N_{\mathrm{e}}\gg0$ einer [Normalverteilung](https://de.wikipedia.org/wiki/Normalverteilung) mit
$$
\begin{equation}
\begin{split}
\mu_{N_{\mathrm{e}}}&=\sum\limits_{1}^{N_{\mathrm{e}}} \mu_{P} \\
\sigma_{N_{\mathrm{e}}} &= \sigma_{P}\,\sqrt{N_{\mathrm{e}}}
\end{split}
\end{equation}
$$
zustrebt. 

Beschränken wir uns auf die vollständige Absorption eines Strahls mono-energetischer Photonen $\gamma$ mit der Energie $E_{\gamma}$ ist aufgrund der statistischen Natur der Prozesse die der Messung zugrunde liegen klar, dass wir für $Q(E_{\gamma})$ keine $\delta$-Distribution erwarten können. Stattdessen erwarten wir eine Normalverteilung deren Erwartungswert wir mit $\mu_{Q}$ und deren Standardabweichung wir mit $\sigma_{Q}$ bezeichnen, und die wir beide aus der aufgenommenen Messreihe bestimmen können. 

Für den Zusammenhang mit $\mu_{N_{\mathrm{e}}}$ und $\sigma_{N_{\mathrm{e}}}$ gilt
$$
\begin{equation}
\mu_{Q}=C\,\mu_{N_{\mathrm{e}}}; \qquad \sigma_{Q} = C\,\sigma_{N_{\mathrm{e}}},
\end{equation}
$$
wobei mit $C$ allerdings noch ein weiterer uns unbekannter Kalibrationsfaktor auftaucht, mit dessen Hilfe wir z.B. $\mu_{N_{\mathrm{e}}}$ aus $\mu_{Q}$ bestimmen würden. Beachten Sie, dass $Q(E_{\gamma})$ primär aus den Kanälen des MCA bestimmt wird. In den Gleichungen **(2)** sind also zwei Gleichungen für die Bestimmung von $\mu_{N_{\mathrm{e}}}$ mit drei Unbekannten zusammengefasst. Können wir trotzdem etwas über $\mu_{N_{\mathrm{e}}}$ erfahren? Die Antwort lautet – ja, denn für den Grenzübergang $N_{\mathrm{e}}\gg0$ und $\mu_{P}\to0$ geht die Normalverteilung, die den Gleichungen **(1)** zugrunde liegt in die [Poisson-Verteilung](https://de.wikipedia.org/wiki/Poisson-Verteilung) über, für deren Standardabweichung bei vorgegebenem Erwartungswert $\mu_{N_{\mathrm{e}}}$ der Zusammenhang 
$$
\begin{equation}
\sigma_{N_{\mathrm{e}}}=\sqrt{\mu_{N_{\mathrm{e}}}}
\end{equation}
$$
gilt. Damit können wir $\sigma_{N_{\mathrm{e}}}$ als eine Unbekannte in den Gleichung **(2)** eliminieren und $\mu_{N_{\mathrm{e}}}$ wie folgt abschätzen:
$$
\begin{equation}
\begin{split}
&\frac{\mu_{Q}}{\sigma_{Q}} = \frac{C\,\mu_{N_{\mathrm{e}}}}{C\,\sigma_{N_{\mathrm{e}}}} = \frac{C\,\mu_{N_{\mathrm{e}}}}{C\,\sqrt{\mu_{N_{\mathrm{e}}}}} = \sqrt{\mu_{N_{\mathrm{e}}}};\\
&\\
&\mu_{N_{\mathrm{e}}} = \left(\frac{\mu_{Q}}{\sigma_{Q}}\right)^{2}.
\end{split}
\end{equation}
$$
Wir klären abschließend noch, warum $\sigma_{Q}$ durch $\mu_{N_{\mathrm{e}}}$ besimmt wird, während z.B. die Vervielfachung im SEV, trotz ihrer statistischen Natur, keine Rolle zu spielen scheint: 

Wir haben weiter oben diskutiert, dass im SEV eine Verstärkung des Signals an der PK von $\mu_{V}\approx10^{6}$ leicht erreicht werden kann. Wir stellen uns vor, dass $\mu_{V}$ Bestandteil des Kalibrationsfaktors $C$ aus den Gleichungen **(2)** ist. Die Varianz von $\mu_{V}$ kann mit 
$$
\begin{equation*}
\mathrm{var}[\mu_{V}] = \frac{\sigma_{V}^{2}}{\mu_{V}}
\end{equation*}
$$
abgeschätzt werden, wobei $\sigma_{V}$ einen festen Wert hat, der aus der Varianz von $\delta$ (siehe oben) abgeleitet werden kann. Die Anzahl der Dynoden im SEV ist ohne Unsicherheit vorgegeben. Dadurch kann $\mathrm{var}[\mu_{V}]$ gerade bei sehr großen Werten von $\mu_{V}$ als sehr klein angenommen werden. Die Fluktuationen in der Bestimmung von $Q(E_{\gamma})$ werden also durch die Stelle in der Auslesekette dominiert, in der die kleinsten Zählraten auftreten. Diese werden durch den anschließenden Verstärkungsprozess dann nur noch skaliert. Diese Überlegungen motivieren, warum für einen Photodetektor, wie wir ihn für diesen Versuch verwenden Szintillatormaterialien mit hoher Szintillationslichtausbeute und PK mit hoher Quanteneffizienz von primärer Bedeutung sind. 

### Eigenschaften des Gammaspektrums

Die schematische Darstellung eines zu erwartenden mit einem Photondetektor aufgezeichneten Spektrums für einen Strahl mono-energetischer Photonen mit der Energie $E_{\gamma}$ ist in **Abbildung 7** gezeigt:

<img src="../figures/GammaSpektrum.png" width="900" style="zoom:100%;" />

**Abbildung 7**: (Schematische Darstellung eines zu erwartenden mit einem Photondetektor aufgezeichneten Spektrums für einen Strahl mono-energetischer Photonen der Energie $E_{\gamma}$, nach [H. Kolanoski, N. Wermes *Teilchendetektoren* (DOI 10.1007/978-3-45350-6)](file:///home/rwolf/Downloads/978-3-662-45350-6-1.pdf).)

---

Es handelt sich dabei um ein Histogramm. Auf der $x$-Achse sind die Kanäle des MCPHA aufgetragen, auf der $y$-Achse die Häufigkeit, mit der ein Eintrag im entsprechenden Kanal aufgezeichnet wurde. Jeder Eintrag im Histogramm entspricht einer einzelnen Messung, ein Spektrum besteht also immer aus einer Vielzahl von Messungen. 

In der Abbildung sind die folgenden grundlegenden Eigenschaften eines Gammaspektrums klar zu erkennen:

- Der **Photopeak** bei $E_{\gamma}$ resultiert aus der vollständigen Absorption der nachgewiesenen Photonen. Wir erwarten eine Normalverteilung deren Erwartungswert mit $\mu_{Q}$ wir $E_{\gamma}$ zuordnen können.

- Einträge rechts des Photopeaks sind auf Energie-Depositionen mehrerer zeitgleich nachgewiesener Photonen (**pile-up**) zurückzuführen. 

- Das **Compton-Kontinuum** resultiert aus Ereignissen bei denen $\gamma$ ein Elektron aus dem Detektormaterial ausgelöst und dann den Detektor wieder verlassen hat. Die **Compton-Kante** entspricht dabei der Rückstreuung mit $\theta=180^{\circ}$. Die Compton-Kante ist für das Spektrum ebenso charakteristisch, wie der Photopeak. Sie befindet sich im Spektrum an der Position $Q(E^{\prime\,\mathrm{max}}_{\mathrm{e}})$, die nur von $E_{\gamma}$ und $m_{\mathrm{e}}$ abhängt.

- Einträge zwischen der Compton-Kante und dem Photopeak können durch **mehrfache Compton-Streuung** erklärt werden, nach der das gestreute Photon $\gamma'$ den Detektor schließlich verlässt. Würde $\gamma'$ den Detektor nicht verlassen würde die Messung zum Photopeak beitragen. 

- Ein weiteres charakteristisches Merkmal des gezeigten Spektrums ist ein Peak, der durch **Compton-Rückstreuung** entsteht. Dabei vollzieht $\gamma$ Compton-Streuung unter $180^{\circ}$, z.B. in einer den Detektor umgebenden Abschirmung. Das gestreute Photon $\gamma'$ wird daraufhin im Detektor aufgefangen und nachgewiesen, wo es die gesamte Energie $E'_{\gamma}(\theta=180^{\circ})$ in einem Photopeak deponiert.

In der Abbildung nicht gezeigt können für Photonen mit $E_{\gamma}\gtrsim10\,\mathrm{MeV}$, für die auch Paarbildung auftreten kann, noch zwei weitere charakteristische Peaks im Spektrum auftreten. Dabei wird das Positron aus der Paarbildung im Detektormaterial abgebremst und zerstahlt schließlich in zwei antiparallel auslaufende Photonen gleicher Energie $E'_{\gamma}=m_{\mathrm{e}}c^{2}$. Beim Auftreten des [**Single-Escape Peaks**](https://de.wikipedia.org/wiki/Escapelinie) entkommt eines dieser Photonen der Detektion; der Peak befindet sich an der Stelle
$$
\begin{equation*}
Q(E_{\mathrm{S.E.}}) = Q(E_{\gamma}-m_{\mathrm{e}}c^{2}),
\end{equation*}
$$
beim **Double-Escape Peak** entkommen beide Photonen der Detektion; der Peak befindet sich an der Stelle
$$
\begin{equation*}
Q(E_{\mathrm{S.E.}}) = Q(E_{\gamma}-2\,m_{\mathrm{e}}c^{2}).
\end{equation*}
$$


 Ihre erste Aufgabe bei diesem Versuch besteht darin, den Messaufbau mit $\gamma$-Stahlen bekannter Energie $E_{\gamma}$ zu kalibrieren, so dass Sie jedem Kanal eine entsprechende Energie zuordnen können.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Gammaspektroskopie)
