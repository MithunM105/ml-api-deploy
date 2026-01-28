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

Response
{
  "input": 4.0,
  "score": 1.2,
  "prediction": 1
}

How It Works

A machine learning model performs inference using a linear equation.

The logic is implemented inside an AWS Lambda function.

API Gateway forwards HTTP POST requests to Lambda.

Lambda returns the prediction as a JSON response.

Outcome

This project successfully demonstrates end-to-end deployment of a machine learning model as a REST API using AWS serverless services.
