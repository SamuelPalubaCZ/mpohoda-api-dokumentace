#!/usr/bin/env python3
"""
mPohoda API - Validátor požadavků
=================================
Kontroluje strukturu JSON požadavků pro mPohoda API.

Použití:
    python validate-request.py --endpoint IssuedInvoices --file request.json
    python validate-request.py --endpoint BusinessPartners --data '{"Name": "Test"}'
    
Návratové kódy:
    0 - Požadavek je validní
    1 - Chyba ve struktuře požadavku
    2 - Neznámý endpoint
    3 - Chyba při čtení souboru
"""

import json
import sys
import argparse
from pathlib import Path

# Základní validační pravidla pro jednotlivé endpointy
VALIDATION_RULES = {
    "IssuedInvoices": {
        "required": ["IssueDate", "BusinessPartnerAddress"],
        "types": {
            "IssueDate": str,
            "DueDate": str,
            "TaxDate": str,
            "Text": str,
            "PaymentMethodId": str,
            "BankAccountId": str,
            "BusinessPartnerAddress": dict,
            "Items": list
        },
        "items_required": ["TextItem", "PriceListItem"],
        "text_item_required": ["Text", "Quantity", "UnitPrice", "UnitPriceType", "VatRateType"],
        "price_list_item_required": ["PriceListItemId", "Quantity"]
    },
    "ReceivedOrders": {
        "required": ["IssueDate", "BusinessPartnerAddress"],
        "types": {
            "IssueDate": str,
            "DueDate": str,
            "BusinessPartnerAddress": dict,
            "Items": list
        }
    },
    "BusinessPartners": {
        "required": ["Name"],
        "types": {
            "Name": str,
            "CompanyId": str,
            "VatId": str,
            "Email": str,
            "Phone": str
        }
    },
    "PriceListItems": {
        "required": ["Name"],
        "types": {
            "Name": str,
            "Code": str,
            "Unit": str,
            "Price": (int, float),
            "VatRateId": str
        }
    }
}


def validate_date_format(date_string: str) -> bool:
    """Kontrola formátu data (ISO 8601)."""
    import re
    # Podporuje: 2024-01-15 nebo 2024-01-15T10:30:00Z
    pattern = r'^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z?)?$'
    return bool(re.match(pattern, date_string))


def validate_uuid(uuid_string: str) -> bool:
    """Kontrola formátu UUID."""
    import re
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(pattern, uuid_string, re.IGNORECASE))


def validate_request(endpoint: str, data: dict) -> list:
    """
    Validace požadavku pro daný endpoint.
    
    Args:
        endpoint: Název endpointu (např. "IssuedInvoices")
        data: JSON data požadavku
        
    Returns:
        Seznam nalezených chyb (prázdný = validní)
    """
    errors = []
    
    # Kontrola známého endpointu
    if endpoint not in VALIDATION_RULES:
        return [f"Neznámý endpoint: {endpoint}. Známé endpointy: {', '.join(VALIDATION_RULES.keys())}"]
    
    rules = VALIDATION_RULES[endpoint]
    
    # Kontrola povinných polí
    for field in rules.get("required", []):
        if field not in data:
            errors.append(f"Chybí povinné pole: '{field}'")
        elif data[field] is None or data[field] == "":
            errors.append(f"Povinné pole '{field}' je prázdné")
    
    # Kontrola typů
    for field, expected_type in rules.get("types", {}).items():
        if field in data and data[field] is not None:
            actual_type = type(data[field])
            if isinstance(expected_type, tuple):
                if actual_type not in expected_type:
                    errors.append(f"Pole '{field}' má špatný typ: {actual_type.__name__}, očekáváno: {expected_type}")
            elif actual_type != expected_type:
                errors.append(f"Pole '{field}' má špatný typ: {actual_type.__name__}, očekáváno: {expected_type.__name__}")
    
    # Speciální validace pro faktury
    if endpoint == "IssuedInvoices":
        # Kontrola data
        if "IssueDate" in data and data["IssueDate"]:
            if not validate_date_format(data["IssueDate"]):
                errors.append("Pole 'IssueDate' není ve formátu ISO 8601 (YYYY-MM-DD nebo YYYY-MM-DDTHH:MM:SSZ)")
        
        # Kontrola BusinessPartnerAddress
        if "BusinessPartnerAddress" in data and isinstance(data["BusinessPartnerAddress"], dict):
            bpa = data["BusinessPartnerAddress"]
            if "DocumentAddressWithAddressBookLink" not in bpa:
                errors.append("BusinessPartnerAddress musí obsahovat 'DocumentAddressWithAddressBookLink'")
            elif "Id" not in bpa.get("DocumentAddressWithAddressBookLink", {}):
                errors.append("DocumentAddressWithAddressBookLink musí obsahovat 'Id'")
            elif not validate_uuid(bpa["DocumentAddressWithAddressBookLink"]["Id"]):
                errors.append("BusinessPartnerAddress.Id není platné UUID")
        
        # Kontrola položek
        if "Items" in data and isinstance(data["Items"], list):
            if len(data["Items"]) == 0:
                errors.append("Faktura musí obsahovat alespoň jednu položku")
            
            for i, item in enumerate(data["Items"]):
                if not isinstance(item, dict):
                    errors.append(f"Položka [{i}] není objekt")
                    continue
                
                # Kontrola typu položky
                item_types = list(item.keys())
                valid_types = rules.get("items_required", [])
                
                if not any(t in item_types for t in valid_types):
                    errors.append(f"Položka [{i}] musí obsahovat jeden z: {valid_types}")
                    continue
                
                # Validace TextItem
                if "TextItem" in item:
                    ti = item["TextItem"]
                    for field in rules.get("text_item_required", []):
                        if field not in ti:
                            errors.append(f"TextItem [{i}] chybí povinné pole: '{field}'")
                    
                    # Kontrola UnitPriceType
                    if "UnitPriceType" in ti:
                        valid_types = ["WithoutVat", "WithVat"]
                        if ti["UnitPriceType"] not in valid_types:
                            errors.append(f"TextItem [{i}].UnitPriceType musí být jeden z: {valid_types}")
                    
                    # Kontrola VatRateType
                    if "VatRateType" in ti:
                        valid_vat = ["ZeroVatRate", "BasicVatRate", "FirstReducedVatRate", "SecondReducedVatRate"]
                        if ti["VatRateType"] not in valid_vat:
                            errors.append(f"TextItem [{i}].VatRateType musí být jeden z: {valid_vat}")
                
                # Validace PriceListItem
                if "PriceListItem" in item:
                    pli = item["PriceListItem"]
                    for field in rules.get("price_list_item_required", []):
                        if field not in pli:
                            errors.append(f"PriceListItem [{i}] chybí povinné pole: '{field}'")
                    
                    if "PriceListItemId" in pli and not validate_uuid(pli["PriceListItemId"]):
                        errors.append(f"PriceListItem [{i}].PriceListItemId není platné UUID")
    
    return errors


def main():
    parser = argparse.ArgumentParser(
        description='Validátor požadavků pro mPohoda API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Příklady:
  %(prog)s --endpoint IssuedInvoices --file faktura.json
  %(prog)s --endpoint BusinessPartners --data '{"Name": "Test s.r.o."}'
  %(prog)s --endpoint IssuedInvoices --data '{"IssueDate": "2024-01-15", "BusinessPartnerAddress": {"DocumentAddressWithAddressBookLink": {"Id": "550e8400-e29b-41d4-a716-446655440000"}}, "Items": [{"TextItem": {"Text": "Test", "Quantity": 1, "UnitPrice": 100, "UnitPriceType": "WithoutVat", "VatRateType": "BasicVatRate"}}]}'
        """
    )
    
    parser.add_argument('--endpoint', '-e', required=True,
                        help='Název endpointu (např. IssuedInvoices, BusinessPartners)')
    parser.add_argument('--file', '-f',
                        help='Cesta k JSON souboru s požadavkem')
    parser.add_argument('--data', '-d',
                        help='JSON data požadavku (přímé zadání)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Podrobný výstup')
    
    args = parser.parse_args()
    
    # Načtení dat
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"❌ Chyba: Soubor '{args.file}' neexistuje", file=sys.stderr)
            sys.exit(3)
        except json.JSONDecodeError as e:
            print(f"❌ Chyba: Neplatný JSON v souboru: {e}", file=sys.stderr)
            sys.exit(3)
    elif args.data:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError as e:
            print(f"❌ Chyba: Neplatný JSON data: {e}", file=sys.stderr)
            sys.exit(3)
    else:
        print("❌ Chyba: Musíte zadat --file nebo --data", file=sys.stderr)
        sys.exit(1)
    
    # Validace
    if args.verbose:
        print(f"🔍 Validuji požadavek pro endpoint: {args.endpoint}")
        print(f"📄 Data: {json.dumps(data, ensure_ascii=False, indent=2)}")
        print()
    
    errors = validate_request(args.endpoint, data)
    
    if errors:
        print(f"❌ Požadavek je NEVALIDNÍ ({len(errors)} chyb):")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        sys.exit(1)
    else:
        print("✅ Požadavek je VALIDNÍ")
        
        if args.verbose:
            # Zobrazení přehledu
            print("\n📋 Přehled požadavku:")
            print(f"   Endpoint: {args.endpoint}")
            print(f"   Povinná pole: {', '.join(VALIDATION_RULES[args.endpoint].get('required', []))}")
            
            if "Items" in data and isinstance(data["Items"], list):
                print(f"   Počet položek: {len(data['Items'])}")
                for i, item in enumerate(data["Items"]):
                    item_type = list(item.keys())[0] if item else "neznámý"
                    print(f"     - Položka {i+1}: {item_type}")
        
        sys.exit(0)


if __name__ == '__main__':
    main()
