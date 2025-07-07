import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import os

ARQUIVO = "supertrunfoteste2.txt"

# Dicionário com descrições das bandeiras
BANDEIRAS_ESTADOS = {
    "AC": "Bandeira do Acre - fundo verde com estrela amarela e faixa diagonal",
    "AL": "Bandeira de Alagoas - fundo branco com brasão central",
    "AM": "Bandeira do Amazonas - listras brancas e vermelhas com estrelas",
    "AP": "Bandeira do Amapá - fundo azul com faixa branca e estrela",
    "BA": "Bandeira da Bahia - fundo branco com triângulo azul e estrela",
    "CE": "Bandeira do Ceará - fundo verde com losango amarelo e círculo azul",
    "DF": "Bandeira do Distrito Federal - fundo branco com setas verdes e amarelas",
    "ES": "Bandeira do Espírito Santo - listras azuis e brancas com estrela",
    "GO": "Bandeira de Goiás - fundo verde com losango amarelo e estrelas",
    "MA": "Bandeira do Maranhão - listras coloridas com estrela branca",
    "MG": "Bandeira de Minas Gerais - triângulo vermelho com frase branca",
    "MS": "Bandeira de Mato Grosso do Sul - listras azuis e verdes com estrela",
    "MT": "Bandeira de Mato Grosso - fundo azul com losango amarelo e estrela",
    "PA": "Bandeira do Pará - fundo branco com faixa vermelha e estrela",
    "PB": "Bandeira da Paraíba - fundo preto com faixa vermelha e estrela",
    "PE": "Bandeira de Pernambuco - listras coloridas com estrela e sol",
    "PI": "Bandeira do Piauí - fundo azul com estrela amarela e faixa branca",
    "PR": "Bandeira do Paraná - fundo verde com círculo azul e estrela",
    "RJ": "Bandeira do Rio de Janeiro - fundo branco com círculo azul e estrela",
    "RN": "Bandeira do Rio Grande do Norte - fundo branco com faixa vermelha e estrela",
    "RO": "Bandeira de Rondônia - fundo azul com estrela amarela e faixa branca",
    "RR": "Bandeira de Roraima - fundo branco com estrela vermelha e faixa azul",
    "RS": "Bandeira do Rio Grande do Sul - listras verdes e amarelas com brasão",
    "SC": "Bandeira de Santa Catarina - listras horizontais vermelhas e brancas",
    "SE": "Bandeira de Sergipe - listras azuis e verdes com estrelas",
    "SP": "Bandeira de São Paulo - listras pretas, brancas e vermelhas com brasão",
    "TO": "Bandeira do Tocantins - fundo branco com faixa laranja e estrela"
}

def ler_cidades():
    cidades = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                partes = linha.strip().split(";")
                if len(partes) == 9:
                    cidades.append(partes)
    except FileNotFoundError:
        pass
    return cidades

def salvar_cidades(cidades):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in cidades:
            f.write(";".join(c) + "\n")

def atualizar_lista():
    for i in tree.get_children():
        tree.delete(i)
    cidades = ler_cidades()
    for i, c in enumerate(cidades):
        tree.insert("", "end", values=(i + 1, c[2], c[0], c[3], c[4], c[5], c[6]))

def exibir_detalhes():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione uma cidade primeiro!", parent=root)
        return
    
    item_index = int(tree.item(selected_item[0], 'values')[0]) - 1
    cidades = ler_cidades()
    
    if item_index < 0 or item_index >= len(cidades):
        messagebox.showerror("Erro", "Índice inválido!", parent=root)
        return
    
    c = cidades[item_index]
    estado_sigla = c[0]
    
    detalhes = (
        f"Estado: {estado_sigla}\n"
        f"Código IBGE: {c[1]}\n"
        f"Nome: {c[2]}\n"
        f"População: {c[3]}\n"
        f"PIB: {c[4]}\n"
        f"Área: {c[5]}\n"
        f"Pontos Turísticos: {c[6]}\n"
        f"Densidade Populacional: {c[7]}\n"
        f"PIB per Capita: {c[8]}\n\n"
    )
    
    detalhes_win = tk.Toplevel(root)
    detalhes_win.title(f"Detalhes da Cidade: {c[2]}")
    detalhes_win.geometry("650x600")  # Aumentei a altura para a bandeira
    detalhes_win.resizable(False, False)
    
    # Frame principal
    main_frame = tk.Frame(detalhes_win, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text=f"Detalhes de {c[2]}", 
             font=("Fira Code", 16, "bold")).pack(pady=(0,15))
    
    # Frame para texto
    texto_frame = tk.Frame(main_frame)
    texto_frame.pack(fill=tk.BOTH)
    
    scrollbar = ttk.Scrollbar(texto_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    texto = tk.Text(texto_frame, wrap=tk.WORD, font=("Fira Code", 12), 
                   width=60, height=10, yscrollcommand=scrollbar.set)
    texto.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=texto.yview)
    
    texto.insert(tk.END, detalhes)
    texto.config(state=tk.DISABLED)
    
    # Frame para a bandeira
    bandeira_frame = tk.Frame(main_frame, pady=15, bd=2, relief=tk.GROOVE)
    bandeira_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título da bandeira
    tk.Label(bandeira_frame, text="Bandeira do Estado:", 
             font=("Fira Code", 12, "bold")).pack(pady=5)
    
    try:
        # Tenta carregar a imagem da bandeira (substitua pelo caminho real)
        img_path = f"bandeiras/{estado_sigla}.png"  # Assumindo que temos as imagens em uma pasta 'bandeiras'
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((200, 120), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(bandeira_frame, image=photo)
            img_label.image = photo  # Manter referência
            img_label.pack()
        else:
            # Exibe um placeholder se a imagem não existir
            placeholder = tk.Label(
                bandeira_frame, 
                text=BANDEIRAS_ESTADOS.get(estado_sigla, "Bandeira não disponível"),
                font=("Fira Code", 10),
                fg="gray",
                wraplength=400
            )
            placeholder.pack()
            
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível carregar a bandeira: {str(e)}", parent=detalhes_win)
    
    # Frame para o botão
    btn_frame = tk.Frame(main_frame)
    btn_frame.pack(pady=(15,0))
    
    tk.Button(btn_frame, text="Fechar", command=detalhes_win.destroy,
             font=("Fira Code", 12), width=15).pack()

# [...] (Manter as funções remover_cidade, adicionar_cidade e inserir_capitais_brasil anteriores)

# Configuração da janela principal
root = tk.Tk()
root.title("Super Trunfo - Cidades")
root.geometry("1000x650")
root.resizable(False, False)

# Configurar estilo
style = ttk.Style()
style.configure('TButton', font=('Fira Code', 11), padding=6)
style.configure('TLabel', font=('Fira Code', 12))
style.configure('Treeview.Heading', font=('Fira Code', 12, 'bold'))
style.configure('Treeview', font=('Fira Code', 11), rowheight=25)

# Frame para os botões com grid layout
btn_frame = tk.Frame(root, padx=10, pady=10)
btn_frame.pack(fill=tk.X)

# Configuração dos botões
btn_config = {
    'font': ('Fira Code', 11, 'bold'),
    'bd': 2,
    'relief': tk.RAISED,
    'padx': 10,
    'pady': 6,
    'highlightthickness': 0
}

# Botões com texto completo
btn_detalhes = tk.Button(btn_frame, text="🔍 Ver Detalhes", command=exibir_detalhes, **btn_config)
btn_adicionar = tk.Button(btn_frame, text="➕ Adicionar Cidade", command=adicionar_cidade, **btn_config)
btn_remover = tk.Button(btn_frame, text="🗑️ Remover Cidade", command=remover_cidade, **btn_config)
btn_atualizar = tk.Button(btn_frame, text="🔄 Atualizar Lista", command=atualizar_lista, **btn_config)
btn_capitais = tk.Button(btn_frame, text="🏙️ Inserir Capitais", command=inserir_capitais_brasil, **btn_config)

# Posicionamento dos botões
btn_detalhes.grid(row=0, column=0, padx=5, sticky="ew")
btn_adicionar.grid(row=0, column=1, padx=5, sticky="ew")
btn_remover.grid(row=0, column=2, padx=5, sticky="ew")
btn_atualizar.grid(row=0, column=3, padx=5, sticky="ew")
btn_capitais.grid(row=0, column=4, padx=5, sticky="ew")

# Configurar pesos das colunas para centralização
for i in range(5):
    btn_frame.columnconfigure(i, weight=1, uniform="btns")

# Frame para a tabela
tabela_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
tabela_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0,15))

# Configuração da Treeview
tree = ttk.Treeview(
    tabela_frame,
    columns=("ID", "Cidade", "Estado", "População", "PIB (R$)", "Área (km²)", "Pontos Tur."),
    show="headings",
    height=20,
    selectmode="browse"
)

# Definir cabeçalhos e colunas
headers = [
    ("ID", 50, "center"),
    ("Cidade", 180, "w"),
    ("Estado", 60, "center"),
    ("População", 120, "e"),
    ("PIB (R$)", 150, "e"),
    ("Área (km²)", 100, "e"),
    ("Pontos Tur.", 90, "center")
]

for text, width, anchor in headers:
    tree.heading(text, text=text)
    tree.column(text, width=width, anchor=anchor, stretch=False)

# Barra de rolagem
scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Carregar dados iniciais
atualizar_lista()

# Centralizar janela na tela
root.eval('tk::PlaceWindow . center')

root.mainloop()
