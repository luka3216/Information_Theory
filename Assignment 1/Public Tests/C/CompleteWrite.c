#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
  int from = open(argv[1], O_RDONLY);
  truncate(argv[2], 0);
  int to = open(argv[2], O_WRONLY);
  char buff[8];
  unsigned char tmp = 128;
  unsigned char bit = 0;
  for (int size = read(from, buff, 8); size > 0; size = read(from, buff, 8))
  {
    bit = 0;
    tmp = 128;
    for (int i = 0; i < size; i++)
    {
      if (buff[i] == '1')
      {
        bit = bit | tmp;
      }
      tmp = tmp >> 1;
    }
    if (size == 8)
    {
      write(to, &bit, 1);
    }
  }
  if (tmp != 0)
  {
    bit = bit | tmp;
    write(to, &bit, 1);
  } else {
    bit = 128;
    write(to, &bit, 1);
  }
  close(from);
  close(to);
  return 0;
}
