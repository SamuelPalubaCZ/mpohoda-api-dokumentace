---
name: mpohoda-api-autentizace
description: |
  Autentizace pro mPohoda API - API klíč, OAuth2 token, zásady bezpečnosti.
  Použij tento skill při dotazech na přihlášení, přístupové údaje, 
  API klíč, token, OAuth2, Client Credentials, ucet.pohoda.cz.
---

# mPohoda API - Autentizace

## Přehled

API pracuje s uživatelskými daty, proto jej nelze používat bez autentizace.

Autentizace se pro jednotlivé uživatele firmy v aplikaci mPohoda spravuje v 
[agendě API](https://app.mpohoda.cz/otevrene-api). Právo na vytvoření nového 
přístupového kódu má pouze **administrátor firmy**.

Vygenerovaný autentizační kód je svázán s firmou, ve které byl vygenerován, 
a uživatelem, který jej vytvořil. V požadavcích tedy není potřeba identifikaci 
uživatele či firmy žádným dalším způsobem specifikovat.

> **Důležité:** Odchodem uživatele z firmy dojde k zneplatnění přístupových 
> údajů a nelze je nadále používat. V případě odebrání administrátorských 
> práv uživateli se uplatňují na API přístupová práva dle nastavení daného 
> uživatele.

---

## Způsoby autentizace

API mPohoda podporuje **dva způsoby autentizace**:

### 1. API klíč (jednodušší)

API klíč je unikátní identifikátor sloužící k identifikaci uživatele a firmy. 
Jedná se o **tajnou informaci** a je tedy nutné ho uchovat na bezpečném místě, 
podobně jako např. hesla.

#### Použití v hlavičce

```http
Api-Key: 4bef30e89dcd352e8371da053b16f0cf6faf27c31f780f52c3a3cb7604a81a85
```

| Název | Typ | Popis |
|-------|-----|-------|
| `Api-Key` | string | API klíč vygenerovaný v agendě API |

#### Vygenerování API klíče

1. Přihlaste se do [mPohoda](https://app.mpohoda.cz) jako administrátor
2. Otevřete agendu **API**
3. Klikněte na tlačítko **Nový klíč** v sekci "Přístup pomocí API klíče"
4. Zadejte název klíče a potvrďte
5. **Klíč se zobrazí jednou** — uložte ho na bezpečné místo

> **Upozornění:** Po zavření dialogu nelze z bezpečnostních důvodů klíč znovu zobrazit.

---

### 2. Přístupový token (OAuth2) — DOPORUČENO

Přístupový token rovněž slouží k identifikaci uživatele a firmy, jeho platnost 
je však **časově omezená**. Klient obdrží token po úspěšné autentizaci na 
autentizačním serveru, s využitím **OAuth2 Client Credentials Grant Type**.

> **Doporučení:** Z hlediska větší bezpečnosti doporučujeme použít přístup 
> pomocí přístupového tokenu.

#### Použití v hlavičce

```http
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
```

| Název | Typ | Popis |
|-------|-----|-------|
| `Authorization` | string | Token ve tvaru `Bearer {token}` |

#### Vygenerování klienta (Client ID + Client Secret)

1. Přihlaste se do [mPohoda](https://app.mpohoda.cz) jako administrátor
2. Otevřete agendu **API**
3. Klikněte na tlačítko **Nový klient** v sekci "Přístup pomocí přístupového tokenu"
4. Zadejte název klienta a potvrďte
5. **Client ID a Client Secret se zobrazí jednou** — uložte je

> **Upozornění:** Po zavření dialogu nelze z bezpečnostních důvodů Client Secret znovu zobrazit.

#### Získání tokenu z autentizačního serveru

```bash
curl -X POST "https://ucet.pohoda.cz/connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=váše-client-id" \
  -d "client_secret=váš-client-secret" \
  -d "scope=Mph.OpenApi.Access.Cz"
```

#### Parametry požadavku na token

| Parametr | Typ | Popis |
|----------|-----|-------|
| `grant_type` | string | `client_credentials` |
| `client_id` | string | Client Id z agendy API |
| `client_secret` | string | Client Secret z agendy API |
| `scope` | string | `Mph.OpenApi.Access.Cz` |

#### Odpověď s tokenem

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```

> **Upozornění:** Token má omezenou platnost (výchozí 3600 sekund = 1 hodina). 
> Po vypršení platnosti nelze token nijak obnovit a je potřeba získat nový.

---

## Zásady bezpečnosti

Při práci s API je třeba dodržovat následující bezpečnostní zásady:

1. **Přistupujte pouze přes HTTPS** — Nikdy neposílejte autentizační údaje přes HTTP
2. **Chraňte přístupová data** — API klíč, Client ID a Client Secret nesmí dostat do nepovolaných rukou
3. **Ověřte certifikát serveru** — Subjekt je doména api.mpohoda.cz, vystavitel je "Encryption Everywhere DV TLS CA - G1"

> **Upozornění:** Pokud váš klient nezná SSL/TLS certifikát a odmítá se k API 
> připojit, nevypínejte kontrolu certifikátu, ale aktualizujte seznam důvěryhodných 
> certifikátů.

---

## Chyby autentizace

| Kód HTTP | Chyba | Popis |
|----------|-------|-------|
| 401 | Unauthorized | Chybí autentizační údaj nebo je neplatný |
| 403 | Forbidden | Uživatel nemá právo provést danou operaci |

### Typické příčiny 401

- Chybí hlavička `Api-Key` nebo `Authorization`
- API klíč je neplatný nebo zneplatněn
- Token vypršel (je třeba získat nový)
- Uživatel byl odebrán z firmy

### Typické příčiny 403

- Uživatel není administrátor a nemá právo vytvářet/mažovat záznamy
- Uživatel nemá přístup k dané agendě v mPohoda

---

## Rychlé odkazy

- [Hlavní skill](../SKILL.md) — Přehled celého API
- [Endpointy](../references/endpointy.md) — Seznam všech API metod
- [Průvodci](../references/pruvodci.md) — Jak začít s API
- [SDK](../references/sdk.md) — C# SDK pro autentizaci

---

**Synchronizováno s:** api.mpohoda.cz/doc/guides/quick-start  
**Verze:** 1.0.0
