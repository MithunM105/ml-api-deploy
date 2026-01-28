# ml-api-deploy
Deploying an ML Model as REST API on AWS Lambda
# Deploying an ML Model as REST API on AWS Lambda

This project demonstrates deploying a simple machine learning model as a REST API using AWS Lambda and Amazon API Gateway.

## Description
A lightweight linear machine learning model is implemented to perform inference on input data. The model logic runs inside an AWS Lambda function and is exposed through a REST API using Amazon API Gateway. The API accepts JSON input and returns predictions in real time. The endpoint is tested using POST requests from the local command prompt with curl.

## Technologies Used
- Python
- AWS Lambda
- Amazon API Gateway (REST API)
- curl (for testing)

## API Usage
**POST** `/predict`

**Request Body:**
```json
{
  "input": 4
}
