from fastapi import FastAPI
import uvicorn
import logging
from logging.config import dictConfig
from config.LogConfig import LogConfig
from models.AzureMonitorAlerts import Data
from models.AnyPayloadInput import AnyPayloadInput

dictConfig(LogConfig().dict())
logger = logging.getLogger("main")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("root route called... responding...")
    return {"data": {"server": "Alert Gateway Mock Server", "adapter": "Azure Alerts Adapter", "endpoint": "/azure-alerts-adapter/alerts"}}

@app.post("/azure-alerts-adapter/alerts")
def create_alert(data: Data):
    logger.info("NEW ALERT...")
    logger.debug(f"REQUEST: {data}")
    logger.debug(f"RESPONSE: {data.alertContext.condition.allOf}")
    return data.alertContext.condition.allOf

@app.post("/just-log-it/alerts")
def just_log_it(input: AnyPayloadInput):
    logger.info("NEW PAYLOAD INPUT...")
    logger.debug(f"REQUEST: {input}")
    return {"data" : "success"}
