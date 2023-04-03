#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int total,price,total_n,item;
    int sum=0;
    scanf("%d\n",&total);
    scanf("%d\n",&total_n);
    for(int i=0;i<total_n;i++){
        scanf("%d %d\n",&price,&item);
        sum=sum+(price*item);
    }
    if(sum==total)
        printf("Yes");
    else
        printf("No");
    return 0;
}