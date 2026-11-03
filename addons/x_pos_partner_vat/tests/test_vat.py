from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestPosPartnerVat(TransactionCase):

    def test_vat_loaded_in_pos(self):
        config = self.env['pos.config'].search([], limit=1) or self.env['pos.config'].new({})
        self.assertIn('vat', self.env['res.partner']._load_pos_data_fields(config))
