//线性表数据结构的定义
#define MAXSIZE 1024
typedef struct
{
	int Data[MAXSIZE];  //存放线性表结点的数据空间
	int Last;           //指示线性表当前长度

} List;

List MakeEmpty();