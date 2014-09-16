# -*- coding:utf-8 -*-

from .model import Model
from ..resource.script import Script
from ..enums.escope import EScope
from ...util import Util

# module saklient.cloud.model.model_script

class Model_Script(Model):
    ## スクリプトを検索・作成するための機能を備えたクラス。
    
    ## @private
    # @return {str}
    def _api_path(self):
        return "/note"
    
    ## @private
    # @return {str}
    def _root_key(self):
        return "Note"
    
    ## @private
    # @return {str}
    def _root_key_m(self):
        return "Notes"
    
    ## @private
    # @return {str}
    def _class_name(self):
        return "Script"
    
    ## 次に取得するリストの開始オフセットを指定します。
    # 
    # @param {int} offset オフセット
    # @return {saklient.cloud.model.model_script.Model_Script} this
    def offset(self, offset):
        Util.validate_type(offset, "int")
        return self._offset(offset)
    
    ## 次に取得するリストの上限レコード数を指定します。
    # 
    # @param {int} count 上限レコード数
    # @return {saklient.cloud.model.model_script.Model_Script} this
    def limit(self, count):
        Util.validate_type(count, "int")
        return self._limit(count)
    
    ## Web APIのフィルタリング設定を直接指定します。
    # 
    # @param {str} key キー
    # @param {any} value 値
    # @param {bool} multiple=False valueに配列を与え、OR条件で完全一致検索する場合にtrueを指定します。通常、valueはスカラ値であいまい検索されます。
    # @return {saklient.cloud.model.model_script.Model_Script}
    def filter_by(self, key, value, multiple=False):
        Util.validate_type(key, "str")
        Util.validate_type(multiple, "bool")
        return self._filter_by(key, value, multiple)
    
    ## 次のリクエストのために設定されているステートをすべて破棄します。
    # 
    # @return {saklient.cloud.model.model_script.Model_Script} this
    def reset(self):
        return self._reset()
    
    ## 指定したIDを持つ唯一のリソースを取得します。
    # 
    # @param {str} id
    # @return {saklient.cloud.resource.script.Script} リソースオブジェクト
    def get_by_id(self, id):
        Util.validate_type(id, "str")
        return self._get_by_id(id)
    
    ## リソースの検索リクエストを実行し、結果をリストで取得します。
    # 
    # @return {saklient.cloud.resource.script.Script[]} リソースオブジェクトの配列
    def find(self):
        return self._find()
    
    ## 指定した文字列を名前に含むリソースに絞り込みます。
    # 
    # 大文字・小文字は区別されません。
    # 半角スペースで区切られた複数の文字列は、それらをすべて含むことが条件とみなされます。
    # 
    # @todo Implement test case
    # @param {str} name
    # @return {saklient.cloud.model.model_script.Model_Script}
    def with_name_like(self, name):
        Util.validate_type(name, "str")
        return self._with_name_like(name)
    
    ## 指定したタグを持つリソースに絞り込みます。
    # 
    # 複数のタグを指定する場合は withTags() を利用してください。
    # 
    # @todo Implement test case
    # @param {str} tag
    # @return {saklient.cloud.model.model_script.Model_Script}
    def with_tag(self, tag):
        Util.validate_type(tag, "str")
        return self._with_tag(tag)
    
    ## 指定したすべてのタグを持つリソースに絞り込みます。
    # 
    # @todo Implement test case
    # @param {str[]} tags
    # @return {saklient.cloud.model.model_script.Model_Script}
    def with_tags(self, tags):
        Util.validate_type(tags, "list")
        return self._with_tags(tags)
    
    ## 指定したDNFに合致するタグを持つリソースに絞り込みます。
    # 
    # @todo Implement test case
    # @param {str[][]} dnf
    # @return {saklient.cloud.model.model_script.Model_Script}
    def with_tag_dnf(self, dnf):
        Util.validate_type(dnf, "list")
        return self._with_tag_dnf(dnf)
    
    ## 名前でソートします。
    # 
    # @todo Implement test case
    # @param {bool} reverse=False
    # @return {saklient.cloud.model.model_script.Model_Script}
    def sort_by_name(self, reverse=False):
        Util.validate_type(reverse, "bool")
        return self._sort_by_name(reverse)
    
    ## パブリックスクリプトに絞り込みます。
    # 
    # @return {saklient.cloud.model.model_script.Model_Script}
    def with_shared_scope(self):
        self._filter_by("Scope", [EScope.shared])
        return self
    
    ## プライベートスクリプトに絞り込みます。
    # 
    # @return {saklient.cloud.model.model_script.Model_Script}
    def with_user_scope(self):
        self._filter_by("Scope", [EScope.user])
        return self
    
