# Django Serverless Web Application

## Overview
This project demonstrates a serverless web application built using Django and AWS services such as Lambda, API Gateway, DynamoDB, S3, and CloudFront.

## Prerequisites
- AWS account
- AWS CLI configured with your AWS credentials
- Python 3.8 or later

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/django-serverless-webapp.git
    cd django-serverless-webapp
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

4. Configure Zappa:
    Update `zappa_settings.json` with your AWS region and S3 bucket.

5. Deploy the application:
    ```sh
    zappa deploy dev
    ```

6. Set up CloudFront:
    - Create a CloudFront distribution with your S3 bucket as the origin.
    - Update frontend URLs to use the CloudFront distribution domain.

7. Sync static files to S3:
    ```sh
    aws s3 sync main/templates s3://YOUR_S3_BUCKET_NAME
    ```

8. Open the CloudFront distribution URL in your browser to use the app.

## Cleaning Up
```sh
zappa undeploy dev

### License

MIT License