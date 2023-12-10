#include <cs50.h>
#include <stdio.h>

void print_p(int i, int height)
{
    int hc = i + 1;
    int sc = height - (i + 1);

    for (int j = 0; j < sc; j++)
    {
        putc(' ', stdout);
    }

    for (int j = 0; j < hc; j++)
    {
        putc('#', stdout);
    }

    putc(' ', stdout);
    putc(' ', stdout);

    for (int j = 0; j < hc; j++)
    {
        putc('#', stdout);
    }
}

int main(void)
{
    int height;

    do
    {
        height = get_int("Height: ");
    } while (height < 1 || height > 8);

    for (int i = 0; i < height; i++)
    {
        print_p(i, height);
        printf("\n");
    }
}
