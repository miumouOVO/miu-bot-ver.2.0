from os import path
import nonebot
import config
import sqlite3

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    #载入awesome/plugins中的插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins'),
        'awesome.plugins'
    )
    #载入awesome/plugins/bread中的插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins','bread'),
        'awesome.plugins.bread'
    )
    #载入awesome/plugins/about_picture中的插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins','about_picture'),
        'awesome.plugins.about_picture'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__),'awesome','plugins','super_command'),
        'awesome.plugins.super_command'
    )
    #启动bot在端口host：port中
    nonebot.run(host='127.0.0.1',port=4567)