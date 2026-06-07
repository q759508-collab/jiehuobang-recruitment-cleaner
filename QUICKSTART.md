# 快速开始

## 1. 先试一个岗位

```text
使用 jiehuobang-recruitment-cleaner，把下面招聘信息清洗成 JSON：

成都新都包装厂招女工10名，18-48岁，白班，包住，月薪4500-5500，李老师 13800000000
```

## 2. 再试风险识别

```text
使用 jiehuobang-recruitment-cleaner，检查下面招聘信息有没有风险：

高薪急招普工，月入8000-12000，包吃包住，先交300服装费，安排进厂，电话13800000000
```

## 3. 再试表格整理

```text
使用 jiehuobang-recruitment-cleaner，把下面求职者信息整理成表格：

本人男，36岁，人在重庆九龙坡，做过叉车，有证，想找长白班，夜班不考虑，工资最好6000以上，微信 aabbcc123
```

## 4. 跑脚本

```bash
python scripts/split_messages.py samples/realistic-messy-messages.md --json
python scripts/validate_output.py samples/realistic-expected-output.json
python scripts/export_csv.py samples/realistic-expected-output.json -o output.csv
```



