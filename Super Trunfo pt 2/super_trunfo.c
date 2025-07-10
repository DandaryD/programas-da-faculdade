#include <stdio.h>

//Passos: 
//1- Definir as requisições a serem feitas para o usuário inserir os dados da carta
//2- Exibir as cartas formadas ao unuário
//====================================================================================

int main () {
    //Definição das varáveis 
    // cidade 1 
    char letra_Cod1[2];
    char numero_Cod1[3];
    char codigo1[5];
    char nome_Cidade1[100];
    int populacao1;
    float area_cidade1;
    float PIB1;
    int pontos_turisticos1;

    // cidade 2
    char letra_Cod2[2];
    char numero_Cod2[3];
    char codigo2[5];
    char nome_Cidade2[100];
    int populacao2;
    float area_cidade2;
    float PIB2;
    int pontos_turisticos2;

//=========================================================================================
//coleta e amarzenamento dos dados da Carta1


    printf("Digite a letra do estado (A-H): ");
    scanf(" %1s", letra_Cod1);

    printf("Digite o número (01 a 04): ");
    scanf(" %2s", numero_Cod1);

    printf("Digite o nome da cidade: ");
    scanf(" %[^\n]", nome_Cidade1);

    printf("Digite o número de habitantes: ");
    scanf("%d", &populacao1);

    printf("Digite a área da cidade em km²: ");
    scanf("%f", &area_cidade1);

    printf("Digite o PIB da cidade: ");
    scanf("%f", &PIB1);

    printf("Digite o número de pontos turísticos: ");
    scanf("%d", &pontos_turisticos1);
  //.......................................................................................
//coleta e amarzenamento dos dados da Carta2 
    printf("Digite a letra do estado (A-H): ");
    scanf(" %1s", letra_Cod2);

    printf("Digite o número (01 a 04): ");
    scanf(" %2s", numero_Cod2);

    printf("Digite o nome da cidade: ");
    scanf(" %[^\n]", nome_Cidade2);

    printf("Digite o número de habitantes: ");
    scanf("%d", &populacao2);

    printf("Digite a área da cidade em km²: ");
    scanf("%f", &area_cidade2);

    printf("Digite o PIB da cidade: ");
    scanf("%f", &PIB2);

    printf("Digite o número de pontos turísticos: ");
    scanf("%d", &pontos_turisticos2);

//===========================================================================================
//2- Exibir as cartas formadas ao unuário
    snprintf(codigo1, sizeof(codigo1), "%s%s", letra_Cod1, numero_Cod1);
    snprintf(codigo2, sizeof(codigo2), "%s%s", letra_Cod2, numero_Cod2);

    printf("\n===========================\n");
    printf("     CARTAS CADASTRADAS     \n");
    printf("===========================\n");

    printf("\n------ CARTA 1 ------\n");
    printf("Código da Carta: %s\n", codigo1);
    printf("Nome da Cidade: %s\n", nome_Cidade1);
    printf("População: %d\n", populacao1);
    printf("Área: %.2f km²\n", area_cidade1);
    printf("PIB: %.2f bilhões\n", PIB1);
    printf("Pontos Turísticos: %d\n", pontos_turisticos1);

    printf("\n------ CARTA 2 ------\n");
    printf("Código da Carta: %s\n", codigo2);
    printf("Nome da Cidade: %s\n", nome_Cidade2);
    printf("População: %d\n", populacao2);
    printf("Área: %.2f km²\n", area_cidade2);
    printf("PIB: %.2f bilhões\n", PIB2);
    printf("Pontos Turísticos: %d\n", pontos_turisticos2);

    return 0;
}
