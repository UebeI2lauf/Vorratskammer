from fractions import Fraction
from typing import Optional

from pydantic import BaseModel

class Component(BaseModel):
    """An component is the smallest listed
    component on a food package.
    On futher note not all components are
    or have to be listed in their dosage
    on packaging. This results in the dosage being 
    an optional parameter.

    :param BaseModel: Pydantic Basemodel.
    :type BaseModel: class
    """
    name: str
    dosage: Optional[Fraction]
    description: str
