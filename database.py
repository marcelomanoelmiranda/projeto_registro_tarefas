import pyodbc

# Conectando ao banco de dados

def conectar_bd():
  conexao = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-Q6T1J9D"
    "DATABASE=SQLEXPRESS;"
    "UID=sa;"
    "PWD=sua_senha"
  )
  return conexao
    
