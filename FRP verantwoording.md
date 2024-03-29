### Verantwoording van Functioneel Programmeren Principes in de Code

#### Hogere-orde functies:
In mijn code heb ik het principe van hogere-orde functies toegepast door gebruik te maken van een timingdecorator genaamd `measure_execution_time`. Deze decorator stelt me in staat om de uitvoeringstijd van verschillende functies te meten zonder de oorspronkelijke code van die functies te wijzigen. Hierdoor kan ik de prestaties van mijn code analyseren en optimaliseren zonder de kernlogica te verstoren.

#### Pure functies:
Een belangrijk concept dat ik heb toegepast, is het gebruik van pure functies, met name in de bindingsklassen zoals `BME280`, `OPT3002`, en `Servo`. Deze klassen bevatten methoden die alleen afhankelijk zijn van hun invoer en geen bijwerkingen hebben buiten het retourneren van resultaten. Door deze pure functies te gebruiken, wordt mijn code eenvoudiger te begrijpen, te testen en te onderhouden. Het voorkomt onverwachte neveneffecten en maakt de code voorspelbaarder.

#### Functiecompositie:
Hoewel ik niet expliciet functiecompositie heb genoemd, heb ik het concept toegepast in de opbouw van de hoofdlogica in mijn `main.py`. Ik heb de hoofdlogica opgedeeld in kleinere, afzonderlijke stappen, waarbij elke stap een specifiek onderdeel van het systeem behandelt. Door deze stappen vervolgens samen te voegen, definieer ik het algehele gedrag van het systeem. Dit maakt mijn code modulair en flexibel, waardoor het gemakkelijk is om wijzigingen aan te brengen zonder de hele logica te verstoren.

#### Verantwoording:
- **Hogere-orde functies**: Door de timingdecorator te gebruiken, kan ik de prestaties van mijn code meten zonder de functies zelf te wijzigen. Dit stelt me in staat om efficiëntieverbeteringen aan te brengen zonder de kernfunctionaliteit van mijn programma te verstoren.

- **Pure functies**: De bindingsklassen zijn ontworpen als pure functies, wat betekent dat ze voorspelbaar gedrag vertonen en geen onverwachte neveneffecten hebben. Hierdoor wordt mijn code gemakkelijker te begrijpen, te testen en te onderhouden, wat bijdraagt aan de algehele kwaliteit van mijn software.

- **Functiecompositie**: Door de hoofdlogica modulair op te bouwen, maak ik mijn code flexibel en gemakkelijk aanpasbaar. Dit zorgt ervoor dat mijn code goed georganiseerd is en dat ik wijzigingen kan aanbrengen zonder de samenhang van het systeem te verstoren. Dit draagt bij aan een beter onderhoudbare en schaalbare codebase.

Deze functionele programmeerprincipes hebben bijgedragen aan de kwaliteit en onderhoudbaarheid van mijn code, waardoor ik een gestructureerde aanpak kon volgen bij het ontwerpen van mijn regelsysteem.
