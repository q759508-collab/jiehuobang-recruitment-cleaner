# 下一步测试流程

## 目标

验证真实链路：

```text
微信群原文 -> Skill 清洗 JSON -> Word 文档输出
```

不是只看手工期望 JSON。

## 第一步：重启 Codex

Skill 已安装到：

```text
C:\Users\Administrator\.codex\skills\jiehuobang-recruitment-cleaner
```

重启 Codex 后，使用这个提示：

```text
使用 jiehuobang-recruitment-cleaner，把 C:\Users\Administrator\jiehuobang-ai-mvp\skill-package\jiehuobang-recruitment-cleaner\samples\wechat-real-test-inbox.md 里任选 3 条真实样本清洗成 JSON，保存为 test-output.json。
```

## 第二步：校验 JSON

```bash
python scripts/validate_output.py test-output.json
```

## 第三步：导出 Word

```bash
python scripts/export_docx.py test-output.json -o test-output.docx
```

## 第四步：人工看 Word

重点看：

- 年龄是否正确。
- 薪资是否正确。
- 风险是否提示。
- 多岗位是否拆开。
- Word 是否方便复制。

## 第五步：修规则

如果输出错：

- 改 `references/risk-rules.md`
- 改 `references/labor-dispatch-rules.md`
- 改 `references/fields.md`

不要先做平台。



