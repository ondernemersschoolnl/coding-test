import sqlite3

#creating database
DatabaseConnection = sqlite3.connect("AuthLog.db")
DatabaseCutsor = DatabaseConnection.cursor()
DatabaseCutsor.execute("CREATE TABLE IF NOT EXISTS AuthLogs(Timestamp, SwitchHost, SwitchPort, SwitchMac, user, Vlan, Result, Reason)")
#res = DatabaseCutsor.execute("SELECT name FROM sqlite_master")
