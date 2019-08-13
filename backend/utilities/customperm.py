from rest_framework import permissions


METHOD_TO_OBJECT_PERM = {
	'GET': 'view',
	'POST': 'add',
	'PUT': 'change',
	'DELETE': 'delete',
}

def make_perm(app_name, class_name, perm_name):
	return '%s.%s_%s' % (app_name, perm_name, class_name.lower())



class Custom(permissions.BasePermission):

	def has_permission(self, request, view):
		print('Perm')
		return True

	def has_object_permission(self, request, view, obj):
		model = obj._meta.model.__name__
		app = obj._meta.app_label
		object_perm = METHOD_TO_OBJECT_PERM.get(request.method)
		perm = make_perm(app, model, object_perm)

		print(request.user.has_perm(perm, obj))

		if (request.user.has_perm(perm, obj)):
			return True
		return False