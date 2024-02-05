import subprocess

website_list = ["google.mu", "myt.mu", "mcb.mu", "okta.com", "topfmradio.com", "freshdesk.com", "govmu.org", "lexpress.mu",
        "inside.news", "intnet.mu", "priceguru.mu", "myjob.mu", "mauritiustelecom.com", "gceguide.com", "vbazz.com",
        "mauritiusturfclub.com", "uom.ac.mu", "lemauricien.com", "france24.com", "newsnow.co.uk", "ib.mcb.mu",
        "moodfeed.net", "pixhost.to", "journee-mondiale.com", "frappe.cloud", "partsouq.com", "riddimsworld.com",
        "fnb.co.za", "naukrigulf.com", "airmauritius.com", "spikbuy.network", "sfimg.com", "mra.mu", "mega.mu",
        "instantly.ai", "ifvod.tv", "refinitiv.com", "mycar.mu", "canalplus.com", "devskiller.com", "Ebmu.sbmgroup.mu",
        "Cyberstorm.mu", "triobelisk.bandcamp.mu", "outputmessage.bandcamp.mu", "curtinmauritius.ac.mu", "abcbanking.mu",
        "radiologymauritius.mu"]

error_list = []
site_count = len(website_list)
print(f"Number of Website to check: {site_count}")

for website in website_list:
      print(f"Checking website {website}")
      try:
            result = subprocess.run(["python3", "./tldr_fail_test.py", website], stdout=subprocess.PIPE, text=True, timeout=10)
            if "[WinError 10054]" in result.stdout or "Errno" in result.stdout:
                error_list.append(website)
      except subprocess.TimeoutExpired:
            error_list.append(website)

with open("./results/popular_website_result/isp.txt", "w") as file:
      file.write(f"Total number of website: {site_count}\n")
      file.write(f"List of website: {website_list}\n")
      file.write(f"Number of errors: {len(error_list)}\n")
      file.write(f"List of website with errors: {error_list}\n")
      file.write(f"Percentage of error: {(len(error_list)/site_count)*100}\n")