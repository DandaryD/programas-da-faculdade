import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os

ARQUIVO = "supertrunfoteste2.txt"

# Dicionário com descrições das bandeiras dos estados brasileiros
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

# Verifica se o Pillow está instalado
try:
    from PIL import Image, ImageTk
    PILLOW_AVAILABLE = True
except ImportError:
    PILLOW_AVAILABLE = False
    print("Aviso: Pillow não está instalado. As bandeiras serão exibidas como texto.")

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
    nome_cidade = c[2]
    
    detalhes = (
        f"Estado: {estado_sigla}\n"
        f"Código IBGE: {c[1]}\n"
        f"Nome: {nome_cidade}\n"
        f"População: {c[3]}\n"
        f"PIB: {c[4]}\n"
        f"Área: {c[5]}\n"
        f"Pontos Turísticos: {c[6]}\n"
        f"Densidade Populacional: {c[7]}\n"
        f"PIB per Capita: {c[8]}\n\n"
        f"Bandeira: {BANDEIRAS_ESTADOS.get(estado_sigla, 'Não disponível')}"
    )
    
    detalhes_win = tk.Toplevel(root)
    detalhes_win.title(f"Detalhes: {nome_cidade}")
    detalhes_win.geometry("650x600")
    detalhes_win.resizable(False, False)
    
    main_frame = tk.Frame(detalhes_win, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    tk.Label(main_frame, text=f"Detalhes de {nome_cidade}", 
             font=("Fira Code", 16, "bold")).pack(pady=(0,15))
    
    texto_frame = tk.Frame(main_frame)
    texto_frame.pack(fill=tk.BOTH, expand=True)
    
    scrollbar = ttk.Scrollbar(texto_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    texto = tk.Text(texto_frame, wrap=tk.WORD, font=("Fira Code", 12), 
                   width=60, height=10, yscrollcommand=scrollbar.set)
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)
    
    texto.insert(tk.END, detalhes)
    texto.config(state=tk.DISABLED)
    
    # Seção da bandeira
    bandeira_frame = tk.Frame(main_frame, pady=15)
    bandeira_frame.pack(fill=tk.BOTH)
    
    if PILLOW_AVAILABLE:
        try:
            img_path = f"bandeiras/{estado_sigla}.png"
            if os.path.exists(img_path):
                img = Image.open(img_path)
                img = img.resize((200, 120), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                
                tk.Label(bandeira_frame, text="Bandeira:", font=("Fira Code", 12, "bold")).pack()
                
                img_label = tk.Label(bandeira_frame, image=photo)
                img_label.image = photo
                img_label.pack()
            else:
                raise FileNotFoundError
        except Exception as e:
            tk.Label(bandeira_frame, 
                    text=f"Não foi possível carregar a bandeira: {BANDEIRAS_ESTADOS.get(estado_sigla, 'Bandeira não disponível')}",
                    font=("Fira Code", 10), fg="gray").pack()
    else:
        tk.Label(bandeira_frame, 
                text=BANDEIRAS_ESTADOS.get(estado_sigla, "Bandeira não disponível"),
                font=("Fira Code", 10), fg="blue").pack()
    
    btn_frame = tk.Frame(main_frame)
    btn_frame.pack(pady=(15,0))
    
    tk.Button(btn_frame, text="Fechar", command=detalhes_win.destroy,
             font=("Fira Code", 12), width=15).pack()

def remover_cidade():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione uma cidade primeiro!", parent=root)
        return
    
    resposta = messagebox.askyesno(
        "Confirmação", 
        "Deseja realmente remover esta cidade?",
        parent=root
    )
    if not resposta:
        return
    
    item_index = int(tree.item(selected_item[0], 'values')[0]) - 1
    cidades = ler_cidades()
    
    if 0 <= item_index < len(cidades):
        del cidades[item_index]
        salvar_cidades(cidades)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Cidade removida com sucesso!", parent=root)

def adicionar_cidade():
    campos = [
        ("Estado (ex: SP)", "Digite a sigla do estado (ex: SP):"),
        ("Código IBGE", "Digite o código IBGE:"),
        ("Nome da Cidade", "Digite o nome da cidade:"),
        ("População", "Digite a população:"),
        ("PIB", "Digite o PIB:"),
        ("Área", "Digite a área:"),
        ("Pontos Turísticos", "Digite o número de pontos turísticos:"),
        ("Densidade Populacional", "Digite a densidade populacional:"),
        ("PIB per Capita", "Digite o PIB per capita:")
    ]
    
    nova = []
    
    for titulo, texto_label in campos:
        valor = simpledialog.askstring(titulo, texto_label, parent=root)
        if valor is None:  # Usuário cancelou
            return
        nova.append(valor)
    
    cidades = ler_cidades()
    cidades.append(nova)
    salvar_cidades(cidades)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Cidade adicionada com sucesso!", parent=root)

def inserir_capitais_brasil():
    resposta = messagebox.askyesno(
        "Confirmação", 
        "Isso irá adicionar todas as capitais brasileiras. Continuar?",
        parent=root
    )
    if not resposta:
        return
    
    dados = [
        ["AC", "1200401", "Rio Branco", "419000", "10955674", "3", "5", "139666.67", "26.15"],
        ["AL", "2704302", "Maceió", "1028000", "27484016", "18", "4", "57111.11", "26.73"],
        ["AM", "1302603", "Manaus", "2200000", "103281436", "2", "6", "1100000.00", "46.94"],
        ["AP", "1600303", "Macapá", "530000", "12938060", "6407", "3", "82.70", "24.43"],
        ["BA", "2927408", "Salvador", "2900000", "62954487", "15", "7", "193333.33", "21.71"],
        ["CE", "2304400", "Fortaleza", "2700000", "73436128", "22", "6", "122727.27", "27.20"],
        ["DF", "5300108", "Brasília", "3000000", "286943782", "6", "8", "500000.00", "95.65"],
        ["ES", "3205309", "Vitória", "365000", "31423572", "25", "4", "14600.00", "86.09"],
        ["GO", "5208707", "Goiânia", "1500000", "59865989", "14", "5", "107142.86", "39.91"],
        ["MA", "2111300", "São Luís", "1100000", "36535225", "17", "5", "64705.88", "33.21"],
        ["MG", "3106200", "Belo Horizonte", "2600000", "105829675", "21", "6", "123809.52", "40.70"],
        ["MS", "5002704", "Campo Grande", "914000", "34731151", "4", "4", "228500.00", "38.00"],
        ["MT", "5103403", "Cuiabá", "622000", "29746934", "8", "4", "77750.00", "47.84"],
        ["PA", "1501402", "Belém", "1500000", "33467126", "13", "6", "115384.62", "22.31"],
        ["PB", "2507507", "João Pessoa", "833000", "22244284", "24", "5", "34708.33", "26.72"],
        ["PE", "2611606", "Recife", "1700000", "54970305", "23", "6", "73913.04", "32.33"],
        ["PI", "2211001", "Teresina", "870000", "23895231", "1673", "4", "520.13", "27.47"],
        ["PR", "4106902", "Curitiba", "1900000", "98003703", "20", "6", "95000.00", "51.58"],
        ["RJ", "3304557", "Rio de Janeiro", "6500000", "359634752", "12", "8", "541666.67", "55.33"],
        ["RN", "2408102", "Natal", "890000", "24186261", "26", "5", "34230.77", "27.19"],
        ["RO", "1100205", "Porto Velho", "550000", "20059521", "1", "4", "550000.00", "36.47"],
        ["RR", "1400100", "Bandeira das Bandeiras", "430000", "13493364", "7", "4", "61428.57", "31.38"],
        ["RS", "4314902", "Porto Alegre", "1500000", "81562848", "19", "6", "78947.37", "54.38"],
        ["SC", "4205407", "Florianópolis", "540000", "23555034", "16", "5", "33750.00", "43.62"],
        ["SE", "2800308", "Aracaju", "680000", "18405677", "25", "4", "27200.00", "27.07"],
        ["SP", "3550308", "São Paulo", "12500000", "828980607", "10", "8", "1250000.00", "66.32"],
        ["TO", "1721000", "Palmas", "310000", "10333418", "9", "4", "34444.44", "33.33"],
    ]
    
    cidades = ler_cidades()
    cidades.extend(dados)
    salvar_cidades(cidades)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Capitais brasileiras adicionadas com sucesso!", parent=root)

# Configuração da janela principal
root = tk.Tk()
root.title("Super Trunfo - Cidades Brasileiras")
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

# Botões com ícones e descrição
btn_detalhes = tk.Button(btn_frame, text="🔍 Ver Detalhes", command=exibir_detalhes, **btn_config)
btn_adicionar = tk.Button(btn_frame, text="➕ Adicionar", command=adicionar_cidade, **btn_config)
btn_remover = tk.Button(btn_frame, text="🗑️ Remover", command=remover_cidade, **btn_config)
btn_atualizar = tk.Button(btn_frame, text="🔄 Atualizar", command=atualizar_lista, **btn_config)
btn_capitais = tk.Button(btn_frame, text="🏙️ Capitais", command=inserir_capitais_brasil, **btn_config)

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

# Cores alternadas para linhas
tree.tag_configure('oddrow', background='#f0f0f0')
tree.tag_configure('evenrow', background='#ffffff')

# Carregar dados iniciais
atualizar_lista()

# Centralizar janela na tela
root.eval('tk::PlaceWindow . center')

root.mainloop()
