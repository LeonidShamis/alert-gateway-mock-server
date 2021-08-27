from fastapi import FastAPI
import uvicorn
import logging
from logging.config import dictConfig
from config.LogConfig import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("main")

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("root route called... responding...")
    return {"data": {"server": "Alert Gateway Mock Server", "adapter": "Azure Alerts Adapter", "endpoint": "/azure-alerts-adapter"}}

@app.get("/azure-alerts-adapter")
def azure_alerts_adapter():
    logger.info("root route called... responding...")
    # return '{"data": {"server": "Alert Gateway Mock Server", "adapter": "Azure Alerts Adapter", "endpoint": "/azure-adapter"}}'
    return {"schemaId": "Microsoft.Insights/activityLogs",
            "data": {
                "status": "Activated",
                "context": {
                "activityLog": {
                    "authorization": {
                    "action": "microsoft.insights/activityLogAlerts/write",
                    "scope": "/subscriptions/…"
                    },
                    "channels": "Operation",
                    "claims": "…",
                    "caller": "logicappdemo@contoso.com",
                    "correlationId": "91ad2bac-1afa-4932-a2ce-2f8efd6765a3",
                    "description": "",
                    "eventSource": "Administrative",
                    "eventTimestamp": "2018-04-03T22:33:11.762469+00:00",
                    "eventDataId": "ec74c4a2-d7ae-48c3-a4d0-2684a1611ca0",
                    "level": "Informational",
                    "operationName": "microsoft.insights/activityLogAlerts/write",
                    "operationId": "61f59fc8-1442-4c74-9f5f-937392a9723c",
                    "resourceId": "/subscriptions/…",
                    "resourceGroupName": "LOGICAPP-DEMO",
                    "resourceProviderName": "microsoft.insights",
                    "status": "Succeeded",
                    "subStatus": "",
                    "subscriptionId": "…",
                    "submissionTimestamp": "2018-04-03T22:33:36.1068742+00:00",
                    "resourceType": "microsoft.insights/activityLogAlerts"
                }
                },
                "properties": {}
            }
            }

