print("---------- INÍCIO ----------\n")

print("----- REGISTRAR USUÁRIO -----\n")

nome_usuario = str(input('- Crie um nome de usuário.\nDigite aqui: '))
nome_usuario_correto = nome_usuario

senha = str(input('- Crie uma senha.\nDigite aqui: '))
senha_correta = senha 
print("")

print("----- LOGIN -----\n")

if input('Qual seu nome de usuário ?\nDigite aqui: ') == nome_usuario_correto:
    if input('Qual sua senha ?\nDigite aqui: ') == senha_correta:
        print(f'- {nome_usuario}, logado com sucesso!')
    else:
        print(f'Senha incorreta para o usuário {nome_usuario}')
else:
    print(f'- {nome_usuario} não cadastrado no sistema :( ')