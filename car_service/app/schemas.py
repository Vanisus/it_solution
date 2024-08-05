from typing import Optional
from pydantic import BaseModel


class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    fuel_type: str
    transmission: str
    mileage: int
    price: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "brand": "Toyota",
                "model": "Camry",
                "year": 2020,
                "fuel_type": "бензин",
                "transmission": "автоматическая",
                "mileage": 50000,
                "price": 25000.0
            }
        }
    }


class CarCreate(BaseModel):
    brand: str
    model: str
    year: int
    fuel_type: str
    transmission: str
    mileage: int
    price: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "brand": "Toyota",
                "model": "Camry",
                "year": 2020,
                "fuel_type": "бензин",
                "transmission": "автоматическая",
                "mileage": 50000,
                "price": 25000.0
            }
        }
    }


class CarUpdate(BaseModel):
    brand: str
    model: str
    year: int
    fuel_type: str
    transmission: str
    mileage: int
    price: float

    model_config = {
        "json_schema_extra": {
            "example": {
                "brand": "Toyota",
                "model": "Camry",
                "year": 2020,
                "fuel_type": "бензин",
                "transmission": "автоматическая",
                "mileage": 50000,
                "price": 25000.0
            }
        }
    }
