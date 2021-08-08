# learning_fastapi_aws_lambda_deployment
Learning FastAPI AWS Lambda Deployment

### List of commands used (OS - Ubuntu):

```python3 -m venv venv```

```source venv/bin/activate```

```pip install uvicorn```

```pip install fastapi```

```uvicorn api.main:app --reload```

```pip install requests```

```pip install pytest```

```pytest```

```pip install mangum```

```pip freeze > requirements.txt```


## Note:
1. Make Sure to keep the region of S3 bucket creation is same as that for the Lambda function creation on the AWS console since we are only using a common secret variable 'secrets.AWS_DEFAULT_REGION' for region for both of them.