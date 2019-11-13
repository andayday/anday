import xlwt 
# -*- coding:utf-8 -*-




def write_excel():
    f = xlwt.Workbook()
    str1="123123234，12323435123， 123342421341，  123243234， ，123234243，"
    l1=str1.split('，')
    sheet1 = f.add_sheet('test',cell_overwrite_ok=True)
    row0 = ["姓名","年龄","出生日期","爱好"]
    colum0 = ["张三","李四","恋习Python","小明","小红","无名"]
    '''
    #写第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    '''
    #写第一列
    for i in range(0,len(l1)):
	if l1[i] != "" and l1[i].strip():
            sheet1.write(i+1,0,l1[i])
    '''

    sheet1.write(1,3,'2006/12/12')
    sheet1.write_merge(6,6,1,3,'未知')#合并行单元格
    sheet1.write_merge(1,2,3,3,'打游戏')#合并列单元格
    sheet1.write_merge(4,5,3,3,'打篮球')
    '''
    f.save('test.xls')


def main():
	write_excel()


if __name__=='__main__':
	main()


