**# TLDR Fail Testing for IP Addresses in Mauritius**

**This repository contains scripts for testing the prevalence of the TLDR Fail vulnerability in websites hosted on IP addresses within Mauritius.**
## Overview
This project was made possible due to the help of [Cyberstorm.mu](cyberstorm.mu). 

Our projects analyses the readyness of Mauritius' against Quantum Computing. As many of you may know, Quantum Computing will be a game changer in the world of IT. 
This project checks if the the websites in Mauritius uses the latest version of TLS and if the TLS was correctly implemented using David Benjamin's code ([source of the tldr_fail_test.py](https://gist.github.com/dadrian/f51e7f96aa659937775232cc3576e5f8#file-tldr_fail_test-py)).
## About TLDR Fail

* Explanation of TLDR Fail: [https://tldr.fail](https://tldr.fail)

## Scripts and Functionality

**Key Scripts:**

* `tldr_fail_test.py`: Tests for the TLDR Fail vulnerability ([source link](https://gist.github.com/dadrian/f51e7f96aa659937775232cc3576e5f8))
* `test_for_port.py`: Scans IP addresses for open ports 80 and 443
* `test_vulnerability.py`: Runs `tldr_fail_test.py` on IPs with open ports and saves results
* `classify_ip_addresses.py`: Classifies vulnerable IP addresses by provider
* `test_popular_websites.py`: Tests 47 popular websites for the vulnerability using different ISPs

**Workflow:**

1. **IP Address Collection:**
   - IP ranges for Mauritius are obtained from [https://lite.ip2location.com/mauritius-ip-address-ranges](https://lite.ip2location.com/mauritius-ip-address-ranges)
2. **Port Scanning:**
   - `test_for_port.py` scans IPs for open ports and saves results to CSV files
3. **Vulnerability Testing:**
   - `test_vulnerability.py` runs `tldr_fail_test.py` on IPs with open ports 80 and 443
   - Results are saved to text files in `./results/vulnerability_result`
4. **IP Address Classification:**
   - `classify_ip_addresses.py` classifies vulnerable IPs by provider
5. **Popular Website Testing:**
   - `test_popular_websites.py` tests 47 popular websites using different ISPs
   - Results are saved to files in `./results/classified_by_provider`

## Results

* See `./results` for detailed results, including:
    - Lists of vulnerable and non-vulnerable IP addresses
    - Vulnerability overview and percentage error
    - Classification of vulnerable IPs by provider
    - Results of popular website testing by ISP

## Usage

1. Clone this repository
2. Run the scripts in the following order:
   - `test_for_port.py`
   - `test_vulnerability.py`
   - `classify_ip_addresses.py` (optional)
   - `test_popular_websites.py` (optional)
3. View the results in the `./results` directory

## Dependencies

* Python 3
* Pandas
