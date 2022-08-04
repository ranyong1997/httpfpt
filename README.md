# python接口自动化测试框架

## 🧠设计思路

- python3 + pytest + parametrize + requests / httpx + yaml / excel ...

## 👀目录结构介绍

- common/: 公共类
- core/: 配置
- data/: 测试数据
- db/: 数据库相关
- log/: 日志文件
- report/: 测试报告存放
- test_case/: 放置接口自动化测试项目和用例
- utils/: 工具包
- conftest.py: pytest.fixture 配置
- pytest.ini pytest 参数配置
- run.py: pytest 主程序运行入口

## 👨‍💻👩‍💻使用

克隆:

```shell
git clone https://gitee.com/wu_cl/automated_api_pytest.git
```

安装依赖包:

```shell
pip install -r requirements.txt
```

## 指定测试项目

多项目数据依据目录层级进行隔离

test_case 目录下的一级文件夹视为单个项目目录

在 config.toml 配置中修改 project = xxx 为对应的项目目录名

## 测试用例数据说明

### 结构展示

yaml 数据：

```yaml
config:
  allure:
    epic:
    feature:
    story:
  request:
    env:
    headers:
    timeout:
    verify:
    redirects:
    proxies:
      requests:
        http:
        https:
  #        httpx:
  #          http://:
  #          https://:
  module:

test_steps:
  - name:
    case_id:
    description:
    is_run:
    request:
      method:
      url:
      params:
      headers:
      data_type:
      data:
      files:
        xxx:
    setup:
      sql:
        - key:
          set_type:
          sql:
          jsonpath:
        - select * from xxx where xxx=xxx
      hooks:
        - func:
      wait_time:
    teardown:
      sql:
      hooks:
      extract:
        - key:
          set_type:
          jsonpath:
      assert:
        - check:
          value:
          type:
          jsonpath:
        - assert 200 = pm.response.get('status_code')
      wait_time:
```

~~excel 数据：~~

```text
release 版本已不推荐使用，因为受限于数据 json 结构，对于 excel 来说，编写及修改都略显繁琐，
尽管数据解析时考虑了 excel 数据的情况，但这种方式已经被提前拦截
```

### 参数说明：

| 参数            |                类型                 | 必填  | 说明                                                               |
|:--------------|:---------------------------------:|-----|:-----------------------------------------------------------------|
| config        |               dict                | Y   | 测试用例配置                                                           |
| + allure      |               dict                | Y   | allure 测试报告配置                                                    |
| ++ epic       |                str                | Y   | allure epic                                                      |
| ++ feature    |                str                | Y   | allure feature                                                   |
| ++ story      |                str                | Y   | allure story                                                     |
| + request     |               dict                | Y   | 请求参数                                                             |
| ++ env        |                str                | Y   | 测试环境                                                             |
| ++ headers    |            dict / null            | N   | 请求头                                                              |
| ++ timeout    |            int / null             | N   | 请超时时长，如果存在且不为空，则应用本数据所有测试用例，<br/> 如果不存在或为空，则默认应用 conf 配置文件       |
| ++ verify     |            bool / null            | N   | 请求验证，应用同上                                                        |
| ++ redirects  |            bool / null            | N   | 重定向，应用同上                                                         |
| ++ proxies    |            dict / null            | N   | 代理，应用同上                                                          |
| +++ requests  |               dict                | N   | requests 引擎代理，仅当使用 requests 发送请求时，才能使用                           |
| ++++ http     |            str / null             | / Y | http 代理                                                          |
| ++++ https    |            str / null             | / Y | https 代理                                                         |
| +++ httpx     |               dict                | N   | httpx 引擎代理，仅当使用 httpx 发送请求时，才能使用                                 |
| ++++ http://  |            str / null             | / Y | http 代理                                                          |
| ++++ https:// |            str / null             | / Y | https 代理                                                         |
| + module      |                str                | Y   | 用例所属模块                                                           |
| test_steps    |            list / dict            | Y   | 测试步骤，多用例时，必须使用 list 格式                                           |
| + name        |                str                | Y   | 用例名称                                                             |
| + case_id     |                str                | Y   | 用例 id                                                            |
| + description |                str                | Y   | 用例描述                                                             |
| + is_run      |            bool / null            | Y   | 是否跳过                                                             |
| + request     |               dict                | Y   | 请求参数                                                             |
| ++ method     |                str                | Y   | 请求方式                                                             |
| ++ url        |                str                | Y   | 请求链接，不包含域名，域名在测试环境中以 host=xxx 配置                                 |
| ++ params     |        dict / bytes / null        | Y   | 请求查询参数                                                           |
| ++ headers    |            dict / null            | Y   | 请求头，如果为空，则会应用上方配置中的请求头                                           |
| ++ data_type  |            str / null             | Y   | 请求数据类型: data / json                                              |
| ++ data       | dict / bytes / Tuple(list) / null | Y   | 请求体                                                              |
| ++ files      |   List\[Dict\[list/str]] / null   | Y   | 请求文件                                                             |
| + setup       |               dict                | N   | 请求前置条件                                                           |
| ++ sql        |    List\[ dict / str ] / null     | N   | 请求前置 sql，当为执行 sql 时，格式为 List\[str]，<br/> 当为设置变量时，格式为 List\[dict] |                                                              |
| ++ hooks      |         List\[str] / null         | N   | 钩子函数                                                             |
| ++ wait_time  |            int / null             | N   | 请求前等待时间                                                          |
| + teardown    |               dict                | N   | 请求后置条件                                                           |
| ++ sql        |    List\[ dict / str ] / null     | N   | 同前置                                                              |
| ++ hooks      |         List\[str] / null         | N   | 同前置                                                              |
| ++ extract    |            List\[dict]            | N   | 变量提取                                                             |
| +++ key       |                str                | / Y | 变量 key                                                           |
| +++ set_type  |                str                | / Y | 变量类型: env / global / cache，默认 cache                              |
| +++ jsonpath  |               dict                | / Y | jsonpath 表达式，依赖 response 数据集                                     |
| ++ assert     |        List\[ dict / str ]        | N   | 断言                                                               |                                                        |
| ++ wait_time  |            int / null             | N   | 请求后等待时间                                                          |

> **sql 参数附加说明：**

set_up / tear_down 的 sql 参数支持两种功能：

1. 设置变量
2. 执行 sql 语句

设置变量格式：

```yaml
sql:
  - key: 变量 key / str
    set_type: 变量类型：env / global / cache，默认 cache
    sql: 执行 sql 查询
    jsonpath: jsonpath 表达式，数据依赖 sql 查询
```

> **assert 参数附加说明：**

断言支持多种格式，详细说明请打开 assert_control.py 文件，以 reStructuredText 方式查阅，
以下两点做概要说明：

1. 常规断言：像正常 assert 的格式，但是比较值受约束，从 response 数据集进行取值，
   并且以 pm.response.get('') 开始取值，后面可以继续 get()，也可以使用其他方法，只要
   是 python 可执行代码，并且为了避免引号问题，断言脚本必须使用单引号处理

2. jsonpath：使用 jsonpath 从 response 进行取值比较
3. 两种断言方式可以同时使用

常规断言格式举例：

```yaml
assert:
  - assert xxx 条件 pm.response.get('')..., '错误说明'
```

jsonpath 格式举例：

```yaml
assert:
  - check: 检查说明 / str
    value: 比较值 / Any
    type: 比较类型，请查阅 assert_type.py 文件
    jsonpath: jsonpath 表达式
```

### 变量及hooks的使用

全局变量定义：

```text
仅在 data 目录下的 global_vars.yml 中以键值对形式进行定义，可参考demo
```

环境变量定义：

```text
在测试用例依赖的环境文件中以键=值的形式进行定义
```

hooks 函数定义:

```text
仅在 data 目录下的 hooks.py 文件中定义，根据定义结构在用例数据文件中使用，可参考 demo    
```

**使用表达式:**

变量：

      ${var} 或 $var

hooks：仅在前后置 hooks 参数下配置时生效

      ${func()} 或 ${func($var1, $var2)}

约束：

      变量和 hooks 开头: a-zA-Z_

### 用例中的变量替换

在测试用例中，寻找变量顺序为： cache > env > global，找到变量后将自动替换数据，未找到将会抛出异常

### 变量设置说明

变量设置含有三种场景：

1. env：即在当前测试用例数据所调用的测试环境中进行持久化写入，键值不会重复，新值覆盖旧值
2. global: 在全局变量文件中进行持久化写入，键值不会重复，新值覆盖旧值
3. cache：写入当前用例类运行过程的内存中，不会持久化，类运行结束清楚自动清除

## 用例创建

1. 根据数据结构及参数说明，手动编写测试用例
2. 通过 cli 自动生成测试用例

cli 生成测试用例说明:

```shell
cd fastpt

python cli.py --gtc
```

## 如何运行测试

运行 run.py 文件即可

main 程序参数根据情况进行自定义

## 如何查看报告

运行完之后到 report 文件夹下查看

## ❓问题相关

### 1: 为什么没有想要的日志内容

日志内容需要手动写入, 详细示例demo中几乎都有体现, 请自行查看

### 2: 为什么没有测试报告

html：

    自动生成，检查 run 参数是否开启 html 报告创建, 默认开启

~~excel：~~

    当前 release 版本已不适用，测试报告要手动写入, 并依赖 excel 测试数据

yaml：

    测试报告要手动写入, 很少用到，调用方法请查看 yaml_handler.py 文件

allure：

    自动生成, 默认开启并自动打开浏览器访问, 前提已正确安装 allure 程序
