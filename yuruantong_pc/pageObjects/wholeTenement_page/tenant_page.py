from yuruantong_pc.pageObjects.basePage import BasePage
from yuruantong_pc.common.handle_yaml import get_yaml_data
from yuruantong_pc.common.handle_path import config_path


# 继承基类
class TenantPage(BasePage):

    # 检索租赁状态为未租房源
    def filter_rent_status_list(self):
        # 读取yaml定位参数locator['rentalStatusSearch']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['rentalStatusSearch']
        # 租赁状态下拉
        self.click_js(locator['element_rental_status_selection_js'],action="点击租赁状态下拉")
        # 未租状态下拉选择
        self.click_js(locator['element_rental_status_dropdown_js'],action="点击未租状态选择")
        # 搜索
        self.click_js(locator['whole_tenement_search_btn_js'],action="点击搜索按钮")

    # 点击登记租客按钮
    def click_register_tenant_button(self):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 点击登记租客按钮
        self.click_js(locator['register_tenant_btn_js'],action="点击登记租客按钮")

    # 点击租客页面下一步按钮
    def tenant_information_next_button(self):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 登记租客页面下一步按钮
        self.click(locator['tenant_information_next_button'],action="点击登记租客页面下一步按钮")

    # 点击租客账单页面下一步按钮
    def tenant_bill_next_button(self):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 租客账单页面下一步按钮
        self.click(locator['tenant_bill_next_button'],action="租客账单页面下一步按钮")

    # 点击租客审批按钮
    def tenant_approval_button(self):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 租客审批按钮
        self.click(locator['tenant_approval_button'],action="租客审批按钮")

    # ----------------------------------------------------------------------------------------------------
    # 租客工作流页面-landlord workflow             page-1  租客信息
    # ----------------------------------------------------------------------------------------------------

    def tenant_Information(self, tenantName=None, tenantId=None, emergencyPhone=None, contactPersonPhone=None):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 租客姓名
        self.input_text(locator['tenant_name_input'],tenantName, action="输入租客姓名")
        # 证件类型下拉
        self.click(locator['element_identity_type_selection'], action="点击证件类型下拉")
        # 证件类型选择
        self.click(locator['element_identity_type_dropdown'], action="点击证件类型选择")
        # 证件号码
        self.input_text(locator['tenant_id_input'],tenantId, action="输入证件号码")
        # 联系人
        self.input_text(locator['contact_person_phone_input'],contactPersonPhone, action="输入联系人")
        # 紧急联系人电话
        self.input_text(locator['emergency_phone_input'],emergencyPhone, action="输入紧急联系人电话")
        # 业务人员下拉
        self.click(locator['element_business_person_selection'], action="点击业务人员下拉")
        # 业务人员选择
        self.click(locator['element_business_person_dropdown'], action="点击业务人员选择")
        # 协助人员下拉
        self.click(locator['element_help_person_selection'], action="点击协助人员下拉")
        # 协助人员选择
        self.click(locator['element_help_person_dropdown'], action="点击协助人员选择")
        # 渠道来源下拉
        self.click(locator['element_channel_source_selection'], action="点击渠道来源下拉")
        # 渠道来源选择
        self.click(locator['element_channel_source_dropdown'], action="点击渠道来源选择")
    # ----------------------------------------------------------------------------------------------------
    # 租客工作流页面                          page-1  租赁信息
    # ----------------------------------------------------------------------------------------------------

    def lease_Information(self, rentalPrice=None, remark=None):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 租赁期限下拉 年
        self.click(locator['element_rental_period_years_selection'],action="点击租赁期限下拉")
        # 租赁期限选择 年
        self.click(locator['element_rental_period_years_dropdown'],action="点击租赁期限选择")
        # 租赁期限下拉 月
        self.click(locator['element_rental_period_month_selection'],action="点击租赁期限下拉")
        # 租赁期限选择 月
        self.click(locator['element_rental_period_month_dropdown'],action="点击租赁期限选择")
        # 点击缴费方式
        self.click(locator['payment_method_btn'],action="点击缴费方式")
        # 输入出房价格
        self.input_text(locator['out_room_price_input'],rentalPrice,action="输入出房价格")
        # 点击房屋押金
        self.click(locator['house_deposit_btn'],action="点击房屋押金")
        # 点击提前缴费
        self.click(locator['pre_payment_btn'],action="点击提前缴费")

        # 输入备注
        self.input_text(locator['remark_textarea'],remark,action="输入备注")

    # ----------------------------------------------------------------------------------------------------
    # 租客工作流页面                          page-3  上传合同
    # ----------------------------------------------------------------------------------------------------
    def upload_contract(self, identityCard=None, contractUpload=None, deliveryPhoto=None, otherPhoto=None):
        # 读取yaml定位参数locator['registerTenant']提取键值数据
        locator = get_yaml_data(rf'{config_path}\element_locator\registerTenantPageElement.yaml')['registerTenant']
        # 身份证照片
        self.upload_picture(locator['identity_card_input'],identityCard,action="上传身份证照片")
        # 点击上传合同
        self.upload_picture(locator['contract_upload_input'],contractUpload,action="点击上传合同")
        # 交割单照片
        self.upload_picture(locator['delivery_photo_input'],deliveryPhoto,action="上传交割单照片")
        # 其它照片
        self.upload_picture(locator['other_input'],otherPhoto,action="上传其他照片")






