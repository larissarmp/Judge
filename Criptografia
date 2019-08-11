/*

Autor: Larissa Ribeiro

Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o texto. 

Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”. O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.
Saída
Para cada entrada, deve-se apresentar a mensagem criptografada.
*/
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class Main{
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(in.readLine()), metade, tamanho;
        char[] M;
        char temporario;
        while (N-- > 0) {
            M = in.readLine().toCharArray();
            tamanho = M.length;
            metade = tamanho / 2;
            for (int i = 0; i < tamanho; i++) {
                if (Character.isLetter(M[i])) {
                    M[i] = (char) ((int) M[i] + 3);
                }
            }
            for (int i = 0; i < metade; i++) {
                temporario = M[i];
                M[i] = M[M.length - i - 1];
                M[M.length - i - 1] = temporario;
            }
            for (int i = (metade); i < tamanho; ++i) {
                M[i] = (char) ((int) M[i] - 1);
            }
            for (char Mi : M) {
                out.print(Mi);
            }
            out.println();
        }
        out.close();
    }
 
}
