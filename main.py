import re
import random
#part指abnormal [æbˈnɔːm(ə)l] a. 反常的，变态的
#wd指abnormal ，tr指[æbˈnɔːm(ə)l] a. 反常的，变态的
def partget():#读取单词表并输出列表，可用于刷新
    with open('单词表.txt','r+',encoding='UTF-8',errors='ignore') as li:
        parts=li.read()
    return parts.split('\n')
parts=partget()
def ran(n):#随机生成编号，长度范围是列表n
    ran=random.randint(0,len(n))
    return ran
def partget(n):#get word,n is 编号no
    part=parts[int(n)]
    return part
def split(text):#分割器，按照音标的[分割，或按照 n.的空格分割
    left_bracket_index = text.find("[")# 查找第一个英文左中括号的位置
    if left_bracket_index != -1:# 如果找到了左中括号
        part1 = text[:left_bracket_index]# 获取左中括号前的部分
        part2 = text[left_bracket_index:]# 获取左中括号（包括）及之后的部分
        return part1, part2
    else:
        space = text.find(" ")
        if space != -1:  # 如果找到了空格
            part1b = text[:space]# 获取空格前的部分
            part2b = text[space+1:]# 获取空格之后的部分
            return part1b, part2b
        else:
        # 如果没有找到，则返回原字符串和空字符串
            return text, "分割失败，记录并告知作者"
def write(content,place):#自动读取写入content在place
    with open(place,'a',encoding='UTF-8',errors='ignore') as li:
        li.write(content+"\n")
#每个单词取出后no固定编号,wd单词
def main():#搞词和翻译
    global no,part,wd,tr
    no=ran(parts)
    part=partget(no)
    wd,tr=split(part)

while 1==1:
    main()
    print(no,wd)
    if input("不会则输入1，会则回车校对：")=='1':#单词不会
        print(tr)
        write(part,"错词表.txt")
        input("已添加错词，回车继续")
    else:#单词会
        print(tr)
        if input("错误则输入1，正确则回车：")=="1":#翻译错
            write(part,"错词表.txt")
            input("已添加错词，回车继续")
        else:#翻译对
            continue
            
            
            