# 欢迎使用 MkDocs

这是一个示例文档，使用 **MkDocs** 进行构建，并通过 **GitHub Actions** 自动部署到 **GitHub Pages**。

## 文档目录

- [关于本项目](about.md)
- [使用指南](guide.md)
- [API 参考](api.md)

!!! note "自动部署说明"
    本页面修改并推送后，GitHub Actions 会自动重新构建站点并覆盖 `gh-pages` 分支，
    约 30 秒后刷新 <https://yang-jian818.github.io/my-docs/> 即可看到最新内容。

## 本实验完成的工作

1. 搭建 MkDocs Material 文档站点，编写 4 个 Markdown 页面；
2. 编写 `.github/workflows/deploy.yml`，实现“推送即构建、构建即部署”；
3. 通过 GitHub Pages 托管 `gh-pages` 分支中的静态站点。
