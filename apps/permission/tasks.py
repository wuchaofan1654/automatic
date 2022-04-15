import datetime
import logging

from captcha.models import CaptchaStore

from frames.utils.decorators import BaseCeleryApp
from frames.response import SuccessResponse

logger = logging.getLogger(__name__)


@BaseCeleryApp(name='apps.permission.tasks.clear_invalid_captcha')
def clear_invalid_captcha():
    """
    清除数据库中废弃失效的验证码
    :return:
    """
    queryset = CaptchaStore.objects.filter(expiration__lt=datetime.datetime.now())
    msg = f"成功删除 {queryset.count()} 条失效验证码!"
    logger.info(msg)
    queryset.delete()
    return SuccessResponse(msg=msg)
