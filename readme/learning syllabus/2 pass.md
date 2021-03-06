# 灭霸的选择--条件判断与条件嵌套--沟通逻辑

# 前言
    上一关，攻克了如何与Python沟通的语言大关——通过三种数据类型（字符串、整数和浮点数）的相互转换，突破现实世界和镜像世界数据差异的墙，将代码成功执行。
    但是，对于Python来讲，光正确使用【镜像世界的数据】还不够，还需要正确的【沟通逻辑】才能让Python准确地执行你的命令。
        沟通逻辑
# 条件判断
    单向判断：if
        main.py
            # 为宝石数量赋值
            stonenumber=6
            
            # 条件：如果你拥有的宝石数量大于等于6个
            if stonenumber>=6:
                
                # 结果：显示‘你拥有了毁灭宇宙的力量’的结果
                print('你拥有了毁灭宇宙的力量') 
    双向判断：if…else…
        main.py
            # 赋值语句：为宝石数量赋值
            stonenumber=3
            
            # 条件：如果你拥有的宝石数量大于等于6个
            if stonenumber>=6:
                
                # 结果：显示‘你拥有了毁灭宇宙的力量’的结果
                print('你拥有了毁灭宇宙的力量')
                
            # 条件：当赋值不满足if条件时，执行else下的命令
            else:
                
                # 结果：显示‘去找灵魂宝石’的结果
                print('带着卡魔拉去沃弥尔星寻找灵魂宝石')
                
    多向判断：if…elif…else…
        main.py
            # 为宝石数量赋值
            stonenumber=5
            
            # 条件：如果你拥有的宝石数量大于等于6个
            if stonenumber>=6:
                
                # 结果：显示‘就拥有了毁灭宇宙的力量’的结果
                print('你拥有了毁灭宇宙的力量')
                
            # 条件：如果想让宝石数量停留在5个以下，至少一个
            elif 0<stonenumber<=5:
            
                # 条件：当赋值不满足if和elif条件时，执行else下的命令，宝石数量在3个以下
                print('红女巫需要亲手毁掉幻视额头上的心灵宝石')
            
            else:
            
                # 结果：显示‘需要惊奇队长逆转未来’的结果
                print('需要惊奇队长逆转未来')
                
        总结一下elif的知识点
![](images\python2_1.png)
# 嵌套
    蜘蛛侠彼得·帕克也仅仅是个18岁的高中生。他曾只顾忙着在街头巷尾当平民英雄，结果在期末历史考试里只考了26分，荣获“学渣”提名。
    但这个“学渣”评价并不是随便来的，而是通过规则一步步过滤出来的：
        考试成绩评价规则：
            1. 如果成绩大于等于60分，就是及格，在此前提下：
                (1)如果成绩大于等于80分，属于优秀范围；
                (2)否则，属于一般范围。
            
            2. 如果成绩小于60分，就是不及格，在此前提下：
                (1)如果成绩小于30分，平时太不认真，属于学渣了；
                (2)如果成绩大于等于30分，那么，至少还能抢救一下。
        像这种如果底下还有如果、条件里还套条件的情况，我们如何用Python把上面的规则写出来，并得出评价呢？
            答案就是——嵌套条件。
        
        if嵌套的应用场景，简单来讲就是：在基础条件满足的情况下，再在基础条件底下增加额外的条件判断。
            就像上面的基础条件是60分及格，想要判断优秀和一般还要增加额外条件——是否大于等于80。
            
            main.py
                historyscore=26
                
                if historyscore>=60:
                    print('你已经及格')
                
                    if historyscore>=80:
                        print('你很优秀')
                
                    else:
                        print('你只是一般般')
                
                else:
                    print('不及格')
                
                    if historyscore<30:
                        print('学渣')
                
                    else:
                        print('还能抢救一下')
                
                print('程序结束')
                
                # 打印结果
                不及格
                学渣
                程序结束
    一张导图理一下if嵌套的逻辑
![](images\python2_2.png)
# 总结一下整节课的知识点
![](images\python2_3.png)
# 练习--寻找宝石
    知识点回顾
        if条件判断语句
            这道题我们用到的知识点是：多向判断：if...elif...else...
            有三种条件的情况，如果if的条件不满足，就按顺序看是否满足elif的条件，如果不满足elif的条件，就执行else的命令。注意if、elif、else是平级关系，后面都跟冒号且不缩进。
    练习介绍：
        在灭霸打了一个响指，宇宙一半生物都灰飞烟灭。
        剩下的复仇者联盟成员们依旧没有放弃反击灭霸的机会，他们决定利用最后一次行动机会，去把灭霸手里的宝石偷回来。
        如果偷回的宝石数是4颗及以上，便获得了打败灭霸的力量；如果偷回的宝石数是1-3颗，他们可以全员出动，殊死一搏；如果偷回的宝石数是0颗，只能尝试呼叫惊奇队长。
        最终，他们因为实力相差太大，1颗宝石都没有偷回来。  
    
    题目要求：
        请你写出一段代码，在一颗宝石都没偷回来的赋值下，进行条件判断，并产生对应的结果：  
        1.如果偷回的宝石数是4颗及以上，输出结果获得了打败灭霸的力量，反杀稳了
        2.如果偷回的宝石数是1-3颗，输出结果可以全员出动，殊死一搏
        3.如果偷回的宝石数是0颗，输出结果没办法了，只能尝试呼叫惊奇队长
        注意：标点符号都为英文格式
    题目讲解
        1.赋值：因为他们一个宝石都没偷回来，为偷来的宝石stonenumber赋值为0。
        2.用if写第一个条件：如果偷回的宝石数是4颗及以上，输出结果：获得了打败灭霸的力量，反杀稳了
        3.用elif写第二个条件：如果偷回的宝石数是1-3颗，输出结果：可以全员出动，殊死一搏
        4.用else写第三个条件：如果偷回的宝石数是0颗，输出结果：没办法了，只能尝试呼叫惊奇队长
    main.py
        stonenumber=0
        if stonenumber>=4:
            print('获得了打败灭霸的力量，反杀稳了')
        elif 1<=stonenumber<=3:
            print('可以全员出动，殊死一搏')
        elif stonenumber==0:
            print('没办法了，只能尝试呼叫惊奇队长')
            
        # 打印输出
        没办法了，只能尝试呼叫惊奇队长
![](images\python2_4.png)
# 进阶练习--美国队长的工资
    关卡2 条件判断与条件嵌套
    知识点回顾
        if条件判断语句
            单向判断：if
                只有一个如果…就…的情况，满足if条件即运行结果，否则什么都不输出。注意if后面要跟冒号，底下的命令需要缩进
![](images\python2_5.png)

            双向判断：if...else...
                不满足条件一时，就执行条件二的情况，如果…不满足，就…。注意if和else不缩进，else后面也要跟冒号。
![](images\python2_6.png)

            多向判断：if...elif...else...
                有三种条件的情况，如果if的条件不满足，就按顺序看是否满足elif的条件，如果不满足elif的条件，就执行else的命令。
                注意if、elif、else是平级关系，后面都跟冒号且不缩进
![](images\python2_7.png)

        if嵌套
           下图为if嵌套的基本逻辑： 
           elif也是可以放进嵌套里的，就是在上述结构的基础上，多加一个带头大哥elif条件，以及底下跟着的elif条件的小弟就好
![](images\python2_8.png)
    
    练习介绍：
        复仇者联盟的成员也是有工资的，然而，由于美国队长一直被冰封在北极，错过了多次调薪机会，所以美国队长的工资一直是每月80美元。
        光荣挺进史塔克穷人榜前三名，并获封“美元队长”称号。  
    
    题目要求：
        请你写出一段代码，判断美国队长的工资水平，代码需要满足如下条件：
            1.如果月工资小于等于500美元，显示“欢迎进入史塔克穷人帮前三名”
                1.1如果月工资在100-500美元之间，显示“请找弗瑞队长加薪”
                1.2如果月工资小于等于100美元，显示“恭喜您荣获“美元队长”称号！”
            2.如果月工资在500-1000美元之间（含1000美元），打印“祝贺您至少可以温饱了。”
            3.其他情况下，如果工资大于1000美元，打印“经济危机都难不倒您！”
                3.1如果工资在1000-20000美元（含20000美元）之间，打印“您快比钢铁侠有钱了！”
                3.2如果月工资大于20000美元，打印“您是不是来自于瓦坎达国？”
            4.不管赋值改变后输出结果如何，都需固定打印结果“程序结束”
    题目讲解
        1.根据题目，我们知道这里涉及嵌套条件，所以可以用扒洋葱法梳理代码逻辑
        2.可以先写最外层的if……elif……else……条件
        3.根据题目的从属关系分析，最外层的if条件和else条件都有额外条件
        4.依次在外层基础条件下添加额外条件
    书写代码
        main.py
            wages=100000
            if wages<=500:
                print('欢迎进入史塔克穷人帮前三名')
                if 100<=wages<=500:
                    print('请找弗瑞队长加薪')
                elif wages<100:
                    print('恭喜您荣获“美元队长”称号')
            if 500<=wages<=1000:
                print('祝贺您至少可以温饱了')
                if 1000<=wages:
                    print('经济危机都难不倒您')
            if 1000<wages:
                print('经济危机都难不倒您')
                if 1000<wages<=20000:
                    print('您快比钢铁侠有钱了')
                if wages>20000:
                    print('您是不是来自于瓦坎达国')
            print('程序结束')
            
            # 打印输出
            经济危机都难不倒您
            您是不是来自于瓦坎达国
            程序结束