# -*- coding:utf-8 -*-

from ...errors.httpconflictexception import HttpConflictException

# module saklient.cloud.errors.templateisincompleteexception

class TemplateIsIncompleteException(HttpConflictException):
    ## 要求された操作を行えません。このテンプレートは不完全です。複製処理等の完了後に再度お試しください。
    
    # (class field) default_message = "要求された操作を行えません。このテンプレートは不完全です。複製処理等の完了後に再度お試しください。"
    
    pass