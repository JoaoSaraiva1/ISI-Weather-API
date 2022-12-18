import asyncio
import logging
import csv

from aiohttp import ClientError, ClientSession

from accuweather import (
    AccuWeather,
    ApiError,
    InvalidApiKeyError,
    InvalidCoordinatesError,
    RequestsExceededError,
)

LATITUDE = 40.42
LONGITUDE = -7.704
LOCATION_KEY = "273407"
API_KEY = "MeQxuknFFZdX6228SAI9eAZK1doAjk1O"

logging.basicConfig(level=logging.DEBUG)

async def main():
    async with ClientSession() as websession:
        try:
            accuweather = AccuWeather(
                API_KEY, websession, latitude=LATITUDE, longitude=LONGITUDE
            )
            current_conditions = await accuweather.async_get_current_conditions()
            forecast = await accuweather.async_get_forecast(metric=True)
            forecast_hourly = await accuweather.async_get_forecast_hourly(metric=True)
        except (
            ApiError,
            InvalidApiKeyError,
            InvalidCoordinatesError,
            ClientError,
            RequestsExceededError,
        ) as error:
            print(f"Error: {error}")
        else:
            print(f"Location: {accuweather.location_name} ({accuweather.location_key})")
            print(f"Requests remaining: {accuweather.requests_remaining}")
            print(f"Current: {current_conditions}")
            print(f"Forecast: {forecast}")
            print(f"Forecast hourly: {forecast_hourly}")

            csv_file = open('json_data.csv', 'w', newline='')
            
            for row in {forecast_hourly}:
                csv_writer.writerow(row.values())

            # Close the CSV file
            csv_file.close()


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
loop.close()