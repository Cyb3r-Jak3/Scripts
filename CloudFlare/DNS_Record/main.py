import requests

base_url = "https://api.cloudflare.com/client/v4/zones/"


def get_auth_headers():
    choice = input("Are you using your global API key or an API token:\n[1] Global Key\n[2] API Token\n>")
    if choice == "1":
        key = input("Please enter your API Key:\n")
        email = input("Please enter the email address associated with the API key:\n")
        return({"X-Auth-Email": email, 'X-Auth-Key': key, "Content-Type": "application/json"})
    if choice == "2":
        key = input("Please enter the API Token (without Bearer):\n")
        email = input("Please enter the email address associated with the API key:\n")
        return {'Authorization': "Bearer " + key, "X-Auth-Email": email, "Content-Type": "application/json"}

def get_zone():
    z = input("Please enter the Zone ID that you want to edit:\n")
    return z

def create_dns_record(zone):
    record = {}
    choice = input("Please enter the type of record that you are trying to create:\n(Currently support are A, SRV, SSHFP, CAA)\n").lower()
    if choice == "a":
        name = input("Please enter the URL:\n")
        dest = input("Please enter the destination IP address\n")
        record["type"] = "A"
        record["name"] = name
        record["content"] = dest
        record["proxied"] = True

    if choice == "srv":
        data = {}
        data['service'] = input("Please enter the service: (remember the underscore)\n")
        data['proto'] = input("Please enter the protocol: (remember the underscore)\n")
        data['name'] = input("Please enter the name:\n")
        data['priority'] = int(input("Please enter the priority:\n"))
        data['weight'] = int(input("Please enter the weight:\n"))
        data['port'] = int(input("Please enter the port:\n"))
        data['target'] = input("Please enter the target:\n")
        record['type'] = "SRV"
        record['data'] = data
    if choice == "sshfp":
        data= {}
        record['name'] = input("Please input the name\n")
        data['algorithm'] = int(input("Please enter the Algorithm as an int:\n"))
        data['type'] = int(input("Please enter the type as an int:\n"))
        data['fingerprint'] = input("Please enter the fingerprint:\n")
        record['type'] = 'SSHFP'
        record['data'] = data
    if choice == "caa":
        data = {}
        record['name'] = input("Please input the name:\n")
        data['tag'] = input("Please enter 'issue', 'issuewild' or 'iodef':\n")
        data['value'] = input("Please enter the domain of the certificate authority or the email to report to:\n")
        data['flags'] = 0
        record['type'] = "CAA"
        record['data'] = data

    api_url = base_url+zone+"/dns_records"
    r = requests.post(api_url, json=record, headers=headers)
    output = r.json()
    if not output['success']:
        print("There was an error\n")
        print(output['errors'])
    if output['success']:
        print("The record was created successfully")
#            print(output)



try:
    import info
    headers = {'X-Auth-Key': info.auth_key, "X-Auth-Email": info.auth_email, "Content-Type": "application/json"}
    zone = info.zone_id
except AttributeError:
    headers = {'Authorization': info.authorization, "X-Auth-Email": info.auth_email, "Content-Type": "application/json"}
    zone = info.zone_id
except SyntaxError:
    headers = get_auth_headers()
    zone = get_zone()
print(headers)
create_dns_record(zone)
