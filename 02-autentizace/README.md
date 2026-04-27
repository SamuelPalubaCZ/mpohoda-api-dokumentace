# Autentizace

## Obsah

- [Zásady bezpečnosti](zasady-bezpecnosti.md)
- [Způsoby autentizace](zpusoby-autentizace.md)
- [Chyby autentizace](chyby-autentizace.md)

## Přehled

API pracuje s uživatelskými daty, proto jej nelze používat bez autentizace.

Autentizace se pro jednotlivé uživatele firmy v aplikaci mPohoda spravuje v [agendě API](https://app.mpohoda.cz/otevrene-api). Právo na vytvoření nového přístupového kódu má pouze administrátor firmy.

Vygenerovaný autentizační kód je svázán s firmou, ve které byl vygenerován, a uživatelem, který jej vytvořil. V požadavcích tedy není potřeba identifikaci uživatele či firmy žádným dalším způsobem specifikovat.

> Odchodem uživatele z firmy dojde k zneplatnění přístupových údajů a nelze je nadále používat. V případě odebrání administrátorských práv uživateli se uplatňují na API přístupová práva dle nastavení daného uživatele.
