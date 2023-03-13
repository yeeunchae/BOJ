//같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
//같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
//모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if(a==b && b==c)
        printf("%d",10000+a*1000);
    else if((a==b&&b!=c)||(a==c&&c!=b)){
        printf("%d",1000+a*100);
    }
    else if(c==b&&b!=a)
        printf("%d",1000+b*100);
    else{
        if(a>b&&a>c)
            printf("%d",a*100);
        else if(a<b&&b>c)
            printf("%d",b*100);
        else if(c>b&&a<c)
            printf("%d",c*100);
    }
    return 0;
}