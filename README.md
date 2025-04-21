# 📨 Email Classifier with PII Masking API

This API takes in support emails, masks sensitive personal data using regex (no LLMs), and classifies the email into categories like Billing, Technical Support, etc.

## 💻 API Endpoint

POST `/classify`

### 🔹 Input
```json
{
  "email_text": "Hi, my name is Priya Mehta. My Aadhar number is 4321-1234-5678. I need help with billing."
}
```

### 🔹 Output
```json
{
  "masked_email": "Hi, my name is [full_name]. My Aadhar number is [aadhar_num]. I need help with billing.",
  "category": "Billing Issues"
}
```
