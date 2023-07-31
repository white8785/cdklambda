from aws_cdk import Stack
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        self.build_lambda_one()
        self.build_lambda_two()

    def build_lambda_one(self):
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="LambdaOne",
            # Function name on AWS
            function_name="LambdaOne",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                directory="service_name/src/lambdas/LambdaOne"
            ),
        )
    def build_lambda_two(self):
        self.prediction_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="LambdaTwo",
            # Function name on AWS
            function_name="LambdaTwo",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                directory="service_name/src/lambdas/LambdaTwo"
            ),
        )