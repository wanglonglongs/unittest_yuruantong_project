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


def generate_random_name():
    # 百家姓列表
    surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱',
                '秦', '尤', '许',
                '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏',
                '水', '窦', '章',
                '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞',
                '任', '袁', '柳',
                '邓', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝',
                '邬', '安', '常',
                '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和',
                '穆', '萧', '尹',
                '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈',
                '宋', '茅', '庞',
                '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾',
                '路', '娄', '危',
                '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊',
                '胡', '凌', '霍',
                '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁',
                '宣', '贲', '邓',
                '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴',
                '陆', '荣', '翁',
                '荀', '羊', '於', '惠', '甄', '魏', '加', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井',
                '段', '富', '巫',
                '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋',
                '仲', '伊', '宫',
                '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶',
                '幸', '司', '韶',
                '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓',
                '蔺', '屠', '蒙',
                '池', '乔', '阴', '郁', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬',
                '申', '扶', '堵',
                '冉', '宰', '郦', '雍', '郤', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏',
                '浦', '尚', '农',
                '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向',
                '古', '易', '慎',
                '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广',
                '禄', '阙', '东',
                '殴', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷',
                '訾', '辛', '阚',
                '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查',
                '后', '荆', '红',
                '游', '竺', '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人',
                '东方', '赫连',
                '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙',
                '轩辕', '令狐', '钟离',
                '宇文', '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '亓官', '司寇', '仉', '督', '子车', '颛孙',
                '端木', '巫马', '公西',
                '漆雕', '乐正', '壤驷', '公良', '拓跋', '夹谷', '宰父', '谷梁', '晋', '楚', '闫', '法', '汝', '鄢',
                '涂', '钦', '段干', '百里',
                '东郭', '南门', '呼延', '归', '海', '羊舌', '微生', '梁丘', '左丘', '东门', '西门', '南宫']

    # 随机选择姓氏
    surname = random.choice(surnames)

    # 随机生成名字长度（2-4个字符）
    name_length = random.randint(2,2)

    # 随机生成名字
    name = ""
    for _ in range(name_length):
        # 随机选择中文字符
        char = chr(random.randint(0x4e00, 0x9FBF))
        name += char

    # 拼接姓名
    full_name = surname + name
    return full_name

