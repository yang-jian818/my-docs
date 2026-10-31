# API 参考

这里是 API 参考文档示例，演示如何用 Markdown 编写接口说明。

## 计算器模块 `calculator.py`

### `add(a, b)`

返回两个数之和。

```python
from calculator import add

assert add(2, 3) == 5
```

### `multiply(a, b)`

返回两个数之积。

```python
from calculator import multiply

assert multiply(3, 4) == 12
```

## 返回码说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| a | int / float | 第一个操作数 |
| b | int / float | 第二个操作数 |
