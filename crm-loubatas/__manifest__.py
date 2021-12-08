{
    'name': "crm_loubatas",
    'summary': """ CRM customization for Loubatas """,
    'license': 'AGPL-3',
    'description': """
============
crm_loubatas
============

Installation
============

Just install crm_loubatas, all dependencies will be installed by default.

Known issues / Roadmap
======================

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/elabore-coop/loubatas-special-modules/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=de95b2e>`_.

Contributors
------------

* Stéphan SAINLEGER <https://github.com/stephansainleger>
* Elabore Teams

Funders
-------

The development of this module has been financially supported by:

* Elabore (https://elabore.coop)
* Loubatas (https://loubatas.org)

Maintainer
----------

This module is maintained by ELABORE.

This module is maintained by ELABORE.
Elabore is a cooperative corporation whose mission is to support the collaborative development of Odoo features and ecosystem for social and solidarity-based economy Organizations.

""",

    'author': "Elabore",
    'website': "https://elabore.coop",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'crm',
            ],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    
    'installable': True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    'auto_install': False,
    'application': False,
}