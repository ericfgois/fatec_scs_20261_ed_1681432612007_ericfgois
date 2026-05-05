# ─────────────────────────────────────────────────────────
# EQUIPE 09 + EQUIPE 10 - Sistema Completo
# Cadastro de Solicitantes + Auditoria de Prioridade
# ─────────────────────────────────────────────────────────
class Cidadao:
    def __init__(self, id_protocolo, nome, idade, pcd):
        self.id_protocolo = id_protocolo
        self.nome = nome
        self.idade = idade
        self.pcd = pcd
        self.prioridade_legal = False

    def __str__(self):
        return f"{self.id_protocolo} - {self.nome} | Idade: {self.idade} | PCD: {self.pcd}"


class No:
    def __init__(self, cidadao):
        self.cidadao = cidadao
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, cidadao):
        novo = No(cidadao)

        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def desenfileirar(self):
        if self.inicio is None:
            return None

        cid = self.inicio.cidadao
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        return cid

    def esta_vazia(self):
        return self.inicio is None


class AuditoriaPrioridade:

    def __init__(self):
        self.fila1 = Fila()
        self.fila2 = Fila()

    def inserir(self):
        id_protocolo = int(input("ID: "))
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        pcd = input("PCD (s/n): ").lower() == 's'

        self.fila1.enfileirar(Cidadao(id_protocolo, nome, idade, pcd))
        print("Cadastrado com sucesso!\n")

    def processar(self):

        fila_prioridade = Fila()
        fila_normal = Fila()

        while not self.fila1.esta_vazia():

            cidadao = self.fila1.desenfileirar()

            if cidadao.idade >= 60 or cidadao.pcd:
                cidadao.prioridade_legal = True
                fila_prioridade.enfileirar(cidadao)
            else:
                cidadao.prioridade_legal = False
                fila_normal.enfileirar(cidadao)

        while not fila_prioridade.esta_vazia():
            self.fila2.enfileirar(fila_prioridade.desenfileirar())

        while not fila_normal.esta_vazia():
            self.fila2.enfileirar(fila_normal.desenfileirar())

        print("Processamento concluído!\n")

    def mostrar_fila(self, fila, nome):
        print(f"\n{nome}:")

        if fila.esta_vazia():
            print("Fila vazia")
            return

        atual = fila.inicio
        while atual is not None:
            cid = atual.cidadao
            print(cid, "| Prioridade:", cid.prioridade_legal)
            atual = atual.proximo

    def mostrar_tudo(self):
        self.mostrar_fila(self.fila1, "Fila de Entrada (não processada)")
        self.mostrar_fila(self.fila2, "Fila Final (processada)")


sistema = AuditoriaPrioridade()

while True:
    print("\n1 - Inserir cidadão")
    print("2 - Processar fila")
    print("3 - Mostrar todas as filas")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        sistema.inserir()
    elif op == "2":
        sistema.processar()
    elif op == "3":
        sistema.mostrar_tudo()
    elif op == "0":
        print("Encerrado.")
        break
    else:
        print("Opção inválida.")