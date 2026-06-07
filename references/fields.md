# 字段说明

## 通用字段

- `type`：消息类型，job、candidate、demand、gig、irrelevant。
- `job_batch`：一条原文包含多个岗位时使用。
- `confidence`：判断置信度，0-1。
- `raw_text`：原文。
- `data`：结构化字段。
- `items`：批量岗位列表。
- `missing_fields`：缺失字段。
- `risk_flags`：风险提示。
- `warnings`：不确定说明。

## 岗位 job

- `title`：岗位标题。
- `category`：岗位分类。
- `city`：城市。
- `district`：区域。
- `headcount`：招聘人数。
- `pay_min`：最低薪资。
- `pay_max`：最高薪资。
- `pay_unit`：薪资单位，月、天、小时、件。
- `age_min`：最低年龄。
- `age_max`：最高年龄。
- `gender_requirement`：性别要求。
- `work_time`：班次或上班时间。
- `benefits`：福利。
- `address`：具体地址。
- `contact_name`：联系人。
- `contact_phone`：电话。
- `contact_wechat`：微信。
- `contacts`：多联系人列表。
- `worker_pay`：员工薪资。
- `supplier_policy`：供应商政策。
- `rebate_policy`：返费或利润政策。
- `invoice_tax_policy`：开票或扣税政策。
- `insurance_fee`：商保费用。
- `medical_exam_fee`：体检费。
- `wage_hold_policy`：压薪或发薪规则。
- `attendance_policy`：出勤、卡点、自离规则。

## 求职者 candidate

- `name`：姓名或称呼。
- `city`：所在城市。
- `district`：所在区域。
- `age`：年龄。
- `gender`：性别。
- `target_type`：找工作、找临时活、接单。
- `desired_jobs`：期望岗位。
- `skills`：技能。
- `available_time`：可上工时间。
- `expected_pay`：期望薪资。
- `avoid_keywords`：不接受条件。
- `preference_keywords`：偏好条件。
- `contact_phone`：电话。
- `contact_wechat`：微信。

## 招人需求 demand

- `title`：需求标题。
- `requester_type`：企业、劳务、HR、个人。
- `requester_name`：发布方或联系人。
- `requester_phone`：电话。
- `requester_wechat`：微信。
- `demand_type`：招工、临时活、外包、项目。
- `city`：城市。
- `district`：区域。
- `headcount`：需要人数。
- `pay_min`：最低薪资。
- `pay_max`：最高薪资。
- `pay_unit`：薪资单位。
- `age_min`：最低年龄。
- `age_max`：最高年龄。
- `gender_requirement`：性别要求。
- `work_time`：班次或时间。
- `required_skills`：技能要求。
- `address`：地点。

## 临时活 gig

- `title`：标题。
- `city`：城市。
- `district`：区域。
- `gig_type`：临时工、日结、小时工、接单、项目。
- `pay_min`：最低报酬。
- `pay_max`：最高报酬。
- `pay_unit`：天、小时、件、单。
- `work_time`：时间。
- `headcount`：人数。
- `contact_name`：联系人。
- `contact_phone`：电话。
- `contact_wechat`：微信。


