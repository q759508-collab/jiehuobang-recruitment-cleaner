# 安装与试用

## 方式 1：作为 Codex Skill 使用

把整个目录复制到 Codex skills 目录。

Windows 示例：

```text
C:\Users\Administrator\.codex\skills\jiehuobang-recruitment-cleaner
```

复制后重启 Codex。

然后输入：

```text
使用 jiehuobang-recruitment-cleaner，把下面招聘信息清洗成 JSON：

成都新都包装厂招女工10名，18-48岁，白班，包住，月薪4500-5500，李老师 13800000000
```

## 方式 2：只使用脚本

如果不使用 Codex Skill，也可以单独使用脚本。

拆分多条文本：

```bash
python scripts/split_messages.py samples/realistic-messy-messages.md --json
```

校验 JSON：

```bash
python scripts/validate_output.py samples/sample-output.json
```

导出 CSV：

```bash
python scripts/export_csv.py samples/sample-output.json -o output.csv
```

## 方式 3：只复制提示词

如果不会安装 Skill，可以直接复制 `references/prompt-examples.md` 里的提示词。

## 注意

- 真实样本请先脱敏。
- 不要上传真实手机号、微信号、姓名、身份证。
- 当前版本不自动调用大模型。
- 脚本只负责拆分、校验和导出。



