#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int i,a,b;
    scanf("%d %d",&a,&b);
    while(a!=0&&b!=0){
        printf("%d\n",a+b);
        scanf("%d %d",&a,&b);
    }
    return 0;
}