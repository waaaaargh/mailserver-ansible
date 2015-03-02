from Defaults import *

MAILMAN_SITE_LIST = 'mailman'

DEFAULT_URL_PATTERN = 'http://%s/'
IMAGE_LOGOS         = '/images/mailman/'

DEFAULT_EMAIL_HOST = 'lists.{{ host_name }}'
DEFAULT_URL_HOST   = 'lists.{{ host_name }}'

add_virtualhost(DEFAULT_URL_HOST, DEFAULT_EMAIL_HOST)
{% for vdomain in mailman_domains %}
add_virtualhost('{{ vdomain }}', '{{ vdomain }}')
{% endfor %}

POSTFIX_STYLE_VIRTUAL_DOMAINS = [
  {% for vdomain in mailman_domains %}
  '{{ vdomain }}',
  {% endfor %}
  'lists.{{ host_name }}'
]

DEFAULT_SERVER_LANGUAGE = 'de'

USE_ENVELOPE_SENDER    = 0
DEFAULT_SEND_REMINDERS = 0
