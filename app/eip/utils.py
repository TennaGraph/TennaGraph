# Stdlib imports
import io

# App imports
from .models import EIP


def parse_eip_details(content):
    is_start_found = False
    is_finish_found = False
    eip_type = EIP.OTHER
    status = EIP.OTHER
    eip = category = title = authors = created = None

    # make iterable sting
    buff = io.StringIO(content)

    while buff.readable() and not is_finish_found:
        line = buff.readline()
        line_lower = line.lower()
        line = line.replace(' \n', '')
        line = line.replace('\n', '')

        if line == '' or not line:
            raise Exception("Not found variables but the end of the content was reached")

        if not is_start_found and '---' in line:
            is_start_found = True
            continue

        if is_start_found and '---' in line:
            is_finish_found = True


        if "eip: " in line_lower:
            eip = line.replace('eip: ', '')

        if "title: " in line_lower:
            title = line.replace('title: ', '')

        if "status: " in line_lower:
            if 'draft' in line_lower:
                status = EIP.DRAFT
            elif 'active' in line_lower:
                status = EIP.ACTIVE
            elif 'last call' in line_lower:
                status = EIP.LAST_CALL
            elif 'replaced' or 'superseded' in line_lower:
                status = EIP.REPLACED
            elif 'accepted' in line_lower:
                status = EIP.ACCEPTED
            elif 'final' in line_lower:
                status = EIP.FINAL
            elif 'deferred' in line_lower:
                status = EIP.DEFERRED

        if "type: " in line_lower:
            if 'standards track' in line_lower:
                eip_type = EIP.CORE
            elif 'informational' in line_lower:
                eip_type = EIP.INFORMATIONAL
            elif 'meta' in line_lower:
                eip_type = EIP.META

        if "category: " in line_lower:
            if 'core' in line:
                category = EIP.CORE
            elif 'networking' in line_lower:
                category = EIP.NETWORKING
            elif 'interface' in line_lower:
                category = EIP.INTERFACE
            elif 'erc' in line_lower:
                category = EIP.ERC

        if "author: " in line_lower:
            authors = line.replace('author: ', '')

        if "authors: " in line_lower:
            authors = line.replace('authors: ', '')

        if "created: " in line_lower:
            created = line.replace('created: ', '')

    return eip, title, status, eip_type, category, authors, created