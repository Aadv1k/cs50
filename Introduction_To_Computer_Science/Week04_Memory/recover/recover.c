#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

#define BLOCK_SIZE 512
#define JPEG_SIGNATURE_1 0xff
#define JPEG_SIGNATURE_2 0xd8
#define JPEG_SIGNATURE_3 0xff
#define JPEG_SIGNATURE_MASK 0xf0
#define JPEG_SIGNATURE_PREFIX 0xe0
#define FILENAME_LENGTH 8

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s IMAGE\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Unable to open the file.\n");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    int jpgCount = 0;
    FILE *currentJpg = NULL;

    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == JPEG_SIGNATURE_1 &&
            buffer[1] == JPEG_SIGNATURE_2 &&
            buffer[2] == JPEG_SIGNATURE_3 &&
            (buffer[3] & JPEG_SIGNATURE_MASK) == JPEG_SIGNATURE_PREFIX)
        {
            if (currentJpg != NULL)
            {
                fclose(currentJpg);
            }

            char filename[FILENAME_LENGTH];
            sprintf(filename, "%03d.jpg", jpgCount);
            currentJpg = fopen(filename, "w");
            jpgCount++;
        }

        if (currentJpg != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, currentJpg);
        }
    }

    if (currentJpg != NULL)
    {
        fclose(currentJpg);
    }

    fclose(file);

    return 0;
}
