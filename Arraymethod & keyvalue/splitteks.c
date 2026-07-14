#include <stdio.h>
#include <string.h>

struct ArraySplit {
 char teks[100][100];
 int len;
};

int main() {
 struct ArraySplit array;
 array.len = 0;
 char teks[] = "apel,rambutan,mangga,pisang,dll";
 int tekslen = strlen(teks);
 int teksperarr = 0;
 for (int i = 0;i<tekslen;i++) {
  if (teks[i] == ',') {
	  array.teks[array.len][teksperarr] = '\0';
	  array.len++;
	  teksperarr = 0;
}
  else {
	  array.teks[array.len][teksperarr] = teks[i]; 
	  teksperarr++;
  }
 }
 array.teks[array.len][teksperarr] = '\0';
 for (int i=0;i<=array.len;i++) {
	 printf("%s\n",array.teks[i]);
 }
 return 0;
}
