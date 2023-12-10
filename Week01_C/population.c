#include <cs50.h>
#include <stdio.h>

#define DEATH_RATE 4
#define BORN_RATE 3

int main(void)
{
    int start_size;
    do
    {
        start_size = get_int("start size: ");
    }
    while (start_size < 9);

    int end_size;
    do
    {
        end_size = get_int("end size: ");
    }
    while (end_size < start_size);

    int years = 0;
    while (start_size < end_size)
    {
        int llama_born = start_size / BORN_RATE;
        int llama_passed = start_size / DEATH_RATE;
        start_size = start_size + llama_born - llama_passed;
        years++;
    }

    printf("Years: %d\n", years);

    return 0;
}
