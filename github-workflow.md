# 🐙 GitHub CLI 工作流程演示

## 在有认证的情况下，这些是典型的 GitHub CLI 操作：

### 1. 📦 仓库管理
```bash
# 创建新仓库
gh repo create my-calculator --description "Python 计算器项目" --public

# 克隆仓库
gh repo clone username/my-calculator

# 查看仓库信息
gh repo view username/my-calculator --json name,description,stargazerCount
```

### 2. 🔄 Pull Request 管理  
```bash
# 创建 PR
gh pr create --title "添加计算器功能" --body "实现了基本四则运算"

# 查看所有 PR
gh pr list

# 查看特定 PR
gh pr view 42

# 检查 PR 的 CI 状态
gh pr checks 42

# 合并 PR
gh pr merge 42 --squash
```

### 3. 🐛 Issue 管理
```bash
# 创建 issue
gh issue create --title "添加科学计算功能" --body "需要支持三角函数"

# 查看 issues
gh issue list

# 分配 issue
gh issue edit 123 --assignee @me

# 关闭 issue
gh issue close 123
```

### 4. 🚀 CI/CD 监控
```bash
# 查看最近的工作流运行
gh run list --limit 10

# 查看特定运行的详情
gh run view 1234567890

# 查看失败的日志
gh run view 1234567890 --log-failed

# 重新运行失败的工作流
gh run rerun 1234567890
```

### 5. 📊 项目分析
```bash
# 获取仓库统计信息
gh api repos/username/my-calculator --jq '.stargazers_count, .forks_count'

# 查看提交历史
gh api repos/username/my-calculator/commits --jq '.[].commit.message'

# 获取贡献者信息
gh api repos/username/my-calculator/contributors
```

## 🔧 实际工作流程示例

假设你要修复一个 bug：

```bash
# 1. 从 issue 创建分支
gh issue develop 456 --name fix-division-bug

# 2. 进行修改并提交
git add . && git commit -m "fix: 修复除法精度问题"

# 3. 推送并创建 PR
git push -u origin fix-division-bug
gh pr create --title "修复除法精度问题" --body "closes #456"

# 4. 监控 CI 状态
gh pr checks --watch

# 5. 合并 PR
gh pr merge --squash
```

## 💡 高级功能

```bash
# 批量操作
gh pr list --json number --jq '.[].number' | xargs -I {} gh pr close {}

# 使用 GitHub Actions
gh workflow run ci.yml --ref main

# 管理 releases
gh release create v1.0.0 --generate-notes

# 管理 secrets
gh secret set API_KEY --body "your-secret-key"
```

---

**这些功能需要 GitHub CLI 完全认证后才能使用。** 🔐