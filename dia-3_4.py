# Sistema de acesso

senha_inserida = "abcd1234"
senha_correta = "abcd1234"
usuario_bloqueado = False

acesso_concedido = (senha_inserida == senha_correta) and not usuario_bloqueado

print("Acesso concedido ? ", acesso_concedido)
