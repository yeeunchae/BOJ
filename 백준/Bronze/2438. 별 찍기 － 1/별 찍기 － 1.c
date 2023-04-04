#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int i,j,n;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        for(j=1;j<=i;j++)
            printf("*");
        printf("\n");
    }

}