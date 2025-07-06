from 2-lazy_pagination import lazy_paginate

for page in lazy_paginate(5):
    print("New Page:")
    for user in page:
        print(user)
