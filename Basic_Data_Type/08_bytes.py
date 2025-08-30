'''
    1. 字符集和编码
    0 1 => 1010101010 => 二进制转换成十进制 <=> 88
    电脑如何进行存储文字信息
    
    ascii => 编排了1128个字符，只需要7个0和1就可以表示了 01111111 => 1 byte = 8bit
    ANSI => 一套标准，每个字符 16bit，2bytes
    00000000 01111111
    
    到了中国，gb2312编码，gbk编码(Windows默认) -> 扩充 gb18030
    到了台湾big5编码
    到了日本，JIS编码
    
    Unicode: 万国码
    早期Unicode没有意思到这个问题，2个字节。进行了扩充1倍，USC-4 4个字节
    00000000 00000000 00000000 01111111
    
    utf：是可变长度的unicode，可以进行数据的传输和存储 
    utf-8：最短字节长度8
        英文：8bit，1byte
        欧洲文字：16bit，2bytes
        中文：24bit，3bytes
        
        总结：
            1. ascii：8bit，1byte
            2. gbk：16bit，2byte windows默认
            3. unicod：32bit，4byte（没法用只是一个标准）
            4. utf-8：mac默认
                英文：8bit，1byte
                欧洲文字：16bit，2bytes
                中文：24bit，3bytes
                
            gbk和utf-8不能直接进行转化
            我军密码本 -> 文字 -> 敌军密码本
    2. bytes 
        程序员平时遇见的所有的数据最终单位都是字节byte
         
'''

# s = "周杰伦"
# bs = s.encode("gbk") # b'xxxx' bytes类型
# b'\xd6\xdc\xbd\xdc\xc2\xd7' "周杰伦"三个字占6个字节
# print(bs)

# b'\xe5\x91\xa8\xe6\x9d\xb0\xe4\xbc\xa6' 9个字节，每个字占3个字节
# bs2 = s.encode("utf-8")
# print(bs2)

# 怎么把一个gbk的字节转化成utf-8的字节
bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
s = bs.decode("gbk")
bs2 = s.encode("utf-8") # 重新编码
print(bs2)

# 1. str.encode("编码")
# 2. bytes.decode("编码")