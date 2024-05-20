from odoo import _, models, fields, api


class WorkOrder(models.Model):
    _name = 'car_workshop.work_order'
    _description = 'Work Order'

    order_number = fields.Char('Order Number',
                               default="",
                               readonly=True, Copy=False)
    customer_id = fields.Many2one(
        'res.partner', string='Customer', required=True)
    vehicle_id = fields.Many2one(
        'fleet.vehicle', string='Vehicle', required=True)
    start_date = fields.Datetime('Start Date', default=fields.Datetime.now)
    end_date = fields.Datetime('End Date')
    product_ids = fields.Many2many(
        'product.product', string='Products', domain="[('type', '=', 'product')]")
    state = fields.Selection([
        ('draft', 'Received'),
        ('in_progress', 'In Progress'),
        ('in_progress', 'Waiting for Parts'),
        ('done', 'Done'),
    ], string='Status', default='draft')
    description = fields.Text('Description')
    vehicle_image = fields.Binary('Vehicle Image')

    @api.model
    def create(self, vals):
        vals['order_number'] = self.env['ir.sequence'].next_by_code(
            'work_order_sequence_code')
        return super(WorkOrder, self).create(vals)
