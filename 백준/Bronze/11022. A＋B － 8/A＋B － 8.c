#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int i,n,a,b;
    scanf("%d",&n);
    for(i=0; i<n; i++){
        scanf("%d %d",&a,&b);
        printf("Case #%d: %d + %d = %d\n",i+1,a,b,a+b);
    }
}