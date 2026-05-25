
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class Intervenant(BaseModel):
    """
    Contrat de données pour un intervenant (prestataire) du fonds.
    Utilise la nomenclature standardisée de l'Asset Servicing international.
    """
    # Roles de marché (Société de gestion, Dépositaire, Valorisateur, etc.)
    role: Literal['SOCIETE_GESTION', 'DEPOSITAIRE', 'VALORISATEUR', 'COMMISSAIRE_COMPTES', 'CONSERVATEUR']
    denomination: str
    lei: Optional[str] = Field(None, description="Legal Entity Identifier unique (20 caractères)")  # Code LEI (Legal Entity Identifier) pour l'identification unique
    confiance: float = Field(ge=0.0, le=1.0, description="Score de confiance de l'extraction (0 à 1)")
    justification: str

class FondExtrait(BaseModel):
    """
    Contrat de données pour un extrait de fonds.
    Contient les informations extraites d'un document PDF (prospectus).
    """
    denomination: str
    forme_juridique: Literal['SICAV', 'FCP', 'AUTRE']
    structure_fonds : Literal['MONO_COMPARTIMENT', 'PARAPLUIE', 'COMPARTIMENT']
    isin_parts: List[str] = []
    sfdr_article: Optional[Literal['6', '8', '9']] = None
    intervenants: List[Intervenant]
    devise: Optional[str] = None
    pays_domicile: Optional[str] = None
    isin_parent: Optional[str] = Field(None, description="Code ISIN du fonds parapluie (si structure COMPARTIMENT)")
    extraction_complete: bool = Field(True, description="False si des champs critiques sont manquants")
