# IT_IS_IT Django 后端模板

## 公共规范

/apps - 目录用于存放 django 的 app

/server
  - urls.py - 连接各app的urls
  - settings.py - 全局配置

/utils
  - authentication.py - 为DRF写的Auth类
    在 APIView(以及各种继承自 APIView 的接口类) 中配置 
        authentication_classes = [ Auth类... ];
    
    - JWTAuthentication
        默认的全局Auth类, 检查请求头, Authentication 字段的 token 值。
    
    - LoginRequiredAuthentication
        可选Auth类, 如果接口需要登录才可访问，添加这个类。
        添加这个类之后 request.user 一定会是 user模型对象。
    
  - custom_exception.py - 自定义Django框架的错误信息
    - custom_exception_handler 函数
        - 当错误发生时回滚数据库事件。
        - 重置错误信息 (i18n)
    - CustomException 异常类
        - 自定义报错, 可以在任意无法判断错误类型的地方抛出这个异常类，但是建议使用适合的异常类。

  - jwt.py - 创建/检查 token 的函数合集。
  - response_format.py - 中间件，用于格式化接口返回结果。


## App 内规范
    创建 app 后，除了公共模块 `user`
        - admin.py 删除！
        - test.py 删除！
        - urls.py 创建!
        - serializer.py 创建!

    - serializer.py 分函数完成: 数据校验, 数据输出，数据库操作。
    - view.py 调度 serializer, 分配上下文。
    