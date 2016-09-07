from pyparsing import Word, alphas, Suppress, Combine, nums, string, Optional, Regex
from time import strftime
import datetime

class Parser(object):
  def __init__(self):
    ints = Word(nums)

    # timestamp
    month = Word(string.uppercase, string.lowercase, exact=3)
    day   = ints
    hour  = Combine(ints + ":" + ints + ":" + ints)

    timestamp = month + day + hour

    # hostname
    hostname = Word(alphas + nums + "_" + "-" + ".")

    # appname
    appname = Word(alphas + "/" + "-" + "_" + ".") + Optional(Suppress("[") + ints + Suppress("]")) + Suppress(":")

    # message
    message = Regex(".*")

    # pattern build
    self.__pattern = timestamp + hostname + appname + message

  def parse(self, line):
    parsed = self.__pattern.parseString(line)
    payload              = {}
    delta1 =  datetime.datetime.now() - datetime.timedelta(minutes=30)
    thisyear = datetime.datetime.now().strftime('%Y')
    loggedtime_str = thisyear + " " + parsed[0] + " " + parsed[1] + " " +  parsed[2]
    loggedtime = datetime.datetime.strptime(loggedtime_str, '%Y %b %d %H:%M:%S')
    if  loggedtime > delta1:
        payload["timestamp"] = loggedtime.strftime("%b %-d %H:%M:%S")
        payload["hostname"]  = parsed[3]
        payload["appname"]   = parsed[4]
        payload["message"]   = parsed[5]
        return payload

""" --------------------------------- """

def main():
  parser = Parser()

  with open('./syslog') as syslogFile:
    for line in syslogFile:
      fields = parser.parse(line)
      if fields != None:
        if fields['appname'] == 'kernel' and 'disabling' in fields['message']:
          print "parsed:", fields

if __name__ == "__main__":
  main()
