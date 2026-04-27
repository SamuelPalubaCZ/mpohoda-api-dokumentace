# Průvodce použitím tokenu

## Přehled

Token získáte pomocí OAuth2 s Client Credentials Grant Type.

## Krok 1: Vygenerování klienta

1. Přihlaste se do aplikace [mPohoda](https://app.mpohoda.cz)
2. Přejděte do agendy **API** (Otevřené API)
3. V sekci "Přístup pomocí přístupového tokenu" klikněte na **Nový klient**
4. Zadejte název klienta a potvrďte kliknutím na **Vytvořit**
5. Zobrazí se **Client Id** a **Client Secret** - **uložte si je**

> Po zavření dialogu nelze z bezpečnostních důvodů Client Secret znovu zobrazit.

## Krok 2: Získání tokenu

```bash
curl -X POST "https://ucet.pohoda.cz/connect/token"   -H "Content-Type: application/x-www-form-urlencoded"   -d "grant_type=client_credentials"   -d "client_id=váše-client-id"   -d "client_secret=váš-client-secret"   -d "scope=Mph.OpenApi.Access.Cz"
```

### Odpověď:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```

## Krok 3: Použití tokenu

Token vložte do hlavičky Authorization:

```http
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
```

## Příklad požadavku s tokenem

```bash
curl -X GET "https://api.mpohoda.cz/v1/BusinessPartners?pageSize=10&pageNumber=1"   -H "Authorization: Bearer váš-token"
```

## Důležité upozornění

- Client Secret je tajná informace - uchovejte ho na bezpečném místě
- Token má omezenou platnost (expires_in sekund)
- Před vypršením platnosti je nutné získat nový token
- Tento typ autentizace je vhodný pro serverové aplikace
