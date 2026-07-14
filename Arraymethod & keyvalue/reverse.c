#include <stdio.h>
#include <string.h>
int main() {
 char teks[] = "Hello World";
 char x;
 int len = strlen(teks);
 int j = len-1;
 for(int i = 0;i<len/2;i++) {
  x = teks[i];
  teks[i] = teks[j];
  teks[j] = x;
  j--;
 }
 printf("%s\n",teks);
 return 0;
}
