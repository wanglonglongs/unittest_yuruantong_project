import random
import string


# 随机生成 某区间 内的任意一个整数

def free_random_one_num(start_num, end_num):
    return random.randint(start_num, end_num)


# 随机生成X位字符 纯数字
def free_random_many_num(num_sign):
    return "".join(map(lambda x: random.choice(string.digits), range(num_sign)))


# 随机生成X位字符 纯字母
def random_string_generator(num_sign):
    random_char = random.sample(string.ascii_letters, num_sign)
    return ''.join(random_char)
    # now_date = str(datetime.date.today())
    # return ''.join(random_char) + now_date


# 随机生成X位字符 字母+数字组合
def random_string_number(n):
    m = random.randint(1, n)
    a = "".join([str(random.randint(0, 9)) for _ in range(m)])
    b = "".join([random.choice(string.ascii_letters) for _ in range(n - m)])
    return ''.join(random.sample(list(a + b), n))


# print(string.digits + string.ascii_letters + string.punctuation)


# 随机生成手机号 暂只对第二位做要求
def random_create_phone():
    # 第二位数字
    second = [3, 4, 5, 6, 7, 8][random.randint(0, 4)]
    # 最后九位数字
    suffix = random.randint(99999999, 1000000000)
    # 拼接手机号
    return "1{}{}".format(second, suffix)


# print(random_create_phone())