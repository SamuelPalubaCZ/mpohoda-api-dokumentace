# Postman

## 1. Co je Postman?

Program Postman je jeden z populárních nástrojů pro testování API.

[Stáhnout program Postman](https://www.postman.com/downloads/)

## 2. Vytvoření nové kolekce a požadavku

V programu Postman se vytvořené požadavky ukládají do tzv. kolekcí. Novou kolekci i nový požadavek vytvoříte povelem **New** v menu **File** a následně zvolením požadované položky **Collection**, resp. **HTTP** v zobrazeném okně.

Volbou **HTTP** se založí nový požadavek, u kterého je nutné zadat název a vybrat kolekci, do které jej chcete zařadit.

> **Tip:** Novou kolekci můžete založit také přímo při vytváření nového požadavku.

> **Info:** Pro zjednodušení práce jsme pro vás připravili kolekci ke stažení se všemi dostupnými požadavky, kterou si můžete naimportovat do aplikace Postman.

## 3. Zadání autentizačního údaje k požadavku

Pro odesílání požadavků na API je nutné v hlavičce každého požadavku uvádět autentizační údaj - získaný token nebo API klíč. Api klíč je nutné vložit do hlavičky každého požadavku. Způsob získání těchto údajů je popsán v kapitole [Způsoby autentizace](../02-autentizace/zpusoby-autentizace.md) na stránce Obecné.

Abyste nemuseli v programu Postman způsob autentizace opakovaně zadávat do hlavičky každého požadavku, nastavte jej přímo u kolekce na záložce **Authorization** v poli **Type** vybráním jedné z možností **Bearer Token** nebo **API Key** a zadáním získaného tokenu, resp. API klíče.

### OAuth 2.0 token v Postmanu

Pokud chcete použít tokeny, umožňuje program Postman zjednodušený způsob získání nového tokenu a to konfigurací přímo v kolekci, kde na záložce **Authorization** zvolte možnost **OAuth 2.0** v poli **Type** a v poli **Add auth data to** nechte vybranou volbu **Request Headers**.

Poté v části **Configure New Token** vyplňte následující údaje:

| Pole | Hodnota |
|------|---------|
| **Token Name** | Vaše pojmenování tokenu |
| **Grant Type** | Client Credentials |
| **Access Token URL** | `https://ucet.pohoda.cz/connect/token` |
| **Client ID** | Client Id vygenerovaný v agendě API v aplikaci mPohoda |
| **Client Secret** | Client Secret vygenerovaný v agendě API v aplikaci mPohoda |
| **Scope** | `Mph.OpenApi.Access.Cz` |
| **Client Authentication** | Lze ponechat kteroukoliv z obou nabízených možností |

Kliknutím na tlačítko **Get New Access Token** se získaný token přidá do seznamu pole **Access Token** v části **Current Token**. Nový token vyberte v seznamu **Available Tokens**. Změny uložte pomocí tlačítka **Save**.

## 4. Metoda požadavku

U každého požadavku před jeho odesláním na API je nutné nastavit požadovanou HTTP metodu a zadat URL adresu.

## 5. Hlavička požadavku

V případě, že jste používaný způsob autentizace nezadali přímo na kolekci, uveďte jej na záložce **Headers**.

## 6. Tělo požadavku

Údaje, které mají být uvedeny na vytvářeném záznamu se uvádějí na záložce **Body**. Pro zápis je nutné nastavit mód **raw** a hodnotu **JSON** v rozbalovacím menu napravo od volby módu.

Obsah těla požadavku pro jednotlivé API metody je popsán v jednotlivých kapitolách na stránce Reference. Průvodce [Navázané záznamy](navazane-zaznamy.md) vás seznámí s tím, jak získat id záznamů, které chcete v požadavku využít.

## 7. Odpověď API

Hotový požadavek odešlete na API kliknutím na tlačítko **Send**.

Ve spodní části obrazovky se zobrazí odpověď API:
- **úspěšná operace** - vygenerovaná data
- **neúspěšná operace** - v sekci detail je uveden důvod

## 8. Kontrola dokladu v aplikaci mPohoda

Úspěšné vytvoření dokladu můžete následně provést i přímo v aplikaci mPohoda v příslušné agendě.
