# -*- coding: utf-8 -*-
from odps.udf import annotate


@annotate("string, string->string")
class array_filter(object):

    def evaluate(self, string, s):
        lst = string.split(',')
        lst1 = list()

        if len(lst) == 0:
            return string

        for index, item in enumerate(lst):

            if item == s:
                pass
                # lst.pop(index)
            else:
                lst1.append(item)

        return ','.join(lst1)


if __name__ == '__main__':
    array_filter = array_filter()
    # print(array_filter.evaluate(',1,2,,4,', ''))
    print(array_filter.evaluate(' , , , , ', ' '))
