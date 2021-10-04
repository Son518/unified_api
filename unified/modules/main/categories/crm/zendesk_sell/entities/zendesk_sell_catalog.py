from dataclasses import dataclass

@dataclass
class ZendesksellCatalog():

    name:str = None
    description:str = None
    sku:str = None
    active:str = None
    max_discount:str = None
    max_markup:str = None
    unit_cost:str = None
    unit_cost_currency:str = None
    unit_price:str = None
    currency:str = None
    catalog_id: str = None