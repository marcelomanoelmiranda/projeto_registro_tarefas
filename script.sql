--Criação da Database e Tabela 
CREATE DATABASE Tarefas;

CREATE TABLE Tarefas (
    TarefaID INT IDENTITY(1,1) PRIMARY KEY,
    Descricao NVARCHAR(255) NOT NULL,
    Status NVARCHAR(50) NOT NULL CHECK (Status IN ('Pendente', 'Concluída')),
    DataCriacao DATETIME DEFAULT GETDATE(),
    DataConclusao DATETIME NULL
);

--Procedimentos a serem criados
CREATE PROCEDURE AdicionarTarefa
@Descricao NVARCHAR(255),
@Status NVARCHAR(50)
AS
INSERT INTO Tarefas (Descricao, Status) VALUES (@Descricao, @Status);

CREATE PROCEDURE AtualizarStatus
@TarefaID INT,
@NovoStatus NVARCHAR(50)
AS
UPDATE Tarefas SET Status = @NovoStatus WHERE TarefaID = @TarefaID;

CREATE PROCEDURE RelatorioTarefas
AS
SELECT * FROM Tarefas WHERE Status = 'Pendente' OR Status = 'Concluída';



-- Inserindo tarefas com status Pendente e Concluída
INSERT INTO Tarefas (Descricao, Status, DataCriacao)
VALUES 
('Comprar materiais de escritório', 'Pendente', GETDATE()),
('Finalizar relatório financeiro', 'Pendente', GETDATE()),
('Reunião com a equipe de vendas', 'Concluída', GETDATE()),
('Organizar evento corporativo', 'Pendente', GETDATE()),
('Responder e-mails de clientes', 'Concluída', GETDATE());

-- Inserindo uma tarefa com a DataConclusao
INSERT INTO Tarefas (Descricao, Status, DataCriacao, DataConclusao)
VALUES 
('Revisar contrato com fornecedor', 'Concluída', GETDATE(), GETDATE());

select * from Tarefas;
