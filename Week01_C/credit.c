#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string card_number;
    do
    {
        card_number = get_string("Number: ");
    }
    while (card_number == NULL || strlen(card_number) == 0);

    int sum = 0;
    int digit_count = 0;

    for (int i = strlen(card_number) - 1; i >= 0; i--)
    {
        int digit = card_number[i] - '0';

        if (digit_count % 2 == 1)
        {
            digit *= 2;

            if (digit > 9)
            {
                digit = digit % 10 + 1;
            }
        }

        sum += digit;
        digit_count++;
    }

    if (sum % 10 == 0)
    {
        if ((strlen(card_number) == 15) &&
            (strncmp(card_number, "34", 2) == 0 || strncmp(card_number, "37", 2) == 0))
        {
            printf("amex\n");
        }
        else if ((strlen(card_number) == 16) &&
                 (strncmp(card_number, "51", 2) == 0 || strncmp(card_number, "52", 2) == 0 ||
                  strncmp(card_number, "53", 2) == 0 || strncmp(card_number, "54", 2) == 0 ||
                  strncmp(card_number, "55", 2) == 0))
        {
            printf("mastercard\n");
        }
        else if ((strlen(card_number) == 13 || strlen(card_number) == 16) &&
                 strncmp(card_number, "4", 1) == 0)
        {
            printf("visa\n");
        }
        else
        {
            printf("invalid\n");
        }
    }
    else
    {
        printf("invalid\n");
    }

    return 0;
}
