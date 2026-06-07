# 示例

## 岗位招聘

输入：

```text
成都新都包装厂招女工10名，18-48岁，白班，包住，月薪4500-5500，李老师 13800000000
```

输出：

```json
{
  "type": "job",
  "confidence": 0.95,
  "raw_text": "成都新都包装厂招女工10名，18-48岁，白班，包住，月薪4500-5500，李老师 13800000000",
  "data": {
    "title": "成都新都包装厂白班女工",
    "city": "成都",
    "district": "新都",
    "headcount": 10,
    "age_min": 18,
    "age_max": 48,
    "gender_requirement": "女",
    "work_time": "白班",
    "benefits": ["包住"],
    "pay_min": 4500,
    "pay_max": 5500,
    "pay_unit": "月",
    "contact_name": "李老师",
    "contact_phone": "13800000000"
  },
  "missing_fields": ["具体地址", "工资结算方式"],
  "risk_flags": [],
  "warnings": []
}
```

## 求职者

输入：

```text
本人女42岁，在成都，想找白班，不进电子厂，最好包住，微信同号13800000000
```

输出：

```json
{
  "type": "candidate",
  "confidence": 0.92,
  "raw_text": "本人女42岁，在成都，想找白班，不进电子厂，最好包住，微信同号13800000000",
  "data": {
    "city": "成都",
    "age": 42,
    "gender": "女",
    "target_type": "找工作",
    "available_time": "白班",
    "avoid_keywords": ["电子厂"],
    "preference_keywords": ["包住"],
    "contact_phone": "13800000000",
    "contact_wechat": "13800000000"
  },
  "missing_fields": ["期望薪资", "具体工种"],
  "risk_flags": [],
  "warnings": []
}
```



