def remove_tags(page):
    outcome = []
    start_tag = page.find('<')
    while (start_tag != -1):
        end_tag = page.find('>', start_tag)
        # print(start_tag, end_tag)
        outcome = outcome + page[:start_tag].strip().split()
        # print(page[:start_tag].strip().split(' '))
        page = page[end_tag + 1:]
        # print(page)
        start_tag = page.find('<')
    if len(page) != 0:
        outcome = outcome + page.strip().split(' ')
    return outcome


print(remove_tags("A <img src='here.img' alt='nothing'>picture,</a> a cat and a mouse! "))
print(remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
#>>> ['Hello','World!']

print(remove_tags("<hello><goodbye>"))
#>>> []

print(remove_tags("This is plain text."))