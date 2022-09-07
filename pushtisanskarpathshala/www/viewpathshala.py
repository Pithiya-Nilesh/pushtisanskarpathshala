import frappe

# import erpnext.education.utils as utils
import pushtisanskarpathshala.www.utils.custom_utils as utils

no_cache = 1
teacher_list = []


def get_context(context):
	global teacher_list
	try:
		reg_no = frappe.form_dict["reg_no"]
	except KeyError:
		frappe.local.flags.redirect_location = "/"
		raise frappe.Redirect
	# context.get_reg_no = reg_no
	teacher_list.clear()
	context.pathshala_list = frappe.db.get_list("Pathshala", filters={'pathshala_reg_no': reg_no}, fields=["pathshala_reg_no", "address_line_1", "address_line_2", "address_line_3", "city", "taluka", "pincode", "district", "state", "mobile_no", "sanchalak_name", "registration_date"])
	student = frappe.db.sql(f"SELECT COUNT(name) AS student FROM `tabStudent` where select_pathshala = '{reg_no}'")
	context.total_students = list(student[0])[0]
	teachers = frappe.db.sql(f"select instructor_name from `tabInstructor` where pathshala='{reg_no}'")
	for teacher in teachers:
		for t in teacher:
			teacher_list.append(t)
	context.teacher_list = teacher_list
	# teacher_list.clear()
	