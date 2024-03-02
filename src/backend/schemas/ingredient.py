from typing import List

from pydantic import BaseModel

from component import Component

class Ingredient(BaseModel):
    """An ingredient, the smallest possible
    component to a recepie. An ingredient itself
    is composed of one or multiple components.
    Note that some ingredients can also be an
    component, for example: water and salt.


    :param BaseModel: Basemodel class of pydantic.
    :type BaseModel: class
    """
    name: str
    manufacturer: str
    nutrison: List[str]
    ean: int
    description: str
    vegan: bool
    vegetarian: bool
    components: List[Component]