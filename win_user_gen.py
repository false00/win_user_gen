
import subprocess
from faker import Faker

def main():
  cmd = "net user /add{}".format(username)
  for _ in range(10000):
    try:
      username = fake.user_name
      run_win_cmd(cmd)
    except:
       print(username + ": already exists"

def run_win_cmd(cmd):
  result = []
  process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
  for line in process.stdout:
      result.append(line)
  errcode = process.returncode
  for line in result:
      print(line)
  if errcode is not None:
      raise Exception('cmd %s failed, see above for details', cmd)

if __name__ == "__main__": main()
