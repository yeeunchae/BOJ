#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int i,n;
    scanf("%d",&n);
    n=n/4;
    for(i=0;i<n;i++){
        printf("long ");
    }
    printf("int");
    return 0;
}