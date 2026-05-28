from pydantic import BaseModel

class WeatherInput(BaseModel):
    city: str