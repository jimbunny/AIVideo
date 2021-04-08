import requests
import base64
f = open('bb.wav','rb+')
sound_wav_rb = f.read()
f.close()
print(sound_wav_rb)
encodestr = base64.b64encode(sound_wav_rb)
print(str(encodestr,'utf-8'))

url = "http://ltalk.speech.sogou.com/index.lt?*fB6qfA4zge6qTYR9RYKoDBJeRYh5TBV7EIR0TYGoDeWqDBAmSoV6RnE5jCGqC70aUYJ7SIJ7OrKdEBJ4RHEnDCSqC70aUXEeiLKdiK45fB6qUYJ7RYheReJ7RYJdRIlrh7AciBAzD7Akgr34RXE7g7qoEA4xEB0siLl4RYZ6SdEdECS6gMWkDB6aiB05UYZrD7KzD7AxUYFrio5cRINeOr0qiK45jCGqUYZrhLKdiLqmgI5cOsGmD7ymE7AkgrKyEY6og75zh74tiX0ugsG6iL6qiLmaEH0eg7iaiXEugsG6iK45jCGqUYJrDBS5fB4zC8W0hLZ4RHE5g7yqgo5bOsSuUYFrDBS5fB4zC8WugBZ4RYDcSeReRYDbTYh9RdEmgrWdg7qpC7qpUXEugBAuC8OqErAdEB0oEY5rgBKoC7KpEMOqh8R4Orqyh7p4OsWqjMWkgLKzEe61fH6ogB9yfLKzhdEbDCSehL4diLqpUB06gLbrD74ziLKoiLyqjY5qS5RqS5SqTYR9RYKoDBJeRYh5TBV7EIR0TYGoDeWqDBAmSoV6RnZ8VdZ8VdEofMAah7qsgo5cOrK6ELqaC8W0hLZ4RXEqgsWdjA45jCGqUYF="
headers = {"s-cookie": "ArUk9DpgoPStApbYCINjUEGwlBDOEfZeeX+dnZOYNWqUwqxPujzDfdvosb+KtDum9+AC0U/nIAdEaAprgMRxuUNYSyysCcYCaPY3LCjxrqiIrZsHEqiq8xuT5QlmO+O1SzQh5Ivs6J3TBCfUqrzVuwiKSAjjJ/qdHknAYSWS1PjKJkwvTSBBVzNAi+fkiitulaAdli/l9vdpM8dZd1cxAN3uU2lhOUlQkBOEsD977DZQv7vbxbyniW+OrHvk9vfkl5ReEbiFlGlOHFloMeZkN7MpKE1uyphjnJHywQiVonzL4CEt6hQlp+2t6P7ybt46",
           "x-cookie": "LWB2ekLKjya86nNDV6MhaRZ1SugQZK5zY2iiFdPzcCpUsNuoEmfC8mqpSUZS8ZT9lN6g24Oz0GpUMv35mWnHa/pUVZzcvWzlIVH4O9mB2SdvPxHdxgZWfWVRAdXykBZfrKvDrJ94Cep0N1fIBvfEJNEom7yKnQnVp9Hc7Q4HFetrw6fJri3tLYSFkwDA0Q6ycP6oSdBVwQ7fxRGULV93V5MU+Gp/gch6Y6HyDfaXebEnu9vmhP0+cnQxVoW4Ytwu",
           "accept-charset": "gbk", "Content-Type": "text/x-markdown; charset=utf-8", "Transfer-Encoding": "chunked",
           "Host": "ltalk.speech.sogou.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.11.0"}
r = requests.post(url,data= "voice_content=")
print(r.status_code)
print(r.content)