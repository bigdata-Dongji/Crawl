# encoding:utf8
'''
Creation time: 2020/11/26 14:27 
Update time:
Purpose:
'''
import logging

# 设置日志的输出样式
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s [%(filename)s:%(lineno)d] '
                    ': %(message)s'
                    ' - %(asctime)s',datefmt='[%d/%b/%Y %H:%M:%S]')

logger=logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('this is log 1')
    logger.warning('this is log 2')