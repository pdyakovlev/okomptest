from fastapi import FastAPI
from forecast.forecast_endpoints import router as forecast_router
import constants

app = FastAPI(title=constants.TITLE, description=constants.DESCRIPTION)
app.include_router(forecast_router)
