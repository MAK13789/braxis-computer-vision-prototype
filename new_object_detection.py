import Algorithmia
f = open("apikey.txt", "r")
apiKey = f.readline()
input = {
  "image": [
    "http://i.imgur.com/GtvDM8X.jpg"
  ],
  "model": "small",
  "tags_only": False
}
client = Algorithmia.client(apiKey)
algo = client.algo('algorithmiahq/DeepFashion/1.5.1')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)