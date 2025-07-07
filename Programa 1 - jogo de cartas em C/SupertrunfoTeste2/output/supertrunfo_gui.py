import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

ARQUIVO = "supertrunfoteste2.txt"

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
        messagebox.showwarning("Aviso", "Selecione uma cidade primeiro!")
        return
    
    # Obter o índice real na lista de cidades
    item_index = int(tree.item(selected_item[0], 'values')[0]) - 1
    cidades = ler_cidades()
    
    if item_index < 0 or item_index >= len(cidades):
        messagebox.showerror("Erro", "Índice inválido!")
        return
    
    c = cidades[item_index]
    detalhes = (
        f"Estado: {c[0]}\n"
        f"Código IBGE: {c[1]}\n"
        f"Nome: {c[2]}\n"
        f"População: {c[3]}\n"
        f"PIB: {c[4]}\n"
        f"Área: {c[5]}\n"
        f"Pontos Turísticos: {c[6]}\n"
        f"Densidade Populacional: {c[7]}\n"
        f"PIB per Capita: {c[8]}"
    )
    
    detalhes_win = tk.Toplevel(root)
    detalhes_win.title("Detalhes da Cidade")
    detalhes_win.geometry("520x340")
    detalhes_win.resizable(False, False)
    
    tk.Label(detalhes_win, text="Detalhes da Cidade", font=("Fira Code", 16, "bold")).pack(pady=10)
    
    texto = tk.Text(detalhes_win, wrap=tk.WORD, font=("Fira Code", 13), width=54, height=12)
    texto.insert(tk.END, detalhes)
    texto.config(state=tk.DISABLED)
    texto.pack(padx=15, pady=5)
    
    tk.Button(
        detalhes_win, 
        text="Fechar", 
        command=detalhes_win.destroy, 
        font=("Fira Code", 13), 
        width=12, 
        height=1
    ).pack(pady=10)

def remover_cidade():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Aviso", "Selecione uma cidade primeiro!")
        return
    
    resposta = messagebox.askyesno("Confirmação", "Deseja realmente remover esta cidade?")
    if not resposta:
        return
    
    item_index = int(tree.item(selected_item[0], 'values')[0]) - 1
    cidades = ler_cidades()
    
    if 0 <= item_index < len(cidades):
        del cidades[item_index]
        salvar_cidades(cidades)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Cidade removida com sucesso!")

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
        valor = simpledialog.askstring(titulo, texto_label)
        if valor is None:  # Usuário cancelou
            return
        nova.append(valor)
    
    cidades = ler_cidades()
    cidades.append(nova)
    salvar_cidades(cidades)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Cidade adicionada com sucesso!")

def inserir_capitais_brasil():
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
        ["RR", "1400100", "Boa Vista", "430000", "13493364", "7", "4", "61428.57", "31.38"],
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
    messagebox.showinfo("Sucesso", "Capitais brasileiras adicionadas com sucesso!")

# Configuração da janela principal
root = tk.Tk()
root.title("Super Trunfo - Cidades")
root.geometry("900x600")
root.resizable(False, False)

# Frame para os botões
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_style = {"font": ("Fira Code", 12), "width": 12, "height": 1}

btns = [
    ("Detalhes", exibir_detalhes),
    ("Adicionar", adicionar_cidade),
    ("Remover", remover_cidade),
    ("Atualizar", atualizar_lista),
    ("Inserir Capitais", inserir_capitais_brasil)
]

for text, command in btns:
    tk.Button(btn_frame, text=text, command=command, **btn_style).pack(side=tk.LEFT, padx=5)

# Frame para a tabela
tabela_frame = tk.Frame(root)
tabela_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Configuração da Treeview
tree = ttk.Treeview(
    tabela_frame,
    columns=("ID", "Cidade", "Estado", "População", "PIB", "Área", "Pontos"),
    show="headings"
)

# Definir cabeçalhos e colunas
headers = [
    ("ID", 50),
    ("Cidade", 150),
    ("Estado", 60),
    ("População", 100),
    ("PIB", 100),
    ("Área", 80),
    ("Pontos", 80)
]

for text, width in headers:
    tree.heading(text, text=text)
    tree.column(text, width=width, anchor=tk.CENTER)

# Barra de rolagem
scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.pack(fill=tk.BOTH, expand=True)

# Carregar dados iniciais
atualizar_lista()

root.mainloop()
