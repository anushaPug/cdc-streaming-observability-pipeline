import base64
import json
from datetime import datetime, timezone

def lambda_handler(event, context):
    output = []

    for record in event["records"]:
        try:
            payload = json.loads(
                base64.b64decode(record["data"]).decode("utf-8")
            )

            ddb = payload.get("dynamodb", {})
            new_image = ddb.get("NewImage", {})

            doc = {
                "ts": datetime.now(timezone.utc).isoformat(),
                "eventName": payload.get("eventName"),
                "tableName": payload.get("tableName"),
                "eventID": payload.get("eventID"),
                "customer_id": (
                    int(new_image["id"]["N"])
                    if "id" in new_image and "N" in new_image["id"]
                    else None
                ),
                "name": new_image.get("lastname", {}).get("S"),
                "source": "dynamodb-cdc"
            }

            encoded = base64.b64encode(
                (json.dumps(doc) + "\n").encode("utf-8")
            ).decode("utf-8")

            output.append({
                "recordId": record["recordId"],
                "result": "Ok",
                "data": encoded
            })

        except Exception:
            output.append({
                "recordId": record["recordId"],
                "result": "ProcessingFailed",
                "data": record["data"]
            })

    return {"records": output}
