# Průvodce použitím API klíče

## Krok 1: Vygenerování API klíče

1. Přihlaste se do aplikace [mPohoda](https://app.mpohoda.cz)
2. Přejděte do agendy **API** (Otevřené API)
3. V sekci "Přístup pomocí API klíče" klikněte na **Nový klíč**
4. Zadejte název klíče a potvrďte kliknutím na **Vytvořit**
5. Klíč se zobrazí v dialogovém okně - **uložte si ho**

> Po zavření dialogu nelze z bezpečnostních důvodů klíč znovu zobrazit.

## Krok 2: Použití API klíče

API klíč vložte do hlavičky každého požadavku:

```http
Api-Key: 4bef30e89dcd352e8371da053b16f0cf6faf27c31f780f52c3a3cb7604a81a85
```

## Příklad požadavku

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1"   -H "Api-Key: váš-api-klíč"
```

## Důležité upozornění

- API klíč je tajná informace - uchovejte ho na bezpečném místě
- Klíč je svázán s firmou a uživatelem, který ho vytvořil
- Odchodem uživatele z firmy dojde k zneplatnění klíče
