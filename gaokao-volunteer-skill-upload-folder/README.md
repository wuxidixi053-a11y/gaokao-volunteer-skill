# 高考志愿院校与专业尽调 Skill

一个面向中国高考志愿填报场景的院校与专业尽调 Skill，重点关注官方数据核验、录取位次、招生计划、毕业去向、考公考研考编、真实评论和隐藏风险。

它可以帮助用户在输入院校、专业、分数、位次、省份、选科等信息后，系统化分析：

- 历年录取分数与位次
- 招生计划变化
- 专业组和调剂风险
- 学校、校区、专业、大类招生、中外合作等差异
- 毕业去向、就业质量、升学、保研、考研、考公、考编
- 真实学生评价与公开平台口碑
- 数据缺失、冲突和可信度

## 安装方式

### ChatGPT

1. 下载 GitHub Release 中的 zip 文件。
2. 打开 ChatGPT。
3. 进入 Skills。
4. 选择 New skill。
5. 选择 Upload from your computer。
6. 上传 zip 文件。
7. 安装并测试。

### Codex / 本地 Agent Skills

将本文件夹放到仓库级 skills 目录：

```text
$REPO_ROOT/.agents/skills/gaokao-volunteer-due-diligence/
```

或用户级 skills 目录：

```text
$HOME/.agents/skills/gaokao-volunteer-due-diligence/
```

目录中应至少包含：

```text
gaokao-volunteer-due-diligence/
└── SKILL.md
```

如果保留扩展文件，可以包含：

```text
gaokao-volunteer-due-diligence/
├── SKILL.md
├── references/
├── examples/
└── scripts/
```

## 使用示例

```text
帮我分析一下南京审计大学，广东物理类 580 分，位次 32000，想报审计学，风险大吗？
```

```text
法学专业适不适合想考公的学生？本科就业怎么样？
```

```text
帮我尽调一下华南农业大学计算机类，重点看校区、录取位次、就业和学生评价。
```

## 重要声明

本 Skill 不承诺录取结果，不替代省教育考试院、高校招生章程和官方志愿填报系统。所有分数、位次、招生计划、就业率等数据必须以官方来源为准。

## 发布检查清单

- [x] SKILL.md 顶部有 name 和 description
- [x] description 清楚说明何时触发 skill
- [x] 没有承诺“一定录取”
- [x] 没有编造数据源
- [x] 明确要求官方数据优先
- [x] 明确数据缺失时不得编造
- [x] 明确区分院校线和专业线
- [x] 明确区分学校、专业组、校区、专业
- [x] 明确真实评论只能作为参考
- [x] README 有安装说明
- [x] README 有使用示例
- [x] 有 LICENSE
- [x] 有版本号 v0.1.0

