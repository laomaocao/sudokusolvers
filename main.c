#include <stdio.h>
#include <stdlib.h>
#include "sudoku.h"
int init(struct sudoku *input)
{int i,j;
for (i=0;i<9;i++)
    for (j=0;j<9;j++)
        {input->d[i][j]=511;
        }
 /*
|8|_|_|_|_|_|_|_|_|
|_|_|3|6|_|_|_|_|_|
|_|7|_|_|9|_|2|_|_|
|_|5|_|_|_|7|_|_|_|
|_|_|_|_|4|5|7|_|_|
|_|_|_|1|_|_|_|3|_|
|_|_|1|_|_|_|_|6|8|
|_|_|8|5|_|_|_|1|_|
|_|9|_|_|_|_|4|_|_|

|8|1|2|7|5|3|6|4|9|
|9|4|3|6|8|2|1|7|5|
|6|7|5|4|9|1|2|8|3|
|1|5|4|2|3|7|8|9|6|
|3|6|9|8|4|5|7|2|1|
|2|8|7|1|6|9|5|3|4|
|5|2|1|9|7|4|3|6|8|
|4|3|8|5|2|6|9|1|7|
|7|9|6|3|1|8|4|5|2|


 input->d[0][0]=EIGHT+READY;
 input->d[1][2]=THREE+READY;
 input->d[1][3]=SIX+READY;
 input->d[2][1]=SEVEN+READY;
 input->d[2][4]=NINE+READY;
 input->d[2][6]=TWO+READY;
 input->d[3][1]=FIVE+READY;
 input->d[3][5]=SEVEN+READY;
 input->d[4][4]=FOUR+READY;
 input->d[4][5]=FIVE+READY;
 input->d[4][6]=SEVEN+READY;
 input->d[5][3]=ONE+READY;
 input->d[5][7]=THREE+READY;
 input->d[6][2]=ONE+READY;
 input->d[6][7]=SIX+READY;
 input->d[6][8]=EIGHT+READY;
 input->d[7][2]=EIGHT+READY;
 input->d[7][3]=FIVE+READY;
 input->d[7][7]=ONE+READY;
 input->d[8][1]=NINE+READY;
 input->d[8][6]=FOUR+READY;
 */
return 1;
};

int rapidlog2(unsigned int a)
{int i=0,b=a^READY;
while( (b>>i) > 0)
    i++;
return i;
}

int show(struct sudoku *input)
{
int i,j;
for (i=0;i<9;i++)
    {
    printf("|");
    for (j=0;j<9;j++)
        (input->d[i][j]&READY)?printf("%d|",rapidlog2(input->d[i][j])):printf(" |");

/*        if (input->d[i][j]&READY)
            printf("%d|",rapidlog2(input->d[i][j]);
        esle
            printf(" |");
        }
*/
    printf("\n");
    }
return 1;
};
/*数1的个数*/
int countnum(unsigned d)
{int t=d&0x01FF,num=0,i;
for(i=0;i<10;i++)
    {
    if (t&(1<<i))
        num++;
    }
return num;
}

unsigned int isvalid(struct sudoku *input)
{
int i,j;
for (i=0;i<9;i++)
    for (j=0;j<9;j++)
        if((input->d[i][j]&READY)==0)
            return 0;
return 1;
}

int dedup(struct sudoku *input)
{
int i,j,x,y,t;
int hasdup=0;
for (i=0;i<9;i++)
    for (j=0;j<9;j++)
        {
        if(input->d[i][j]&READY)/*某个确定值*/
            {t=input->d[i][j]^READY;
            /*本行去重*/
            for(x=0;x<9;x++)
                {if((x!=j)&&(t&input->d[i][x]))
                    {if (input->d[i][j]==input->d[i][x])
                        return -1;  /*这个分支有错误*/
                    if(countnum(input->d[i][x])==2)
                        {input->d[i][x]=input->d[i][x]^t;
                        input->d[i][x]=input->d[i][x]|READY;
                        }
                    else
                        input->d[i][x]=input->d[i][x]^t;
                    hasdup=1;
                    }
                }

            /*本列去重 */
            for(y=0;y<9;y++)
                {if((y!=i)&&(t&input->d[y][j]))
                    {if(input->d[i][j]==input->d[y][j])
                        return -1;
                     if(countnum(input->d[y][j])==2)
                        {input->d[y][j]=input->d[y][j]^t;
                        input->d[y][j]=input->d[y][j]|READY;
                        }
                    else
                        input->d[y][j]=input->d[y][j]^t;
                    hasdup=1;
                    }
                }
            /*本块去重*/
            for(x=i/3*3;x<i/3*3+3;x++)
                for(y=j/3*3;y<j/3*3+3;y++)
                    {if((x!=i)&&(y!=j)&&(t&input->d[x][y]))
                        {if(input->d[x][y]==input->d[i][j])
                            return -1;
                         if(countnum(input->d[x][y])==2)
                            {input->d[x][y]=input->d[x][y]^t;
                            input->d[x][y]=input->d[x][y]|READY;
                            }
                         else
                            input->d[x][y]=input->d[x][y]^t;
                        hasdup=1;
                        }

                    }

        }
    }
 return hasdup;
}

int findmin(struct sudoku *input,int *x,int *y)
{int i,j,count=10,c;
for (i=0;i<9;i++)
    for (j=0;j<9;j++)
        {c=countnum(input->d[i][j]);
        if(!(input->d[i][j]&READY) && c<count)
            {count=c;
            *x=i;
            *y=j;
            }
        }
return 1;
}

unsigned int resolv(struct sudoku *input)
{int guessx,guessy,i;
unsigned short int select;
struct sudoku guess;
switch (dedup(input))
    {
    case 1:/* 有消除的数字，继续消除*/
        {
        resolv(input);
        }
    case -1: /*这个分支不对，返回*/
        return -1;
    case 0: /*消无可消，要么解出来了，要么找各最少的？穷举一下*/
        {
        if (isvalid(input))
            {show(input);
            exit(1);
            }
        findmin(input,&guessx,&guessy);
        select=input->d[guessx][guessy];
        for (i=0;i<10;i++)
            {if(select&(1<<i))
                {guess=*input;
                guess.d[guessx][guessy]=((1<<i)+READY);
                resolv(&guess);
                }
            }
        }

    }
return 1;
}
int main()
{   struct sudoku p;
    unsigned int inputd[9],line,i;
    init(&p);
    while (1)
        {printf("select line:\n");
         scanf("%1ud",&line);
         printf("input value for line %d. 0 for blank.for example:'0,0,4,0,0,3,2,0,0':\n",line);
         scanf("%u,%u,%u,%u,%u,%u,%u,%u,%u",&inputd[0],&inputd[1],&inputd[2],&inputd[3],&inputd[4],&inputd[5],&inputd[6],&inputd[7],&inputd[8]);
         for (i=0;i<9;i++)
            {if (inputd[i]!=0)
                {
                p.d[line-1][i]=(1<<(inputd[i]-1))+READY;
                }
            printf("row: %d , column: %d, value %d \n",line,i,inputd[i]);
            }
         getchar();
         printf("finished?(y/n)");
         if (getchar()=='y')
            break;
        }
    printf("begin to solve:\n");
    show(&p);
    printf("\nresult:\n");
    resolv(&p);
    return 0;
}
