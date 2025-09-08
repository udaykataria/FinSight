import boto3
import json
from datetime import datetime, timedelta
import os


def main():
    # AWS Cost Explorer client
    ce = boto3.client('ce')

    # Yesterday's date range
    end = datetime.utcnow().date()
    start = end - timedelta(days=1)

    # Fetch daily cost
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    # Extract amount
    amount = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']

    # Prepare JSON
    data = {
        "date": str(start),
        "cost": amount
    }

    # Ensure folder exists
    os.makedirs("daily-costs", exist_ok=True)

    # Save to file
    file_path = f"daily-costs/{start}.json"
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved daily cost to {file_path}")


if __name__ == "__main__":
    main()
