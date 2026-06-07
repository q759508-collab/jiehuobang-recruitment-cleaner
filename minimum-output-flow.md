# 最小可用输出链路

## 当前原则

先不做完整平台，也不做复杂自动化。

第一阶段只打通最小链路：

```text
微信群招聘文本 -> AI 清洗 -> Word 文档输出
```

## 为什么

目标用户不是开发者，很多人不需要 JSON、CSV、API。

他们更需要：

- 能复制。
- 能转发。
- 能给老板看。
- 能发给同事。
- 能人工再改。

所以 Word 文档比表格更适合第一版试用。

## 当前已跑通

输入：

- `samples/wechat-real-expected-output.json`

输出：

- `samples/wechat-real-output.docx`

命令：

```bash
python scripts/export_docx.py samples/wechat-real-expected-output.json -o samples/wechat-real-output.docx
```

验证：

```text
WROTE samples\wechat-real-output.docx
OK 9 item(s)
```

## 第一阶段不做

- 不做网站。
- 不做后台。
- 不做登录。
- 不做支付。
- 不做数据库。
- 不做微信自动采集。
- 不主推 CSV。

## 第一阶段要做好

- 招聘文本清洗准确。
- 风险提示清楚。
- 多岗位能拆开。
- 输出 Word 方便复制。
- 文档内容可人工修改。



