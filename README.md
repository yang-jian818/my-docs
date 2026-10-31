# my-docs

开源软件设计与分析 —— 实验二：GitHub Action 和 GitHub Pages 使用。

本仓库同时包含两个实践项目：

1. **实践项目1：使用 GitHub Actions 实现自动化测试**
   - `calculator.py`、`test_calculator.py`
   - `.github/workflows/ci.yml`：推送代码时自动运行 `pytest`
2. **实践项目2：通过 GitHub Actions 自动部署静态文档到 GitHub Pages**
   - `mkdocs.yml`、`docs/`
   - `.github/workflows/deploy.yml`：推送时自动构建并部署到 `gh-pages` 分支

## 目录结构

```text
my-docs/
├── docs/
│   ├── index.md
│   ├── about.md
│   ├── guide.md
│   └── api.md
├── .github/workflows/
│   ├── ci.yml
│   └── deploy.yml
├── mkdocs.yml
├── calculator.py
├── test_calculator.py
└── README.md
```

## 本地使用

```bash
pip install mkdocs-material pytest
pytest -v
mkdocs serve
```
