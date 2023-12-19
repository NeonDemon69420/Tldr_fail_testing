import os

list = ["google.mu", "myt.mu", "mcb.mu", "okta.com", "topfmradio.com", "freshdesk.com", "govmu.org", "lexpress.mu",
        "inside.news", "intnet.mu", "priceguru.mu", "myjob.mu", "mauritiustelecom.com", "gceguide.com", "vbazz.com"]


for item in list:
    command = "python3 tldr_fail_test.py " + item
    print(command)
    os.system(command=command)
    print("---------------------------------------------------")