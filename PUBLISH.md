# 接活帮招聘信息清洗 Skill

## 这是做什么的

这是一个免费开源的 Codex Skill，用来清洗中文招聘和求职信息。

适合处理：

- 微信群招聘信息。
- 劳务群招工信息。
- 求职者自荐。
- 招人需求。
- 临时活。
- 一人公司接单信息。

## 能输出什么

- JSON。
- Word 文档。
- 正式发布文案。
- 风险提示。
- 缺失字段。

## 示例用法

### 清洗成 JSON

```text
使用 jiehuobang-recruitment-cleaner，把下面招聘信息清洗成 JSON：

成都新都包装厂招女工10名，18-48岁，白班，包住，月薪4500-5500，李老师 13800000000
```

### 整理成表格

```text
使用 jiehuobang-recruitment-cleaner，把下面多条招聘信息整理成表格：

...
```

### 检查风险

```text
使用 jiehuobang-recruitment-cleaner，检查下面招聘信息有没有风险：

急招普工，工资8000-12000，包吃包住，名额有限，先交300报名费，电话13800000000
```

## 当前版本限制

- 不自动采集微信。
- 不保存数据。
- 不提供网站后台。
- 不保证所有文本都能识别正确。

## 可选脚本

脚本目录：

```text
scripts/
```

拆分多条文本：

```bash
python scripts/split_messages.py samples/sample-messages.md
```

校验 JSON 输出：

```bash
python scripts/validate_output.py samples/sample-output.json
```

导出 Word：

```bash
python scripts/export_docx.py samples/wechat-real-expected-output.json -o output.docx
```

备用导出 CSV：

```bash
python scripts/export_csv.py samples/sample-output.json -o output.csv
```

如果 JSON 里包含 `job_batch`，导出时会把每个岗位展开成多行。

检测重复：

```bash
python scripts/detect_duplicates.py samples/wechat-real-test-inbox.md
```

## 适合谁试用

- 招聘群群主。
- 县城招聘站运营者。
- 劳务公司。
- HR 公司。
- 每天整理招聘信息的人。

## 希望收到的反馈

- 哪些文本识别错了。
- 哪些字段不够用。
- 是否需要批量处理。
- 是否需要导出 Excel。
- 是否需要网页版本。

## 真实样本

项目内置了两类样本：

- `samples/sample-messages.md`
- `samples/realistic-messy-messages.md`

如果你愿意反馈真实样本，请先脱敏手机号、微信号、姓名等隐私信息。


