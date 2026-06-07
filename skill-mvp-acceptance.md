# Skill MVP 验收标准

## 发布前必须通过

### 1. 样本覆盖

- 至少 20 条招聘/求职/招人真实风格样本。
- 至少包含 5 条岗位。
- 至少包含 5 条求职者自荐。
- 至少包含 3 条招人需求。
- 至少包含 3 条临时活或接单信息。
- 至少包含 3 条风险信息。

### 2. 类型判断

必须能区分：

- 岗位招聘：`job`
- 求职者：`candidate`
- 招人需求：`demand`
- 临时活/接单：`gig`
- 无关信息：`irrelevant`

### 3. 字段提取

重点字段：

- 城市。
- 区域。
- 岗位或需求标题。
- 薪资。
- 年龄。
- 班次或时间。
- 联系人。
- 电话。
- 微信。
- 福利。

### 4. 特殊规则

必须正确处理：

- `18-40周岁` 不变成 `1840`。
- `10月17日` 不变成 `1017`。
- `0830` 在时间语境下识别为 `08:30`。
- `微信同号` 能识别为电话也是微信。
- 表情符号不导致脚本报错。

### 5. 风险提示

必须识别：

- 押金。
- 服装费。
- 报名费。
- 体检费。
- 高薪夸张。
- 联系方式缺失。
- 招聘主体不明。

### 6. 输出模式

必须支持：

- JSON。
- Markdown 表格。
- 发布文案。
- 风险检查。

### 7. 脚本

必须通过：

```bash
python scripts/split_messages.py samples/realistic-messy-messages.md --json
python scripts/validate_output.py samples/sample-output.json
python scripts/export_csv.py samples/sample-output.json -o samples/sample-output.csv
```

## 不通过就不发布

如果出现这些问题，先不要开源发布：

- README 看不懂怎么用。
- JSON 输出格式不稳定。
- 年龄、日期、时间频繁识别错。
- 风险信息完全识别不出来。
- 样本太少，看不出真实效果。



