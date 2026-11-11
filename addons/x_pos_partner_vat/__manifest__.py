{
    'name': 'POS Customer VAT in Customer List',
    'version': '20.0.1.0.0',
    'summary': "Show the customer's VAT number in the POS customer list screen",
    'category': 'Point of Sale',
    'author': 'Custom',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'x_pos_partner_vat/static/src/app/partner_line.xml',
        ],
    },
    'installable': True,
    'application': False,
}
