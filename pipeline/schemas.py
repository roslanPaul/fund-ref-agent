
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class ServiceProvider(BaseModel):
    """
    Contrat de données pour un service provider (prestataire) du fonds.
    Utilise la nomenclature standardisée de l'Asset Servicing international.
    """
    role_code: Literal['ISSUER', 'MGMT', 'CUST', 'FNAV', 'AUDT'] # ISO/SWIFT standard
    denomination: str
    lei: Optional[str] = Field(None, description="Unique Legal Entity Identifier (20 alphanumeric characters)")  # Code LEI (Legal Entity Identifier) pour l'identification unique
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score of the extraction (0 to 1)")
    justification: str

class FundExtract(BaseModel):
    """
    Contrat de données pour un extrait de fonds.
    Contient les informations extraites d'un document PDF (prospectus).
    """
    denomination: str
    entity_legal_type: Literal['UMBRELLA_FUND', 'SUB_FUND', 'MGMT_CO', 'CUSTODIAN']
    legal_form: Literal['SICAV', 'FCP', 'OTHER']
    isin_units: List[str] = Field(default=[], description="List of ISIN codes for the fund's units")
    sfdr_article: Optional[Literal['6', '8', '9']] = None
    service_providers: List[ServiceProvider]
    currency: Optional[str] = None
    domicile_country: Optional[str] = None
    parent_umbrella_id: Optional[int] = Field(None, description="Reference ID of the umbrella fund if the structure is SUB_FUND")
    extraction_complete: bool = Field(True, description="False if critical fields are missing")
