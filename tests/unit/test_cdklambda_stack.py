import aws_cdk as core
import aws_cdk.assertions as assertions

from service_name.src.stacks.lambdas import CdklambdaStack


def test_lambda_function_created():
    app = core.App()
    stack = CdklambdaStack(app, "cdklambda")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
        "VisibilityTimeout": 300
    })