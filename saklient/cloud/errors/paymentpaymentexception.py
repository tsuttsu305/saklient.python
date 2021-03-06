# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.httppaymentrequiredexception import HttpPaymentRequiredException
import saklient

str = six.text_type
# module saklient.cloud.errors.paymentpaymentexception

class PaymentPaymentException(HttpPaymentRequiredException):
    ## お客様のご都合により操作を受け付けることができません。
    
    ## @param {int} status
    # @param {str} code=None
    # @param {str} message=""
    def __init__(self, status, code=None, message=""):
        super(PaymentPaymentException, self).__init__(status, code, "お客様のご都合により操作を受け付けることができません。" if message is None or message == "" else message)
    
