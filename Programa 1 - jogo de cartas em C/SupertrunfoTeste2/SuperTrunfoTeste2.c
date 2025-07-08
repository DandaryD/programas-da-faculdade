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

// Exibe detalhes de uma cidade
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

void corrigirCidade(Cidade *c) {
    int opcao;
    do {
        printf("\nQual campo deseja corrigir?\n");
        printf("1 - Estado\n2 - Codigo IBGE\n3 - Nome da Cidade\n4 - Populacao\n");
        printf("5 - PIB\n6 - Area\n7 - Pontos Turisticos\n0 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        while (getchar() != '\n');

        switch (opcao) {
            case 1:
                printf("Digite a sigla do estado (ex: SP): ");
                scanf("%2s", c->estado);
                break;
            case 2:
                printf("Digite o codigo IBGE: ");
                scanf("%d", &c->codigo);
                break;
            case 3:
                printf("Digite o nome do municipio: ");
                fgets(c->nomeCidade, sizeof(c->nomeCidade), stdin);
                c->nomeCidade[strcspn(c->nomeCidade, "\n")] = 0;
                break;
            case 4:
                printf("Digite a populacao: ");
                scanf("%ld", &c->populacao);
                break;
            case 5:
                printf("Digite o PIB: ");
                scanf("%lf", &c->pib);
                break;
            case 6:
                printf("Digite a area: ");
                scanf("%lf", &c->area);
                break;
            case 7:
                printf("Digite o numero de pontos turisticos: ");
                scanf("%d", &c->numPontosTuristicos);
                break;
            case 0:
                break;
            default:
                printf("Opcao invalida!\n");
        }

        // Atualiza campos derivados
        c->densidadePopulacional = (c->area > 0) ? (double)c->populacao / c->area : 0.0;
        c->pibPerCapita = (c->populacao > 0) ? c->pib / (double)c->populacao : 0.0;

    } while (opcao != 0);
}

void cadastrarCidade(Cidade *c) {
    printf("\nCadastrando nova cidade:\n");

    printf("Digite a sigla do estado (ex: SP): ");
    scanf("%2s", c->estado);
    while (getchar() != '\n');

    printf("Digite o codigo IBGE: ");
    scanf("%d", &c->codigo);
    while (getchar() != '\n');

    printf("Digite o nome do municipio: ");
    fgets(c->nomeCidade, sizeof(c->nomeCidade), stdin);
    c->nomeCidade[strcspn(c->nomeCidade, "\n")] = 0;

    printf("Digite a populacao: ");
    scanf("%ld", &c->populacao);

    printf("Digite o PIB: ");
    scanf("%lf", &c->pib);

    printf("Digite a area: ");
    scanf("%lf", &c->area);

    printf("Digite o numero de pontos turisticos: ");
    scanf("%d", &c->numPontosTuristicos);
    while (getchar() != '\n');

    // Atualiza campos derivados
    c->densidadePopulacional = (c->area > 0) ? (double)c->populacao / c->area : 0.0;
    c->pibPerCapita = (c->populacao > 0) ? c->pib / (double)c->populacao : 0.0;

    // Permite correção
    char corrigir;
    do {
        exibirCarta(c, 0);
        printf("\nDeseja corrigir algum dado? (s/n): ");
        scanf(" %c", &corrigir);
        while (getchar() != '\n');
        if (corrigir == 's' || corrigir == 'S') {
            corrigirCidade(c);
        }
    } while (corrigir == 's' || corrigir == 'S');
}

void exibirTodasCidades(const Cidade cidades[], int total) {
    if (total == 0) {
        printf("\nNenhuma cidade cadastrada ainda.\n");
        return;
    }
    for (int i = 0; i < total; i++) {
        exibirCarta(&cidades[i], i);
    }
}

void removerCidade(Cidade cidades[], int *total) {
    if (*total == 0) {
        printf("\nNenhuma cidade cadastrada para remover.\n");
        return;
    }

    exibirTodasCidades(cidades, *total);

    int indice;
    printf("\nDigite o numero da carta a remover (1 a %d): ", *total);
    scanf("%d", &indice);
    if (indice < 1 || indice > *total) {
        printf("Indice invalido!\n");
        return;
    }

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
        printf("2 - Ver cidades cadastradas\n");
        printf("3 - Remover cidade\n");
        printf("0 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        while (getchar() != '\n');

        switch (opcao) {
            case 1:
                if (total < MAX_CIDADES) {
                    cadastrarCidade(&cidades[total]);
                    total++;
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
                printf("Encerrando o programa...\n");
                break;
            default:
                printf("Opcao invalida!\n");
        }

    } while (opcao != 0);

    return 0;
}
