# 接活帮招聘信息清洗 Skill

This is a Codex Skill for cleaning Chinese WeChat group recruitment messages into JSON, tables, publishable copy, and risk warnings.

一个用于中文招聘、求职、招人需求、临时活信息清洗的 Codex Skill。

它适合处理微信群、朋友圈、私聊、招聘群、劳务群里的混乱文本，并输出结构化 JSON、表格、发布文案和风险提示。

关键词：Codex Skill、招聘信息清洗、微信群招聘、私域招聘、劳务招聘、求职信息整理、招人需求、招聘 JSON、招聘表格、招聘风险识别、recruitment cleaner、Chinese recruitment、WeChat group recruiting。

## 适合谁

- 招聘群群主。
- 县城招聘站运营者。
- 劳务公司。
- HR 服务公司。
- 工厂招工中介。
- 每天手工整理招聘信息的人。

## 能做什么

- 判断消息类型。
- 提取城市、岗位、薪资、年龄、班次、联系人、电话、微信。
- 识别求职者自荐。
- 识别招人需求。
- 识别临时活和接单信息。
- 检查风险和缺失字段。
- 输出 JSON、Word 文档、发布文案。
- 可选脚本支持拆分文本、校验 JSON、导出 Word 文档。
- 支持 `job_batch`，一条消息里多个岗位可导出为多行 CSV。
- 支持基础重复信息识别。

## 联系方式说明

真实业务清洗时默认保留联系方式。招聘广告、劳务发单、名单报备、政策咨询、财务结算、投诉反馈等联系人和手机号都应被提取出来。

本仓库里的样例手机号使用 `13800000000` 演示，是为了避免把真实微信群数据公开到开源仓库，不代表工具会删除真实手机号。

## 快速使用

详细安装见：

- `INSTALL.md`
- `QUICKSTART.md`
- `USER_TEST_GUIDE.md`

在 Codex 中输入：

```text
使用 jiehuobang-recruitment-cleaner，把下面招聘信息清洗成 JSON：

成都新都包装厂招女工10名，18-48岁，白班，包住，月薪4500-5500，李老师 13800000000
```

也可以要求：

```text
把下面多条招聘信息整理成表格。
```

```text
把下面招聘信息改成正式发布文案。
```

```text
检查下面招聘信息有没有风险。
```

## 可选脚本

拆分多条文本：

```bash
python scripts/split_messages.py samples/sample-messages.md
```

校验 JSON：

```bash
python scripts/validate_output.py samples/sample-output.json
```

导出 Word：

```bash
python scripts/export_docx.py samples/wechat-real-expected-output.json -o output.docx
```

备用导出 CSV：

```bash
python scripts/export_csv.py samples/sample-output.json -o samples/sample-output.csv
```

检测重复：

```bash
python scripts/detect_duplicates.py samples/wechat-real-test-inbox.md
```

## 测试样本

- `samples/sample-messages.md`：基础样本。
- `samples/realistic-messy-messages.md`：真实微信群风格样本。
- `samples/realistic-expected-notes.md`：真实样本期望识别要点。

## 当前限制

- 不自动采集微信。
- 不保存数据库。
- 不提供网站后台。
- 不保证所有文本都能识别正确。
- 批量脚本只负责拆分、校验和导出，不负责调用大模型。

## 希望收到的反馈

- 哪些招聘信息识别错了。
- 哪些字段不够用。
- 是否需要批量处理。
- 是否需要导出 Excel。
- 是否需要网页版本。
- 是否需要接入微信或飞书表格。

反馈格式见：

- `USER_TEST_GUIDE.md`
- `feedback-channel-design.md`

项目使用情况观察见：

- `ADOPTION_METRICS.md`

## 许可证

MIT License


