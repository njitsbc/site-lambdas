import boto3

# TODO: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('njitsbc-pendingBiographies')
    
    fields = {"id", "name", "major", "graduationDate", "favoriteTrick", "aboutMe", "imgBase64"}
    keys_as_set = set(event.keys())


    if "id" not in event:
        import uuid
        event["id"] = str(uuid.uuid4())

    if "imgBase64" not in event:
        event["imgBase64"] = "NO PICTURE PROVIDED"

    if(keys_as_set != fields):
        return {
            'statusCode': 400,
            'message': "Field mismatch. " + str(fields - keys_as_set) + " not provided"
        }
    
    for key, value in event.items():
        if not value:
            return {
                'statusCode': 400,
                'message': f"{key} cannot be empty"
            }
        elif not isinstance(value, str):
            return {
                'statusCode': 400,
                'message': f"{value} must be of type 'str'"
            }

    
    try:
        table.put_item(Item = event)
    except Exception as e:
        return {
            'statusCode': 400,
            'message': f"Error: {e}"
        }
    
    return {
        'statusCode': 200,
    }
