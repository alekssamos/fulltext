from __future__ import absolute_import

import xlrd

from six import StringIO

from fulltext import BaseBackend


class Backend(BaseBackend):

    def handle_path(self, path):
        text = StringIO()
        wb = xlrd.open_workbook(path)
        for n in wb.sheet_names():
            ws = wb.sheet_by_name(n)
            for x in range(ws.nrows):
                for y in range(ws.ncols):
                    v = ws.cell_value(x, y)
                    if v:
                        if isinstance(v, (int, float)):
                            v = str(v)
                        text.write(v)
                        text.write(u' ')
                text.write(u'\n')
        return text.getvalue()
