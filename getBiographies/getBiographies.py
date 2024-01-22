import json
import boto3
import decimal


def lambda_handler(event, context):
    """
    Access biographies table from DynamoDB resource
    and return all items in the table
    """
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("njitsbc-biographies")
    response = table.scan()
    items = response["Items"]

    # handle Decimal type
    for item in items:
        for key in item:
            if isinstance(item[key], decimal.Decimal):
                item[key] = int(item[key])

    return {"statusCode": 200, "body": json.dumps(items)}
