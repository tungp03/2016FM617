
# coding: utf-8

# In[1]:


#載入os套件
import os


# In[ ]:


#定義main
def main():
    #上面那樣輸入後開頭會固定空4格
    print 'Helo world!' #呼叫main後會自動輸入'helo world!'，且下一行是空白(因為下面多空了一行)
    
    print "This is Alice's greeting."
    print 'This is Bob\'s greeting.'  #""跟''在定義字串上是沒差的
    
    #foo函數
    foo(5,10)
    
    print ('='*10)   #印出==========
    print('current working dictionary is'+os.getcwd())  #'+'是連結stirng用，os.getcwd()是os套件的函數
    
    counter = 0  #變數必須要實例化
    counter += 1
    
    food = ['apples','oranges','cats']  #建立food的list，裏面可以放不同型態的變數
    
    for i in food:
        print ('I like to eat'+i)       #print之前多空4格表示他在這個for迴圈內。這段就是分別列出喜歡吃蘋果橘子跟cats
    
    print ('count to ten:')
    for i in range(10):    #range(10)為取數字0~9的函數
        print(i)

#定義food函數
def food (param1, secondParam):
    res=param1+secondParam
    
    print ('%s pluse %s is equal to %s' % (param1, secondParam,res))  #string也可以一起運作
    
    if res < 50:
        print('foo')
    elif (res >= 50) and (param1==42) or (secondParam==24):    #'and'與'or'為條件式，與&、|相同。':'必須要加在for、if等迴圈後
        print('bar')
    else:
        print('moo')
    return res 
#打註解可以用#或是'''
if __name__ == '__main__':
    main()   #我們把main()放最後可以讓我們在呼叫main()時執行所有的def。這段__name__只有在__name__=__main__時才會執行，當不等於時不會跑
    

