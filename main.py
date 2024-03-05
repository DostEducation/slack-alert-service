import json
import functions_framework
from app.helpers import notification_helper
from utils import logger

# Endpoint of the `slack-alert-service` cloud function.
@functions_framework.http
def handle_alerts(req):
    try:
        if not req.method == "POST":
            return "Method not allowed"

        # Retrieving data from the request
        jsonData = req.get_json()
        slack_block = jsonData.get("slack_block")
        notification_helper.notify(slack_block)
    except Exception as e:
        error_message = "Error while handling request for slack alert service"
        logger.error(f"{error_message}: {e}")
        return {"message": f"{error_message}"}, 500
    return (json.dumps({"Success": True}), 200, {"ContentType": "application/json"})
