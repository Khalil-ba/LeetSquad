def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(emails = ['user.name+foo@hostname.com', 'user.name+bar@hostname.com', 'user.name@hostname.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+foo@hostname.com', 'user.name+bar@hostname.com', 'user.name@hostname.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['m.y+name@email.com', 'my.name@email.com', 'myname@email.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['m.y+name@email.com', 'my.name@email.com', 'myname@email.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['m.y+name@email.com', 'my@email.com', 'm+y.name@email.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['m.y+name@email.com', 'my@email.com', 'm+y.name@email.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['me+alex@leetcode.com', 'me@leetcode.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['me+alex@leetcode.com', 'me@leetcode.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['m.y+name@email.com', 'my@email.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['m.y+name@email.com', 'my@email.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['foo@bar.com', 'foo@bar.com', 'foo@bar.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['foo@bar.com', 'foo@bar.com', 'foo@bar.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['my.email@gmail.com', 'myemail+foo@gmail.com', 'my_email+bar@gmail.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['my.email@gmail.com', 'myemail+foo@gmail.com', 'my_email+bar@gmail.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a+b@leetcode.com', 'a@leetcode.com+b', 'a+b+c+d@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a+b@leetcode.com', 'a@leetcode.com+b', 'a+b+c+d@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['foo@gmail.com+foo', 'foo2@gmail.com+bar', 'foo3@gmail.com+baz']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['foo@gmail.com+foo', 'foo2@gmail.com+bar', 'foo3@gmail.com+baz']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['foo@bar.com', 'foo.bar@bar.com', 'foo.bar.baz@bar.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['foo@bar.com', 'foo.bar@bar.com', 'foo.bar.baz@bar.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe@example.com', 'john.doe+foo@example.com', 'johndoe@example.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe@example.com', 'john.doe+foo@example.com', 'johndoe@example.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice+bob.cathy@leetcode.com', 'alice.bob.cathy@leetcode.com', 'alicebobcathy@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice+bob.cathy@leetcode.com', 'alice.bob.cathy@leetcode.com', 'alicebobcathy@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com', 'al.icez@leetcode.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com', 'al.icez@leetcode.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['foo@bar.com', 'foo@bar.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['foo@bar.com', 'foo@bar.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alex@leetcode.com', 'alex+alex@leetcode.com', 'alex.alex@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alex@leetcode.com', 'alex+alex@leetcode.com', 'alex.alex@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+more@domain.co.uk', 'user.name+tag@domain.co.uk', 'user+tag@domain.co.uk', 'user@domain.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+more@domain.co.uk', 'user.name+tag@domain.co.uk', 'user+tag@domain.co.uk', 'user@domain.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['email+filter@domain.com', 'email@domain.com', 'email+filter+ignore@domain.com', 'email.filter@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['email+filter@domain.com', 'email@domain.com', 'email+filter+ignore@domain.com', 'email.filter@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag@domain.com', 'user.name.tag@domain.com', 'user.name@domain.com', 'user.name@sub.domain.com', 'user.name+tag@sub.domain.com', 'user.name.tag@sub.domain.com']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag@domain.com', 'user.name.tag@domain.com', 'user.name@domain.com', 'user.name@sub.domain.com', 'user.name+tag@sub.domain.com', 'user.name.tag@sub.domain.com']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+newsletter@domain.com', 'johndoe+offers@domain.com', 'johndoe@sub.domain.com', 'john.doe@domain.co.uk']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+newsletter@domain.com', 'johndoe+offers@domain.com', 'johndoe@sub.domain.com', 'john.doe@domain.co.uk']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag@domain.co', 'user.name@domain.co', 'user.name+tag+another.tag@domain.co']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag@domain.co', 'user.name@domain.co', 'user.name+tag+another.tag@domain.co']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+extra.info@company.org', 'john.doe@company.org', 'john.doe+extra+info@company.org', 'john.doe+extra+info+more@company.org']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+extra.info@company.org', 'john.doe@company.org', 'john.doe+extra+info@company.org', 'john.doe+extra+info+more@company.org']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice..bob.cathy@leetcode.com', 'alice+bob.cathy@leetcode.com', 'alice+bob..cathy@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice..bob.cathy@leetcode.com', 'alice+bob.cathy@leetcode.com', 'alice+bob..cathy@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+notes@leetcode.com', 'john.doe+notes1@leetcode.com', 'johndoe+notes@leetcode.com', 'john.doe@leetcode.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+notes@leetcode.com', 'john.doe+notes1@leetcode.com', 'johndoe+notes@leetcode.com', 'john.doe@leetcode.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a+b+c+d@domain.com', 'a.b.c.d@domain.com', 'abcd@domain.com', 'a..b.c+d.@domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a+b+c+d@domain.com', 'a.b.c.d@domain.com', 'abcd@domain.com', 'a..b.c+d.@domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+sorting@example.com', 'user.name@example.com', 'user.name+sorting@example.com', 'user+name@example.com', 'user+name+tag@example.com', 'user+name+tag+sorting@example.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+sorting@example.com', 'user.name@example.com', 'user.name+sorting@example.com', 'user+name@example.com', 'user+name+tag@example.com', 'user+name+tag+sorting@example.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+some.text@domain.com', 'johndoe+some.text@domain.com', 'johndoe@domain.com', 'john.doe@domain.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+some.text@domain.com', 'johndoe+some.text@domain.com', 'johndoe@domain.com', 'john.doe@domain.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['multiple+dots.here+ignore@sample.com', 'multiple+dots.here@sample.com', 'multiple.dots+here@sample.com', 'multiple.dots.here@sample.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['multiple+dots.here+ignore@sample.com', 'multiple+dots.here@sample.com', 'multiple.dots+here@sample.com', 'multiple.dots.here@sample.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+foo@domain.com', 'user+name@domain.com', 'user.name+foo.bar@domain.com', 'user+name+foo@domain.com', 'user.name+bar.foo@domain.com', 'user+bar.foo@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+foo@domain.com', 'user+name@domain.com', 'user.name+foo.bar@domain.com', 'user+name+foo@domain.com', 'user.name+bar.foo@domain.com', 'user+bar.foo@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['multiple+parts+in+the+local@name.com', 'multiple.parts.in.the.local@name.com', 'multiple+parts+in.the+local@name.com', 'multiple.parts+in+the.local@name.com', 'multiplepartsinthe.local@name.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['multiple+parts+in+the+local@name.com', 'multiple.parts.in.the.local@name.com', 'multiple+parts+in.the+local@name.com', 'multiple.parts+in+the.local@name.com', 'multiplepartsinthe.local@name.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com', 'my.email+alex@leetcode.co.uk', 'my.e.mail+alex@leetcode.co.uk', 'myemail+alex@leetcode.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com', 'my.email+alex@leetcode.co.uk', 'my.e.mail+alex@leetcode.co.uk', 'myemail+alex@leetcode.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a.b.c.d+e@website.com', 'abcd@website.com', 'a.b.c.d@website.com', 'abc.d+efg@website.com', 'a.b.c.d+efg@website.com', 'a.b.c+defg@website.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a.b.c.d+e@website.com', 'abcd@website.com', 'a.b.c.d@website.com', 'abc.d+efg@website.com', 'a.b.c.d+efg@website.com', 'a.b.c+defg@website.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com', 'al.i.c.e+blog@leetcode.com', 'alic.e@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com', 'al.i.c.e+blog@leetcode.com', 'alic.e@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user@my+invalid+input.com', 'user.myinvalid+input@com', 'user.my+invalid@input.com', 'user@myinvalidinput+com']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user@my+invalid+input.com', 'user.myinvalid+input@com', 'user.my+invalid@input.com', 'user@myinvalidinput+com']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['email.name+suffix@sub.domain.com', 'email+suffix@sub.domain.com', 'email.name@sub.domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['email.name+suffix@sub.domain.com', 'email+suffix@sub.domain.com', 'email.name@sub.domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag1+tag2@domain.com', 'user.name+tag1.tag2@domain.com', 'user+name+tag1.tag2@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag1+tag2@domain.com', 'user.name+tag1.tag2@domain.com', 'user+name+tag1.tag2@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['example.email+alex@leetcode.com', 'e.x.a.m.p.l.e.e.mail+bob.cathy@leetcode.com', 'ex.ampleemail+david@lee.tcode.com', 'ex.ample.email+david@lee.tcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['example.email+alex@leetcode.com', 'e.x.a.m.p.l.e.e.mail+bob.cathy@leetcode.com', 'ex.ampleemail+david@lee.tcode.com', 'ex.ample.email+david@lee.tcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice+bob.cathy@leetcode.com', 'alice.bob.cathy@leetcode.com', 'alice.bob+cathy@leetcode.com', 'alice+bob+cathy@leetcode.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice+bob.cathy@leetcode.com', 'alice.bob.cathy@leetcode.com', 'alice.bob+cathy@leetcode.com', 'alice+bob+cathy@leetcode.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['name@domain.com', 'name@sub.domain.com', 'name+suffix@sub.domain.com', 'name.suffix@domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['name@domain.com', 'name@sub.domain.com', 'name+suffix@sub.domain.com', 'name.suffix@domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name@domain.com', 'user.name+everything_after@domain.com', 'user.name.+everything_after@domain.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name@domain.com', 'user.name+everything_after@domain.com', 'user.name.+everything_after@domain.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com', 'my.email+alex@leetcode.co.uk', 'my.e.mail+alex@sub.leetcode.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com', 'my.email+alex@leetcode.co.uk', 'my.e.mail+alex@sub.leetcode.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['peter.parker+spiderman@marvel.com', 'peter.parker+spiderman+amazing@marvel.com', 'peter+spiderman@marvel.com', 'spiderman+@marvel.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['peter.parker+spiderman@marvel.com', 'peter.parker+spiderman+amazing@marvel.com', 'peter+spiderman@marvel.com', 'spiderman+@marvel.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['complex+part.with.dots@complex.com', 'complex.partwithdots@complex.com', 'complexpart+with.dots@complex.com', 'complexpartwithdots@complex.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['complex+part.with.dots@complex.com', 'complex.partwithdots@complex.com', 'complexpart+with.dots@complex.com', 'complexpartwithdots@complex.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['jane.doe+newsletter@example.com', 'jane.doe@example.com', 'janedoe@example.com', 'jane.doe.+ignore@example.com', 'jane.doe+ignore@example.co.uk', 'jane+doe@example.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['jane.doe+newsletter@example.com', 'jane.doe@example.com', 'janedoe@example.com', 'jane.doe.+ignore@example.com', 'jane.doe+ignore@example.co.uk', 'jane+doe@example.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['long.email.name+with.many.dots.and.tags@longdomain.com', 'long.email+name+with.many.dots.and.tags@longdomain.com', 'longemail+name+with.many.dots.and.tags@longdomain.com', 'longemailname+with.many.dots.and.tags@longdomain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['long.email.name+with.many.dots.and.tags@longdomain.com', 'long.email+name+with.many.dots.and.tags@longdomain.com', 'longemail+name+with.many.dots.and.tags@longdomain.com', 'longemailname+with.many.dots.and.tags@longdomain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['tom+tommy+tomm@mydomain.com', 'tommy.tom+tom@mydomain.com', 'tom.tommy.tom+tommy@mydomain.com', 'tommy+tom+tommy@mydomain.com', 'tom.tommy@mydomain.com']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['tom+tommy+tomm@mydomain.com', 'tommy.tom+tom@mydomain.com', 'tom.tommy.tom+tommy@mydomain.com', 'tommy+tom+tommy@mydomain.com', 'tom.tommy@mydomain.com']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user+ignore@domain.com', 'user+ignore@sub.domain.com', 'user+ignore@subdomain.com', 'user@domain.com', 'user@sub.domain.com', 'user@subdomain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user+ignore@domain.com', 'user+ignore@sub.domain.com', 'user+ignore@subdomain.com', 'user@domain.com', 'user@sub.domain.com', 'user@subdomain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name@sub.domain.com', 'user.name+ignore@sub.domain.com', 'user.name@sub.domain.org', 'user.name+ignore@sub.domain.org']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name@sub.domain.com', 'user.name+ignore@sub.domain.com', 'user.name@sub.domain.org', 'user.name+ignore@sub.domain.org']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user@sub.domain.com', 'user@subdomain.com', 'user.sub@domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user@sub.domain.com', 'user@subdomain.com', 'user.sub@domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['first.last+tag1+tag2@service.com', 'firstlast+tag1tag2@service.com', 'first.last@service.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['first.last+tag1+tag2@service.com', 'firstlast+tag1tag2@service.com', 'first.last@service.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a.b.c+d.e.f+g.h.i@website.com', 'a.b.c.d.e.f.g.h.i@website.com', 'a+b+c+d+e+f+g+h+i@website.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a.b.c+d.e.f+g.h.i@website.com', 'a.b.c.d.e.f.g.h.i@website.com', 'a+b+c+d+e+f+g+h+i@website.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['abc.d.+def@example.com', 'abc.d+def@example.com', 'abc.def@example.com', 'abc.d.@example.com', 'abc.d+@example.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['abc.d.+def@example.com', 'abc.d+def@example.com', 'abc.def@example.com', 'abc.d.@example.com', 'abc.d+@example.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user+ignore.all.this@mydomain.net', 'user@mydomain.net', 'user.name+ignore@mydomain.net', 'user.name@mydomain.net']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user+ignore.all.this@mydomain.net', 'user@mydomain.net', 'user.name+ignore@mydomain.net', 'user.name@mydomain.net']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a.b.c.d.e@domain.com', 'a+b+c+d+e@domain.com', 'abcde@domain.com', 'a.b+c.d+e@domain.com', 'a+b.c.d.e@domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a.b.c.d.e@domain.com', 'a+b+c+d+e@domain.com', 'abcde@domain.com', 'a.b+c.d+e@domain.com', 'a+b.c.d.e@domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user@sub.domain.com', 'user@sub.sub.domain.com', 'user.sub@sub.domain.com', 'user@sub.domain.co', 'user@sub.domain.co.uk']) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user@sub.domain.com', 'user@sub.sub.domain.com', 'user.sub@sub.domain.com', 'user@sub.domain.co', 'user@sub.domain.co.uk']) == 5: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+ignore@domain.com', 'user.name+tag_ignore@domain.com', 'user.name+tag_ignore@domain.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+ignore@domain.com', 'user.name+tag_ignore@domain.com', 'user.name+tag_ignore@domain.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+foo@sub.domain.com', 'user.name@sub.domain.com', 'user+name@sub.domain.com', 'user@sub.domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+foo@sub.domain.com', 'user.name@sub.domain.com', 'user+name@sub.domain.com', 'user@sub.domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+foo@domain.com', 'user+name@domain.com', 'user.name+foo.bar@domain.com', 'user+name+foo@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+foo@domain.com', 'user+name@domain.com', 'user.name+foo.bar@domain.com', 'user+name+foo@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+info@domain.com', 'user.name+tag@domain.com', 'user.name@domain.com', 'user+name@domain.com', 'username@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+info@domain.com', 'user.name+tag@domain.com', 'user.name@domain.com', 'user+name@domain.com', 'username@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['x+y.z+@example.com', 'x.y.z.@example.com', 'x.y.z@example.com', 'x+y+z@example.com', 'x.y.z+tag@example.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['x+y.z+@example.com', 'x.y.z.@example.com', 'x.y.z@example.com', 'x+y+z@example.com', 'x.y.z+tag@example.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['first.last+alias1@domain.org', 'first.last+alias2@domain.org', 'first.last+alias1@another.org', 'first.last@another.org']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['first.last+alias1@domain.org', 'first.last+alias2@domain.org', 'first.last+alias1@another.org', 'first.last@another.org']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+sorting@example.com', 'user.name@example.com', 'user.name+sorting@example.com', 'user+name@example.com', 'user+name+tag@example.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+sorting@example.com', 'user.name@example.com', 'user.name+sorting@example.com', 'user+name@example.com', 'user+name+tag@example.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['nested+dot.and.plus@sub.sub.domain.com', 'nested.dot.and.plus@sub.sub.domain.com', 'nested+dot.and+plus@subdomain.com', 'nested.dot.and.plus@subdomain.com']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['nested+dot.and.plus@sub.sub.domain.com', 'nested.dot.and.plus@sub.sub.domain.com', 'nested+dot.and+plus@subdomain.com', 'nested.dot.and.plus@subdomain.com']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice+bob.cathy+david@leetcode.com', 'alice.david+bob.cathy@leetcode.com', 'alice+david@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice+bob.cathy+david@leetcode.com', 'alice.david+bob.cathy@leetcode.com', 'alice+david@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+more@sub.domain.com', 'user.name+tag@sub.domain.com', 'user+tag@sub.domain.com', 'user@sub.domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+more@sub.domain.com', 'user.name+tag@sub.domain.com', 'user+tag@sub.domain.com', 'user@sub.domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user@domain.com', 'user+tag@domain.com', 'user+tag+ignore@domain.com', 'user+tag@domain.co.uk', 'user+tag@sub.domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user@domain.com', 'user+tag@domain.com', 'user+tag+ignore@domain.com', 'user+tag@domain.co.uk', 'user+tag@sub.domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['nested+dot.dot.dot@domain.org', 'nested.dot+dot.dot@domain.org', 'nested.dot.dot+dot@domain.org', 'nesteddot.dotdot@domain.org', 'nesteddotdotdot@domain.org']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['nested+dot.dot.dot@domain.org', 'nested.dot+dot.dot@domain.org', 'nested.dot.dot+dot@domain.org', 'nesteddot.dotdot@domain.org', 'nesteddotdotdot@domain.org']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+newsletter@tech.com', 'johndoe+news+letter@tech.com', 'john+doe+news@tech.com', 'johndoe@tech.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+newsletter@tech.com', 'johndoe+news+letter@tech.com', 'john+doe+news@tech.com', 'johndoe@tech.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['contact+info@info.contact.org', 'contact.info@info.contact.org', 'contact.info+more@info.contact.org', 'contact+info+more@info.contact.org']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['contact+info@info.contact.org', 'contact.info@info.contact.org', 'contact.info+more@info.contact.org', 'contact+info+more@info.contact.org']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+ignore.this.part@domain.co.uk', 'user.name@domain.co.uk', 'user+name@domain.co.uk', 'user@domain.co.uk', 'user.name+another.part@domain.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+ignore.this.part@domain.co.uk', 'user.name@domain.co.uk', 'user+name@domain.co.uk', 'user@domain.co.uk', 'user.name+another.part@domain.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag@domain.co.uk', 'user.name@domain.co.uk', 'user+name@domain.co.uk', 'user.name+@domain.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag@domain.co.uk', 'user.name@domain.co.uk', 'user+name@domain.co.uk', 'user.name+@domain.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+newsletter@tech.com', 'johndoe+news+letter@tech.com', 'john+doe+news@tech.com', 'johndoe@tech.com', 'johndoe+ignore@tech.com', 'john.doe+ignore@tech.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+newsletter@tech.com', 'johndoe+news+letter@tech.com', 'john+doe+news@tech.com', 'johndoe@tech.com', 'johndoe+ignore@tech.com', 'john.doe+ignore@tech.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['email.with+plus.and.dots@website.com', 'emailwith+plusanddots@website.com', 'emailwithplus.anddots@website.com', 'emailwithplusanddots@website.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['email.with+plus.and.dots@website.com', 'emailwith+plusanddots@website.com', 'emailwithplus.anddots@website.com', 'emailwithplusanddots@website.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a.b.c+d@domain.com', 'a.b.c+e+f@domain.com', 'a+b+c+d@domain.com', 'a.b.c.d@domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a.b.c+d@domain.com', 'a.b.c+e+f@domain.com', 'a+b+c+d@domain.com', 'a.b.c.d@domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user+name+with+many+pluses@mydomain.com', 'user+name.with+many+pluses@mydomain.com', 'user.name+with+many+pluses@mydomain.com', 'user.name.with+many+pluses@mydomain.com', 'user.name.with.many+pluses@mydomain.com']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user+name+with+many+pluses@mydomain.com', 'user+name.with+many+pluses@mydomain.com', 'user.name+with+many+pluses@mydomain.com', 'user.name.with+many+pluses@mydomain.com', 'user.name.with.many+pluses@mydomain.com']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+department=mailing@company.com', 'jane.doe+department=hr@company.com', 'johndoe@company.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+department=mailing@company.com', 'jane.doe+department=hr@company.com', 'johndoe@company.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a.b.c+d.e.f@domain.com', 'a.b.c.d.e.f@domain.com', 'a+b.c+d.e.f@domain.com', 'a+b.c.d.e.f@domain.com', 'a.b+c.d.e+f@domain.com']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a.b.c+d.e.f@domain.com', 'a.b.c.d.e.f@domain.com', 'a+b.c+d.e.f@domain.com', 'a+b.c.d.e.f@domain.com', 'a.b+c.d.e+f@domain.com']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com', 'test.email+david@lee.tcode.com', 'testemail+david+extra@lee.tcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com', 'test.email+david@lee.tcode.com', 'testemail+david+extra@lee.tcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a+@domain.com', 'a@domain.com', 'a+very+long+part+here@domain.com', 'a.very.long.part.here@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a+@domain.com', 'a@domain.com', 'a+very+long+part+here@domain.com', 'a.very.long.part.here@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z@domain.com', 'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z@domain.com', 'abcdefghijklmnopqrstuvwxyz@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z@domain.com', 'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z@domain.com', 'abcdefghijklmnopqrstuvwxyz@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['x.y.z+12345@service.net', 'x.y.z@service.net', 'x.y.z+67890@service.net']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['x.y.z+12345@service.net', 'x.y.z@service.net', 'x.y.z+67890@service.net']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe@example.com', 'john.doe+newsletter@example.com', 'johndoe@example.com', 'john.doe.+ignore@example.com', 'john.doe+ignore@example.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe@example.com', 'john.doe+newsletter@example.com', 'johndoe@example.com', 'john.doe.+ignore@example.com', 'john.doe+ignore@example.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user+filter+ignore@site.com', 'user@site.com', 'user.filter@site.com', 'user+filter@site.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user+filter+ignore@site.com', 'user@site.com', 'user.filter@site.com', 'user+filter@site.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['peter.parker+spiderman@marvel.com', 'peter.parker+spiderman+amazing@marvel.com', 'peter+spiderman@marvel.com', 'spiderman+@marvel.com', 'peter.parker@marvel.com', 'peter+spiderman+@marvel.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['peter.parker+spiderman@marvel.com', 'peter.parker+spiderman+amazing@marvel.com', 'peter+spiderman@marvel.com', 'spiderman+@marvel.com', 'peter.parker@marvel.com', 'peter+spiderman+@marvel.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice+bob+cathy@domain.com', 'alice+bob.cathy@domain.com', 'alice+bob.cathy@domain.co.uk']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice+bob+cathy@domain.com', 'alice+bob.cathy@domain.com', 'alice+bob.cathy@domain.co.uk']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['first.last+middle.name@company.com', 'first.last@company.com', 'first+last@company.com', 'firstlast@company.com', 'first+last+middle@company.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['first.last+middle.name@company.com', 'first.last@company.com', 'first+last@company.com', 'firstlast@company.com', 'first+last+middle@company.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['same.name+tag@same.domain.com', 'same.name+another.tag@same.domain.com', 'same.name@same.domain.com', 'same.name+tag@different.domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['same.name+tag@same.domain.com', 'same.name+another.tag@same.domain.com', 'same.name@same.domain.com', 'same.name+tag@different.domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag.info@domain.com', 'user.name+taginfo@domain.com', 'user.name+tag+info@domain.co', 'user.name+taginfo@domain.co.uk', 'user.name@domain.com']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag.info@domain.com', 'user.name+taginfo@domain.com', 'user.name+tag+info@domain.co', 'user.name+taginfo@domain.co.uk', 'user.name@domain.com']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice.z+ignore@leetcode.com', 'alicez+ignore@leetcode.com', 'alice+ignore@leetcode.com', 'alice.z@leetcode.com', 'alicez@leetcode.com', 'alice@leetcode.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice.z+ignore@leetcode.com', 'alicez+ignore@leetcode.com', 'alice+ignore@leetcode.com', 'alice.z@leetcode.com', 'alicez@leetcode.com', 'alice@leetcode.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice.bob.john+foo@mydomain.com', 'alice.bob.john@mydomain.com', 'alice.bob.john+bar@mydomain.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice.bob.john+foo@mydomain.com', 'alice.bob.john@mydomain.com', 'alice.bob.john+bar@mydomain.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag1+tag2@domain.com', 'user.name.tag1+tag2@domain.com', 'user.name+tag1.tag2@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag1+tag2@domain.com', 'user.name.tag1+tag2@domain.com', 'user.name+tag1.tag2@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['example+ignore.this@domain.net', 'example.ignore.this@domain.net', 'example+ignore+this@domain.net', 'exampleignorethis@domain.net']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['example+ignore.this@domain.net', 'example.ignore.this@domain.net', 'example+ignore+this@domain.net', 'exampleignorethis@domain.net']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['a.b.c.d+e@website.com', 'abcd@website.com', 'a.b.c.d@website.com', 'abc.d+efg@website.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['a.b.c.d+e@website.com', 'abcd@website.com', 'a.b.c.d@website.com', 'abc.d+efg@website.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['alice.bob+c@site.org', 'alice+offers@site.org', 'alice.bob@site.org', 'alice.b+o+b@site.org']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['alice.bob+c@site.org', 'alice+offers@site.org', 'alice.bob@site.org', 'alice.b+o+b@site.org']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['complex.email+with+plus@longdomain.com', 'complex.email+with.plus@longdomain.com', 'complex.email@longdomain.com', 'complex+email@longdomain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['complex.email+with+plus@longdomain.com', 'complex.email+with.plus@longdomain.com', 'complex.email@longdomain.com', 'complex+email@longdomain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['john.doe+department=sales+division=west@company.com', 'john.doe+department=hr+division=east@company.com', 'john.doe@company.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['john.doe+department=sales+division=west@company.com', 'john.doe+department=hr+division=east@company.com', 'john.doe@company.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user+ignore+ignore@domain.com', 'user.name+ignore+ignore@domain.com', 'user.name+ignore.ignore@domain.com', 'user.name+ignore.ignore+ignore@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user+ignore+ignore@domain.com', 'user.name+ignore+ignore@domain.com', 'user.name+ignore.ignore@domain.com', 'user.name+ignore.ignore+ignore@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag1@domain.com', 'user.name+tag2@domain.com', 'user.name+tag1.tag2@domain.com', 'user.name+tag2.tag1@domain.com']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag1@domain.com', 'user.name+tag2@domain.com', 'user.name+tag1.tag2@domain.com', 'user.name+tag2.tag1@domain.com']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user.name+tag+more@domain.com', 'user.name+tag@domain.com', 'user+tag@domain.com', 'user@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user.name+tag+more@domain.com', 'user.name+tag@domain.com', 'user+tag@domain.com', 'user@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['x+user.name+y@domain.com', 'user.name+z@domain.com', 'user.name+@domain.com', 'user.name@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['x+user.name+y@domain.com', 'user.name+z@domain.com', 'user.name+@domain.com', 'user.name@domain.com']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(emails = ['user+tag@domain.com', 'user@domain.com', 'user.name@domain.com', 'user+tag.name@domain.com']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(emails = ['user+tag@domain.com', 'user@domain.com', 'user.name@domain.com', 'user+tag.name@domain.com']) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(emails = ['user.name+foo@hostname.com', 'user.name+bar@hostname.com', 'user.name@hostname.com']) == 1
    assert candidate(emails = ['m.y+name@email.com', 'my.name@email.com', 'myname@email.com']) == 2
    assert candidate(emails = ['m.y+name@email.com', 'my@email.com', 'm+y.name@email.com']) == 2
    assert candidate(emails = ['me+alex@leetcode.com', 'me@leetcode.com']) == 1
    assert candidate(emails = ['m.y+name@email.com', 'my@email.com']) == 1
    assert candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com']) == 1
    assert candidate(emails = ['foo@bar.com', 'foo@bar.com', 'foo@bar.com']) == 1
    assert candidate(emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']) == 2
    assert candidate(emails = ['my.email@gmail.com', 'myemail+foo@gmail.com', 'my_email+bar@gmail.com']) == 2
    assert candidate(emails = ['a+b@leetcode.com', 'a@leetcode.com+b', 'a+b+c+d@leetcode.com']) == 2
    assert candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com']) == 1
    assert candidate(emails = ['foo@gmail.com+foo', 'foo2@gmail.com+bar', 'foo3@gmail.com+baz']) == 3
    assert candidate(emails = ['foo@bar.com', 'foo.bar@bar.com', 'foo.bar.baz@bar.com']) == 3
    assert candidate(emails = ['john.doe@example.com', 'john.doe+foo@example.com', 'johndoe@example.com']) == 1
    assert candidate(emails = ['alice+bob.cathy@leetcode.com', 'alice.bob.cathy@leetcode.com', 'alicebobcathy@leetcode.com']) == 2
    assert candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com', 'al.icez@leetcode.com']) == 1
    assert candidate(emails = ['foo@bar.com', 'foo@bar.com']) == 1
    assert candidate(emails = ['alex@leetcode.com', 'alex+alex@leetcode.com', 'alex.alex@leetcode.com']) == 2
    assert candidate(emails = ['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com']) == 3
    assert candidate(emails = ['user.name+tag+more@domain.co.uk', 'user.name+tag@domain.co.uk', 'user+tag@domain.co.uk', 'user@domain.co.uk']) == 2
    assert candidate(emails = ['email+filter@domain.com', 'email@domain.com', 'email+filter+ignore@domain.com', 'email.filter@domain.com']) == 2
    assert candidate(emails = ['user.name+tag@domain.com', 'user.name.tag@domain.com', 'user.name@domain.com', 'user.name@sub.domain.com', 'user.name+tag@sub.domain.com', 'user.name.tag@sub.domain.com']) == 4
    assert candidate(emails = ['john.doe+newsletter@domain.com', 'johndoe+offers@domain.com', 'johndoe@sub.domain.com', 'john.doe@domain.co.uk']) == 3
    assert candidate(emails = ['user.name+tag@domain.co', 'user.name@domain.co', 'user.name+tag+another.tag@domain.co']) == 1
    assert candidate(emails = ['john.doe+extra.info@company.org', 'john.doe@company.org', 'john.doe+extra+info@company.org', 'john.doe+extra+info+more@company.org']) == 1
    assert candidate(emails = ['alice..bob.cathy@leetcode.com', 'alice+bob.cathy@leetcode.com', 'alice+bob..cathy@leetcode.com']) == 2
    assert candidate(emails = ['john.doe+notes@leetcode.com', 'john.doe+notes1@leetcode.com', 'johndoe+notes@leetcode.com', 'john.doe@leetcode.com']) == 1
    assert candidate(emails = ['a+b+c+d@domain.com', 'a.b.c.d@domain.com', 'abcd@domain.com', 'a..b.c+d.@domain.com']) == 3
    assert candidate(emails = ['user.name+tag+sorting@example.com', 'user.name@example.com', 'user.name+sorting@example.com', 'user+name@example.com', 'user+name+tag@example.com', 'user+name+tag+sorting@example.com']) == 2
    assert candidate(emails = ['john.doe+some.text@domain.com', 'johndoe+some.text@domain.com', 'johndoe@domain.com', 'john.doe@domain.com']) == 1
    assert candidate(emails = ['multiple+dots.here+ignore@sample.com', 'multiple+dots.here@sample.com', 'multiple.dots+here@sample.com', 'multiple.dots.here@sample.com']) == 3
    assert candidate(emails = ['user.name+foo@domain.com', 'user+name@domain.com', 'user.name+foo.bar@domain.com', 'user+name+foo@domain.com', 'user.name+bar.foo@domain.com', 'user+bar.foo@domain.com']) == 2
    assert candidate(emails = ['multiple+parts+in+the+local@name.com', 'multiple.parts.in.the.local@name.com', 'multiple+parts+in.the+local@name.com', 'multiple.parts+in+the.local@name.com', 'multiplepartsinthe.local@name.com']) == 3
    assert candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com', 'my.email+alex@leetcode.co.uk', 'my.e.mail+alex@leetcode.co.uk', 'myemail+alex@leetcode.co.uk']) == 2
    assert candidate(emails = ['a.b.c.d+e@website.com', 'abcd@website.com', 'a.b.c.d@website.com', 'abc.d+efg@website.com', 'a.b.c.d+efg@website.com', 'a.b.c+defg@website.com']) == 2
    assert candidate(emails = ['alice.z@leetcode.com', 'alicez@leetcode.com', 'al.i.c.e+blog@leetcode.com', 'alic.e@leetcode.com']) == 2
    assert candidate(emails = ['user@my+invalid+input.com', 'user.myinvalid+input@com', 'user.my+invalid@input.com', 'user@myinvalidinput+com']) == 4
    assert candidate(emails = ['email.name+suffix@sub.domain.com', 'email+suffix@sub.domain.com', 'email.name@sub.domain.com']) == 2
    assert candidate(emails = ['user.name+tag1+tag2@domain.com', 'user.name+tag1.tag2@domain.com', 'user+name+tag1.tag2@domain.com']) == 2
    assert candidate(emails = ['example.email+alex@leetcode.com', 'e.x.a.m.p.l.e.e.mail+bob.cathy@leetcode.com', 'ex.ampleemail+david@lee.tcode.com', 'ex.ample.email+david@lee.tcode.com']) == 2
    assert candidate(emails = ['alice+bob.cathy@leetcode.com', 'alice.bob.cathy@leetcode.com', 'alice.bob+cathy@leetcode.com', 'alice+bob+cathy@leetcode.com']) == 3
    assert candidate(emails = ['name@domain.com', 'name@sub.domain.com', 'name+suffix@sub.domain.com', 'name.suffix@domain.com']) == 3
    assert candidate(emails = ['user.name@domain.com', 'user.name+everything_after@domain.com', 'user.name.+everything_after@domain.com']) == 1
    assert candidate(emails = ['my.email+alex@leetcode.com', 'my.e.mail+alex@leetcode.com', 'myemail+alex@leetcode.com', 'my.email+alex@leetcode.co.uk', 'my.e.mail+alex@sub.leetcode.com']) == 3
    assert candidate(emails = ['peter.parker+spiderman@marvel.com', 'peter.parker+spiderman+amazing@marvel.com', 'peter+spiderman@marvel.com', 'spiderman+@marvel.com']) == 3
    assert candidate(emails = ['complex+part.with.dots@complex.com', 'complex.partwithdots@complex.com', 'complexpart+with.dots@complex.com', 'complexpartwithdots@complex.com']) == 3
    assert candidate(emails = ['jane.doe+newsletter@example.com', 'jane.doe@example.com', 'janedoe@example.com', 'jane.doe.+ignore@example.com', 'jane.doe+ignore@example.co.uk', 'jane+doe@example.com']) == 3
    assert candidate(emails = ['long.email.name+with.many.dots.and.tags@longdomain.com', 'long.email+name+with.many.dots.and.tags@longdomain.com', 'longemail+name+with.many.dots.and.tags@longdomain.com', 'longemailname+with.many.dots.and.tags@longdomain.com']) == 2
    assert candidate(emails = ['tom+tommy+tomm@mydomain.com', 'tommy.tom+tom@mydomain.com', 'tom.tommy.tom+tommy@mydomain.com', 'tommy+tom+tommy@mydomain.com', 'tom.tommy@mydomain.com']) == 5
    assert candidate(emails = ['user+ignore@domain.com', 'user+ignore@sub.domain.com', 'user+ignore@subdomain.com', 'user@domain.com', 'user@sub.domain.com', 'user@subdomain.com']) == 3
    assert candidate(emails = ['user.name@sub.domain.com', 'user.name+ignore@sub.domain.com', 'user.name@sub.domain.org', 'user.name+ignore@sub.domain.org']) == 2
    assert candidate(emails = ['user@sub.domain.com', 'user@subdomain.com', 'user.sub@domain.com']) == 3
    assert candidate(emails = ['first.last+tag1+tag2@service.com', 'firstlast+tag1tag2@service.com', 'first.last@service.com']) == 1
    assert candidate(emails = ['a.b.c+d.e.f+g.h.i@website.com', 'a.b.c.d.e.f.g.h.i@website.com', 'a+b+c+d+e+f+g+h+i@website.com']) == 3
    assert candidate(emails = ['abc.d.+def@example.com', 'abc.d+def@example.com', 'abc.def@example.com', 'abc.d.@example.com', 'abc.d+@example.com']) == 2
    assert candidate(emails = ['user+ignore.all.this@mydomain.net', 'user@mydomain.net', 'user.name+ignore@mydomain.net', 'user.name@mydomain.net']) == 2
    assert candidate(emails = ['a.b.c.d.e@domain.com', 'a+b+c+d+e@domain.com', 'abcde@domain.com', 'a.b+c.d+e@domain.com', 'a+b.c.d.e@domain.com']) == 3
    assert candidate(emails = ['user@sub.domain.com', 'user@sub.sub.domain.com', 'user.sub@sub.domain.com', 'user@sub.domain.co', 'user@sub.domain.co.uk']) == 5
    assert candidate(emails = ['user.name+tag+ignore@domain.com', 'user.name+tag_ignore@domain.com', 'user.name+tag_ignore@domain.co.uk']) == 2
    assert candidate(emails = ['user.name+foo@sub.domain.com', 'user.name@sub.domain.com', 'user+name@sub.domain.com', 'user@sub.domain.com']) == 2
    assert candidate(emails = ['user.name+foo@domain.com', 'user+name@domain.com', 'user.name+foo.bar@domain.com', 'user+name+foo@domain.com']) == 2
    assert candidate(emails = ['user.name+tag+info@domain.com', 'user.name+tag@domain.com', 'user.name@domain.com', 'user+name@domain.com', 'username@domain.com']) == 2
    assert candidate(emails = ['x+y.z+@example.com', 'x.y.z.@example.com', 'x.y.z@example.com', 'x+y+z@example.com', 'x.y.z+tag@example.com']) == 2
    assert candidate(emails = ['first.last+alias1@domain.org', 'first.last+alias2@domain.org', 'first.last+alias1@another.org', 'first.last@another.org']) == 2
    assert candidate(emails = ['user.name+tag+sorting@example.com', 'user.name@example.com', 'user.name+sorting@example.com', 'user+name@example.com', 'user+name+tag@example.com']) == 2
    assert candidate(emails = ['nested+dot.and.plus@sub.sub.domain.com', 'nested.dot.and.plus@sub.sub.domain.com', 'nested+dot.and+plus@subdomain.com', 'nested.dot.and.plus@subdomain.com']) == 4
    assert candidate(emails = ['alice+bob.cathy+david@leetcode.com', 'alice.david+bob.cathy@leetcode.com', 'alice+david@leetcode.com']) == 2
    assert candidate(emails = ['user.name+tag+more@sub.domain.com', 'user.name+tag@sub.domain.com', 'user+tag@sub.domain.com', 'user@sub.domain.com']) == 2
    assert candidate(emails = ['user@domain.com', 'user+tag@domain.com', 'user+tag+ignore@domain.com', 'user+tag@domain.co.uk', 'user+tag@sub.domain.com']) == 3
    assert candidate(emails = ['nested+dot.dot.dot@domain.org', 'nested.dot+dot.dot@domain.org', 'nested.dot.dot+dot@domain.org', 'nesteddot.dotdot@domain.org', 'nesteddotdotdot@domain.org']) == 4
    assert candidate(emails = ['john.doe+newsletter@tech.com', 'johndoe+news+letter@tech.com', 'john+doe+news@tech.com', 'johndoe@tech.com']) == 2
    assert candidate(emails = ['contact+info@info.contact.org', 'contact.info@info.contact.org', 'contact.info+more@info.contact.org', 'contact+info+more@info.contact.org']) == 2
    assert candidate(emails = ['user.name+ignore.this.part@domain.co.uk', 'user.name@domain.co.uk', 'user+name@domain.co.uk', 'user@domain.co.uk', 'user.name+another.part@domain.co.uk']) == 2
    assert candidate(emails = ['user.name+tag@domain.co.uk', 'user.name@domain.co.uk', 'user+name@domain.co.uk', 'user.name+@domain.co.uk']) == 2
    assert candidate(emails = ['john.doe+newsletter@tech.com', 'johndoe+news+letter@tech.com', 'john+doe+news@tech.com', 'johndoe@tech.com', 'johndoe+ignore@tech.com', 'john.doe+ignore@tech.com']) == 2
    assert candidate(emails = ['email.with+plus.and.dots@website.com', 'emailwith+plusanddots@website.com', 'emailwithplus.anddots@website.com', 'emailwithplusanddots@website.com']) == 2
    assert candidate(emails = ['a.b.c+d@domain.com', 'a.b.c+e+f@domain.com', 'a+b+c+d@domain.com', 'a.b.c.d@domain.com']) == 3
    assert candidate(emails = ['user+name+with+many+pluses@mydomain.com', 'user+name.with+many+pluses@mydomain.com', 'user.name+with+many+pluses@mydomain.com', 'user.name.with+many+pluses@mydomain.com', 'user.name.with.many+pluses@mydomain.com']) == 4
    assert candidate(emails = ['john.doe+department=mailing@company.com', 'jane.doe+department=hr@company.com', 'johndoe@company.com']) == 2
    assert candidate(emails = ['a.b.c+d.e.f@domain.com', 'a.b.c.d.e.f@domain.com', 'a+b.c+d.e.f@domain.com', 'a+b.c.d.e.f@domain.com', 'a.b+c.d.e+f@domain.com']) == 4
    assert candidate(emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com', 'test.email+david@lee.tcode.com', 'testemail+david+extra@lee.tcode.com']) == 2
    assert candidate(emails = ['a+@domain.com', 'a@domain.com', 'a+very+long+part+here@domain.com', 'a.very.long.part.here@domain.com']) == 2
    assert candidate(emails = ['a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z@domain.com', 'a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z@domain.com', 'abcdefghijklmnopqrstuvwxyz@domain.com']) == 2
    assert candidate(emails = ['x.y.z+12345@service.net', 'x.y.z@service.net', 'x.y.z+67890@service.net']) == 1
    assert candidate(emails = ['john.doe@example.com', 'john.doe+newsletter@example.com', 'johndoe@example.com', 'john.doe.+ignore@example.com', 'john.doe+ignore@example.co.uk']) == 2
    assert candidate(emails = ['user+filter+ignore@site.com', 'user@site.com', 'user.filter@site.com', 'user+filter@site.com']) == 2
    assert candidate(emails = ['peter.parker+spiderman@marvel.com', 'peter.parker+spiderman+amazing@marvel.com', 'peter+spiderman@marvel.com', 'spiderman+@marvel.com', 'peter.parker@marvel.com', 'peter+spiderman+@marvel.com']) == 3
    assert candidate(emails = ['alice+bob+cathy@domain.com', 'alice+bob.cathy@domain.com', 'alice+bob.cathy@domain.co.uk']) == 2
    assert candidate(emails = ['first.last+middle.name@company.com', 'first.last@company.com', 'first+last@company.com', 'firstlast@company.com', 'first+last+middle@company.com']) == 2
    assert candidate(emails = ['same.name+tag@same.domain.com', 'same.name+another.tag@same.domain.com', 'same.name@same.domain.com', 'same.name+tag@different.domain.com']) == 2
    assert candidate(emails = ['user.name+tag.info@domain.com', 'user.name+taginfo@domain.com', 'user.name+tag+info@domain.co', 'user.name+taginfo@domain.co.uk', 'user.name@domain.com']) == 3
    assert candidate(emails = ['alice.z+ignore@leetcode.com', 'alicez+ignore@leetcode.com', 'alice+ignore@leetcode.com', 'alice.z@leetcode.com', 'alicez@leetcode.com', 'alice@leetcode.com']) == 2
    assert candidate(emails = ['alice.bob.john+foo@mydomain.com', 'alice.bob.john@mydomain.com', 'alice.bob.john+bar@mydomain.com']) == 1
    assert candidate(emails = ['user.name+tag1+tag2@domain.com', 'user.name.tag1+tag2@domain.com', 'user.name+tag1.tag2@domain.com']) == 2
    assert candidate(emails = ['example+ignore.this@domain.net', 'example.ignore.this@domain.net', 'example+ignore+this@domain.net', 'exampleignorethis@domain.net']) == 2
    assert candidate(emails = ['a.b.c.d+e@website.com', 'abcd@website.com', 'a.b.c.d@website.com', 'abc.d+efg@website.com']) == 1
    assert candidate(emails = ['alice.bob+c@site.org', 'alice+offers@site.org', 'alice.bob@site.org', 'alice.b+o+b@site.org']) == 3
    assert candidate(emails = ['complex.email+with+plus@longdomain.com', 'complex.email+with.plus@longdomain.com', 'complex.email@longdomain.com', 'complex+email@longdomain.com']) == 2
    assert candidate(emails = ['john.doe+department=sales+division=west@company.com', 'john.doe+department=hr+division=east@company.com', 'john.doe@company.com']) == 1
    assert candidate(emails = ['user+ignore+ignore@domain.com', 'user.name+ignore+ignore@domain.com', 'user.name+ignore.ignore@domain.com', 'user.name+ignore.ignore+ignore@domain.com']) == 2
    assert candidate(emails = ['user.name+tag1@domain.com', 'user.name+tag2@domain.com', 'user.name+tag1.tag2@domain.com', 'user.name+tag2.tag1@domain.com']) == 1
    assert candidate(emails = ['user.name+tag+more@domain.com', 'user.name+tag@domain.com', 'user+tag@domain.com', 'user@domain.com']) == 2
    assert candidate(emails = ['x+user.name+y@domain.com', 'user.name+z@domain.com', 'user.name+@domain.com', 'user.name@domain.com']) == 2
    assert candidate(emails = ['user+tag@domain.com', 'user@domain.com', 'user.name@domain.com', 'user+tag.name@domain.com']) == 2


