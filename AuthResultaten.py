import sqlite3

#creating database
DatabaseConnection = sqlite3.connect("AuthLog.db")
DatabaseCutsor = DatabaseConnection.cursor()
DatabaseCutsor.execute("CREATE TABLE IF NOT EXISTS AuthLogs(Timestamp, SwitchHost, SwitchPort, SwitchMac, user, Vlan, Result, Reason)")
#res = DatabaseCutsor.execute("SELECT name FROM sqlite_master")
#parsing auth-log.txt to database
with open("auth_log.txt") as AuthBestand:
  for AuthRecord in AuthBestand:
    #print(AuthRecord)
    #zin = AuthBestand.readline()
    #zin = AuthBestand.readline()
    #zin = AuthBestand.readline()
    RecordValues = AuthRecord.split()
    RecordLength = len(RecordValues)
    RecordTulple = tuple(RecordValues)
    #print(RecordTulple)
    #print(RecordLength)
    if RecordLength == 7:
    #    print("Has no reson field")
        RecordValues.append("accepted")
        RecordTulple = tuple(RecordValues)
        #print(RecordTulple)
        DatabaseCutsor.execute("INSERT INTO AuthLogs VALUES (:Timestamp, :SwitchHost, :SwitchPort, :SwitchMac, :user, :Vlan, :Result, :Reason)", RecordTulple)

    elif RecordLength == 8:
    #   print has reason field
        DatabaseCutsor.execute("INSERT INTO AuthLogs VALUES (:Timestamp, :SwitchHost, :SwitchPort, :SwitchMac, :user, :Vlan, :Result, :Reason)", RecordTulple)
#result = DatabaseCutsor.execute("SELECT * FROM AuthLogs")
#print(result.fetchall())

