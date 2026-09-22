import os
os.system('cls')

db_config = dict(
    host="localhost",
    porta = 3306,
    usuario = "root",
    senai = "senai@126"
)
print(f"Conexão com o banco {db_config['host']}, na porta {db_config['porta']}...")
