from nb_log import get_logger, LogManager
logger = LogManager('test').get_logger_and_add_handlers(10,log_filename='tests.log')
# logger = get_logger('lalala',log_filename='lalala.log',formatter_template=5,log_file_handler_type=2) # get_logger有很多其他入参可以自由定制logger。
logger.debug(f'debug是绿色，说明是调试的，代码ok ')
logger.info('info是天蓝色，日志正常 ')
logger.warning('黄色yello，有警告了 ')
logger.error('粉红色说明代码有错误 ')
logger.critical('血红色，说明发生了严重错误 ')


# logger_aa = LogManager('aa').get_logger_and_add_handlers(10, log_filename='aa.log')
# logger_bb = get_logger("bb", log_level_int=30, is_add_stream_handler=False, ding_talk_token='your_dingding_token')
# logger_cc = get_logger('cc', log_level_int=10, log_filename='cc.log')

# logger_aa.debug('哈哈哈')
# 将会同时记录到控制台和文件aa.log中，只要debug及debug以上级别都会记录。

# logger_bb.warning('嘿嘿嘿')
# 将只会发送到钉钉群消息，并且logger_bb的info debug级别日志不会被记录，非常方便测试调试然后稳定了调高界别到生产。

# logger_cc.debug('嘻嘻')
# logger_cc的日志会写在cc.log中，和logger_aa的日志是不同的文件。