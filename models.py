from fastapi import APIRouter
from database import conectar_bd

router = APIRouter()

# Endpoint para adicionar uma nova tarefa
@router.post("/tarefas")
def adicionar_tarefa(descricao: str, status: str = "Pendente"):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("EXEC AdicionarTarefa ?, ?", (descricao, status))
    conn.commit()
    conn.close()
    return {"mensagem": "Tarefa adicionada com sucesso!"}

# Endpoint para listar todas as tarefas
@router.get("/tarefas")
def listar_tarefas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT TarefaID, Descricao, Status, DataCriacao, DataConclusao FROM Tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "descricao": row[1],
            "status": row[2],
            "data_criacao": row[3],
            "data_conclusao": row[4]
        }
        for row in tarefas
    ]

# Endpoint para atualizar o status de uma tarefa
@router.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, novo_status: str):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("EXEC AtualizarStatus ?, ?", (tarefa_id, novo_status))
    conn.commit()
    conn.close()
    return {"mensagem": "Status atualizado com sucesso!"}

# Endpoint para deletar uma tarefa
@router.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE TarefaID = ?", (tarefa_id,))
    conn.commit()
    conn.close()
    return {"mensagem": "Tarefa deletada com sucesso!"}

# Endpoint para gerar um relatório de tarefas concluídas e pendentes
@router.get("/relatorio")
def gerar_relatorio():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("EXEC RelatorioTarefas")
    tarefas = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "descricao": row[1],
            "status": row[2],
            "data_criacao": row[3],
            "data_conclusao": row[4]
        }
        for row in tarefas
    ]
