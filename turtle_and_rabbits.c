#include "stdio.h"

int main(){
    const int turtleV = 3, rabbitV = 9;
    
    int turtleS = 0,rabbitS = 0;
    
    int T;
    
    int move = 1,timeMove=0,timeRest = 0;
    
    scanf("%d",&T);
    
    while(T--){
        turtleS += turtleV*1;
        
        //bug 出现的原因是 - move=0触发后，下面的if(move=0)也会触发，导致timeRest++，继而影响%30这个条件的判断。需要将if(move==0)改为else
        if(move==1){
            rabbitS += rabbitV*1;
            timeMove++;
            if((timeMove%10== 0)&&(rabbitS>turtleS))
                move = 0;
            printf("tM=%d\n",timeMove);
        }
        
        if(move==0){
            timeRest++;
            if(timeRest%30 == 0)
                move = 1;
            printf("tR=%d\n",timeRest);
        }
        
        printf("%d  %d\n",turtleS ,rabbitS);
        
        if(rabbitS==turtleS){
            printf("%d, timeMove=%d,timeRest=%d,%d \n",
            timeMove+timeRest,timeMove, timeRest,rabbitS);
        }
    }
    
    if(turtleS>rabbitS)
        printf("@_@ %d",turtleS);
    else if(turtleS<rabbitS)
        printf("^_^ %d",rabbitS);
    else
        printf("-_- %d",turtleS);
    
}