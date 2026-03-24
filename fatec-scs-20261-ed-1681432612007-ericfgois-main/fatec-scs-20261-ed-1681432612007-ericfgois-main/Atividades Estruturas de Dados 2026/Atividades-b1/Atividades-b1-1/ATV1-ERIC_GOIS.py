''' 
*---------------------------------------------------------* 
*              Fatec São Caetano do Sul                   * 
*                   Atividade B1-1                        * 
*    Autor: 1681432612007 - Eric Fracassi de Gois         * 
*    Objetivo: Aprender dicionários em python.            * 
*    data: 02/03/2026                                     * 
*---------------------------------------------------------* 
'''

# Estrutura Global: Dicionario de Dicionarios
catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    """Insere um novo filme se o ID nao existir."""
    if id_filme not in catalogo:
        catalogo[id_filme] = {'titulo': titulo, 'diretor': diretor}

def buscar_filme(id_filme):
    """Consulta um filme usando o metodo seguro .get()."""
    return catalogo.get(id_filme)

def remover_filme(id_filme):
    """Remove um filme do dicionario usando .pop()."""
    if id_filme in catalogo:
        catalogo.pop(id_filme)

def listar_todos():
    # Itera sobre os itens do dicionario para listagem
    if not catalogo:
        print("\nO catalogo esta vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Titulo: {dados['titulo']} | Diretor: {dados['diretor']}")


# --- teste de funcionamento ---

listar_todos()

adicionar_filme(1, "O Padrinho", "Francis Ford Coppola")
adicionar_filme(2, "Titanic", "James Cameron")
adicionar_filme(3, "Star Wars: Episódio IV", "George Lucas")
adicionar_filme(4, "O Senhor dos Anéis: A Sociedade do Anel", "Peter Jackson")

listar_todos()

print("Buscar filme", buscar_filme(1))
print("Remover filme", remover_filme(1))
listar_todos()