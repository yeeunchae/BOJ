#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int n,a,b;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
    }
    return 0;
}