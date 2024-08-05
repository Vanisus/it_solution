from typing import List

from fastapi import HTTPException
from sqlalchemy import select
from models import CarSQL
from db import get_async_session


async def create_car(car_data: dict) -> CarSQL:
    async with get_async_session() as session:
        car = CarSQL(**car_data)
        session.add(car)
        await session.commit()
        await session.refresh(car)
        return car


async def get_car_with_filter(
        brand: str | None,
        model: str | None,
        year: int | None,
        fuel_type: str | None,
        transmission: str | None,
        mileage: int | None,
        price: float | None,
        limit: int = 10,
        offset: int = 0
) -> List[CarSQL]:
    async with get_async_session() as session:
        query = select(CarSQL)

        if brand:
            query = query.where(CarSQL.brand == brand)
        if model:
            query = query.where(CarSQL.model == model)
        if year:
            query = query.where(CarSQL.year == year)
        if fuel_type:
            query = query.where(CarSQL.fuel_type == fuel_type)
        if transmission:
            query = query.where(CarSQL.transmission == transmission)
        if mileage:
            query = query.where(CarSQL.mileage == mileage)
        if price:
            query = query.where(CarSQL.price == price)

        query = query.limit(limit).offset(offset)
        result = await session.execute(query)
        if not result:
            raise HTTPException(status_code=404, detail="Cars not found")
        return result.scalars().all()


async def get_car_with_id(car_id: int):
    async with get_async_session() as session:
        car = await session.get(CarSQL, car_id)
        if car is None:
            raise HTTPException(status_code=404, detail="Car not found")
        return car


async def update_car_data(
        car_id: int,
        car_data: dict
):
    async with get_async_session() as session:
        car = await get_car_with_id(car_id)
        for key, value in car_data.items():
            setattr(car, key, value)
        session.add(car)
        await session.commit()
        await session.refresh(car)
        return car


async def remove_car(car_id: int):
    async with get_async_session() as session:
        car = await session.get(CarSQL, car_id)
        await session.delete(car)
        await session.commit()
        return {"message": f"Car with id={car.id} was deleted"}
