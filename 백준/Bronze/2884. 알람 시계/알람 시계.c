#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void) {
    int hour, min, total;
    scanf("%d %d", &hour, &min);
    if (hour == 0) {
        total = 24 * 60 + min;
    }
    else
        total = hour * 60 + min;

    total = total - 45;
    hour = total / 60;
    if (hour == 24) {
        hour = 0;
    }
    min = total % 60;
    printf("%d %d", hour, min);
    return 0;
}