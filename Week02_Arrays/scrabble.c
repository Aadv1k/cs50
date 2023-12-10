#include <stdio.h>
#include <cs50.h>
#include <ctype.h>

static int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string s);

int main(void)
{
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }

    return 0;
}

int compute_score(string s)
{
    int score = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (isalpha(s[i]))
        {
            score += POINTS[tolower(s[i]) - 'a'];
        }
    }

    return score;
}
