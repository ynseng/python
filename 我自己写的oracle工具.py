import cx_Oracle
import os
import sys
os.environ['NLS_LANG'] ='AMERICAN_AMERICA.ZHS16GBK';

connectresult=0;
promptstr="";
fetchsize=50;
#conn = cx_Oracle.connect('yzs/yzs@mydb');
print("------------Welcome To Python Sqlplus ----------------------");
print("|  Version     : 0.1");
print("|  Author      : johnny");
print("|  Release Date: 2011-08-08");
print("|  Login Example1:username/password@tnsname");
print("|  Login Example2:username/password@host:port/dbname");
print("|  Input exit to Quit");
print("-----------------------------------------------------------");
print("");

def getConnect(loginstr):
  global connectresult
  global promptstr
  try:
    connectresult=0;
    promptstr="";
    dsn_tns = cx_Oracle.makedsn('10.111.124.71', 1521,'ems');
    conn=cx_Oracle.connect('emw','emw',dsn_tns);
    #conn= cx_Oracle.connect(loginstr);
    promptstr=conn.username+"@"+conn.dsn;
    print("Database version:",conn.version);
    print("Connected.");
    connectresult=1;
    return conn
  except cx_Oracle.InterfaceError as exc:
    error, = exc.args
    print(exc);
  except cx_Oracle.DatabaseError as exc:
    error, = exc.args
    print(error.message);

def getcolformatstr(coldef):
  if coldef[1]==cx_Oracle.NUMBER:
    formatstr='%12s';
  else:
    if coldef[2]<=32:
      formatstr='%-'+str(coldef[2])+'s';
    else:
      formatstr='%-32s';
  return formatstr
  
#########################################################################
while 1:
  try:
    loginstr=raw_input("login>").strip();
    if loginstr=="" :
      continue;
    elif loginstr in ["exit","exit;"]:
      print("...bye...");
      exit();    
    conn = getConnect(loginstr);
    if connectresult==1:
      break;
  except KeyboardInterrupt:
    print("^C");
    continue;  
while 1:
  sqlstr="";
  try:
    sqlstrline=raw_input(promptstr+">").strip();
    if sqlstrline=="" :
      continue;
    elif sqlstrline.lower() in ["exit","exit;"]:
      print("...bye...");
      exit();
    elif sqlstrline[0:7].lower()=="connect" :
      conn = getConnect(sqlstrline[8:]);
    elif sqlstrline.lower() in ["disconnect","disconnect;"] :
      conn.close();
      print("Connection closed.");
    elif sqlstrline[0:4].lower()=="host" :
      os.system(sqlstrline[4:])
    else:
      sqlstr=sqlstr+sqlstrline+'\n';
      while sqlstrline[-1]!=";" :
        sqlstrline=raw_input().strip();
        sqlstr=sqlstr+sqlstrline+'\n';
      sqlstr=sqlstr[0:len(sqlstr)-2]
      try:
        cursor = conn.cursor();
        cursor.execute(sqlstr);
        if sqlstr[0:6].lower()=="select" :
          cols=[]
          for col in cursor.description:
            print(getcolformatstr(col) % (col[0])),
          print('');
          for col in cursor.description:
            if col[1]==cx_Oracle.NUMBER:
              print('-'*12),;
            else:
              if col[2]<=32:
                print('-'*col[2]),;
              else:
                print('-'*32),;
          print('');
          recs = cursor.fetchmany(fetchsize);
          while len(recs)>0:
            for row in recs:
              for i in range(len(row)):
                if row[i]!=None:
                  print(getcolformatstr(cursor.description[i]) % row[i]),;
                else:
                  print(getcolformatstr(cursor.description[i]) % ''),;  
              print('')
            recs = cursor.fetchmany(fetchsize);
          print(str(cursor.rowcount)+" rows selected.");
        elif sqlstr[0:6].lower()=="insert" :
          print(str(cursor.rowcount)+" rows inserted.");
        elif sqlstr[0:6].lower()=="update" :
          print(str(cursor.rowcount)+" rows updated.");
        elif sqlstr[0:6].lower()=="delete" :
          print(str(cursor.rowcount)+" rows deleted.");
        elif sqlstr[0:5].lower()=="merge" :
          print(str(cursor.rowcount)+" rows merged.");
        elif sqlstr[0:6].lower()=="commit" :
          print("Commit complete.");
        elif sqlstr[0:6].lower()=="rollback" :
          print("Rollback complete.");
        else :
          print("sql execute complete.");
      except cx_Oracle.InterfaceError as exc:
        error, = exc.args
        print(exc);
      except cx_Oracle.DatabaseError as exc:
        error, = exc.args
        print(error.message);
  except KeyboardInterrupt:
    print("^C");
    continue;  
  
  