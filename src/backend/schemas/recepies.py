from typing import List, Optional

from pydantic import BaseModel

from ingredient import Ingredient


class Recepie(BaseModel):
    """A Recepie list all needed components and
    instructions to recreate the recepie.

    
    :param BaseModel: Pydantic Basemodel.
    :type BaseModel: class
    """    
    ingridients: List[Ingredient]
    instructions: str
    modifications: Optional[str]