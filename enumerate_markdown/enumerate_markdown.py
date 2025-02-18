import re

from enumerate_markdown import enumerator
from enumerate_markdown import headers_finder


class EnumerationFormatter(object):
    ENUMERATION_FORMAT_PATTERN = re.compile("^ \\d+(\\.|(\\.\\d+)+) ")

    def format(self, full_index):
        if len(full_index) == 1:
            return ' ' + str(full_index[0]) + '.' + ' '

        return ' ' + '.'.join(map(str, full_index)) + ' '

    def old_enumeration_length(self, text):
        m = self.ENUMERATION_FORMAT_PATTERN.match(text)
        if m:
            return m.end() - m.start()
        else:
            return 0


def enumerate_headers(text, finder=headers_finder.HeadersFinder(), enumeration_formatter=EnumerationFormatter(),
                      minimal_level=1):
    e = enumerator.EnumeratorWithMinimalLevel(minimal_level)
    headers = finder.find_headers(text)
    prev_offset = 0
    res = ''
    for header in headers:
        if inside_code_block(text, header.offset()):
            continue
        assert header.offset() >= prev_offset
        header.advance_enumerator(e)
        stripped_text = lstrip_text(text[prev_offset: header.offset()])
        res += stripped_text + enumeration_formatter.format(e.get_index())
        length = enumeration_formatter.old_enumeration_length(text[header.offset():])
        prev_offset = header.offset() + length
    res += lstrip_text(text[prev_offset:])
    return res


def inside_code_block(text, offset):
    res = False
    current_offset = 0
    while True:
        if offset + 1 >= len(text):
            break
        if current_offset >= offset:
            break
        i = text.find("```", current_offset, offset)
        if i == -1:
            break
        else:
            res = not res
            current_offset = i + 1
    return res


def lstrip_text(text):
    return text.lstrip(' \t')
