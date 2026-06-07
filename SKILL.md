---
name: jiehuobang-recruitment-cleaner
description: Use when cleaning, structuring, rewriting, or analyzing Chinese recruitment, job-seeking, hiring-demand, gig, labor-dispatch, WeChat group, or private-domain recruiting messages. Helps classify raw text, extract fields, identify risks, preserve contact info when appropriate, and produce JSON, table rows, or publishable Chinese copy.
---

# 接活帮招聘信息清洗 Skill

## 目标

把中文私域招聘文本清洗成可用数据，适合微信群、朋友圈、私聊、招聘群、劳务群、HR 群里的信息整理。

## 适用输入

- 岗位招聘。
- 求职者自荐。
- 招人需求。
- 临时活。
- 一人公司接单信息。
- 无关消息识别。

## 工作流程

1. 保留原文。
2. 判断消息类型。
3. 提取关键字段。
4. 标记风险和缺失字段。
5. 输出用户需要的格式。

需要字段细节时，读取 `references/fields.md`。

需要风险判断时，读取 `references/risk-rules.md`。

需要输出格式时，读取 `references/output-formats.md`。

需要示例时，读取 `references/examples.md`。

需要提示词模板时，读取 `references/prompt-examples.md`。

遇到劳务派遣、供应商政策、返费、开票扣税、多联系人发单时，读取 `references/labor-dispatch-rules.md`。

## 类型

只使用这些类型：

- `job`：岗位招聘。
- `candidate`：求职者或接单人自荐。
- `demand`：招人需求。
- `gig`：临时活或接单机会。
- `irrelevant`：无关信息。
- `job_batch`：一条原文包含多个岗位。

## 清洗规则

- 不编造原文没有的信息。
- 联系电话、微信号、联系人可以保留。
- `18-40周岁` 要识别成年龄范围，不要变成 `1840`。
- `8点30`、`8:30`、`0830` 要识别为时间。
- `10月17日` 要识别为日期，不要变成 `1017`。
- 不确定字段留空，并写入 `warnings`。
- 风险信息要写入 `risk_flags`。
- 劳务发单里的返费、开票扣税、商保、体检费、压薪、自离无工资、多联系人角色要保留。

## 默认输出 JSON

```json
{
  "type": "job",
  "confidence": 0.9,
  "raw_text": "",
  "data": {},
  "missing_fields": [],
  "risk_flags": [],
  "warnings": []
}
```

## 常用输出模式

用户要求“整理成表格”时，输出 Markdown 表格。

用户要求“转成发布文案”时，输出正式中文招聘文案。

用户要求“转 JSON”时，只输出 JSON。

一条原文包含多个岗位时，输出 `job_batch`，并把每个岗位放入 `items`。

用户要求“看看有没有风险”时，重点输出风险点和需要核实的字段。

## 风险识别重点

- 押金。
- 体检费。
- 服装费。
- 高薪夸张。
- 地址不清。
- 联系方式缺失。
- 工资结算方式不清。
- 年龄、性别限制可能引发争议。
- 招聘主体不明。


