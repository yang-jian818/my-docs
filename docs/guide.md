# 使用指南

## 本地预览

```bash
pip install mkdocs-material
mkdocs serve
```

执行后访问 <http://127.0.0.1:8000> 即可预览文档站点。

## 发布流程

1. 编写 Markdown 文档；
2. 提交代码到 GitHub（`git add`、`git commit`、`git push`）；
3. GitHub Actions 自动构建并部署。

## 在线访问

文档站点已由 GitHub Actions 自动部署，网址为：
<https://yang-jian818.github.io/my-docs/>

每次向 `main` 分支推送 `docs/` 或 `mkdocs.yml` 的修改，都会自动触发一次构建与部署。

## 关键命令

```bash
# 本地构建，生成 site/ 目录
mkdocs build

# 推送到远端，触发自动部署
git push origin main
```
