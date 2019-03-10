#define ONE 1
#define TWO 2
#define THREE 4
#define FOUR 8
#define FIVE 16
#define SIX 32
#define SEVEN 64
#define EIGHT 128
#define NINE 256
#define READY 1024

/*单元结构定义，1-9位表示某个数字的可能性，11位表示是否市确定值。发挥C语言牛逼的位操作*/
/* 9×9=81个单元*/
struct sudoku
{
unsigned short int d[9][9];
};
/*递归主函数*/
unsigned int resolv(struct sudoku *input);
/*去重*/
int dedup(struct sudoku *input);
/*检查合法性，是不是去重去到有单元市空值 */
unsigned int isvalid(struct sudoku *input);

