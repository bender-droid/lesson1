import json

file = """
{
  "response": [
    {
      "id": 210700286,
      "first_name": "Lindsey",
      "last_name": "Stirling"
    },
    {
      "id": 297428682,
      "first_name": "Jared",
      "last_name": "Leto"
    }
  ]
}
"""

data = json.loads(file)

value_1 = data['response']
# print(value_1)

for item in value_1:
    print(item['id'])
