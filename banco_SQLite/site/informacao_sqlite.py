import sqlite3
from sqlite3.dbapi2 import sqlite_version, sqlite_version_info

conn = sqlite3.connect('banco_SQLite/bancos/pessoas.db')

# O número da versão deste módulo, como uma sequência. 
# Esta não é a versão da biblioteca SQLite.
print(sqlite3.version)

# O número da versão deste módulo, como uma tupla de números inteiros. 
# Esta não é a versão da biblioteca SQLite.
print(sqlite_version)

conn.close()
