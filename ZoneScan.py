import os
import sys
import dns.resolver
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import route53

# Function to check if AWS keys are valid
def validate_aws_keys():
    try:
        # Using Boto3 to create a Route53 client
        client = boto3.client(
            'route53',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )
        
        # Try to get hosted zones to verify if the credentials are valid
        client.list_hosted_zones()
        return True  # If no exception, keys are valid
    
    except (NoCredentialsError, PartialCredentialsError):
        print("\033[91mInvalid AWS credentials! Please check your AWS keys.\033[0m")
        return False
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        return False

# Function to check if domain is vulnerable
def check_vulnerability(domain):
    targetNS = []
    nsRecords = []

    # Fetch NS records
    try:
        nsRecords = dns.resolver.resolve(domain, 'NS')
    except Exception as e:
        print(f"Unable to fetch NS records for {domain}. Skipping.")
        return None

    for nameserver in nsRecords:
        targetNS.append(str(nameserver.target).strip("."))

    # Connect to AWS Route 53
    conn = route53.connect(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    )

    vulnerable = False
    try:
        # Try creating a hosted zone on AWS
        new_zone, change_info = conn.create_hosted_zone(domain, comment='zaheck')
        if new_zone:
            nsAWS = new_zone.nameservers
            intersection = set(nsAWS).intersection(set(targetNS))
            if intersection:
                vulnerable = True
            else:
                new_zone.delete()
    except Exception as e:
        print(f"Error while checking vulnerability for {domain}: {e}")

    return vulnerable

# Read domains from file
def read_domains_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Main function to loop through all domains in the file
def main():
    # Ensure file path is provided
    if len(sys.argv) < 3 or sys.argv[1] not in ["--file"]:
        print("Usage: python script.py --file domain.txt")
        sys.exit(1)

    # Validate AWS credentials first
    if not validate_aws_keys():
        sys.exit(1)

    file_path = sys.argv[2]
    domains = read_domains_from_file(file_path)

    for domain in domains:
        print(f"Checking domain: {domain}")
        is_vulnerable = check_vulnerability(domain)

        if is_vulnerable:
            print(f"\033[91m{domain} is Vulnerable\033[0m")  # Red color for vulnerable
        else:
            print(f"\033[92m{domain} is Not Vulnerable\033[0m")  # Green color for not vulnerable

if __name__ == "__main__":
    main()

