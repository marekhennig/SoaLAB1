from suds.client import Client
url = "http://localhost:8088/mockApiPortSoap11?WSDL"
client = Client(url)
register_call = client.service.registerCall("Marek Hennig")
results = client.service.results("Marek Hennig")
print("Register_call:")
print("Name: "+register_call.name)
print("Note: "+register_call.note)
print("Results:")
print('\n'.join(results))


