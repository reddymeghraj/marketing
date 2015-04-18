# Copyright (c) 2013, wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class WeeklyReport(Document):
	pass
@frappe.whitelist()
def get_brand_name(brand):
	query=frappe.db.sql(""" select brand_name from `tabAdd Brand` where name=%s""",(brand))
	brand_name=str(query[0][0])
	return brand_name
@frappe.whitelist()
def get_item_name(item):
	query=frappe.db.sql("""select item_name from `tabAdd Item` where name=%s""",(item))
	item_name=str(query[0][0])
	return item_name	    	