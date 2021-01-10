import json


def hello(event, context):
    if 'queryStringParameters' in event and 'uid' in event['queryStringParameters']:
        print("value found")
        uid = (event["queryStringParameters"]['uid'])
        body = {
            "message": "GGGGo Go Serverless v1.0! ",
            "uid": uid
        }
    else:
        print("no valid value found")
        body = {
            "message": " no valid parameters found"
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)

    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
