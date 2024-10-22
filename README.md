Programmering

Denne obligen består av 2 programmeringsoppgaver, som først blir kort og overordnet omtalt i teksten under. LES DETTE:

I oppgave 1 skal du jobbe bittelitt med klasser, objekter og metoder. Denne oppgaven går ikke noe dypere enn de vi vil gå gjennom i forelesning, så benytt den som referanse. Vi vil generelt også anbefale å løse denne oppgaven så fort som mulig slik at du kan benytte mest mulig tid på oppgave 2, som er betydelig mer krevende.

I oppgave 2 vil du jobbe med de fleste av konseptene du har lært om hittil og benytte dem for å lage et litt større program enn det du har gjort i tidligere obliger. Det er en del tekst i oppgavebeskrivelsen, og dette er for å beskrive de fleste detaljene du må ta hensyn til. Denne oppgaven ER utfordrende og er designet for å tvinge deg til å tenke om programmering på et høyere nivå enn konseptene individuelt. Dermed, beregn GOD TID til å løse oppgave 2 og jobb med den jevnlig. Du klarer ikke å løse denne på en eller to dager, så start med en gang. Bruk øvingstimene godt for veiledning!

 

Oppgave 1 - Klasser og objekter

A)

Opprett en klasse for filmer med inneholder instansvariabler for filmtittel, utgivelsesår og score.  

Bruk denne klassen til å opprette et objekt for hver av de følgende filmene: 

    Inception - Utgivelsesår: 2010, Score: 8.8 
    The Martian - Utgivelsesår: 2015, Score: 8.0 
    Joker - Utgivelsesår: 2019, Score: 8.4 

 

Skriv ut all informasjon om hver film med formatet; "title was released in year and currently has a score of score", ved å benytte de opprettede objektene. 

 B) Metoder 

Opprett en metode i filmklassen som returnerer en tekststreng med all informasjon om en gitt film på samme format som i forrige deloppgave. Igjen, skriv ut all informasjon om filmobjektene opprettet i forrige deloppgave, men denne gangen ved å benytte den nylig opprettede metoden. 

 

Oppgave 2 - Blackjack

Fremgangsmåter

For denne oppgaven kan du velge mellom 2 fremgangsmåter (begge er like gyldige, men det er anbefalt å ta utgangspunkt i fremgangsmåte A for å få "best" læringsutbytte, og eventuelt bytte til fremgangsmåte B senere):

A. Forsøke å løse oppgaven på egenhånd, kun basert på "kravene" definert i oppgavebeskrivelsen under. Det er anbefalt å gjøre et forsøk på denne fremgangsmåten, ettersom man da må vurdere hva som skal implementeres generelt, hva hvordan man stegvis skal gå frem for å komme i mål. Hint: Start med de mest essensielle bitene av programmet. Deretter utvid med "kulere" funksjonalitet.

B. Hvis du synes fremgangsmåte A er for utfordrende, eller om du setter deg fast underveis og trenger et hint, har vi også delt opp i mer detaljerte og iterative oppgaver, som stegvis leder frem til en komplett løsning:

  --Oblig 4 - Oppgave 2B - BlackJack - detaljerte og iterative oppgaver--

 

Oppgavebeskrivelse, 2A

Blackjack er et gamblingbasert kortspill med et relativt enkelt premiss. En gitt spiller spiller mot en dealer, hvor målet er å ha en kort-hånd som er verdt mer enn dealerens, uten at håndens verdien er over 21. I konteksten av denne oppgaven er kortene baserte på èn vanlig kortstokk med 52 kort. Altså 4 av hver kortverdi. Typen kort (hjerte, kløver, spar, ruter) har ingen betydning i Blackjack. Kun kortenes verdi. Kortverdiene for forskjellige kort er som følger: 

    2 til 10 --> verdt tilsvarende kortets tall
    Billedkort (J, Q, K) --> alle er individuelt verdt 10 
    Ess --> verdt enten 1 eller 11, avhengig av hånden - Tallet som er mest fordelaktig, gjelder. 

 

I blackjack er det 4 mulige utfall: 

    Spilleren vinner --> Spilleren tjener like mange chips som spesifisert i innsatsen 
    Dealeren vinner --> Spilleren mister like mange chips som spesifisert i innsatsen.
    Ingen vinner --> Spillerens chips forblir det samme som før innsatsen 
    Blackjack --> Spilleren tjener 2 x antallet chips spesifisert i innsatsen 

 

De 4 utfallene forekommer ut ifra spill-flyten, som beskrives under:

Spilleren starter enhver runde med Blackjack med å oppgi en innsats av sine chips. Spilleren må oppgi en innsats som er høyere enn 0, men kan ikke være høyere enn det totale antallet chips spilleren har.

Spilleren og dealeren får så tildelt 2 kort hver, tilfeldig trukket fra kortstokken (kortene blir tatt ut av stokken). Spilleren kan se sine egne kort, men bare ett av dealerens kort.
Hvis spillerens initielle kort har en sammenlagt verdi av 21 (kombinasjonen av et Ess og et kort som er verdt 10) kalles dette en "blackjack", og spilleren vinner automatisk. I dette tilfellet tjener spilleren 2 ganger innsatsen av chips. Hvis den initielle trekningen ikke resulterer i en "blackjack", vil spilleren få et valg mellom det som kalles "Hit" eller "Stand": 

    Hit --> Spilleren får et nytt kort, tilfeldig trukket fra stokken, lagt til i hånden sin. 
    Stand --> Spilleren velger å låse hånden sin slik den nå er 

Spilleren vil iterativt fortsette å ha å muligheten til å velge mellom Hit eller Stand helt til spilleren velger Stand, eller hvis håndens verdi har gått over 21 som resultatet av en Hit. Hvis håndens verdi går over 21 kalles dette at spilleren har "Bustet" og dealeren vinner automatisk, som medfører at spillerens innsats blir tapt.

Derimot hvis spilleren ikke har blitt Bustet og velger Stand, vil dealeren iterativt trekke ett kort av gangen helt til han/hennes håndverdi er større enn 17. Hvis dette medfører at dealeren får en håndverdi større enn 21, vil dealeren buste, som betyr at spilleren vinner og tjener samme antall chips som ble satset.

Hvis dealeren ikke buster, vil spillerens og dealerens håndverdi sammenlignes og den med høyeste håndverdi vil vinne. I motsetning, hvis håndverdiene er like, vinner ingen, og spilleren verken mister eller tjener chips.  

 

Det følgende er et eksempel av outputen av et spill av Blackjack (merk at utskriften av din kode ikke trenger å være helt likt dette): 

You currently have 7 chips. How many do you bet?: 2 

You bet 2 chips out of your 7 total. 

The cards have been dealt. You have a Eight of clubs and a Three of hearts, with a total value of 11. 

The dealers visible card is a Five of hearts, with a value of 5. 

Do you wish to hit or stand? 
1 - Hit 
2 - Stand
Answer: 1

You chose to Hit.

You have been dealt one card (5). Your hand now consists of the following cards: 
- Eight of clubs 
- Three of hearts 
- Five of diamonds
The total value of your hand is now 16, and the dealers' is 5. 

Do you wish to hit or stand?
1 - Hit
2 - Stand
Answer: 1 

You chose to Hit. 

You have been dealt one card (2). Your hand now consists of the following cards: 
- Eight of clubs 
- Three of hearts 
- Five of diamonds
- Two of clubs
The total value of your hand is now 18, and the dealers' is 5. 

Do you wish to hit or stand? 
1 - Hit 
2 - Stand 
Answer: 2 

You chose to Stand. 

The dealer draws cards until their hand value is greater than 17. The dealers cards are the following:
- Five of hearts 
- Six of hearts
- Three of spades 
- Four of diamonds 
The total value of the dealers hand is 18 compared to your hand's value; 18.

No one wins. You keep your chips, and your total amount remains 7.

Do you wish to play again? 
y - Yes 
n - No 
Answer: n

See you next time! :) 

Process finished with exit code 0
