from pydantic import BaseModel, field_validator, ValidationError
from typing import Literal

class CustomData(BaseModel):
    gender: Literal['Female', 'Male']
    seniorcitizen: Literal['No', 'Yes']
    partner: Literal['Yes', 'No']
    dependents: Literal['No', 'Yes']
    tenure: int
    phoneservice: Literal['No', 'Yes']
    multiplelines: Literal['No phone service', 'No', 'Yes']
    internetservice: Literal['DSL', 'Fiber optic', 'No']
    contract: Literal['Month-to-month', 'One year', 'Two year']
    paperlessbilling: Literal['Yes', 'No']
    paymentmethod: Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    monthlycharges: float
    totalcharges: float
    streamingtv: Literal['No', 'Yes', 'No internet service']
    streamingmovies: Literal['No', 'Yes', 'No internet service']
    onlinebackup: Literal['No', 'Yes', 'No internet service']
    deviceprotection: Literal['No', 'Yes', 'No internet service']
    techsupport: Literal['No', 'Yes', 'No internet service']
    internetsecurity: Literal['No', 'Yes', 'No internet service']
    contract_type: Literal['Month-to-month', 'One year', 'Two year']
    payment_type: Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    tenure_group: Literal['0-12 Months', '12-24 Months', '24-48 Months', '48-60 Months', '60-72 Months']
    monthly_charges_group: Literal['Low', 'Medium', 'High']
    total_charges_group: Literal['Low', 'Medium', 'High']
    
