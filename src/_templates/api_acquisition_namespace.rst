..
   This file is auto-generated.

{{ name_formatted }}
{{ underline }}

.. doxygennamespace:: {{ name }}
    :desc-only:

{% if enums -%}
Enums
-----

{{ enums }}
{% endif -%}

{% if classes -%}
Classes
-------

{{ classes }}
{% endif -%}

{% if structs -%}
Structs
-------

{{ structs }}
{% endif -%}
