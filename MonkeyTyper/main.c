#include <stdio.h>
#include <string.h>
#include <termios.h>
#include <unistd.h>

int readFile(char allText[][100], int maxlines) {
  FILE *ftpr = fopen("./text.txt", "r");
  if (ftpr == NULL) {
    perror("Error opening file");
    return 0;
  }

  char mystring[100] = {};
  int i = 0;

  while (fgets(mystring, 100, ftpr) && i < maxlines) {
    mystring[strcspn(mystring, "\n")] = '\0';
    strcpy(allText[i], mystring);
    i++;
  }

  fclose(ftpr);
  return i;
}

char getch(void) {
  struct termios oldt, newt;
  char ch;

  // Get terminal settigns
  tcgetattr(STDIN_FILENO, &oldt);
  newt = oldt;

  // Disable canonical mode and echo
  newt.c_lflag &= ~(ICANON | ECHO);
  tcsetattr(STDIN_FILENO, TCSANOW, &newt);

  // Read one character
  ch = getchar();

  // Restore terminal settings
  tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

  return ch;
}
int typing(char leString[100]) {
  printf("%s\n", leString);
  int i = 0;
  char in;
  char myString[100] = {};

  while (1) {
    in = getch();
    if (in == leString[i]) {
      printf("\e[0;32m%c", in);
      myString[i] = in;
    } else {
      if ((int)in == 127) {
        printf("\b \b");
        i--;
        continue;
      }
      if ((int)in == 10) {
        return -1;
      }
      printf("\e[0;31m%c", in);
    }
    i++;
    if (strcmp(myString, leString) == 0) {
      printf("\e[0m\n");
      return 1;
    }
  }
}
int main(int argc, char *argv[]) {
  char allText[100][100];
  int line_count = readFile(allText, sizeof(allText));

  for (int i = 0; i < line_count; i++) {
    typing(allText[i]);
  }

  return 0;
}
