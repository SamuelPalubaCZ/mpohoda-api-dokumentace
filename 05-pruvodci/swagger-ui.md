# Swagger UI

## 1. Co je Swagger UI?

Swagger je nástroj pro automatizované generování API dokumentace z OpenApi specifikace. Přehledně zobrazuje dostupné API metody a strukturu dat. Umožňuje rovněž interakci s API, včetně zadání podporovaných autentizačních údajů.

[Otevřít Swagger](https://api.mpohoda.cz/swagger/index.html)

## 2. Zadání autentizačního údaje

Aby bylo možné požadavky odesílat na API, je potřeba nejdříve zadat autentizační údaje.

Nad seznamem API metod se po kliknutí na tlačítko **Authorize** zobrazí dialogové okno, ve kterém v závislosti na používaném typu autorizace:
- v části **ApiKeyAuth** zapište API klíč, nebo
- v části **Oauth2** zadejte **Client Id** a **Client Secret** a zatrhněte volbu **Scope**.

Způsob získání autentizačních údajů je popsán v kapitole [Způsoby autentizace](../02-autentizace/zpusoby-autentizace.md) na stránce Obecné.

Nastavení potvrďte kliknutím na tlačítko **Authorize** a dialogové okno zavřete prostřednictvím tlačítka **Close**.

## 3. Odeslání požadavku na API

Vyhledejte požadovanou metodu, rozbalte její detail a následně klikněte na tlačítko **Try it out**.

V závislosti na API metodě vyplňte požadované údaje a požadavek odešlete na API příkazem **Execute**.

V případě POST metody je nutné před odesláním požadavku po kliknutí na tlačítko **Try it out** v části **Request body** zadat v těle požadavku data potřebná pro vygenerování výsledného záznamu.

## 4. Odpověď API

V části **Responses/Server response** se po vykonání požadavku zobrazí výsledná odpověď:
- **vygenerovaná data** - úspěšná operace
- **Error** - neúspěšná operace; v sekci **Response body** je uveden důvod
