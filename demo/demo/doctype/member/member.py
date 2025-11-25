import frappe
from frappe.website.website_generator import WebsiteGenerator

class Member(WebsiteGenerator):

    def validate(self):
        if not self.age:
            frappe.throw("Age is required")
        
        if self.age < 18:
            frappe.throw("Age must be greater than 18")


@frappe.whitelist()
def get_member_with_empty_email():
    """Get members with empty email addresses"""
    return frappe.get_all(
        "Member",
        filters={"mail_id": ""},
        fields=["name", "full_name", "mail_id"]
    )


@frappe.whitelist()
def get_mail_id():
    return frappe.db.get_value("Member", "61", "mail_id")


@frappe.whitelist()
def create_member():
    """Create a new member"""
    first_name = "Siva"
    last_name = "Kumaran"
    full_name = f"{first_name} {last_name}".strip()
    
    member = frappe.get_doc({
        "doctype": "Member",
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "mail_id": "siva@test.com",
        "age": 23
    })
    member.insert()
    return member


@frappe.whitelist()
def approve_member(names=None):
    # Step 1: Get names from List View Action if not passed
    if not names:
        names = frappe.form_dict.get("names")

    # Step 2: Validate
    if not names:
        frappe.throw("No members selected")

    # Step 3: Parse JSON list
    names = frappe.parse_json(names)

    # Step 4: Loop & approve
    for docname in names:
        doc = frappe.get_doc("Member", docname)
        doc.status = "Approved"
        doc.save()

    return "Approved successfully"

