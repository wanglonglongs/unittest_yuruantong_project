import time

from yuruantong_pc.pageObjects.basePage import BasePage
from yuruantong_pc.common.handle_yaml import get_yaml_data
from yuruantong_pc.common.handle_path import config_path


# 继承基类
class LandlordPage(BasePage):
    # 点击房东按钮
    def click_landlord_button(self):
        # 读取yaml定位参数locator['LoginPage']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['RegisterLandLord']
        # 点击登记房东按钮
        self.click(locator['register_landlord_btn'],action="点击登记按钮")

    # 点击下一步按钮 （房东信息）
    def click_landlord_next_btn(self):
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['RegisterLandLord']
        self.click(locator['click_landlord_next_btn'],action="点击下一步按钮")

    # 点击下一步按钮 （物品信息）
    def click_item_next_btn(self):
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['RegisterLandLord']
        self.click(locator['click_item_next_btn'],action="点击下一步按钮")

    # 点击下一步按钮 (账单信息)
    def click_bill_next_btn(self):
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['RegisterLandLord']
        self.click(locator['click_bill_next_btn'],action="点击下一步按钮")

    # 点击房东初审按钮
    def submit_first_review_btn(self):
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['RegisterLandLord']
        self.click(locator['submit_first_review_btn'],action="点击房东初审按钮")
    # ----------------------------------------------------------------------------------------------------
    # 房东工作流页面-landlord workflow             page-1  登记房东
    # ----------------------------------------------------------------------------------------------------

    # 基本信息
    def landlord_base_info(self, buildingNumber=None, unitNumber=None, houseNumber=None, buildingArea=None, floor=None, allFloor=None):
        # 读取yaml定位参数locator['LandlordBaseInfo']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['LandlordBaseInfo']
        # 点击店面
        self.click(locator['element_shop_selection'], action="点击店面下拉")
        # 点击店面下拉菜单
        self.click(locator['element_shop_dropdown'], action="点击店面下拉菜单")
        # 输入房屋楼幢
        self.input_text(locator['building_number_input'],buildingNumber, action="输入房屋楼幢")
        # 输入房屋单元
        self.input_text(locator['unit_number_input'],unitNumber, action="输入房屋单元")
        # 输入门牌号
        self.input_text(locator['house_number_input'],houseNumber, action="输入房屋单元")
        # 点击物业地址
        self.click(locator['element_property_address_selection'], action="点击物业地址下拉")
        # 点击物业地址下拉菜单
        self.click(locator['element_property_address_dropdown'], action="点击物业地址下拉菜单")
        # 输入建筑面积
        self.input_text(locator['building_area_input'],buildingArea, action="输入建筑面积")
        # 点击房屋类型
        self.click(locator['element_house_type_selection'], action="点击房屋类型下拉")
        # 点击房屋类型下拉菜单
        self.click(locator['element_house_type_dropdown'], action="点击房屋类型下拉菜单")
        # 点击装修程度
        self.click(locator['element_decoration_level_selection'], action="点击房屋类型下拉")
        # 点击装修程度下拉菜单
        self.click(locator['element_decoration_level_dropdown'], action="点击装修程度下拉菜单")
        # 输入所在楼层
        self.input_text(locator['floor_input'],floor, action="输入所在楼层")
        # 输入总楼层
        self.input_text(locator['all_floor_input'],allFloor, action="输入总楼层")
        # 点击朝向
        self.click(locator['element_orientation_selection'], action="点击朝向")
        # 点击朝向下拉菜单
        self.click(locator['element_orientation_dropdown'], action="点击朝向下拉菜单")

    # 房东信息
    def landlord_info(self, landlordName=None, idNumber=None, iphoneNumber=None, payeeName=None, bankCardsNumber=None,
                      payeeIdNumber=None, payeePhoneNumber=None):
        # 读取yaml定位参数locator['LandlordInfo']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['LandlordInfo']
        # 输入房东姓名
        self.input_text(locator['landlord_name_input'], landlordName, action="输入房东姓名")
        # 输入证件号码
        self.input_text(locator['id_number_input'], idNumber, action="输入证件号码")
        # 输入手机号码
        self.input_text(locator['iphone_number_input'], iphoneNumber, action="输入手机号码")
        # 输入收款人姓名
        self.input_text(locator['payee_name_input'], payeeName, action="输入收款人姓名")
        # 输入银行卡卡号
        self.input_text(locator['bank_cards_number_input'], bankCardsNumber, action="输入银行卡卡号")
        # 输入身份证号码
        self.input_text(locator['payee_id_number_input'], payeeIdNumber, action="输入身份证号码")
        # 输入收款人手机号
        self.input_text(locator['payee_phone_number_input'], payeePhoneNumber, action="输入收款人手机号")
        # 点击渠道来源
        self.click(locator['element_channel_source_selection'], action="点击渠道来源")
        # 点击渠道来源下拉菜单
        self.click(locator['element_channel_source_dropdown'], action="点击渠道来源下拉菜单")
        # 点击房东包物业
        self.click(locator['element_landlord_Property_selection'], action="点击房东包物业")
        time.sleep(1)
        # 点击房东包物业下拉菜单
        self.click(locator['element_landlord_Property_dropdown'], action="点击房东包物业下拉菜单")

    # 托管信息
    def trusteeship_info(self, housePrice=None, remark=None):
        # 读取yaml定位参数locator['TrusteeshipInfo']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['TrusteeshipInfo']
        # 点击合同期限 3年
        self.click(locator['joint_deadline_btn'], action="点击合同期限")
        # 输入收房价格
        self.input_text(locator['house_price_input'], housePrice, action="输入收房价格")
        # 点击房屋押金 押一
        self.click(locator['house_deposit_btn'], action="点击房屋押金")
        # 点击维修方案
        self.click(locator['element_repair_scheme_selection'], action="点击维修方案")
        # 点击维修方案下拉菜单
        self.click(locator['element_repair_scheme_dropdown'], action="点击维修方案下拉菜单")
        # 点击装修方案
        self.click(locator['element_renovation_plan_selection'], action="点击装修方案")
        # 点击装修方案下拉菜单
        self.click(locator['element_renovation_plan_dropdown'], action="点击装修方案下拉菜单")
        # 点击首次付款日期选择
        self.click(locator['element_payment_date_selection'], action="点击首次付款日期选择")
        time.sleep(1)
        # 点击首次付款日期下拉菜单
        self.click(locator['element_payment_date_dropdown'], action="点击首次付款日期下拉菜单")
        # 点击业务人员
        self.click(locator['element_business_people_selection'], action="点击业务人员")
        # 点击业务人员下拉菜单
        self.click(locator['element_business_people_dropdown'], action="点击业务人员下拉菜单")
        # 点击累计免租期
        self.click(locator['element_cumulation_Rent-free_period_selection'], action="点击累计免租期")
        # 点击累计免租期下拉菜单
        self.click(locator['element_cumulation_Rent-free_period_dropdown'], action="点击累计免租期下拉菜单")
        # 输入备注
        self.input_text(locator['remark_textarea'], remark,action="输入备注")

    # ----------------------------------------------------------------------------------------------------
    # 房东工作流页面-landlord workflow             page-2 物品登记
    # ----------------------------------------------------------------------------------------------------

    # 物品登记
    def item_information(self, itemNumber=None, itemRemark=None, itemImage=None):
        # 读取yaml定位参数locator['itemInformation']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['itemInformation']
        # 点击物品名称
        self.click(locator['element_item_name_selection'], action="点击物品名称")
        # 点击物品名称下拉菜单
        self.click(locator['element_item_name_dropdown'], action="点击物品名称下拉菜单")
        # 输入物品数量
        self.input_text(locator['item_number_input'],itemNumber, action="输入物品数量")
        # 输入物品备注
        self.input_text(locator['item_remark_input'],itemRemark, action="输入物品备注")
        # 点击物品图片按钮
        # self.click(locator['item_image_btn'], action="点击物品图片按钮")
        # 上传物品图片
        # self.input_text(locator['item_image_input'],itemImage, action="上传物品图片")

    # ----------------------------------------------------------------------------------------------------
    # 房东工作流页面-landlord workflow             page- 上传合同
    # ----------------------------------------------------------------------------------------------------
    def upload_contract(self, titleDeeds=None, identityCard=None, entrustment=None, originalHouse=None):
        # 读取yaml定位参数locator['contractInformation']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerLandlordPageElement.yaml')['uploadContractInfo']
        # 上传房产证照片
        self.upload_picture(locator['title_deeds_input'],titleDeeds, action="上传房产证照片")
        # 上传身份证照片
        self.upload_picture(locator['identity_card_input'],identityCard, action="上传身份证照片")
        # 上传委托书照片
        self.upload_picture(locator['entrustment_input'],entrustment, action="上传委托书照片")
        # 上传原房照片
        self.upload_picture(locator['original_house_input'],originalHouse, action="上传原房照片")
        # 上传合同照片
        # self.input_text(locator['contract_upload_input'],contractUpload, action="上传合同照片")
    # ------------------------------------------------------------------------------------------------------

    def landlord_approval(self):
        # 读取yaml定位参数locator['landlord_approval']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\approvalLandlordPageElement.yaml')['Approval']
        # 点击初审
        self.click(locator['landlord_first_approval_btn'], action="点击初审")
        # 点击初审确认按钮
        self.click(locator['landlord_first_approval_confirm_btn'], action="点击初审确认按钮")
        # 点击复审
        self.click(locator['landlord_Review_approval_btn'], action="点击复审")
        # 点击复审确认按钮
        self.click(locator['landlord_Review_approval_confirm_btn'], action="点击复审确认按钮")
