
### 📌 **Shrnutí poznatků**

Bellman-Fordův algoritmus:

* Je univerzální algoritmus pro hledání nejkratší cesty z jednoho vrcholu ke všem ostatním.
* Na rozdíl od Dijkstrova algoritmu si poradí i s **negativními hranami**.
* Jeho hlavní princip je **relaxace hran** – postupně zlepšuje odhady vzdáleností.
* Umí také detekovat **záporný cyklus**, což je důležité v grafových aplikacích, kde by cyklické zisky (nebo chyby) mohly způsobit nekonečné smyčky.

### 🔍 **Možnosti rozšíření**

* **A\*** – chytrý algoritmus pro hledání cesty v grafech, který používá heuristiku (např. vzdálenost vzdušnou čarou).
* **Johnsonův algoritmus** – umí efektivně najít nejkratší cesty **mezi všemi dvojicemi vrcholů**, i když graf obsahuje negativní hrany (pokud nemá záporné cykly).
* **Grafové knihovny** – místo ruční implementace můžeš později zkusit knihovny jako `networkx` (Python), které umí grafy vizualizovat i analyzovat.
