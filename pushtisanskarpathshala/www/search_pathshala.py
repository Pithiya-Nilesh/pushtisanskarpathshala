import frappe

# import erpnext.education.utils as utils
import pushtisanskarpathshala.www.utils.custom_utils as utils

no_cache = 1
pathshala_list = []

def get_context(context):
	context.cities = frappe.db.sql("SELECT DISTINCT city from `tabPathshala` order by city")
	for pathshala in pathshala_list:
		context.pathshala_list = pathshala
	pathshala_list.clear()

@frappe.whitelist(allow_guest=True)
def list_pathshala(city):
	global pathshala
	pathshala = frappe.db.get_list("Pathshala", filters={'city': city}, fields=["pathshala_reg_no", "address_line_1", "address_line_2", "address_line_3", "city", "taluka", "pincode", "district", "state", "mobile_no", "sanchalak_name", "registration_date"])
	pathshala_list.append(pathshala)
