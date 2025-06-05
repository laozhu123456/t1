# -*- coding: utf-8 -*-
import time;
import os;
import sys;

class dict1(dict):
  def __setattr__(self, k,v):
    self[k] = v if not isinstance(v, dict) else dict1(v);
  def __getattr__(self, k):

    v = self.get(k);
    if( isinstance(v, dict )):
      v = dict1(v);
      self[k] = v;
    return  v;



def format(str, *args):
    return str %args;
def printf(*args):
    count = len(args);
    if(count==1):
        print (args[0]);
    else:
        print (args);
def pf(*args):
    count = len(args);
    if(count==1):
        print (args[0]);
    else:
      if( isinstance( args[0], str ) and args[0].find("%") != -1):
        print (args[0] %args[1:]);   
      else:
        print (args);


true=True;
false = False;
none = None;
null = None;
enum = enumerate;


s1 = '''serverAddr = "frp.freefrp.net"
serverPort = 7000
auth.method = "token"
auth.token = "freefrp.net"

[[proxies]]
name = "__name__"
type = "tcp"
localIP = "127.0.0.1"
localPort = 51000
remotePort = __rp__
'''

def main2():  
  #create frp config txt
  tm = time.strftime("cnn_%Y%m%d%H%M%S");
  s2 = s1.replace("__name__", tm);
  rp = "31235";
  if(len(sys.argv)>1):
    rp = sys.argv[1];
  s2 = s2.replace("__rp__", rp);
  
  f = open("frpc_h2.txt", "w");
  f.write(s2);
  f.close();
  pf("------make frpc config");

  #make frp
  os.system("cat frpc_h2.txt");  
  pf("------oooooook");  

main2();
