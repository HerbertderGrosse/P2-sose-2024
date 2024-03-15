# Hinweise für den Versuch Gammaspektroskopie

## Wechselwirkung von Photonen mit Materie

Es gibt drei Arten, auf die ein Photon $\gamma$ mit der Energie $E_{\gamma}$ mit Materie in Wechselwirkung treten kann: 

- [**Photoeffekt**](https://de.wikipedia.org/wiki/Photoelektrischer_Effekt): Das Photon trifft auf ein Elektron aus der Atomhülle des Materials, überträgt dabei seine gesamte Energie und wird voll absorbiert. Der Energieübertrag erfolgt zunächst virtuell. Die erneute Reaktion des Elektrons mit dem elektromagnetischen Feld, z.B. eines Atomkerns stellt Energie- und Impulserhaltung im Endzustand der Reaktion sicher. Das Elektron wird aus der Atomhülle ausgeschlagen und bewegt sich zunächst als freie Ladung durch das Material. 
- [**Compton-Effekt**](https://de.wikipedia.org/wiki/Compton-Effekt): Auch in diesem Fall erfolgt der Impulsübertrag zwischen $\gamma$ und Elektron zunächst virtuell, das ausgeschlagene Elektron emittiert unmittelbar ein neues Photon $\gamma^{\prime}$ mit der Energie $E'_{\gamma}\lt E_{\gamma}$. Dieser Prozess kann als elastischer Stoßprozess zwischen Elektron und Photon angesehen werden. Es handelt sich jedoch nicht um einen elastischen Stoßprozess im klassischen Sinne, sondern um einen Prozess der [Quantenelektrodynamik](https://de.wikipedia.org/wiki/Quantenelektrodynamik) (QED), bei dem $\gamma$ zerstört und $\gamma^{\prime}$ erzeugt wird.
- [**Paarbildung**](https://de.wikipedia.org/wiki/Paarbildung_(Physik)): In diesem Fall zerfällt $\gamma$ in ein Elektron-Positron-Paar. Aus Gründen der Energie- und Impulserhaltung ist dieser Prozess nur oberhalb der kinematischen Schwelle von $E_{\gamma}\gtrsim 2\,m_{\mathrm{e}}c^{2}$ und ebenfalls nur im elektromagnetischen Feld, z.B. eines Atomkerns möglich.

Die Häufigkeit, mit der jeweils einer der oben genannten Prozesse stattfindet wird durch die Wirkungsquerschnitte $\sigma_{\mathrm{P.E.}}$ (für Photoeffekt), $\sigma_{\mathrm{C.E.}}$ (für Compton-Effekt) und $\sigma_{\mathrm{pair}}$ (für Paarbildung) quantifiziert. In **Abbildung 2** sind die drei Reaktionen schematisch dargestellt:

<img src="../figures/Wechselwirkungen.png" width="900" style="zoom:100%;" />

**Abbildung 2** (Schematische Darstellung des (links) Photon-, (mitte) Compton- und (rechts) Paarbildungseffekts. Das Kreuz symbolisiert jeweils die Wechselwirkung mit dem elektromagnetischen Feld, z.B. eines Atomkerns)

---

Elektronen sind durch gerade Linien mit Pfeilen und Photonen durch Wellenlinien dargestellt. In den jeweiligen Diagrammen sind die einlaufenden Teilchen links und die auslaufenden Teilchen rechts dargestellt. Linien, die kein freies Ende haben gelten als virtuell, d.h. sie verletzen im Rahmen der Heisenbergschen Unschärferelation kurzfristig Energie- und Impulserhaltung. Das Kreuz symbolisiert jeweils die Wechselwirkung mit dem elektromagnetischen Feld, z.B. eines Atomkerns. 

Im linken Diagramm (für den Photoeffekt) läuft das Photon $\gamma$ von links in die Reaktion ein und trifft auf ein quasifreies Elektron. Durch die unmittelbare Wechselwirkung des Elektrons mit dem elektromagnetischen Feld, z.B. eines Atomkerns sind Energie- und Impulserhaltung im Endzustand der Reaktion sichergestellt. Das Elektron läuft schließlich auf der rechten Seite  des Diagramms aus der Reaktion aus. 

Im mittleren Diagramm (für den Compton-Effekt) läuft das Photon $\gamma$ von links in die Reaktion ein und trifft auf ein quasifreies Elektron. Das Elektron strahlt das Photon $\gamma'$ ab und läuft ebenso, wie $\gamma'$ auf der rechten Seite des Diagramms aus der Reaktion aus.

Im rechten Diagramm (für die Paarbildung) zerfällt das von links einlaufende Photon $\gamma$ in ein Elektron-Positron-Paar. Das Elektron koppelt unmittelbar an das elektromagnetische Feld, z.B. eines Atomkerns, wodurch Energie- und Impulserhaltung im Endzustand sichergestellt sind. Danach laufen das Elektron und das Positron auf der rechten Seite des Diagramms aus der Reaktion aus. 

Im Folgenden gehen wir auf die einzelnen Prozesse etwas näher ein. 

### Photoeffekt

Beim Photoeffekt geht $E_{\gamma}$ vollständig auf das gestreute Elektron über. Dieser Effekt ist nur im elektrischen Feld, z.B. eines Atomkerns, möglich. Der Atomkern nimmt dabei als Rückstoßpartner zusätzlichen Impuls aus der Reaktion auf, so dass im Endzustand der Reaktion Energie- und Impulserhaltung gewährleistet sind. Dies ist umso leichter möglich, je stärker das Elektron an den Atomkern gebunden ist, weshalb der Photoeffekt hauptsächlich mit Elektronen aus der K- und L-Schale von Atomen mit großer Kernladungszahl $Z$ auftritt. Die vollständige theoretische Beschreibung dieses Prozesses über den gesamten Energiebereich ist schwierig und auf Näherungen angewiesen. Die Abhängigkeit von $\sigma_{\mathrm{P.E.}}$ von $Z$ und $E_{\gamma}$ beträgt 
$$
\begin{equation*}
\sigma_{\mathrm{P.E.}}(E_{\gamma}, Z)\propto\frac{Z^{n}}{E_{\gamma}^{m}}; \qquad \text{mit: } n=4\ldots5; \, m\leq 3.5,
\end{equation*}
$$
weshalb der Photoeffekt gerade bei kleinen Werten von $E_{\gamma}$ und großen Werten von $Z$ dominiert. Für $E_{\gamma}\gg m_{\mathrm{e}}c^{2}$ gilt $m\to 1$, $\sigma_{\mathrm{P.E.}}$ fällt also mit zunehmener Energie der Photonen weniger stark ab.

Im Material erfolgt die Absorption durch Photoeffekt nicht durch eine einzige Reaktion sondern in schnell aufeinander folgenden Schritten: Das Photon $\gamma$ schlägt ein Elektron, z.B. aus der K-Schale eines Atoms aus; dieses verliert Energie durch Ionisation oder Bremsstrahlung, d.h. Emission eines weiteren Photons $\gamma'$ niedrigerer Energie $E'_{\gamma}\lt E_{\gamma}$. Die Lücke in der K-Schale des Atoms wird, z.B. durch ein Elektron aus einer höheren Schale aufgefüllt, wobei wiederum ein Photon $\gamma^{\prime\prime}$ mit $E_{\gamma}^{\prime\prime}\ll E_{\gamma}$ emittiert wird. Aufgrund der niedrigeren Energien $E_{\gamma}^{\prime}$ und $E_{\gamma}^{\prime\prime}$ steigt die Wahrscheinlichkeit für den Photoeffekt für $\gamma'$ und $\gamma^{\prime\prime}$, wodurch eine Absorptionskaskade in Gang gesetzt wird, bis $E_{\gamma}$ vollständig auf Elektronen übertragen wurde.

### Compton-Effekt

Der Compton-Effekt ist der dominierende Wechselwirkungsprozess von Photonen im Energiebereich von $E_{\gamma}=100\,\mathrm{keV}$ bis $10\,\mathrm{MeV}$ mit Materie. Er wurde 1922 erstmals von [Arthur Compton](https://de.wikipedia.org/wiki/Arthur_Holly_Compton) nachgewiesen, erklärt und untersucht. Compton stellte fest, dass bei der Streuung von Röntgenstrahlung an Graphit, die Wellenlänge $\lambda'$ des gestreuten Lichts größer als die Wellenlänge $\lambda$ des eingestrahlten Lichts ist. Für die Änderung der Wellenlänge gilt der einfache Zusammenhang: 
$$
\begin{equation*}
\begin{split}
&\Delta\lambda=\lambda'-\lambda = \frac{h}{m_{\mathrm{e}}\,c}\left(1-\cos\theta\right);\\
&\\
&\text{with:} \\
&\\
&\lambda_{\mathrm{C}} = \frac{h}{m_{\mathrm{e}}\,c}.
\end{split}
\end{equation*}
$$
Dabei bezeichnet $\lambda_{\mathrm{C}}$ die sogenannte Compton-Wellenlänge und $\theta$ den Streuwinkel (im Laborsystem). Es ist bemerkenswert, dass der Energieübertrag des einlaufenden Photons, der zu $\Delta\lambda$ korrespondiert, nur von $\theta$ und nicht von $E_{\gamma}$ abhängt. Er wird bei der Rückstreuung des einlaufenden Photons (d.h. für $\theta=180^{\circ}$) maximal. Die Energie $E'_{\mathrm{e}}$ des gestreuten Elektrons und die Energie $E'_{\gamma}$ des gestreuten Photons lassen sich unter der Annahme, dass es sich um eine elastische Zwei-Körper-Streuung des Photons (mit $E_{\gamma}=h\,\nu$ und $p_{\gamma}=h/\lambda$) an einem ruhenden freien Elektron (mit $E_{\mathrm{e}}=m_{\mathrm{e}}c^{2}$ und $p_{\mathrm{e}}=0$) handelt, quasi-klassisch berechnen: 
$$
\begin{equation}
\begin{split}
&E'_{\gamma}(\theta) = \frac{E_{\gamma}}{1+\frac{E_{\gamma}}{E_{\mathrm{e}}}\left(1-\cos\theta\right)};
\qquad
E'_{\mathrm{e}}(\theta) = E_{\gamma}-E'_{\gamma}(\theta).\\
&\\
&E^{\prime\,\mathrm{max}}_{\mathrm{e}} = E^{\prime}_{\mathrm{e}}(\theta=180^{\circ}) = \frac{E_{\gamma}}{1+\frac{E_{\mathrm{e}}}{2\,E_{\gamma}}},\\
\end{split}
\end{equation}
$$
wobei $E^{\prime\,\mathrm{max}}_{\mathrm{e}}$ die Energie des Elektrons nach maximalem Energieübertrag ist. Diesen Punkt im Spektrum der gestreuten Elektronen bezeichnet man als Compton-Kante. Zu niedrigen Energien hin schließt sich das sog. Compton-Kontinuum, an die Compton-Kante an. 

Zwar stimmen die auf quasi-klassischem Wege bestimmten Beziehungen für $E'_{\mathrm{e}}(\theta)$ und $E'_{\gamma}(\theta)$ "zufällig" mit den im Rahmen der QED gewonnenen Ergebnissen überein, der exakte Verlauf des Spektrums lässt sich jedoch erst mit Hilfe des [Klein-Nishina-Wirkungsquerschnitts](https://de.wikipedia.org/wiki/Klein-Nishina-Wirkungsquerschnitt) vollständig verstehen. Eine schematische Darstellung des erwarteten Energiespektrums für die Compton-Streuung eines Photons mit $E_{\gamma}$ ist in **Abbildung 4** gezeigt: 

<img src="../figures/ComptonSpektrum.png" width="900" style="zoom:100%;" />

**Abbildung 4** (Schematische Darstellung des erwarteten Energiespektrums für die Compton-Streuung eines Photons mit $E_{\gamma}$. Die vertikale Linie rechts im Bild markiert die vollständige Absorption des Photons im Detektor, z.B. durch den Photoeffekt. Für das Compton-Kontinuum sind die verläufe für zwei unterschiedliche Energien $E_{\gamma}$ des einlaufenden Photons skizziert)

---

Auf der $x$-Achse ist die Energie $E'_{\mathrm{e}}$, auf der $y$-Achse der Wirkungsquerschnitt $\mathrm{d}\sigma_{\mathrm{C.E.}}/\mathrm{d}E'_{\mathrm{e}}$  aufgetragen. Die vertikale Linie rechts im Bild markiert die vollständige Absorption des Photons im Detektor, z.B. durch den Photoeffekt.  

Die Abhängigkeit von $\sigma_{\mathrm{C.E.}}$ von $Z$ und $E_{\gamma}$ beträgt 
$$
\begin{equation*}
\sigma_{\mathrm{C.E.}}(E_{\gamma}, Z)\propto\frac{Z}{E_{\gamma}}; \qquad \text{f\"ur: } E_{\gamma}\gg m_{\mathrm{e}}c^{2}.
\end{equation*}
$$

### Paarbildung

Aus Gründen der Energie- und Impulserhaltung ist dieser Prozess nur oberhalb der kinematischen Schwelle von $E_{\gamma}\gtrsim 2\,m_{\mathrm{e}}c^{2}$ und auch nur im elektrischen Feld, z.B. eines Atomkerns möglich. Erstmals wurde dieser Prozess 1934 von Hans Bethe und Walter Heitler gemeinsam mit dem Prozess der Bremsstrahlung (zu dem der Prozess der Paarbildung sehr ähnlich ist) beschrieben und erklärt, weshalb beide Prozesse auch als Bethe-Heitler-Prozesse bezeichnet werden. 

Die Abhängigkeit von $\sigma_{\mathrm{pair}}$ von $Z$ beträgt 
$$
\begin{equation*}
\sigma_{\mathrm{pair}}(E_{\gamma}, Z)\propto Z^{2}.
\end{equation*}
$$
Für $E_{\gamma}\gg m_{\mathrm{e}}c^{2}$ ist $\sigma_{\mathrm{pair}}$ unabhängig von $E_{\gamma}$. Die Paarbildung erfolgt insbesondere für schwere Kerne in erster Linie im hohen elektrischen Feld des Atomkerns; das elektrische Feld der Elektronen in der Atomhülle spielt nur bei sehr leichten Elementen eine Rolle. 

Im Material wird das Positron abgebremst, bis es mit einem Elektron aus dem Material rekombiniert und über den Prozess der [Elektron-Positron-Annihiliation](https://de.wikipedia.org/wiki/Annihilation) zerstrahlt. Aus dieser Reaktion gehen zwei, zueinander anti-parallel auslaufende Photonen mit der charakteristischen Energie $E_{\gamma}=m_{\mathrm{e}}c^{2}$ hervor, die selbst wieder mit dem Material in Wechselwirkung treten.

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Kreisel) | [Weiter](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/tree/main/Kreisel/doc/Hinweise-Aufgabe-1-a.md)

