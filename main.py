import requests ,os,configparser


def cloudflare_authenticate(arg1):
    file_path = os.path.join(os.path.expanduser("~"), ".cloudflare", "ADAPTUREcloudflare.cfg")
    if not os.path.isfile(file_path):
        print("Error: ADAPTUREcloudflare.cfg not found.")
        return None

    config = configparser.ConfigParser()
    config.read(file_path)
    if "Cloudflare" not in config:
        print("Error: [Cloudflare] section not found in cloudflare.cfg.")
        return None


    cloudflare_section = config["Cloudflare"]
    email = cloudflare_section.get("email", None)
    api_key = cloudflare_section.get("key", None)
    
    if email is None or api_key is None:
        print("Error: email and/or key fields not found in the [Cloudflare] section.")
        return None

    return {"email": email, "api_key": api_key}


credentials = cloudflare_authenticate()
headers = {
            'Content-Type': 'application/json',
            'X-Auth-Email': credentials["email"],  
            'X-Auth-Key': credentials["api_key"] 
        }





zone_id= "01a2d4117396b781261eaa8345daad2c"
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/always_use_https"

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP error status codes

    # Process the response here
    print("Request was successful. Processing response...")
    
except requests.exceptions.HTTPError as http_err:
    # Handle HTTP errors (e.g., 404, 500, etc.)
    print(f"HTTP error occurred: {http_err}")
    
except requests.exceptions.ConnectionError as conn_err:
    # Handle connection errors (e.g., network issues)
    print(f"Connection error occurred: {conn_err}")
    
except requests.exceptions.Timeout as timeout_err:
    # Handle timeout errors (e.g., request took too long)
    print(f"Timeout error occurred: {timeout_err}")
    
except Exception as e:
    # Handle other exceptions that may occur
    print(f"An unexpected error occurred: {e}")
    

print("Request was successful")
print(response.json())







