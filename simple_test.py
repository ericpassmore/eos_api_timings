import requests
import time

# path of the command to fetch
path = '/v1/chain/get_info'

# Mapping for HTTP versions, defined by HTTP standard
http_versions = {
    9: '0.9',
    10: '1.0',
    11: '1.1',
    20: '2',
}

# errors array
errors = []
# good response array
replies = []

# Open the file
with open('endpoints.txt', 'r') as file:
    # Loop over each line (URL) in the file
    for url in file:
        # Strip off any leading/trailing whitespace
        # add on the specific path
        url = url.strip() + path

        try:
            # start timer
            start_time = time.time()
            # Send a GET request to the URL
            response = requests.get(url)
            # end timer
            elapsed_time = time.time() - start_time
            rounded_elasped_time_in_ms = round(elapsed_time*1000)

            # check for good status
            if response.status_code == 200:
                # Parse the JSON data from the response
                data = response.json()
                replies.append(f"URL:{url} \
Version:{data['server_version_string']} \
HTTP_Version:{http_versions.get(response.raw.version, 'unknown')} \
Request_time_ms:{rounded_elasped_time_in_ms} \
chain_id:{data['chain_id']} \
head_block_num:{data['head_block_num']}")

            else:
                # Print the status code
                errors.append(f"Bad Request Failed with status : {response.status_code} for URL: {url}")

        except requests.exceptions.RequestException as e:
            errors.append(f"An error occurred for URL: {url}. Exception: {e}")

print ('\n'.join(replies))
print ('\n'.join(errors))
