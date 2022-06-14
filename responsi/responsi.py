import requests
import json

def is_json(djson):
  try:
    json.loads(djson)
  except ValueError as e:
    return False
  return True

def parsing(djson):
  res = djson["data"]
  fields = djson["data"]["fields"]
  str = ""
  for key in fields:
    str += key + ", "
  return str[:-2]
  
def save_to_file(filename, content):
  try:
    f = open(filename, "w")
    f.write(content)
    f.close()
    return True
  except OSError as e:
    print("Terjadi kesalahan ketika menyimpan file", str(e))

try:
  f = open("url.md", "r")
  url = f.read()
  filename = url.split("?")[0].split("/")[-1] + ".json"

  print("Proses request dari url..")
  req = requests.get(url)

  if req.status_code == 200:
    if is_json(req.text):
      res = req.json()
      print("Berhasil melakukan request data!")
      print("Entitas data:", parsing(res))
      print()

      print("Proses menyimpan data kedalam file..")
      if save_to_file(filename, req.text):
        print("Data tersimpan dengan nama file", filename)
    
    else:
      print("Tipe File tidak didukung!")

  else:
    print("Gagal melakukan request, cek kembali url!")

except Exception as e:
  print("Terjadi kesalahan", str(e))