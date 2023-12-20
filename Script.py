import os
Error_Count = 0


list = ["google.mu", "myt.mu", "mcb.mu", "okta.com", "topfmradio.com", "freshdesk.com", "govmu.org", "lexpress.mu",
        "inside.news", "intnet.mu", "priceguru.mu", "myjob.mu", "mauritiustelecom.com", "gceguide.com", "vbazz.com",
        "mauritiusturfclub.com", "uom.ac.mu", "lemauricien.com", "france24.com", "newsnow.co.uk", "ib.mcb.mu",
        "moodfeed.net", "pixhost.to", "journee-mondiale.com", "frappe.cloud", "partsouq.com", "riddimsworld.com",
        "fnb.co.za", "naukrigulf.com", "airmauritius.com", "spikbuy.network", "sfimg.com", "mra.mu", "mega.mu",
        "instantly.ai", "ifvod.tv", "refinitiv.com", "mycar.mu", "canalplus.com", "devskiller.com", "Ebmu.sbmgroup.mu",
        "Cyberstorm.mu", "triobelisk.bandcamp.mu", "outputmessage.bandcamp.mu", "curtinmauritius.ac.mu", "abcbanking.mu",
        "radiologymauritius.mu"]

error_list = []
Site_count = len(list)
print(f"Number of Website to check: {Site_count}")


for item in list:
    command = "python3 tldr_fail_test.py " + item
    print(command)
    if os.system(command=command) != 0:
        Error_Count +=1
        error_list.append(item)


file = open("OutText.txt", "w")
file.write(f"Total number of website: {Site_count}\n")
file.write(f"List of website: {list}\n")
file.write(f"Number of errors: {Error_Count}\n")
file.write(f"List of website with errors: {error_list}\n")
file.write(f"Percentage of error: {(Error_Count/Site_count)*100}\n")

file.close()