# -*- coding:utf-8 -*-

# This code is automatically transpiled by Saklient Translator

import six
from ...errors.saklientexception import SaklientException
from ..client import Client
from .resource import Resource
from ...util import Util
import saklient

str = six.text_type
# module saklient.cloud.resources.commonserviceprovider

class CommonServiceProvider(Resource):
    ## ライセンス種別情報。
    
    # (instance field) m_id
    
    # (instance field) m_clazz
    
    # (instance field) m_name
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/commonserviceprovider"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "CommonServiceProvider"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "CommonServiceProviders"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "CommonServiceProvider"
    
    ## @private
    # @return {str}
    def _id(self):
        return self.get_id()
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    # @param {any} obj
    # @param {bool} wrapped=False
    def __init__(self, client, obj, wrapped=False):
        super(CommonServiceProvider, self).__init__(client)
        Util.validate_type(client, "saklient.cloud.client.Client")
        Util.validate_type(wrapped, "bool")
        self.api_deserialize(obj, wrapped)
    
    # (instance field) n_id = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_id(self):
        return self.m_id
    
    ## ID
    id = property(get_id, None, None)
    
    # (instance field) n_clazz = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_clazz(self):
        return self.m_clazz
    
    ## クラス {@link ECommonServiceClass}
    clazz = property(get_clazz, None, None)
    
    # (instance field) n_name = False
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @return {str}
    def get_name(self):
        return self.m_name
    
    ## 名前
    name = property(get_name, None, None)
    
    ## (This method is generated in Translator_default#buildImpl)
    # 
    # @param {any} r
    def api_deserialize_impl(self, r):
        self.is_new = r is None
        if self.is_new:
            r = {
                
            }
        self.is_incomplete = False
        if Util.exists_path(r, "ID"):
            self.m_id = None if Util.get_by_path(r, "ID") is None else str(Util.get_by_path(r, "ID"))
        else:
            self.m_id = None
            self.is_incomplete = True
        self.n_id = False
        if Util.exists_path(r, "Class"):
            self.m_clazz = None if Util.get_by_path(r, "Class") is None else str(Util.get_by_path(r, "Class"))
        else:
            self.m_clazz = None
            self.is_incomplete = True
        self.n_clazz = False
        if Util.exists_path(r, "Name"):
            self.m_name = None if Util.get_by_path(r, "Name") is None else str(Util.get_by_path(r, "Name"))
        else:
            self.m_name = None
            self.is_incomplete = True
        self.n_name = False
    
    ## @ignore
    # @param {bool} withClean=False
    # @return {any}
    def api_serialize_impl(self, withClean=False):
        Util.validate_type(withClean, "bool")
        ret = {
            
        }
        if withClean or self.n_id:
            Util.set_by_path(ret, "ID", self.m_id)
        if withClean or self.n_clazz:
            Util.set_by_path(ret, "Class", self.m_clazz)
        if withClean or self.n_name:
            Util.set_by_path(ret, "Name", self.m_name)
        return ret
    
