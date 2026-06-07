#!/usr/bin/env python3
import argparse
import html
import json
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""


def paragraph(text: str, bold: bool = False) -> str:
    safe = html.escape(text or "")
    if bold:
        run = f"<w:r><w:rPr><w:b/></w:rPr><w:t>{safe}</w:t></w:r>"
    else:
        run = f"<w:r><w:t>{safe}</w:t></w:r>"
    return f"<w:p>{run}</w:p>"


def line(label: str, value) -> str:
    if value in (None, "", []):
        return ""
    if isinstance(value, list):
        value = "、".join(str(v) for v in value)
    return paragraph(f"{label}：{value}")


def render_job(item: dict, index: int | None = None) -> list[str]:
    data = item.get("data") or item
    title = data.get("title") or "未命名岗位"
    heading = f"{index}. {title}" if index else title
    parts = [paragraph(heading, bold=True)]
    parts.append(line("企业", data.get("company")))
    parts.append(line("城市", data.get("city")))
    parts.append(line("区域", data.get("district")))
    parts.append(line("岗位", data.get("category") or data.get("work_content")))
    parts.append(line("薪资", build_pay(data)))
    parts.append(line("年龄", build_age(data)))
    parts.append(line("性别", data.get("gender_requirement")))
    parts.append(line("时间", data.get("work_time")))
    parts.append(line("福利", data.get("benefits")))
    parts.append(line("地址", data.get("address") or data.get("interview_address")))
    parts.append(line("面试时间", data.get("interview_time")))
    parts.append(line("联系人", data.get("contact_name")))
    parts.append(line("电话", data.get("contact_phone")))
    parts.append(line("微信", data.get("contact_wechat")))
    parts.append(line("多联系人", format_contacts(data.get("contacts"))))
    parts.append(line("供应商政策", data.get("supplier_policy")))
    parts.append(line("返费/利润", data.get("rebate_policy")))
    parts.append(line("开票扣税", data.get("invoice_tax_policy")))
    parts.append(line("商保", data.get("insurance_fee")))
    parts.append(line("体检费", data.get("medical_exam_fee")))
    parts.append(line("压薪/发薪", data.get("wage_hold_policy")))
    parts.append(line("出勤规则", data.get("attendance_policy")))
    parts.append(line("缺失字段", item.get("missing_fields")))
    parts.append(line("风险提示", item.get("risk_flags")))
    parts.append(line("备注", item.get("warnings")))
    return [p for p in parts if p]


def build_pay(data: dict) -> str:
    if data.get("pay_min") and data.get("pay_max"):
        if data["pay_min"] == data["pay_max"]:
            return f"{data['pay_min']}/{data.get('pay_unit', '')}".strip("/")
        return f"{data['pay_min']}-{data['pay_max']}/{data.get('pay_unit', '')}".strip("/")
    if data.get("monthly_pay_min") and data.get("monthly_pay_max"):
        return f"{data['monthly_pay_min']}-{data['monthly_pay_max']}/月"
    if data.get("pay_day_shift") or data.get("pay_night_shift"):
        return f"白班{data.get('pay_day_shift', '')}，夜班{data.get('pay_night_shift', '')}"
    return ""


def build_age(data: dict) -> str:
    if data.get("age_min") is not None and data.get("age_max") is not None:
        return f"{data['age_min']}-{data['age_max']}岁"
    return ""


def format_contacts(contacts) -> str:
    if not contacts:
        return ""
    parts = []
    for contact in contacts:
        if not isinstance(contact, dict):
            parts.append(str(contact))
            continue
        role = contact.get("role") or "联系人"
        name = contact.get("name") or ""
        phone = contact.get("phone") or ""
        wechat = " 微信同号" if contact.get("wechat_same_as_phone") else ""
        parts.append(f"{role} {name} {phone}{wechat}".strip())
    return "；".join(parts)


def render_document(items: list[dict]) -> str:
    body: list[str] = [paragraph("接活帮招聘信息清洗结果", bold=True)]
    counter = 1

    for item in items:
        if item.get("type") == "job_batch":
            body.append(paragraph("批量岗位", bold=True))
            for child in item.get("items") or []:
                merged = {
                    "data": child,
                    "missing_fields": item.get("missing_fields", []),
                    "risk_flags": item.get("risk_flags", []),
                    "warnings": item.get("warnings", []),
                }
                body.extend(render_job(merged, counter))
                counter += 1
        else:
            body.extend(render_job(item, counter))
            counter += 1

    body_xml = "".join(body)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body_xml}
    <w:sectPr/>
  </w:body>
</w:document>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Export cleaned recruitment JSON to a Word .docx file.")
    parser.add_argument("input", help="Input JSON file.")
    parser.add_argument("-o", "--output", required=True, help="Output .docx file.")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8-sig") as f:
        payload = json.load(f)

    items = payload if isinstance(payload, list) else [payload]
    document_xml = render_document(items)

    output = Path(args.output)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS)
        docx.writestr("word/document.xml", document_xml)

    print(f"WROTE {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


