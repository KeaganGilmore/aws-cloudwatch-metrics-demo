import boto3
import random
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration Variables
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')  # Default to 'us-east-1' if not set

def send_custom_metric(namespace, metric_name, dimensions, value, unit):
    """
    Sends a custom metric to AWS CloudWatch.

    :param namespace: Namespace for the metric (e.g., 'Application')
    :param metric_name: Name of the metric
    :param dimensions: List of dictionaries defining metric dimensions
    :param value: Value of the metric
    :param unit: Unit of the metric (e.g., 'None', 'Seconds', 'Count', etc.)
    """
    try:
        # Initialize CloudWatch client using credentials from environment variables
        cloudwatch = boto3.client(
            'cloudwatch',
            region_name=AWS_REGION,
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        # Put metric data
        response = cloudwatch.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': dimensions,
                    'Value': value,
                    'Unit': unit
                },
            ]
        )
        print(f"Successfully sent metric: {metric_name} with value: {value}")
    except Exception as e:
        print(f"Error sending metric: {e}")

if __name__ == "__main__":
    # Example usage
    NAMESPACE = 'Application'
    METRIC_NAME = 'Requests'
    DIMENSIONS = [
        {
            'Name': 'Endpoint',
            'Value': 'Home'
        }
    ]
    VALUE = random.randint(100, 1000)
    UNIT = 'Count'

    send_custom_metric(NAMESPACE, METRIC_NAME, DIMENSIONS, VALUE, UNIT)

    # Optional: Send multiple metrics over time
    # for _ in range(5):
    #     VALUE = random.randint(100, 1000)
    #     send_custom_metric(NAMESPACE, METRIC_NAME, DIMENSIONS, VALUE, UNIT)
    #     time.sleep(60)  # Wait for 60 seconds before sending the next metric
