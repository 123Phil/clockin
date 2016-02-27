
def is_mobile(request):
	mobile = False
	UA_string = str(request.META["HTTP_USER_AGENT"]).lower()
	mobiles = ['mobile', 'iphone', 'android', 'fennec']
	if any(m in UA_string for m in mobiles):
		mobile = True
	return {"mobile": mobile}
