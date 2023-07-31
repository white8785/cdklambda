# Required:  sam local start-lambda
import boto3
from botocore import UNSIGNED
from botocore.config import Config

lambda_client = boto3.client('lambda',
                             endpoint_url="http://127.0.0.1:3001",
                             use_ssl=False,
                             verify=False,
                             config=Config(signature_version=UNSIGNED,
                                           read_timeout=1,
                                           retries={'max_attempts': 0}
                                           )
                            )
lambda_client.invoke(FunctionName="LambdaOne")
# lambda_client.invoke(FunctionName="LambdaTwo")