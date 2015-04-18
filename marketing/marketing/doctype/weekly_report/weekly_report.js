cur_frm.cscript.brand=function(doc,cdt,cdn)
{
	var d=locals[cdt][cdn];
	frappe.call({
		method:"marketing.marketing.doctype.weekly_report.weekly_report.get_brand_name",
		args:{brand:d.brand},
		callback:function(r)
		{
			d.brand_name=r.message;
			refresh_field("report_details");
		}
	});
}
cur_frm.cscript.item=function(doc,cdt,cdn)
{
	var d=locals[cdt][cdn];
	frappe.call({
		method:"marketing.marketing.doctype.weekly_report.weekly_report.get_item_name",
		args:{item:d.item},
		callback:function(r)
		{
			d.item_name=r.message;
			refresh_field("report_details");
		}
	});
}