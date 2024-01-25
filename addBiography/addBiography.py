import boto3
import json


# TODO: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html
# CREATE_RAW_PATH = "/addBiography"
def lambda_handler(event, context):
    # if event['rawPath'] == CREATE_RAW_PATH:

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("njitsbc-pendingBiographies")
    dynamodb = boto3.resource("dynamodb")

    fields = {"name", "major", "graduationDate", "favoriteTrick", "aboutMe"}
    body_as_json = json.loads(event["body"])
    keys_as_set = set(body_as_json.keys())

    if not event.get("id"):
        import uuid

        body_as_json["id"] = str(uuid.uuid4())

    if not event.get("imgBase64"):
        body_as_json["imgBase64"] = "NO PICTURE PROVIDED"

    if keys_as_set != fields:
        print("Field mismatch. " + str(fields - keys_as_set) + " not provided")
        return {
            "statusCode": 400,
            "message": "Field mismatch. " + str(fields - keys_as_set) + " not provided",
        }

    for key, value in body_as_json.items():
        if not value:
            return {"statusCode": 400, "message": f"{key} cannot be empty"}
        elif not isinstance(value, str):
            return {"statusCode": 400, "message": f"{value} must be of type 'str'"}

    try:
        table.put_item(Item=body_as_json)
    except Exception as e:
        return {"statusCode": 400, "message": f"Error: {e}"}

    return {"statusCode": 200, "message": "S"}
