# Security notes

- DEBUG = False in production (set env var DJANGO_DEBUG)
- SECRET_KEY must be set via DJANGO_SECRET_KEY env var
- Cookies: SESSION_COOKIE_SECURE = True, CSRF_COOKIE_SECURE = True
- CSP: configured via django-csp (see settings C﻿﻿SP_*)
- Use ModelForm for create/update; avoid raw SQL queries
- Test:
  - Submit form without CSRF token -> expect 403
  - Try XSS payload -> must be escaped
  - Check headers in browser devtools (CSP, X-Frame-Options, X-Content-Type-Options)
