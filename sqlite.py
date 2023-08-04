import sqlite3, os, json
con = sqlite3.connect("statsdefinitions.db")
cur = con.cursor()
try:
    cur.execute("DROP TABLE definitions")
    cur.execute(" DROP TABLE images");
    cur.execute("DROP TABLE metadata");
except sqlite3.OperationalError as e:
    print(e)
    print("Probably brand new db, ignoring")
cur.execute("""CREATE TABLE "definitions" (
	"Identifier"	TEXT NOT NULL,
	"name"	TEXT NOT NULL,
	"alternateName"	INTEGER,
	"disambiguatingDescription"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("Identifier")
);
""")
cur.execute("""
CREATE TABLE "images" (
	"id"	INTEGER,
	"contentUrl"	TEXT NOT NULL,
	"accessibilitySummary"	TEXT,
	"caption"	TEXT,
	"name"	TEXT,
	"definitionIdentifier"	TEXT,
	FOREIGN KEY("definitionIdentifier") REFERENCES "definitions"("Identifier"),
	PRIMARY KEY("id" AUTOINCREMENT)
);""")
termsDir = os.path.join(os.path.dirname(__file__), 'terms')
termFiles = os.listdir(termsDir)

definitions = []
images = []

for fname in termFiles:
    with open(os.path.join(termsDir, fname), encoding="utf8") as f:
        termData = f.read()

    term = json.loads(termData)
    definitions.append((
        term["identifier"], term["name"], term.get("alternateName", None),
        term["disambiguatingDescription"], term["description"]
    ))
    if term.get("image", {"@type":None})["@type"] == "ImageObject":
        images.append((
            term["image"]["contentUrl"], term["image"]["accessibilitySummary"],
            term["image"]["caption"], term["image"]["name"], term["identifier"]
        ))
cur.executemany('INSERT INTO "definitions"("Identifier","name","alternateName","disambiguatingDescription","description") '
                'VALUES (?,?,?,?,?);', definitions)
cur.executemany('INSERT INTO "images"("id","contentUrl","accessibilitySummary","caption","name","definitionIdentifier")'
                'VALUES (NULL,?,?,?,?,?);', images)
con.commit()

cur.execute("""
CREATE TABLE "metadata" (
	"fieldName"	TEXT NOT NULL,
	"value"	TEXT NOT NULL,
	PRIMARY KEY("fieldName")
);""")

commitHash = os.environ.get("GITHUB_SHA", "No hash")
cur.execute('INSERT INTO "metadata"("fieldName", "value") VALUES ("commithash",?)', (commitHash,))
con.commit()