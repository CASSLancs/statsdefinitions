
SOURCE = "https://jackdunncodes.github.io/statsdefinitions"

import sqlite3, sys, urllib.request
localSqlitePath = sys.argv[1]

localHash = "MISSING"

def getLocalHash():
    conn = sqlite3.connect(localSqlitePath)
    cur = conn.cursor()
    res = cur.execute("SELECT value FROM metadata WHERE fieldName = 'commithash'")
    return res.fetchone()[0].strip()

try:
    localHash = getLocalHash()
except Exception as e:
    print(e)
    overwrite = "x"
    while not (overwrite in ["y", "n"]):
        overwrite = input("Perhaps you don't have it downloaded. Download a fresh one right now? Will overwrite any existing file.\n[Y]es/[N]o >").lower()
    if overwrite == "n":
        raise e
        exit()
print("Local:\t"+localHash)

res = urllib.request.urlopen(SOURCE+"/commithash.txt")
remoteHash = res.read().decode().strip()
print("Remote:\t"+remoteHash)

if localHash != remoteHash:
    print("Updating...")
    res = urllib.request.urlretrieve(SOURCE+"/statsdefinitions.db", localSqlitePath)
    print("Validating...")
    print("Expecting:\t"+remoteHash)
    newLocalHash = getLocalHash()
    print("New hash:\t"+newLocalHash)
    if remoteHash != newLocalHash:
        raise Exception("Sorry, something must have gone wrong. You can try re-running or do it manually.")
else:
    print("No update required :)")