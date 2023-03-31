#include<stdio.h>
#define _CRT_SECURE_NO_WARNINGS
int main(void) {
    int hour, minute, time;
    scanf("%d %d", &hour, &minute);
    scanf("%d", &time);
    int total_m;
    int total_h;
    if (minute + time > 59) {
        total_m = (minute + time) % 60;
        total_h = (minute + time) / 60;
        hour = hour + total_h;
        if (hour > 23) {
            hour=hour - 24;
        }
    }
    else if (minute + time < 59) {
        total_m = minute + time;
    }
    printf("%d %d", hour,total_m);
    return 0;
}