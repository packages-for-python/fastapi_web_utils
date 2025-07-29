# FastAPI Web Utils

一个为FastAPI Web框架提供实用工具和数据库客户端的Python包。

## 项目简介

`fastapi_web_utils` 是一个轻量级的Python工具包，专门为FastAPI Web应用开发提供常用的工具函数和数据库客户端。该包包含了日志管理、PostgreSQL数据库连接和ClickHouse数据库连接等实用功能。

## 功能特性

### 🔧 核心工具

- **日志管理** (`tools.log`): 提供灵活的日志配置，支持控制台和文件输出
- **PostgreSQL客户端** (`tools.postgres`): 基于SQLAlchemy的PostgreSQL连接池管理
- **ClickHouse客户端** (`tools.clickhouse`): 基于SQLAlchemy的ClickHouse数据库连接器

### 📦 技术栈

- Python 3.11
- SQLAlchemy 2.0.41
- Greenlet 3.2.3
- 支持PostgreSQL和ClickHouse数据库

## 安装

```bash
pip install git+https://github.com/packages-for-python/fastapi_web_utils
```

## 使用指南

### 日志管理

```python
from fastapi_web_utils_tools.log import get_logger

# 创建控制台日志
logger = get_logger("my_app")
logger.info("这是一条信息日志")

# 创建同时输出到文件的日志
file_logger = get_logger("my_app", to_file=True)
file_logger.warning("这条日志会同时输出到控制台和文件")
```

### PostgreSQL数据库连接

```python
from fastapi_web_utils_tools.postgres import PostgresClient

# 创建PostgreSQL客户端
pg_client = PostgresClient(
    user="your_username",
    password="your_password",
    host="localhost",
    port=5432,
    database="your_database"
)

# 使用上下文管理器
with pg_client as session:
    # 执行数据库操作
    result = session.execute("SELECT * FROM users")
    users = result.fetchall()

# 或者直接获取session
session = pg_client.get_session()
try:
    # 数据库操作
    pass
finally:
    session.close()
```

### ClickHouse数据库连接

```python
from fastapi_web_utils_tools.clickhouse import ClickhouseClient

# 创建ClickHouse客户端
ch_client = ClickhouseClient(
    user="default",
    password="your_password",
    host="localhost",
    port=9000,
    database="your_database"
)

# 使用上下文管理器
with ch_client as session:
    # 执行查询
    result = session.execute("SELECT * FROM events LIMIT 10")
    events = result.fetchall()

# 或者直接获取session
session = ch_client.get_session()
try:
    # 数据库操作
    pass
finally:
    session.close()
```

## 配置说明

### 日志配置

- 日志文件位置: `logs/{logger_name}/{logger_name}.log`
- 文件大小限制: 2MB
- 备份文件数量: 5个
- 日志格式: `时间 - 级别 - 名称 - 消息`

### 数据库连接池配置

#### PostgreSQL
- 默认连接池大小: 50
- 最大溢出连接数: 0
- 时区设置: UTC

#### ClickHouse  
- 连接池大小: 10
- 最大溢出连接数: 20
- 连接超时: 30秒
- 连接回收时间: 3600秒
- 最大块大小: 100000

## 依赖要求

```
greenlet==3.2.3
SQLAlchemy==2.0.41
typing_extensions==4.14.1
```

## 开发环境

- Python 3.11
- 建议使用虚拟环境

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

## 项目结构

```
fastapi_web_utils/
├── README.md
├── requirements.txt
├── setup.py
└── fastapi_web_utils_tools/
    ├── __init__.py
    ├── log.py          # 日志管理工具
    ├── postgres.py     # PostgreSQL客户端
    └── clickhouse.py   # ClickHouse客户端
```

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 作者

- **lei.wang** - [greatbestlei@gmail.com](mailto:greatbestlei@gmail.com)

## 更新日志

### v0.1.0
- 初始版本发布
- 添加日志管理功能
- 添加PostgreSQL客户端
- 添加ClickHouse客户端
