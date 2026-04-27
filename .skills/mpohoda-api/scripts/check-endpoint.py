#!/usr/bin/env python3
"""
mPohoda API - Kontrola endpointu
===============================
Kontroluje dostupnost a odpověď mPohoda API endpointů.

Použití:
    python check-endpoint.py --endpoint IssuedInvoices --method GET --api-key "váš-klíč"
    python check-endpoint.py --endpoint BusinessPartners --method GET --token "váš-token"
    python check-endpoint.py --endpoint IssuedInvoices --method POST --token "váš-token" --data '{"IssueDate": "2024-01-15", ...}'
    
Návratové kódy:
    0 - Endpoint je dostupný a odpověď je OK
    1 - Chyba spojení nebo neplatná odpověď
    2 - Chyba autentizace (401/403)
    3 - Chyba validace (400/422)
    4 - Endpoint nenalezen (404)
"""

import json
import sys
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlencode


BASE_URL = "https://api.mpohoda.cz/v1"


def check_endpoint(
    endpoint: str,
    method: str = "GET",
    api_key: str = None,
    token: str = None,
    data: dict = None,
    params: dict = None,
    verbose: bool = False
) -> dict:
    """
    Kontroluje dostupnost endpointu.
    
    Args:
        endpoint: Název endpointu (např. "IssuedInvoices")
        method: HTTP metoda (GET/POST/PUT/DELETE)
        api_key: API klíč pro autentizaci
        token: Bearer token pro autentizaci
        data: JSON data pro POST/PUT
        params: Query parametry pro GET
        verbose: Podrobný výstup
        
    Returns:
        Dict s výsledkem kontroly
    """
    # Sestavení URL
    url = f"{BASE_URL}/{endpoint}"
    
    if params:
        query_string = urlencode(params)
        url = f"{url}?{query_string}"
    
    # Příprava hlaviček
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    if api_key:
        headers["Api-Key"] = api_key
    elif token:
        headers["Authorization"] = f"Bearer {token}"
    else:
        return {
            "success": False,
            "status": None,
            "error": "Chybí autentizační údaje (api-key nebo token)"
        }
    
    # Příprava dat
    json_data = None
    if data and method in ("POST", "PUT"):
        json_data = json.dumps(data).encode('utf-8')
        headers["Content-Length"] = str(len(json_data))
    
    # Odeslání požadavku
    try:
        req = urllib.request.Request(
            url,
            data=json_data,
            headers=headers,
            method=method
        )
        
        with urllib.request.urlopen(req, timeout=30) as response:
            status = response.status
            body = response.read().decode('utf-8')
            
            result = {
                "success": 200 <= status < 300,
                "status": status,
                "url": url,
                "method": method,
                "response_body": body[:500] if body else None  # Omezení délky
            }
            
            if verbose:
                result["headers"] = dict(response.headers)
            
            return result
            
    except urllib.error.HTTPError as e:
        return {
            "success": False,
            "status": e.code,
            "url": url,
            "method": method,
            "error": f"HTTP {e.code}: {e.reason}",
            "response_body": e.read().decode('utf-8')[:500] if e.fp else None
        }
    except urllib.error.URLError as e:
        return {
            "success": False,
            "status": None,
            "url": url,
            "method": method,
            "error": f"Spojení selhalo: {e.reason}"
        }
    except Exception as e:
        return {
            "success": False,
            "status": None,
            "url": url,
            "method": method,
            "error": f"Neočekávaná chyba: {str(e)}"
        }


def main():
    parser = argparse.ArgumentParser(
        description='Kontrola dostupnosti mPohoda API endpointů',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Příklady:
  # Kontrola GET endpointu s API klíčem
  %(prog)s --endpoint IssuedInvoices --method GET --api-key "váš-klíč"
  
  # Kontrola s tokenem a parametry
  %(prog)s --endpoint BusinessPartners --method GET --token "váš-token" --params "pageSize=10&pageNumber=1"
  
  # Kontrola POST endpointu
  %(prog)s --endpoint IssuedInvoices --method POST --token "váš-token" --data '{"IssueDate": "2024-01-15", "BusinessPartnerAddress": {"DocumentAddressWithAddressBookLink": {"Id": "550e8400-e29b-41d4-a716-446655440000"}}, "Items": [{"TextItem": {"Text": "Test", "Quantity": 1, "UnitPrice": 100, "UnitPriceType": "WithoutVat", "VatRateType": "BasicVatRate"}}]}'
        """
    )
    
    parser.add_argument('--endpoint', '-e', required=True,
                        help='Název endpointu (např. IssuedInvoices)')
    parser.add_argument('--method', '-m', default='GET',
                        choices=['GET', 'POST', 'PUT', 'DELETE'],
                        help='HTTP metoda (výchozí: GET)')
    parser.add_argument('--api-key', '-k',
                        help='API klíč pro autentizaci')
    parser.add_argument('--token', '-t',
                        help='Bearer token pro autentizaci')
    parser.add_argument('--data', '-d',
                        help='JSON data pro POST/PUT')
    parser.add_argument('--params', '-p',
                        help='Query parametry (format: "key1=value1&key2=value2")')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Podrobný výstup')
    
    args = parser.parse_args()
    
    # Parsování dat
    request_data = None
    if args.data:
        try:
            request_data = json.loads(args.data)
        except json.JSONDecodeError as e:
            print(f"❌ Chyba: Neplatný JSON data: {e}", file=sys.stderr)
            sys.exit(1)
    
    # Parsování parametrů
    query_params = None
    if args.params:
        query_params = {}
        for param in args.params.split('&'):
            if '=' in param:
                key, value = param.split('=', 1)
                query_params[key] = value
    
    # Kontrola
    if args.verbose:
        print(f"🔍 Kontroluji endpoint: {args.endpoint}")
        print(f"📡 URL: {BASE_URL}/{args.endpoint}")
        print(f"📝 Metoda: {args.method}")
        if args.api_key:
            print(f"🔑 Autentizace: API klíč")
        elif args.token:
            print(f"🔑 Autentizace: Bearer token")
        print()
    
    result = check_endpoint(
        endpoint=args.endpoint,
        method=args.method,
        api_key=args.api_key,
        token=args.token,
        data=request_data,
        params=query_params,
        verbose=args.verbose
    )
    
    # Výstup
    if result["success"]:
        print(f"✅ Endpoint je DOSTUPNÝ")
        print(f"   Status: {result['status']}")
        print(f"   URL: {result['url']}")
        
        if result.get("response_body"):
            try:
                body = json.loads(result["response_body"])
                print(f"\n📄 Odpověď:")
                print(json.dumps(body, ensure_ascii=False, indent=2)[:1000])
            except:
                print(f"\n📄 Odpověď: {result['response_body']}")
        
        sys.exit(0)
    else:
        status = result.get("status")
        error = result.get("error", "Neznámá chyba")
        
        print(f"❌ Endpoint je NEDOSTUPNÝ")
        print(f"   Status: {status}")
        print(f"   Chyba: {error}")
        
        if result.get("response_body"):
            print(f"\n📄 Tělo odpovědi:")
            print(result["response_body"])
        
        # Návratový kód podle typu chyby
        if status in (401, 403):
            sys.exit(2)
        elif status in (400, 422):
            sys.exit(3)
        elif status == 404:
            sys.exit(4)
        else:
            sys.exit(1)


if __name__ == '__main__':
    main()
