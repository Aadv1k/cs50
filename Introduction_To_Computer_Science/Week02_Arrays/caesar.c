#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (!only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int offset = atoi(argv[1]);
    string input = get_string("plaintext: ");

    const string lower = "abcdefghijklmnopqrstuvwxyz";
    const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const int max = 26;

    printf("ciphertext: ");
    for (int i = 0; i < strlen(input); i++)
    {
        char current = input[i];
        if (isalpha(current))
        {
            char base = isupper(current) ? 'A' : 'a';
            int idx = (current - base + offset) % max;
            printf("%c", isupper(current) ? upper[idx] : lower[idx]);
        }
        else
        {
            printf("%c", current);
        }
    }

    printf("\n");
    return 0;
}

bool only_digits(string s)
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}
