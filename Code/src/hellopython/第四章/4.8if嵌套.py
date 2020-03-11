#层层筛选

#学历
master = input("是否本科？")
bachelor = input("是否研究生？")
#大学
university985 = input("是否985高校？")
university211 = input("是否211高校？")

#技术
basic = input("是否基本功扎实？")

if master != "是":
    print("对不起，不符合我们的学历要求。")
else:
    if bachelor != "是":
        print("对不起，建议您先考研吧。")
    else:
        if university985 != "是":
            print("非985，暂不考虑，谢谢")
        else:
            if university211 != "是":
                print("一本双非，二本？亲，建议您重读")
            else:
                if basic != "是":
                    print("亲，你挺好的，但不适合本公司。")
                else:
                    print("亲，恭喜你！！！！")


