## AWS CloudWatch Metrics

This project demonstrates how to send custom metrics to AWS CloudWatch using Python. It utilizes the `boto3` library to interact with AWS services and `python-dotenv` to manage environment variables.

## Features

- Send custom metrics to AWS CloudWatch
- Configure metrics with namespaces, names, dimensions, values, and units
- Load AWS credentials and region from a `.env` file

## Requirements

- Python 3.12 or higher
- `boto3` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/KeaganGilmore/aws-cloudwatch-metrics.git
    cd aws-cloudwatch-metrics
    ```

2. Install dependencies:
    ```sh
    pip install poetry
    poetry install
    ```

3. Create a `.env` file in the project root and add your AWS credentials:
    ```dotenv
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    AWS_REGION=your_aws_region
    ```

## Usage

1. Run the script:
    ```sh
    poetry run python main.py
    ```

2. The script will send a custom metric to AWS CloudWatch with the specified configuration.

## Configuration

You can configure the metric details in the `main.py` file. The following parameters can be adjusted:

- `NAMESPACE`: The namespace for the metric (e.g., 'Application')
- `METRIC_NAME`: The name of the metric (e.g., 'Requests')
- `DIMENSIONS`: A list of dictionaries defining metric dimensions
- `VALUE`: The value of the metric (e.g., a random integer between 100 and 1000)
- `UNIT`: The unit of the metric (e.g., 'Count')

## License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for details.

## Contact

- **Email:** [keagangilmore@gmail.com](mailto:keagangilmore@gmail.com)
- **Discord:** [keagan2980](https://discord.com/users/keagan2980)