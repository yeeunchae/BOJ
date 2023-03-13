// 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void){
    int year;
    scanf("%d",&year);
    if(year%4==0&&year%100!=0||year%400==0){
        printf("1");
    }
    else{
        printf("0");
    }
    return 0;
}