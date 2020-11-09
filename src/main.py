import time
from godaddypy import Client, Account
import requests

import config


def main():
    account = Account(api_key=config.GODADDY_KEY,
                      api_secret=config.GODADDY_SECRET)
    client = Client(account)

    # Check that user owns the specified domain
    domains = client.get_domains()
    print("INFO: Checking target domain ownership.")
    if domains.count(config.GODADDY_DOMAIN) != 1:
        raise AssertionError("ERROR: User must own the domain specified.")

    print("INFO: Retrieving currentIP.")
    currentIP = client.get_records(
        config.GODADDY_DOMAIN, record_type="A", name="@")[0]["data"].strip()
    print("INFO: currentIP retrieved.")

    # main update loop
    while True:
        try:
            print("INFO: Retrieving publicIP.")
            publicIP = requests.get("http://ip.42.pl/raw").text.strip()
            print("INFO: publicIP retrieved.")
        except:
            print("ERROR: Could not fetch public IP!")

        print("INFO: Checking publicIP against currentIP")
        if publicIP != currentIP:
            print(
                f"INFO: IP out of date. Updating current IP to: {publicIP}.")
            try:
                client.update_ip(publicIP, domains=[
                    config.GODADDY_DOMAIN])
                currentIP = publicIP
                print(f"INFO: IP update successful.")
            except:
                print("ERROR: Could not update IP!")

        # Pause execution for UPDATE_INTERVAL seconds.
        time.sleep(config.UPDATE_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKill signal recieved. Terminating...")
