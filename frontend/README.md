# IT_IS_IT Nuxt 前端模板

## 公共规范

/src - 源码目录

/src/assets - 项目资源, image, video, audio, icon 等..

/src/components - 组件, 按模块/页面拆分
    - common 为公共组件
    - default_layout 默认布局的组件
    - xxx_page 某页面的组件
    - xxx_module 某模块的组件

/service - 服务, 与服务端通讯的脚本
    - fetch.ts 封装后的 fetch API, 自动携带 token, 序列化数据, 处理异常。
    - /api 服务端接口合集, 模块名-api.ts。

/stores - 全局状态, 按模块划分。

/types - 全局类型定义, 按模块划分。

/utils - 工具函数合集。

/src/layout, /src/pages, /src/plugins, /src/public 为 Nuxt 自带规范，默认开发者已掌握, 理解。
