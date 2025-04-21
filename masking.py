import re

PII_PATTERNS = {
    "full_name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",
    "email": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "phone_number": r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b",
}

def mask_pii(text):
    for entity, pattern in PII_PATTERNS.items():
        text = re.sub(pattern, f"[{{entity}}]", text)
    return text
