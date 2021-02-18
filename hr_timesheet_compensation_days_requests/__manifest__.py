{
    'name': "hr_timesheet_compensation_days_requests",
    'summary': """ Request compensation days based on timesheet """,
    'license': 'AGPL-3',
    'description': """
=======================================
hr_timesheet_compensation_days_requests
=======================================

This module allows
* the users to request compensation days based on the timesheet lines he registered
* the manager to list the requests and validate them

Installation
============

Just install hr_timesheet_compensation_days_requests, all dependencies will be installed by default.

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
    'category': 'Leaves',
    'version': '12.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'hr',
                'hr_timesheet',
                'hr_holidays',
            ],

    # always loaded
    'data': [
        'wizard/timesheet_compensation_days_request_view.xml',
        'views/hr_timesheet_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    
    'installable': True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    'auto_install': False,
    'application': False,
}