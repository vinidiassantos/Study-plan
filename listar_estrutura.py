with open("estrutura.md", "w", encoding="utf-8") as f:
    def listar_estrutura_em_bullets(caminho, nivel=0):
        prefixo = "  " * nivel + "- "
        for item in sorted(os.listdir(caminho)):
            item_path = os.path.join(caminho, item)
            f.write(f"{prefixo}{item}\n")
            if os.path.isdir(item_path):
                listar_estrutura_em_bullets(item_path, nivel + 1)

    listar_estrutura_em_bullets(".")
