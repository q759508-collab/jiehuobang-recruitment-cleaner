# 开源发布说明

## 当前发布范围

本版本只发布：

- 招聘信息清洗 Skill。
- 已脱敏的真实微信群风格样本。
- 风险规则。
- 劳务发单规则。
- JSON 校验脚本。
- Word 导出脚本。

不发布：

- 微信采集。
- 自动化采集。
- 后台系统。
- 数据库。
- 支付。
- 商业授权。

## 推荐仓库名

```text
jiehuobang-recruitment-cleaner
```

## 推荐描述

```text
Codex Skill for cleaning Chinese WeChat recruitment messages into structured JSON and Word documents.
```

中文描述：

```text
接活帮招聘信息清洗 Skill：把微信群招聘、劳务发单、求职信息整理成结构化 JSON 和 Word 文档。
```

## 发布平台

优先：

- GitHub。
- Gitee。

## 发布前命令

```bash
python scripts/validate_output.py samples/representative-expected-output.json
python scripts/export_docx.py samples/representative-expected-output.json -o samples/representative-output.docx
python scripts/detect_duplicates.py samples/wechat-real-test-inbox.md
```

## 发布标签

```text
v0.1.3-alpha
```

## 隐私和联系方式说明

真实业务使用时，招聘信息里的手机号、微信号、联系人必须保留，否则数据无法用于报名、报备、政策咨询和结算对接。

开源仓库中的样例号码统一替换为 `13800000000`，只是为了避免公开真实微信群联系人信息。不要把样例脱敏理解为产品规则。

## 发布文案

这是一个免费开源的招聘信息清洗 Skill。

它可以把微信群里的招聘信息、劳务发单、求职/招人需求整理成结构化 JSON 和 Word 文档，并识别押金、体检费、商保、开票扣税、卡点离职无费用、年龄薪资粘连等风险。

当前版本不做微信采集，只处理用户提供的文本。



