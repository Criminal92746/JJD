HELLO  WORLD!
TERMINAL 🌎 
FUCK THE SYSTEM
include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main (int argc, const char* argv) {
  int fd = open(".hello_there", O_RDONLY);
  int res = dup2(fd, 99);
  char *newargv[] = { NULL };
  char *newenviron[] = { NULL };

  printf("%d\n", res);
  printf("Success\n");
  execve("./riddle", newargv, newenviron);
}
