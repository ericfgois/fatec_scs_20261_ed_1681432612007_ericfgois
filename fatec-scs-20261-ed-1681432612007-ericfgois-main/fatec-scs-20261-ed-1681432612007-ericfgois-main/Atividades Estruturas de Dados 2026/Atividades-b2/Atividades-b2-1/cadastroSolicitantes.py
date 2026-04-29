# ─────────────────────────────────────────────────────────
# EQUIPE 09 - Cadastro de Solicitantes
# Setor Jurídico | Emissão de Passaportes e RGs
# ─────────────────────────────────────────────────────────


class Cidadao:
    def __init__(self, id_protocolo: int, nome: str, idade: int, pcd: bool):
        self.id_protocolo = id_protocolo
        self.nome = nome
        self.idade = idade
        self.pcd = pcd

    def __str__(self):
        return (f"Prot: {self.id_protocolo}, Nome: {self.nome}, "
                f"Idade: {self.idade}, PCD: {self.pcd}")


class No:
    def __init__(self, cidadao: Cidadao):
        self.cidadao = cidadao
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, cidadao: Cidadao):
        novo_no = No(cidadao)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
        self.tamanho += 1

    def desenfileirar(self) -> Cidadao:
        if self.inicio is None:
            raise IndexError("Fila vazia.")
        cidadao = self.inicio.cidadao
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return cidadao

    def esta_vazia(self) -> bool:
        return self.inicio is None

    def __len__(self):
        return self.tamanho
