def lambda_handler(event, context):
    print("Hello Lakshya!")
    return {
        'statusCode': 200,
        'body': 'Hello Lakshya!'
    }
