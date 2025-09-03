def verificar_senha(senha):
    # ✅ Regra 1: Verificar se tem pelo menos 8 caracteres
    if len(senha) < 8:
        return "Senha inválida! Deve ter pelo menos 8 caracteres."
    
    # ✅ Regra 2: Verificar se contém pelo menos um número
    if not any(char.isdigit() for char in senha):
        return "Senha inválida! Deve conter pelo menos um número."
    
    return "Senha válida!"

# 🔁 Loop até o usuário digitar 'sair'
while True:
    senha_usuario = input("Digite sua senha (ou 'sair' para encerrar): ")

    if senha_usuario.lower() == 'sair':
        print("Encerrando o programa.")
        break

    resultado = verificar_senha(senha_usuario)
    print(resultado)
    