'''
*----------------------------------------------------------*
* Fatec Antônio Russo - São Caetano do Sul                 *
* Exemplo de Manipulação de Pilhas                         *
* Autor: Eric Fracassi de Gois                             *
* Objetivo: Mostrar manipulação de pilhas em python        *
* reproduzindo o funcionamento da HP12c.                   *
* Data: 30/03/2026                                         *
*----------------------------------------------------------*
'''
def calculadora(entrada):
    pilha = []
    pilha_alg = []
    tokens = entrada.split()

    if len(tokens) == 0:
        return "Erro: Você não digitou nada."

    print(f"\n{'-'*40}")
    print(f"Processando a expressão RPN: {entrada}")
    print(f"{'-'*40}")

    for token in tokens:
        print(f"\n> Token lido: '{token}'")
        
        if token in ('+', '-', '*', '/'):
            if len(pilha) < 2:
                return f"Erro: Faltam números na pilha para usar o operador '{token}'."

            # O primeiro a sair (pop) é o operando da direita (Y na matemática, mas chamamos de val2)
            # O segundo a sair é o operando da esquerda (X na matemática, mas chamamos de val1)
            val2 = pilha.pop()
            val1 = pilha.pop()

            expr2 = pilha_alg.pop()
            expr1 = pilha_alg.pop()

            if token == '+':
                resultado = val1 + val2
            elif token == '-':
                resultado = val1 - val2
            elif token == '*':
                resultado = val1 * val2
            elif token == '/':
                if val2 == 0:
                    return "Erro: Divisão por zero não é permitida."
                resultado = val1 / val2

            pilha.append(resultado)
            pilha_alg.append(f"({expr1} {token} {expr2})")

        else:
            try:
                # Substitui vírgula por ponto para aceitar o formato brasileiro (ex: 0,03)
                numero_str = token.replace(',', '.')
                numero = float(numero_str)
                
                pilha.append(numero)
                
                # Formatação para não exibir casas decimais desnecessárias na expressão algébrica
                txt_numero = str(int(numero)) if numero.is_integer() else str(numero)
                pilha_alg.append(txt_numero)
                
            except ValueError:
                return f"Erro: O item '{token}' não é um número válido."

        # Requisito Obrigatório: Exibir memórias X, Y, Z e T a cada passo
        # Mapeando os 4 últimos itens da lista para simular os registradores da HP12c.
        t = pilha[-4] if len(pilha) >= 4 else 0.0
        z = pilha[-3] if len(pilha) >= 3 else 0.0
        y = pilha[-2] if len(pilha) >= 2 else 0.0
        x = pilha[-1] if len(pilha) >= 1 else 0.0

        print(f"  Memória T: {t}")
        print(f"  Memória Z: {z}")
        print(f"  Memória Y: {y}")
        print(f"  Memória X: {x}")

    if len(pilha) == 0:
         return "Erro: Expressão inválida."

    print(f"\n{'-'*40}")
    return f"Expressão algébrica gerada: {pilha_alg[-1]}\nResultado Final: {pilha[-1]}"

print("Calculadora HP12c Iniciada! (Digite 'sair' para fechar o programa)")
while True:
    rpn = input("\nDigite a expressão RPN: ")

    if rpn.strip().lower() == 'sair':
        print("Obrigado por usar nossa calculadora!")
        break

    resultado = calculadora(rpn)
    print(resultado)