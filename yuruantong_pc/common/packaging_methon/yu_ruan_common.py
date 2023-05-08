import random
import string
from selenium.webdriver.common.action_chains import ActionChains


# 随机生成 某区间 内的任意一个整数

def free_random_one_num(start_num, end_num):
    return random.randint(start_num, end_num)


# 随机生成X位字符 纯数字
def free_random_many_num(num_sign):
    # 生成第一位不为零的数字
    first_digit = random.choice(string.digits[1:])
    # 生成剩余位数的数字
    rest_digits = "".join(random.choice(string.digits) for _ in range(num_sign - 1))
    return f"{first_digit}{rest_digits}"


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

def perform_action(driver, offset_x, offset_y, click=True, reset=False):
    actions = ActionChains(driver)
    actions.move_by_offset(offset_x, offset_y)
    if click:
        actions.click()
    actions.perform()
    if reset:
        actions.reset_actions()
