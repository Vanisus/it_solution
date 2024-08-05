from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class CarSQL(Base):
    __tablename__ = 'car'

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int]
    fuel_type: Mapped[str] = mapped_column(nullable=False)
    transmission: Mapped[str] = mapped_column(nullable=False)
    mileage: Mapped[int]
    price: Mapped[float] = mapped_column(nullable=False)

