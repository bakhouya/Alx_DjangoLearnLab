# Permissions and Groups Setup

## Custom Permissions (defined in Book model)
- can_view: allow viewing books
- can_create: allow adding new books
- can_edit: allow editing existing books
- can_delete: allow deleting books

## Groups and their permissions
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Usage in views
Each view is protected using @permission_required decorator:
Example:
@permission_required('library.can_edit', raise_exception=True)
