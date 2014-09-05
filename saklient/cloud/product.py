# -*- coding:utf-8 -*-

from saklient.cloud.model.model_serverplan import Model_ServerPlan
from saklient.cloud.model.model_diskplan import Model_DiskPlan
from saklient.cloud.model.model_routerplan import Model_RouterPlan
from saklient.cloud.client import Client
from saklient.util import Util

# module saklient.cloud.product

class Product:
    ## 商品情報にアクセスするためのモデルを集めたクラス。
    
    # (instance field) _server
    
    ## @return {saklient.cloud.model.model_serverplan.Model_ServerPlan}
    def get_server(self):
        return self._server
    
    ## サーバプラン情報。
    server = property(get_server, None, None)
    
    # (instance field) _disk
    
    ## @return {saklient.cloud.model.model_diskplan.Model_DiskPlan}
    def get_disk(self):
        return self._disk
    
    ## ディスクプラン情報。
    disk = property(get_disk, None, None)
    
    # (instance field) _router
    
    ## @return {saklient.cloud.model.model_routerplan.Model_RouterPlan}
    def get_router(self):
        return self._router
    
    ## ルータ帯域プラン情報。
    router = property(get_router, None, None)
    
    ## @ignore
    # @param {saklient.cloud.client.Client} client
    def __init__(self, client):
        Util.validate_type(client, "saklient.cloud.client.Client")
        self._server = Model_ServerPlan(client)
        self._disk = Model_DiskPlan(client)
        self._router = Model_RouterPlan(client)
    
