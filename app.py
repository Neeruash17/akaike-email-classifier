from fastapi import FastAPI
from pydantic import BaseModel
from masking import mask_pii
from utils import classify_email

app = FastAPI()

class EmailInput(BaseModel):
    email_text: str

class EmailResponse(BaseModel):
    masked_email: str
    category: str

@app.post("/classify", response_model=EmailResponse)
def classify(input: EmailInput):
    masked = mask_pii(input.email_text)
    category = classify_email(masked)
    return EmailResponse(masked_email=masked, category=category)
