#!/usr/bin/python3
import copy
sudu=[[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]

'''
# NO.124
def init():
	sudu[1][2]=[3]
	sudu[1][3]=[4]
	sudu[1][5]=[1]
	sudu[1][6]=[2]
	sudu[2][1]=[7]
	sudu[2][4]=[9]
	sudu[2][7]=[3]
	sudu[3][2]=[6]
	sudu[3][3]=[7]
	sudu[3][5]=[8]
	sudu[3][6]=[9]
	sudu[4][1]=[2]
	sudu[4][7]=[5]
	sudu[5][2]=[1]
	sudu[5][3]=[2]
	sudu[5][5]=[3]
	sudu[5][6]=[4]
	sudu[6][1]=[9]
	sudu[6][4]=[6]
	sudu[6][7]=[7]
	sudu[7][2]=[2]
	sudu[7][3]=[1]
	sudu[7][5]=[4]
	sudu[7][6]=[3]
'''
def init():
    global sudu,checkcell
    sudu=[[[8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [6], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [5], [7], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [3], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [6], [8]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [8], [5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [4], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]
        
    
def initfrom(input):
    for i in range(9):
        for j in range(9):
            if input[i*9+j] != '':
                global sudu
                sudu[i][j]=[input[i*9+j]]
                

def show(inputsudu):
	for i in range(9):
		for j in range(9):
			print('|',end='')
			if len(inputsudu[i][j]) > 1:
				print ("_",end='')
			else:
				print (inputsudu[i][j][0],end='')
		print('|')

def showreturn(inputsudu):
	result=""
	for i in range(9):
		for j in range(9):
			result=result+'|'
			if len(inputsudu[i][j]) > 1:
				result=result+'_'
			else:
				result=result+str(inputsudu[i][j][0])
		result=result+"\n"
	return result

#检查是不是无法去重了
def isdone(inputsudu):
    for i in range(9):
        for j in range(9):
            if len(inputsudu[i][j]) > 1:
                return False
    return True

#检查猜测的分支是否合法，是不是有的格子没有数值了
def isvalid(inputsudu):
    for i in range(9):
        for j in range(9):
            if len(inputsudu[i][j]) == 0:
                return False
    return True

#检查是不是合法解
def isdonevalid(inputsudu):
#每一行检查是否有重复
#    for i in range(9):
#        for j in range(9):
#            for k in range(j+1,9):
#                if sudu[i][j]==sudu[i][k]:
#                    return False

    for i in range(9):
       if list(set(inputsudu[i])) != inputsudu[i]:
           return False
#每一列检查是否有重复
    for i in range(9):
        for j in range(9):
            for k in range(j+1,9):
                if inputsudu[j][i]==inputsudu[k][i]:
                    return False
#每一块检查是否有重复
    for i in range(9):
        for j in range(9):
            for x in range(int(i/3)*3,int(i/3)*3+3):
                for y in range(int(j/3)*3,int(j/3)*3+3):
                    if not (x == i and y == j) and inputsudu[x][y]==inputsudu[i][j]:
                        return False
    return True

def removedup(inputsudu):
    hasdup=False
    for i in range(9):
        for j in range(9):
#逐行寻找已确定的值
            if len(inputsudu[i][j])==1:
#在本行去重
                for x in range(9):
                    if x != j and inputsudu[i][j][0] in inputsudu[i][x]:
                        inputsudu[i][x].remove(inputsudu[i][j][0])
                        if len(inputsudu[i][x])==1:
                            hasdup=True
#在本列去重
                for x in range(9):
                    if x != i and inputsudu[i][j][0] in inputsudu[x][j]:
                        inputsudu[x][j].remove(inputsudu[i][j][0])
                        if len(inputsudu[x][j])==1:
                            hasdup=True
#在本块去重
                for x in range(int(i/3)*3,int(i/3)*3+3):
                    for y in range(int(j/3)*3,int(j/3)*3+3):
                        if not(x == i and y ==j) and inputsudu[i][j][0] in inputsudu[x][y]:
                            inputsudu[x][y].remove(inputsudu[i][j][0])
                            if len(inputsudu[x][y])==1:
                                hasdup=True
    return hasdup

def removedup2(inputsudu):
    hasdup=False
    for i in range(9):
        for j in range(9):
#逐行寻找待确定的值
            if len(inputsudu[i][j])>1:
#在本行去重
                for x in range(9):
                    if x != j and len(inputsudu[i][x])==1 and inputsudu[i][x][0] in inputsudu[i][j]:
                        inputsudu[i][j].remove(inputsudu[i][x][0])
                        if len(inputsudu[i][j])==1:
                            hasdup=True
#在本列去重
                for x in range(9):
                    if x != i and len(inputsudu[x][j])==1 and inputsudu[x][j][0] in inputsudu[i][j]:
                        inputsudu[i][j].remove(inputsudu[x][j][0])
                        if len(inputsudu[i][j])==1:
                            hasdup=True
#在本块去重
                for x in range(int(i/3)*3,int(i/3)*3+3):
                    for y in range(int(j/3)*3,int(j/3)*3+3):
                        if not(x == i and y ==j) and len(inputsudu[x][y])==1 and inputsudu[x][y][0] in inputsudu[i][j]:
                            inputsudu[i][j].remove(inputsudu[x][y][0])
                            if len(inputsudu[i][j])==1:
                                hasdup=True
    return hasdup

def findmin(inputsudu):
    minlen = 9
    minx=9
    miny=9
    for i in range(9):
        for j in range(9):
            if len(inputsudu[i][j]) > 1 and (len(inputsudu[i][j]) < minlen):
                minlen=len(inputsudu[i][j])
                minx=i
                miny=j
    return(minx,miny)            


def resolv(inputsudu):
    while removedup(inputsudu):
        print("again")
        pass
    if not isvalid(inputsudu):
#        print("not valid . go up")
        return False
#无解则返回上一层，有多个值再猜个数量最小的，往下分解
    if not isdone(inputsudu):
        guessx,guessy=findmin(inputsudu)
#        print("guess point at:",guessx,guessy,"   guess value:",inputsudu[guessx][guessy])      
#存个分叉点，让函数复制一个新的列表
        for guess in inputsudu[guessx][guessy]:
            tempsudu=copy.deepcopy(inputsudu)
            tempsudu[guessx][guessy]=[guess]
#            print("go deeper")
            if(resolv(tempsudu)):
                return True
    else:
        show(inputsudu)
        return True
    return False


init()
show(sudu)
input()
resolv(sudu)
