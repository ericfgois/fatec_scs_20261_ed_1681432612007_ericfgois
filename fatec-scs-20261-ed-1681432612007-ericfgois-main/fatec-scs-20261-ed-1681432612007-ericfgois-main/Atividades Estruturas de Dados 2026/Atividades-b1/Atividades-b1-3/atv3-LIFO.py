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
        
    if len(tokens) > 4:
        return "Erro: O limite máximo é de 4 itens por expressão."
    
    if len(tokens) == 4 and tokens[3] not in ('+', '-', '*', '/'):
        return "Erro: O quarto item deve ser uma operação (+, -, *, /)."
    
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            if len(pilha) < 2:
                return f"Erro: Faltam números na pilha para usar o operador '{token}'."
            
            x = pilha.pop()
            y = pilha.pop()
            
            x_alg = pilha_alg.pop()
            y_alg = pilha_alg.pop()
            
            if token == '+':
                resultado = x + y
            elif token == '-':
                resultado = x - y
            elif token == '*':
                resultado = x * y
            elif token == '/':
                if y == 0:
                    return "Erro: Divisão por zero não é permitida."
                resultado = x / y
                
            pilha.append(resultado)
            
            expr = f"({x_alg} {token} {y_alg})"
            pilha_alg.append(expr)

        else:
            try:
                numero = float(token)
                pilha.append(numero)
                txt_numero = str(int(numero)) if numero.is_integer() else str(numero)
                pilha_alg.append(txt_numero)
            except ValueError:
                return f"Erro: O item '{token}' não é um número válido."

    if len(pilha_alg) == 0 or len(tokens) < 3:
        return "Erro: expressão inválida, operadores insuficientes."
        
    return f"Expressão algébrica: {pilha_alg[-1]}\nO resultado da expressão algébrica é: {pilha[-1]}"

'''------------------------------------------------------'''
'''rpn = input("Digite a expressão RPN: ")
resultado = calculadora_rpn_limite(rpn)
print(resultado)'''
'''------------------------------------------------------'''

print("Calculadora Iniciada! (Digite 'sair' para fechar o programa)")
while True:
    rpn = input("\nDigite a expressão RPN: ")

    if rpn.strip().lower() == 'sair':
        print("Obrigado por usar nossa calculadora!")
        break
        
    resultado = calculadora(rpn)
    print(resultado)