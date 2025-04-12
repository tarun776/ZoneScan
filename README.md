# 🛡️ZoneScan🛡️ - AWS Route 53 NS Vulnerability Detection Tool

**ZoneScan** is a Python tool designed to detect potential vulnerabilities in AWS Route 53 Hosted Zones' nameserver configurations. It scans domain NS (nameserver) records, identifies possible misconfigurations, and performs an automated test to check for DNS hijacking risks by interacting with AWS Route 53.

## Features

- **Multi-Domain Scanning**: Scan multiple domains listed in a file.
- **AWS Integration**: Automatically checks and interacts with AWS Route 53 using the AWS API.
- **NS Vulnerability Detection**: Identifies misconfigured or vulnerable NS records that could lead to DNS hijacking.
- **Detailed Output**: Color-coded output to highlight vulnerable and non-vulnerable domains.
- **AWS Key Validation**: Verifies if the AWS keys are valid and present before starting the scan.

## Prerequisites

- **AWS Account** with Route 53 access
- **Python 3.x** installed
- **Boto3** library (AWS SDK for Python)
- **AWS CLI** (optional but recommended for quick configuration)

### AWS Key Setup

Before running the tool, make sure your **AWS credentials** are properly set up.

### Option 1: **Set AWS Keys in the Environment Variables**

1. Set your AWS credentials using environment variables:

   ```bash
   export AWS_ACCESS_KEY_ID="your-access-key-id"
   export AWS_SECRET_ACCESS_KEY="your-secret-access-key"

- **Clone the repository:**
git clone https://github.com/your-username/ZoneScan.git
cd ZoneScan
pip install boto3


- **Usage**
Scan a Single Domain
You can scan a single domain for vulnerability detection by running:
``python ZoneScan.py --domain example.com``


- **Scan Multiple Domains from a File**
If you have a list of domains in a text file (domains.txt), use the following command to scan all of them:
``python ZoneScan.py --file domains.txt``
Each domain should be listed on a new line in the text file.

- **Force Delete Option**
The script will automatically clean up any created AWS Route 53 hosted zones. You can force delete the zones by using:
``python ZoneScan.py --file domains.txt --forceDelete``

- **Help Command**
To view the help and available options, use:
``python ZoneScan.py --help``

- **License**
This tool is provided under the MIT License.

- **Contributing**
Feel free to fork the repository, raise issues, or submit pull requests if you find bugs or have suggestions for improvement.

- **Contact**
For any questions or feedback, please contact us via GitHub Issues or email.

**Disclaimer**
This tool is intended for ethical security testing and vulnerability detection. It should only be used on domains that you own or have explicit permission to test. Unauthorized access to or manipulation of domains without consent is illegal and unethical.

