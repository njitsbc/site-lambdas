import json
import boto3
import decimal

paths = {
    "/getPendingBiographies": "njitsbc-pendingBiographies",
    "/getBiographies": "njitsbc-biographies",
}


def lambda_handler(event, context):
    """
    Access biographies table from DynamoDB resource
    and return all items in the table
    """
    dynamodb = boto3.resource("dynamodb")

    raw_path = event["rawPath"]
    if raw_path not in paths:
        return {"statusCode": 400, "message": f"{raw_path} is not a supported endpoint."}
    table = dynamodb.Table(paths[raw_path])

    response = table.scan()
    items = response["Items"]

    # handle Decimal type

    for item in items:
        for key in item:
            if isinstance(item[key], decimal.Decimal):
                item[key] = int(item[key])

    return {"statusCode": 200, "body": json.dumps(items)}
