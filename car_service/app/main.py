from typing import List, Optional

from fastapi import FastAPI, HTTPException

from db import init_db
from schemas import Car, CarCreate, CarUpdate
from crud import create_car, get_car_with_filter, remove_car, update_car_data, get_car_with_id

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.post("/api/cars", response_model=CarCreate)
async def add_car(
        car_data: CarCreate
):
    new_car = await create_car(car_data.dict())
    return new_car


@app.get("/api/cars/", response_model=List[Car])
async def get_cars(
        brand: Optional[str] = None,
        model: Optional[str] = None,
        year: Optional[int] = None,
        fuel_type: Optional[str] = None,
        transmission: Optional[str] = None,
        mileage: Optional[int] = None,
        price: Optional[float] = None,
        limit: int = 10,
        offset: int = 0
):
    cars = await get_car_with_filter(
        brand=brand,
        model=model,
        year=year,
        fuel_type=fuel_type,
        transmission=transmission,
        mileage=mileage,
        price=price,
        limit=limit,
        offset=offset
    )

    return cars


@app.get("/api/cars/{car_id}", response_model=Car)
async def get_car(car_id: int):
    return await get_car_with_id(car_id)


@app.put("/api/cars/{car_id}", response_model=CarUpdate)
async def update_car(
        car_id: int,
        car_data: CarUpdate,
):
    updated_car = await update_car_data(car_id, car_data.dict(exclude_unset=True))
    return updated_car


@app.delete("/api/cars/{car_id}")
async def delete_car(car_id: int):
    return await remove_car(car_id)
