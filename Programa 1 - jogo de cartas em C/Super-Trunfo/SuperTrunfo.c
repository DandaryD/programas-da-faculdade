#include <stdio.h>
#include <string.h>

#define MAX_CIDADES 100

typedef struct {
    char estado[3];
    int codigo;
    char nomeCidade[100];
    long int populacao;
    double pib;
    double area;
    int numPontosTuristicos;
    double densidadePopulacional;
    double pibPerCapita;
} Cidade;

// Função para exibir uma carta/cidade
void exibirCarta(const Cidade *c, int indice) {
    printf("\n--- Detalhes da Carta %d ---\n", indice + 1);
    printf("Estado: %s\n", c->estado);
    printf("Codigo: %d\n", c->codigo);
    printf("Nome da Cidade: %s\n", c->nomeCidade);
    printf("Populacao: %ld habitantes\n", c->populacao);
    printf("PIB: %.2lf\n", c->pib);
    printf("Area: %.2lf km2\n", c->area);
    printf("Pontos Turisticos: %d\n", c->numPontosTuristicos);
    printf("Densidade Populacional: %.2lf hab/km2\n", c->densidadePopulacional);
    printf("PIB per Capita: %.2lf\n", c->pibPerCapita);
}

// Função para corrigir dados de uma cidade já cadastrada
void corrigirCidade(Cidade *c) {
    int opcao;
    do {
        printf("\nQual campo deseja corrigir?\n");
        printf("1 - Estado\n");
        printf("2 - Codigo IBGE\n");
        printf("3 - Nome da Cidade\n");
        printf("4 - Populacao\n");
        printf("5 - PIB\n");
        printf("6 - Area\n");
        printf("7 - Pontos Turisticos\n");
        printf("0 - Sair da correcao\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        while (getchar() != '\n');

        switch (opcao) {
            case 1:
                printf("Digite a sigla do estado (ex: SP): ");
                scanf("%2s", c->estado);
                while (getchar() != '\n');
                break;
            case 2:
                printf("Digite o codigo IBGE oficial do municipio: ");
                scanf("%d", &c->codigo);
                while (getchar() != '\n');
                break;
            case 3:
                printf("Digite o nome do municipio: ");
                fgets(c->nomeCidade, sizeof(c->nomeCidade), stdin);
                c->nomeCidade[strcspn(c->nomeCidade, "\n")] = 0;
                break;
            case 4:
                printf("Digite o numero de habitantes do municipio: ");
                scanf("%ld", &c->populacao);
                while (getchar() != '\n');
                break;
            case 5:
                printf("Digite o PIB da cidade (em unidades monetarias, ex: milhoes de Reais): ");
                scanf("%lf", &c->pib);
                while (getchar() != '\n');
                break;
            case 6:
                printf("Digite a area da cidade (em km2): ");
                scanf("%lf", &c->area);
                while (getchar() != '\n');
                break;
            case 7:
                printf("Digite o numero de pontos turisticos: ");
                scanf("%d", &c->numPontosTuristicos);
                while (getchar() != '\n');
                break;
            case 0:
                printf("Saindo da correcao.\n");
                break;
            default:
                printf("Opcao invalida! Tente novamente.\n");
        }
        // Atualiza propriedades derivadas após qualquer alteração
        if (c->area > 0)
            c->densidadePopulacional = (double)c->populacao / c->area;
        else
            c->densidadePopulacional = 0.0;

        if (c->populacao > 0)
            c->pibPerCapita = c->pib / (double)c->populacao;
        else
            c->pibPerCapita = 0.0;
    } while (opcao != 0);
}

// Função para cadastrar uma nova cidade (com possibilidade de correção)
void cadastrarCidade(Cidade *c) {
    printf("\nCadastrando nova cidade:\n");

    printf("Digite a sigla do estado (ex: SP): ");
    scanf("%2s", c->estado);
    while (getchar() != '\n');

    printf("Digite o codigo IBGE oficial do municipio: ");
    scanf("%d", &c->codigo);
    while (getchar() != '\n');

    printf("Digite o nome do municipio: ");
    fgets(c->nomeCidade, sizeof(c->nomeCidade), stdin);
    c->nomeCidade[strcspn(c->nomeCidade, "\n")] = 0;

    printf("Digite o numero de habitantes do municipio: ");
    scanf("%ld", &c->populacao);
    while (getchar() != '\n');

    printf("Digite o PIB da cidade (em unidades monetarias, ex: milhoes de Reais): ");
    scanf("%lf", &c->pib);
    while (getchar() != '\n');

    printf("Digite a area da cidade (em km2): ");
    scanf("%lf", &c->area);
    while (getchar() != '\n');

    printf("Digite o numero de pontos turisticos: ");
    scanf("%d", &c->numPontosTuristicos);
    while (getchar() != '\n');

    // Calcula propriedades derivadas
    if (c->area > 0)
        c->densidadePopulacional = (double)c->populacao / c->area;
    else
        c->densidadePopulacional = 0.0;

    if (c->populacao > 0)
        c->pibPerCapita = c->pib / (double)c->populacao;
    else
        c->pibPerCapita = 0.0;

    // Exibe os dados e pergunta se deseja corrigir
    char corrigir;
    do {
        exibirCarta(c, 0);
        printf("\nDeseja corrigir algum dado desta cidade? (s/n): ");
        scanf(" %c", &corrigir);
        while (getchar() != '\n');
        if (corrigir == 's' || corrigir == 'S') {
            corrigirCidade(c);
        }
    } while (corrigir == 's' || corrigir == 'S');
}

// Função para exibir todas as cidades cadastradas
void exibirTodasCidades(const Cidade cidades[], int total) {
    if (total == 0) {
        printf("\nNenhuma cidade cadastrada ainda.\n");
        return;
    }
    printf("\n--- Cartas Cadastradas ---\n");
    for (int i = 0; i < total; i++) {
        exibirCarta(&cidades[i], i);
    }
}

// Função para remover uma cidade cadastrada
void removerCidade(Cidade cidades[], int *total) {
    if (*total == 0) {
        printf("\nNenhuma cidade cadastrada para remover.\n");
        return;
    }
    exibirTodasCidades(cidades, *total);
    int indice;
    printf("\nDigite o numero da carta que deseja remover (1 a %d): ", *total);
    scanf("%d", &indice);
    while (getchar() != '\n');
    if (indice < 1 || indice > *total) {
        printf("Indice invalido!\n");
        return;
    }
    // Remove a cidade deslocando as demais
    for (int i = indice - 1; i < *total - 1; i++) {
        cidades[i] = cidades[i + 1];
    }
    (*total)--;
    printf("Cidade removida com sucesso!\n");
}

int main() {
    Cidade cidades[MAX_CIDADES];
    int total = 0;
    int opcao;

    printf("--- Cadastro de Cartas Super Trunfo (Cidades) ---\n");

    do {
        printf("\nMenu Principal:\n");
        printf("1 - Cadastrar nova cidade\n");
        printf("2 - Verificar cidades cadastradas\n");
        printf("3 - Remover cidade cadastrada\n");
        printf("0 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        while (getchar() != '\n');

        switch (opcao) {
            case 1:
                if (total < MAX_CIDADES) {
                    cadastrarCidade(&cidades[total]);
                    total++;
                    printf("Cidade cadastrada com sucesso!\n");
                } else {
                    printf("Limite maximo de cidades atingido!\n");
                }
                break;
            case 2:
                exibirTodasCidades(cidades, total);
                break;
            case 3:
                removerCidade(cidades, &total);
                break;
            case 0:
                printf("Saindo do programa...\n");
                break;
            default:
                printf("Opcao invalida! Tente novamente.\n");
        }
    } while (opcao != 0);

    return 0;
}
