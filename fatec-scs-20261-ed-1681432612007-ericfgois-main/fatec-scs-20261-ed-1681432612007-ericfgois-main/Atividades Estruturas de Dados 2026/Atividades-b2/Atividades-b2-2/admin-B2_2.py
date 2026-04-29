class No:
    def __init__(self, nome_arq, paginas):
        self.nome_arq = nome_arq
        self.paginas = paginas
        self.proximo = None

class Fila:
    def __init__(self, nome):
        self.nome = nome
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def vazia(self):
        return self.inicio is None

    def inserir(self, nome_arq, paginas):
        novo = No(nome_arq, paginas)
        if self.vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def remover(self):
        if self.vazia():
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return removido

    def mostrar(self):
        print(f"Fila {self.nome} - Total: {self.tamanho}")
        atual = self.inicio
        while atual:
            print(f"- {atual.nome_arq} ({atual.paginas} pags)")
            atual = atual.proximo
        print()

class impressao:
    def __init__(self):
        self.fila_adm = Fila("ADM")
        self.fila_aluno = Fila("Aluno")
        self.fila_geral = Fila("Geral")

    def adicionar(self, tipo, nome_arq, paginas):
        if tipo == 'ADM':
            self.fila_adm.inserir(nome_arq, paginas)
        elif tipo == 'ALUNO':
            self.fila_aluno.inserir(nome_arq, paginas)
        else:
            print("Tipo invalido")

    def reorganizar(self):
        if not self.fila_geral.vazia():
            print("A fila geral precisa estar vazia para reorganizar.")
            return

        while not self.fila_adm.vazia():
            doc = self.fila_adm.remover()
            self.fila_geral.inserir(doc.nome_arq, doc.paginas)
            
        while not self.fila_aluno.vazia():
            doc = self.fila_aluno.remover()
            self.fila_geral.inserir(doc.nome_arq, doc.paginas)
            
        print("Filas reorganizadas para a fila geral.\n")

    def imprimir(self):
        if self.fila_geral.vazia():
            print("Nada para imprimir na fila geral.")
            return
        
        doc = self.fila_geral.remover()
        print(f"Imprimindo: {doc.nome_arq} ({doc.paginas} pags)")

    def listar_tudo(self):
        print("--- Estado das Filas ---")
        self.fila_adm.mostrar()
        self.fila_aluno.mostrar()
        self.fila_geral.mostrar()



"""TESTES"""

if __name__ == "__main__":
    sistema = impressao()

    sistema.adicionar("ALUNO", "monografia.pdf", 15)
    sistema.adicionar("ALUNO", "exercicios.docx", 2)
    sistema.adicionar("ADM", "conteudo.pdf", 5)
    sistema.adicionar("ADM", "planilha.pdf", 12)

    sistema.listar_tudo()

    sistema.reorganizar()
    sistema.listar_tudo()

    sistema.imprimir()
    sistema.imprimir()
    sistema.imprimir()
    print()
    
    sistema.listar_tudo()