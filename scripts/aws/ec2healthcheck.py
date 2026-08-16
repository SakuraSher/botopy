
import json

def lambda_handler(event, context):
    if event['status'] == 'running':
        return {
        'statusCode': 200,
        'body': json.dumps({"instance_id": event["instance_id"],"healthy": True,"message": "Instance is healthy"})
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps({"instance_id": event["instance_id"], "healthy": False, "message": "Instance is not healthy"})
    }

