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

## How It Works

- A linear machine learning model calculates a score using a predefined weight and bias.  
- Based on the calculated score, the model generates a binary prediction.  
- The inference logic runs inside an AWS Lambda function.  
- Amazon API Gateway forwards HTTP POST requests to the Lambda function.  
- The Lambda function returns the prediction as a JSON response.

## Outcome

The project successfully demonstrates end-to-end deployment of a machine learning model as a REST API using AWS Lambda. The serverless architecture ensures scalability, low operational cost, and ease of deployment. The API works correctly and returns predictions when tested using curl from the local system.

## Conclusion

This project provides a clear example of deploying a machine learning model as a REST API using AWS serverless services, making machine learning inference accessible through HTTP endpoints without managing servers.

**Request Body:**
```json
{
  "input": 4
}

## Response
```json
{
  "input": 4.0,
  "score": 1.2000000000000002,
  "prediction": 1
}


