from fastapi import APIRouter
from database import conectar_bd

router = APIRouter()

@router.post("/tarefas")
def adicionar_tarefa(descricao: str, status: str = "Pendente"):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("EXEC AdicionarTarefa ?, ?", (descricao, status))
    conn.commit()
    return {"mensagem": "Tarefa adicionada com sucesso!"}

@router.get("/tarefas")
def listar_tarefas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    return [{"id": row[0], "descricao": row[1], "status": row[2]} for row in tarefas]

@router.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, novo_status: str):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("EXEC AtualizarStatus ?, ?", (tarefa_id, novo_status))
    conn.commit()
    return {"mensagem": "Status atualizado com sucesso!"}

@router.get("/relatorio")
def gerar_relatorio():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("EXEC RelatorioTarefas")
    tarefas = cursor.fetchall()
    return [{"id": row[0], "descricao": row[1], "status": row[2]} for row in tarefas]
