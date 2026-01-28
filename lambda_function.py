import json

WEIGHT = 0.8
BIAS = -2.0

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        x = float(body["input"])
        score = WEIGHT * x + BIAS

        if score >= 0:
            prediction = 1
        else:
            prediction = 0

        return {
            "statusCode": 200,
            "body": json.dumps({
                "input": x,
                "score": score,
                "prediction": prediction
            })
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": str(e)
            })
        }
