"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    return "Bem-vindo ao Desafio de Git!"

def listar_comandos_git_basicos():
    print(["git init", "git add", "git commit", "git status", "git push"])


def criar_mensagem_commit(funcao_nome):
    print(f"Implementa função {funcao_nome}")


def verificar_tag_valida(tag: str):
    cont_nu = 0
    if "v" in tag and "." in tag:
        for i in tag:
            if i.isdecimal():
                cont_nu += 1
        if cont_nu > 3:
            return False
        else:
            return True
    else:
        return False


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass
