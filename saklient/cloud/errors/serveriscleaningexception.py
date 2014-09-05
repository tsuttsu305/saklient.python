# -*- coding:utf-8 -*-

from saklient.errors.httpconflictexception import HttpConflictException
from saklient.errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.serveriscleaningexception

class ServerIsCleaningException(HttpConflictException):
    ## 要求された操作を行えません。サーバが終了処理中です。しばらく時間をおいてから再度お試しください。
    
    # (class field) default_message = "要求された操作を行えません。サーバが終了処理中です。しばらく時間をおいてから再度お試しください。"
    
    pass
