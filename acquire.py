

### Functions

url = 'https://swapi.dev/api/people/5'
response = requests.get(url)

data = response.json()

root_url = 'https://swapi.dev/api/'
response = requests.get(root_url)

df = pd.DataFrame(data['results'])

response = requests.get(data['next'])
data = response.json()

pd.concat([df, pd.DataFrame(data['results'])]).reset_index()

# you can build on a 'base_url'
base_url = "https://swapi.dev/api/"

base_url + "people/"

# Use a base_url to get to a certain endpoint and specify it's pagination.
ppl_url = base_url + "people/"
requests.get(ppl_url + "?page=8").json()