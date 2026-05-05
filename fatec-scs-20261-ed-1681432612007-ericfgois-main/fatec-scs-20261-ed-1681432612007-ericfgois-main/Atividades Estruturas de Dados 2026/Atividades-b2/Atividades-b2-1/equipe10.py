from cadastroSolicitantes import Cidadao, Fila


class AuditoriaPrioridade:

    def __init__(self, fila1: Fila, fila2: Fila):
        self.fila1 = fila1
        self.fila2 = fila2

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