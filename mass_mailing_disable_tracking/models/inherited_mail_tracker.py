# SPDX-FileCopyrightText: 2025 hugues de keyzer
#
# SPDX-License-Identifier: AGPL-3.0-or-later

from odoo import api, models

from .res_config_settings import TRACK_LINKS_PARAMETER


class InheritedMailTracker(models.Model):
    _inherit = "link.tracker"

    def convert_links(self, html, vals, blacklist=None):
        """Override the convert_links method to prevent links from being converted into tracked links."""
        if self.env["ir.config_parameter"].sudo().get_param(TRACK_LINKS_PARAMETER):
            return super().convert_links(html, vals, blacklist)
        return html
