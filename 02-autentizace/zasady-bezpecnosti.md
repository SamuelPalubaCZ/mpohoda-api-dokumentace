# Zásady bezpečnosti

Při práci s API je třeba dodržovat následující bezpečnostní zásady:

## 1. Používejte pouze HTTPS

Přistupujte pouze přes HTTPS.

## 2. Chraňte autentizační data

Přístupová autentizační data se nesmí dostat do nepovolaných rukou.

## 3. Ověřte certifikát serveru

Subjekt je doména, na které API běží. Vystavitel je `Encryption Everywhere DV TLS CA - G1`.

```
Encryption Everywhere DV TLS CA - G1
```

> Pokud váš klient nezná SSL/TLS certifikát a odmítá se k API připojit, nevypínejte kontrolu certifikátu, ale aktualizujte seznam důvěryhodných certifikátů.
