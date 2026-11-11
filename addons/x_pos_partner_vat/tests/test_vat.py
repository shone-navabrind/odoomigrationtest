import re

from odoo.tests.common import TransactionCase, tagged
from odoo.tools import file_open


@tagged('post_install', '-at_install')
class TestPosPartnerVat(TransactionCase):

    def test_vat_loaded_in_pos(self):
        config = self.env['pos.config'].search([], limit=1) or self.env['pos.config'].new({})
        self.assertIn('vat', self.env['res.partner']._load_pos_data_fields(config))

    def test_template_owl3_syntax(self):
        with file_open('x_pos_partner_vat/static/src/app/partner_line.xml') as f:
            content = f.read()
        self.assertIn('this.props.partner.vat', content)
        self.assertNotIn('t-esc', content)
        self.assertIsNone(re.search(r'(?<![.\w])props\.partner', content))
