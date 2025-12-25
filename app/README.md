# English Tutor Tracking API

Backendowy serwis wspierający **Custom GPT jako personalnego tutora języka angielskiego**.  
API służy wyłącznie do **długoterminowego trackingu postępów**, powtórek (SRS) oraz analizy błędów użytkownika.

Projekt jest zaprojektowany tak, aby:
- Custom GPT mógł **dynamicznie zapisywać i odczytywać dane** przez Actions
- model miał **ciągłość nauki między sesjami**
- system był prosty, skalowalny i framework-agnostic po stronie AI

---

## Główna idea

Custom GPT:
- prowadzi rozmowy i ćwiczenia
- analizuje błędy, płynność i zakres językowy
- **samodzielnie wywołuje Actions (HTTP)**, aby:
  - pobrać dane o postępach
  - zapisać wyniki sesji
  - zaktualizować kolejkę powtórek (SRS)

API:
- **nie zawiera logiki AI**
- odpowiada wyłącznie za:
  - przechowywanie danych
  - agregację statystyk
  - deterministyczną logikę SRS

---

## Zakres odpowiedzialności API

API odpowiada za:

1. **Tracking postępów**
   - historia sesji nauki
   - oceny (fluency, accuracy, range, clarity)
   - czas nauki i regularność

2. **Spaced Repetition System (SRS)**
   - przechowywanie elementów do nauki (słówka, frazy, gramatyka)
   - wyznaczanie dat kolejnych powtórek (`due_at`)
   - aktualizację harmonogramu na podstawie wyniku (correct / wrong)

3. **Error Bank**
   - agregacja powtarzających się błędów językowych
   - identyfikacja trendów (np. “articles”, “prepositions”)
   - dostarczanie danych do spersonalizowanego feedbacku

4. **Agregaty do decyzji dydaktycznych**
   - backlog powtórek
   - accuracy z ostatnich dni
   - top błędy w ostatnim okresie