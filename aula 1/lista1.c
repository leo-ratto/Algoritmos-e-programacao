# include <stdio.h>
# include <string.h>

//Exercício 01
/*
Escreva um programa que converte a temperatura de Celsius para Fahrenheit.

fahrenheit = celcius * 9/5 + 32
*/
/*
int main() {
    
    float c, f;

    printf("Insira a temperatura em Celsius: ");

    scanf("%f", &c);

    f = (c * 9.0f / 5.0f) + 32.0f;

    printf("Temperatura em Fahrenheit: %.2f\n", f);
    
    return 0;
}
*/

//Exercício 02
/*
Escreva um programa para calcular a área de uma esfera. Seu programa deve declarar uma
constante Pi de valor 3.141592. Para calcularmos a área da superfície da esfera utilizamos a
seguinte fórmula: A = 4 * pi * r^2.
*/
/*
int main(){
    float r, pi = 3.141592;
    
    printf("\nInsira o valor do raio da esfera em cm: ");
    
    scanf("%f", &r);
    
    float A = 4 * pi * r * r;
    
    printf("\nÁrea: %.2fcm³\n", A);
    
    return 0;
}
*/

//Exercício 03
/*
Uma biblioteca está digitalizando seu acervo e precisa de um sistema para registrar os livros. O
sistema deve coletar o título do livro, o número de páginas e o ano de publicação. Deve então
calcular o número total de caracteres no título, dobrar o número de páginas e ajustar o ano de
publicação multiplicando-o por 2.
*/
/*
int main(){
    char livro[100];
    
    int ano;
    unsigned int paginas;
    
    printf("\ninsira o título do livro: ");
    fgets(livro, sizeof(livro), stdin);
    livro[strcspn(livro, "\n")] = 0;
    
    int tamanho = strlen(livro);
    
    printf("\nInsira o número de páginas do livro: ");
    scanf("%u", &paginas);
    
    printf("\nInsira o ano de publicação do livro: ");
    scanf("%d", &ano);
    
    ano *= 2;
    
    paginas <<= 1;
    
    printf("\nO livro '%s' possui %d caracteres no título, com o número de páginas dobrado sendo %u e o ano de publicação * 2 sendo %d.\n", livro, tamanho, paginas, ano);
    
    return 0;
}
*/

//Exercício 04
/*
Uma fábrica precisa calcular a produção diária de uma linha de montagem. Cada linha tem um
nome, o número de itens produzidos por hora e o número de horas trabalhadas no dia. O sistema
deve calcular a produção total do dia, triplicar a produção usando deslocamento de bits e mostrar
1 se a linha for produtiva ou 0, caso contrário. A linha é classificada como produtiva se os itens
produzidos forem superior a 1000. 
*/
/*
int main(){
    char nome[100];
    
    unsigned int itens, horas, total;
    
    printf("\nInsira o nome da linha de montagem: ");
    
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = 0;
    
    printf("\nInsira o total de itens produzidos por hora: ");
    scanf("%u", &itens);
    
    printf("\nInsira a quantidade de horas trabalhadas no dia: ");
    scanf("%u", &horas);
    
    total = itens * horas;
    
    total = (total << 1) + total;
    
    printf("\nNome da linha de produção: %s\nTotal do Dia (triplicada): %u\nItens Produzidos por Hora: %u\n", nome, total, itens);
    
    return 0;
}
*/