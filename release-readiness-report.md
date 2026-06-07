# 发布就绪检查报告

## 检查时间

2026-06-07

## 当前结论

当前 Skill 已具备小范围试用条件，但还没有经过用户微信真实群样本验证，不建议正式大范围推广。

建议状态：

```text
可以发给熟人试用，暂不大规模公开推广。
```

当前版本：

```text
0.1.3
```

当前最小链路：

```text
微信群招聘文本 -> AI 清洗 -> Word 文档输出
```

已生成测试文档：

- `samples/wechat-real-output.docx`
- `test-output.docx`

当前结论：

```text
Word 输出形式已通过人工确认，可以进入小范围试用。
```

当前发布范围：

```text
只发布招聘信息清洗和 Word 输出，不发布微信采集能力。
```

## 已通过

### 文件结构

已具备：

- `README.md`
- `SKILL.md`
- `LICENSE`
- `.gitignore`
- `PUBLISH.md`
- `demo-cases.md`
- `trial-invitation-copy.md`
- `skill-mvp-acceptance.md`
- `INSTALL.md`
- `QUICKSTART.md`
- `references/`
- `samples/`
- `scripts/`

### 脚本验证

已执行并通过：

```bash
python scripts/split_messages.py samples/realistic-messy-messages.md --json
python scripts/validate_output.py samples/sample-output.json
python scripts/export_csv.py samples/sample-output.json -o samples/sample-output.csv
```

结果：

- 真实风格样本拆分为 10 条有效消息。
- JSON 样本校验通过：`OK 2 item(s)`。
- CSV 导出命令通过。

说明：

- `sample-output.csv` 是生成文件，验证后已删除，发布仓库不保留。

## 还缺什么

### 1. 真实微信样本尚未测试

当前样本更偏模拟真实风格，还没有直接用用户微信里的真实发单群、招聘群文本测试。

目标：

- 20-50 条真实脱敏样本。

收集文件：

- `samples/wechat-real-test-inbox.md`

当前进度：

- 已收集 39 条真实有效样本。
- 已标记 2 条重复样本，不计入有效样本。

当前真实样本覆盖：

- 电子厂。
- 食品厂。
- 注塑厂。
- 物流夜班日结。
- 汽车小零件厂。
- 打磨工。
- 电热毯厂。
- 大龄工。
- 暑假工。
- 派遣供应商政策。
- 顺丰日结。
- 保安周结。
- 批量多岗位发单。
- 高风险志愿者/代理混入信息。
- 外卖骑手。
- 应届实习生。
- 仓库管理员。
- 汽配厂。
- 食品仓库。
- 周结仓储。
- 短期大龄工。
- 骑手租车模式。
- 押金和体检费场景。

第一轮最低样本量已达标。

下一步重点：

- 不再继续大量收样本。
- 抽取代表性样本补齐期望输出。
- 特别补 `job_batch` 批量岗位输出。
- 特别补高风险混入信息识别。

已根据真实样本新增专项规则：

- `references/labor-dispatch-rules.md`

新增支持方向：

- 劳务派遣发单。
- 供应商政策。
- 返费和利润。
- 开票扣税。
- 商保。
- 体检费。
- 压薪和自离无工资。
- 多联系人角色。
- 年龄和薪资数字粘连。

### 2. 真实输出验收不足

已补 `samples/realistic-expected-output.json`，包含 10 条完整期望输出。

目标：

- 后续用真实脱敏样本继续扩充。

### 3. 反馈入口

已补反馈入口设计：

- `feedback-channel-design.md`
- `.github/ISSUE_TEMPLATE/cleaning-error.yml`
- `.github/ISSUE_TEMPLATE/feature-request.yml`

第一阶段建议使用：

- 微信私聊或微信群。
- GitHub / Gitee Issue。

### 4. 开源仓库还没创建

待定：

- GitHub。
- Gitee。
- 两边都发。

## 下一步

建议下一步只做三件事：

1. 补真实脱敏样本。
2. 补 10 条完整期望输出。
3. 定反馈入口。

完成前不要继续做网页、后台、数据库。


