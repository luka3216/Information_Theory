#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char const *argv[])
{
  int from = open(argv[1], O_RDONLY);
  truncate(argv[2], 0);
  int to = open(argv[2], O_WRONLY);
  char buff[256];
  for (int size = read(from, buff, 256); size > 0; size = read(from, buff, 256))
  {
    for (int i = 0; i < size; i++)
    {
      unsigned char tmp = 128;
      for (int j = 0; j < 8; j++)
      {
        int bit = tmp & buff[i];
        if (bit)
        {
          write(to, "1", 1);
        }
        else
        {
          write(to, "0", 1);
        }
        tmp = tmp >> 1;
      }
    }
  }
  close(from);
  close(to);
  return 0;
}
