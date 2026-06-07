# 开源仓库检查清单

## 文件

- [ ] `README.md`
- [ ] `SKILL.md`
- [ ] `LICENSE`
- [ ] `.gitignore`
- [ ] `PUBLISH.md`
- [ ] `demo-cases.md`
- [ ] `trial-invitation-copy.md`
- [ ] `skill-mvp-acceptance.md`

## 目录

- [ ] `references/`
- [ ] `samples/`
- [ ] `scripts/`

## 脚本验证

```bash
python scripts/split_messages.py samples/realistic-messy-messages.md --json
python scripts/validate_output.py samples/sample-output.json
python scripts/export_csv.py samples/sample-output.json -o samples/sample-output.csv
python scripts/detect_duplicates.py samples/wechat-real-test-inbox.md
```

## README 必须讲清楚

- [ ] 这个项目是做什么的。
- [ ] 适合谁用。
- [ ] 能输出什么。
- [ ] 怎么快速使用。
- [ ] 当前限制。
- [ ] 怎么反馈。

## 发布前不要包含

- [ ] 真实手机号。
- [ ] 真实微信号。
- [ ] 真实姓名。
- [ ] 未脱敏聊天记录。
- [ ] 公司内部信息。
- [ ] 生成出来的临时 CSV。

## 发布后要观察

- [ ] 是否有人 Star / 收藏。
- [ ] 是否有人问用法。
- [ ] 是否有人发真实样本。
- [ ] 是否有人问批量处理。
- [ ] 是否有人问 Excel。
- [ ] 是否有人问网页版本。


