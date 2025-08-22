# ==============================
#  Controle de Biblioteca (v1)
#  Solução completa
# ==============================

def mostrar_menu():
    print("\n=== MENU ===")
    print("1) Cadastrar livro")
    print("2) Emprestar livro")
    print("3) Listar livros")
    print("4) Sair")

def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    print("\nCatálogo:")
    print("-" * 60)
    print(f"{'Título':30} | {'Autor':20} | {'Ano':4} | {'Qtd':3}")
    print("-" * 60)
    for livro in livros:
        titulo = livro["titulo"][:30]
        autor = livro["autor"][:20]
        ano = livro["ano"]
        qtd = livro["qtd"]
        print(f"{titulo:30} | {autor:20} | {ano:4} | {qtd:3}")
    print("-" * 60)

def cadastrar_livro(livros):
    print("\nCadastro de livro")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    try:
        ano = int(input("Ano de publicação: ").strip())
        qtd = int(input("Quantidade de exemplares: ").strip())
    except ValueError:
        print("Ano e quantidade precisam ser números inteiros.")
        return
    if ano < 0 or qtd < 0:
        print("Ano e quantidade não podem ser negativos.")
        return
    novo = {"titulo": titulo, "autor": autor, "ano": ano, "qtd": qtd}
    livros.append(novo)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def emprestar_livro(livros):
    if not livros:
        print("Não há livros cadastrados para emprestar.")
        return
    titulo = input("Título do livro para empréstimo: ").strip()
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["qtd"] > 0:
                livro["qtd"] -= 1
                print(f"Empréstimo realizado: '{livro['titulo']}'. Restam {livro['qtd']} unidade(s).")
            else:
                print(f"Não há unidades disponíveis de '{livro['titulo']}'.")
            break
    else:
        print("Livro não encontrado.")

def main():
    livros = []
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            emprestar_livro(livros)
        elif opcao == "3":
            listar_livros(livros)
        elif opcao == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

