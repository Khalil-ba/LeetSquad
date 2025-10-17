def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d)e)") == "ebcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d)e)") == "ebcda": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c(d(e)f)g)") == "gdefcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c(d(e)f)g)") == "gdefcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abc)(def)") == "cbafed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abc)(def)") == "cbafed": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c(d)e(f)g)") == "gfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c(d)e(f)g)") == "gfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "(z)") == "z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(z)") == "z": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abcd)") == "dcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abcd)") == "dcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b)c(d(e)f)g") == "abcfedg"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b)c(d(e)f)g") == "abcfedg": {e}')
    
    total += 1
    try:
        result = candidate(s = "(ed(et(oc))el)") == "leetcode"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(ed(et(oc))el)") == "leetcode": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(abc)d(efg)h(ij(k(lm)n)op)q") == "xcbadgfehpokmlnjiq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(abc)d(efg)h(ij(k(lm)n)op)q") == "xcbadgfehpokmlnjiq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghij(klmnop(qrstuvwxyz))") == "abcdefghijqrstuvwxyzponmlk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghij(klmnop(qrstuvwxyz))") == "abcdefghijqrstuvwxyzponmlk": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc") == "abc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc") == "abc": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abc)d(efg)") == "cbadgfe"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abc)d(efg)") == "cbadgfe": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d)e(f(g)h)i") == "(adcbehgfi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d)e(f(g)h)i") == "(adcbehgfi": {e}')
    
    total += 1
    try:
        result = candidate(s = "()") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a)") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a)") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "(u(love)i)") == "iloveu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(u(love)i)") == "iloveu": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab(c(d(e(fg)h)i)j)k") == "abjdhfgeick"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab(c(d(e(fg)h)i)j)k") == "abjdhfgeick": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o") == "(anclejghifkdmbo"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o") == "(anclejghifkdmbo": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z(wvu)tsr)qpo)nm") == "xopqzuvwtsrynm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z(wvu)tsr)qpo)nm") == "xopqzuvwtsrynm": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d)e(f(g(h)i)j)k)l") == "kfihgjebcdal"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d)e(f(g(h)i)j)k)l") == "kfihgjebcdal": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(bc(def(ghi)jkl)mno(pqr(stu)vwx)y(z))") == "azypqrutsvwxonmdefihgjklcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(bc(def(ghi)jkl)mno(pqr(stu)vwx)y(z))") == "azypqrutsvwxonmdefihgjklcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g)h)i)j(k(l(m)n)o)p") == "a(bcdifghejolmnkp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g)h)i)j(k(l(m)n)o)p") == "a(bcdifghejolmnkp": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(bc(def(ghi(jkl(mno)pqr)stu)vwx(yz))") == "a(bcyzxwvghirqpmnolkjstufed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(bc(def(ghi(jkl(mno)pqr)stu)vwx(yz))") == "a(bcyzxwvghirqpmnolkjstufed": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m") == "alejghifkdcbm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m") == "alejghifkdcbm": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z))a(b(c)d)e(f(g(h)i)j)k") == "xzyadcbejghifk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z))a(b(c)d)e(f(g(h)i)j)k") == "xzyadcbejghifk": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z))w") == "xzyw"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z))w") == "xzyw": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))z(y(x(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "(a(b(c(d(e(fhjlnprtvxzywusqomkigz(y(x(w(v(usqomkigecabdfhjlnprt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))z(y(x(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "(a(b(c(d(e(fhjlnprtvxzywusqomkigz(y(x(w(v(usqomkigecabdfhjlnprt": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p)q)r)s)t)u)v)w)x)y)z))))") == "(a(bdfyhwjulsnqpormtkvixgzec"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p)q)r)s)t)u)v)w)x)y)z))))") == "(a(bdfyhwjulsnqpormtkvixgzec": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z)))))))))))))))))))))(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))") == "(a(b(c(d(egikmoqsuwyzxvtrpnljhf(a(b(c(d(e(fhjlnprtvxzywusqomkig"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z)))))))))))))))))))))(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))") == "(a(b(c(d(egikmoqsuwyzxvtrpnljhf(a(b(c(d(e(fhjlnprtvxzywusqomkig": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abc)(def)((ghi)(jkl))(mno)(pqr)((stu)(vwx))(yz)") == "cbafedjklghionmrqpvwxstuzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abc)(def)((ghi)(jkl))(mno)(pqr)((stu)(vwx))(yz)") == "cbafedjklghionmrqpvwxstuzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i))))))))") == "(acegihfdb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i))))))))") == "(acegihfdb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p)q)r)s)t)u)v)w)x)y)z))))z(y(x(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "(a(bdfyhwjulsnqpormtkvixgzecz(y(x(w(v(usqomkigecabdfhjlnprt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p)q)r)s)t)u)v)w)x)y)z))))z(y(x(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "(a(bdfyhwjulsnqpormtkvixgzecz(y(x(w(v(usqomkigecabdfhjlnprt": {e}')
    
    total += 1
    try:
        result = candidate(s = "p(q(r(s)t)u)v(w(x(y(z))w)v)u") == "purstqvvxzywwu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "p(q(r(s)t)u)v(w(x(y(z))w)v)u") == "purstqvvxzywwu": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g)h)i)j)k)l)m") == "alcjehgfidkbm"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g)h)i)j)k)l)m") == "alcjehgfidkbm": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(bc)de)") == "edbca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(bc)de)") == "edbca": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x(yz))))))))))") == "(anclejghifkdmboqsuwyzxvtrp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x(yz))))))))))") == "(anclejghifkdmboqsuwyzxvtrp": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(bc(def(ghi(jkl(mno(pqr(stu(vwx(yz)))))))))b") == "adefjklpqrvwxzyutsonmihgcbb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(bc(def(ghi(jkl(mno(pqr(stu(vwx(yz)))))))))b") == "adefjklpqrvwxzyutsonmihgcbb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v)w)x)y)z)") == "(anclejghifkdmbozqxsvutwryp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v)w)x)y)z)") == "(anclejghifkdmbozqxsvutwryp": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefgh(ijklmnopqrstuvwxyz)") == "abcdefghzyxwvutsrqponmlkji"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefgh(ijklmnopqrstuvwxyz)") == "abcdefghzyxwvutsrqponmlkji": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abc(def(ghi(jkl(mno)pqr)stu)vwx(yz))(abc(def(ghi(jkl(mno)pqr)stu)vwx(yz))") == "(abcyzxwvghirqpmnolkjstufed(abcyzxwvghirqpmnolkjstufed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abc(def(ghi(jkl(mno)pqr)stu)vwx(yz))(abc(def(ghi(jkl(mno)pqr)stu)vwx(yz))") == "(abcyzxwvghirqpmnolkjstufed(abcyzxwvghirqpmnolkjstufed": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abcdefgh)ijklmnopqrstuvwxyz") == "hgfedcbaijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abcdefgh)ijklmnopqrstuvwxyz") == "hgfedcbaijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(vw)x)y)z)))") == "anclejghifkdmbo(prztxvwuysq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(vw)x)y)z)))") == "anclejghifkdmbo(prztxvwuysq": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f)g)h)i") == "ahefgdcbi"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f)g)h)i") == "ahefgdcbi": {e}')
    
    total += 1
    try:
        result = candidate(s = "((abc)(def))") == "defabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((abc)(def))") == "defabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d)e(f(g(h)i)j)k)") == "kfihgjebcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d)e(f(g(h)i)j)k)") == "kfihgjebcda": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z)))") == "(acnejghifklmdotqrspuxwvyzb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z)))") == "(acnejghifklmdotqrspuxwvyzb": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g)h)i)j(k(l(m)n)o)p(q(r)s)t(u(v)w)x(y(z)))") == "ayzxuvwtqrspknmlojehgfidcb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g)h)i)j(k(l(m)n)o)p(q(r)s)t(u(v)w)x(y(z)))") == "ayzxuvwtqrspknmlojehgfidcb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x(y(z(u(v(w(x)y)z))))))))))))))") == "prtvxzvyxwzuywusqobmdkfihgjelcna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x(y(z(u(v(w(x)y)z))))))))))))))") == "prtvxzvyxwzuywusqobmdkfihgjelcna": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m(n(o)p)q)r)s(t(u(v)w)x)yz") == "adcbejghifkrmponqlsxuvwtyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m(n(o)p)q)r)s(t(u(v)w)x)yz") == "adcbejghifkrmponqlsxuvwtyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w)x)y(z))") == "zyvwxupsrqtobmdkfihgjelcna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w)x)y(z))") == "zyvwxupsrqtobmdkfihgjelcna": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d)e(f(g)h)i)") == "ifghebcda"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d)e(f(g)h)i)") == "ifghebcda": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc(def(ghi)jkl)(mno(pqr)stu)(vw(x(yz)))") == "abclkjghifedutspqronmxzywv"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc(def(ghi)jkl)(mno(pqr)stu)(vw(x(yz)))") == "abclkjghifedutspqronmxzywv": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))b)c") == "a(b(c(d(ebgikmoqsuwyzxvtrpnljhfc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))b)c") == "a(b(c(d(ebgikmoqsuwyzxvtrpnljhfc": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r)s)t)u)v)w)x)y)z)))))))))") == "acegizkxmvotqrspunwlyjhfdb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r)s)t)u)v)w)x)y)z)))))))))") == "acegizkxmvotqrspunwlyjhfdb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(ab)(cd)(ef)(gh)(ij)(kl)(mn)(op)(qr)(st)(uv)(wx)(yz)") == "badcfehgjilknmporqtsvuxwzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(ab)(cd)(ef)(gh)(ij)(kl)(mn)(op)(qr)(st)(uv)(wx)(yz)") == "badcfehgjilknmporqtsvuxwzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abcdefgh(i(jklm(nopq)rst)uv)wxyz)") == "zyxwitsrnopqmlkjuvhgfedcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abcdefgh(i(jklm(nopq)rst)uv)wxyz)") == "zyxwitsrnopqmlkjuvhgfedcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v(w)x)y)z)))") == "(anclejghifkdmboqzsxwvutyrp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v(w)x)y)z)))") == "(anclejghifkdmboqzsxwvutyrp": {e}')
    
    total += 1
    try:
        result = candidate(s = "(p(q(r)s)t)(u(v(w)x)y)") == "tqrspyvwxu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(p(q(r)s)t)(u(v(w)x)y)") == "tqrspyvwxu": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u") == "anclejghifkdmbotqrspu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u") == "anclejghifkdmbotqrspu": {e}')
    
    total += 1
    try:
        result = candidate(s = "(ab(cd(ef(gh(ij)kl)mn)op)qr)st") == "rqcdnmghjiklfeopbast"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(ab(cd(ef(gh(ij)kl)mn)op)qr)st") == "rqcdnmghjiklfeopbast": {e}')
    
    total += 1
    try:
        result = candidate(s = "(x(y(z)))") == "yzx"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(x(y(z)))") == "yzx": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w)x)y)z)u)v)w)x)y(z))") == "zypwrutyvwxuzsvqxobmdkfihgjelcna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w)x)y)z)u)v)w)x)y(z))") == "zypwrutyvwxuzsvqxobmdkfihgjelcna": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c(d(e(f(g)h)i)j)k(l(m)n)o(p(q(r)s)t)u)") == "upsrqtolmnkdifghejcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c(d(e(f(g)h)i)j)k(l(m)n)o(p(q(r)s)t)u)") == "upsrqtolmnkdifghejcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a(b)c)(d(e(f)g)h)i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))j)") == "(cbahefgdijkmoqsuwyzxvtrpnlj"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a(b)c)(d(e(f)g)h)i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))j)") == "(cbahefgdijkmoqsuwyzxvtrpnlj": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u)v)") == "(avcnelghijkfmdotqrspub"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u)v)") == "(avcnelghijkfmdotqrspub": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z))") == "xzy"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z))") == "xzy": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(a(y(b(z(c)d)e)f)g)h(i(j(k(l)m)n)o)p") == "xgyezcdbfahojmlknip"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(a(y(b(z(c)d)e)f)g)h(i(j(k(l)m)n)o)p") == "xgyezcdbfahojmlknip": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x)y)z)u)v)w)x)y(z))w)x)y(z)") == "xpzyrwtuvyxwzuvsxqwobmdkfihgjelcnayz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x)y)z)u)v)w)x)y(z))w)x)y(z)") == "xpzyrwtuvyxwzuvsxqwobmdkfihgjelcnayz": {e}')
    
    total += 1
    try:
        result = candidate(s = "(ab)(cd)((ef)(gh))(ij(kl(mn(op)qr)st)(uv(w(x(yz))))") == "badcghef(ijtsmnpoqrlkwyzxvu"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(ab)(cd)((ef)(gh))(ij(kl(mn(op)qr)st)(uv(w(x(yz))))") == "badcghef(ijtsmnpoqrlkwyzxvu": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))") == "(a(b(c(d(e(fhjlnprtvxzywusqomkig"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))") == "(a(b(c(d(e(fhjlnprtvxzywusqomkig": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z)(w))v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "xwzyv(usqomkigecabdfhjlnprt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z)(w))v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "xwzyv(usqomkigecabdfhjlnprt": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((((a))))))))))))") == "a"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((((a))))))))))))") == "a": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v)w)x)y)z))") == "(pyrwtuvsxqzobmdkfihgjelcna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v)w)x)y)z))") == "(pyrwtuvsxqzobmdkfihgjelcna": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z))a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p(q(r)s)t(u(v)w)x(y(z)))") == "xzyadcbejghifknmloyzxuvwtqrsp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z))a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p(q(r)s)t(u(v)w)x(y(z)))") == "xzyadcbejghifknmloyzxuvwtqrsp": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g)))))))") == "bdfgeca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g)))))))") == "bdfgeca": {e}')
    
    total += 1
    try:
        result = candidate(s = "m(n(o(p(q(r(s(t(u(v(w(x(y(z(abc)def)ghi)jkl)mno)pqr)stu)vwx)yzz)") == "m(n(o(p(q(rzzytutsvonmxihgzcbadefyjklwpqruvwxs"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "m(n(o(p(q(r(s(t(u(v(w(x(y(z(abc)def)ghi)jkl)mno)pqr)stu)vwx)yzz)") == "m(n(o(p(q(rzzytutsvonmxihgzcbadefyjklwpqruvwxs": {e}')
    
    total += 1
    try:
        result = candidate(s = "(p(q(r(s(t(u(v(w(x(y(z)))))))))))") == "qsuwyzxvtrp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(p(q(r(s(t(u(v(w(x(y(z)))))))))))") == "qsuwyzxvtrp": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))b") == "a(b(c(d(e(fhjlnprtvxzywusqomkigb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))b") == "a(b(c(d(e(fhjlnprtvxzywusqomkigb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(p(q(r(s(t(u)v)w)x)y)z)") == "zqxsvutwryp"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(p(q(r(s(t(u)v)w)x)y)z)") == "zqxsvutwryp": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abc(def(ghi(jkl(mno(pqr(stu(vwx(yz)))))))))") == "defjklpqrvwxzyutsonmihgcba"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abc(def(ghi(jkl(mno(pqr(stu(vwx(yz)))))))))") == "defjklpqrvwxzyutsonmihgcba": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g)h)i)j)k)l)") == "alcjehgfidkb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g)h)i)j)k)l)") == "alcjehgfidkb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(ij)kl)mno)pqr)stu)vw)xy)z)") == "(azcwverqpglkijhmnofstudxyb"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(ij)kl)mno)pqr)stu)vw)xy)z)") == "(azcwverqpglkijhmnofstudxyb": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v)w)x)y(z))") == "zypsrqtwvuxobmdkfihgjelcna"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v)w)x)y(z))") == "zypsrqtwvuxobmdkfihgjelcna": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(bc(def)ghi)jkl)") == "lkjbcfedghia"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(bc(def)ghi)jkl)") == "lkjbcfedghia": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z)(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "x(yz(w(v(usqomkigecabdfhjlnprt"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z)(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "x(yz(w(v(usqomkigecabdfhjlnprt": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a(b)c)(d(e(f)g)h)i(j(k(l(m)n)o)p)q") == "(cbahefgdipknmlojq"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a(b)c)(d(e(f)g)h)i(j(k(l(m)n)o)p)q") == "(cbahefgdipknmlojq": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc(def(ghi(jkl(mno(pqr(stu(vwx)y(z)))))))") == "abcghimnostuxwvyzrqplkjfed"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc(def(ghi(jkl(mno(pqr(stu(vwx)y(z)))))))") == "abcghimnostuxwvyzrqplkjfed": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z)))(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z))))") == "(acnejghifklmdotqrspuxwvyzbbzyvwxupsrqtodmlkfihgjenca"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z)))(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z))))") == "(acnejghifklmdotqrspuxwvyzbbzyvwxupsrqtodmlkfihgjenca": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))") == "(a(b(c(dfhjlnprtvxzywusqomkiglnprtvxzywusqome"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))") == "(a(b(c(dfhjlnprtvxzywusqomkiglnprtvxzywusqome": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f)g)h)i)j)") == "(ajchefgdib"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f)g)h)i)j)") == "(ajchefgdib": {e}')
    
    total += 1
    try:
        result = candidate(s = "x(y(z((a)(b))c)d)e") == "xdzbacye"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "x(y(z((a)(b))c)d)e") == "xdzbacye": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h(i(jk)lm)n)o)p)q)r)s)t)u)") == "ubsdqfohmljkingpercta"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h(i(jk)lm)n)o)p)q)r)s)t)u)") == "ubsdqfohmljkingpercta": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(a(b(c)d)e)") == "ebcda"
    assert candidate(s = "(a(b)c(d(e)f)g)") == "gdefcba"
    assert candidate(s = "(abc)(def)") == "cbafed"
    assert candidate(s = "(a(b)c(d)e(f)g)") == "gfedcba"
    assert candidate(s = "(z)") == "z"
    assert candidate(s = "(abcd)") == "dcba"
    assert candidate(s = "a(b)c(d(e)f)g") == "abcfedg"
    assert candidate(s = "(ed(et(oc))el)") == "leetcode"
    assert candidate(s = "x(abc)d(efg)h(ij(k(lm)n)op)q") == "xcbadgfehpokmlnjiq"
    assert candidate(s = "abcdefghij(klmnop(qrstuvwxyz))") == "abcdefghijqrstuvwxyzponmlk"
    assert candidate(s = "abc") == "abc"
    assert candidate(s = "(abc)d(efg)") == "cbadgfe"
    assert candidate(s = "(a(b(c)d)e(f(g)h)i") == "(adcbehgfi"
    assert candidate(s = "()") == ""
    assert candidate(s = "a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
    assert candidate(s = "(a)") == "a"
    assert candidate(s = "(u(love)i)") == "iloveu"
    assert candidate(s = "ab(c(d(e(fg)h)i)j)k") == "abjdhfgeick"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o") == "(anclejghifkdmbo"
    assert candidate(s = "x(y(z(wvu)tsr)qpo)nm") == "xopqzuvwtsrynm"
    assert candidate(s = "(a(b(c)d)e(f(g(h)i)j)k)l") == "kfihgjebcdal"
    assert candidate(s = "a(bc(def(ghi)jkl)mno(pqr(stu)vwx)y(z))") == "azypqrutsvwxonmdefihgjklcb"
    assert candidate(s = "a(b(c)d(e(f(g)h)i)j(k(l(m)n)o)p") == "a(bcdifghejolmnkp"
    assert candidate(s = "a(bc(def(ghi(jkl(mno)pqr)stu)vwx(yz))") == "a(bcyzxwvghirqpmnolkjstufed"
    assert candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m") == "alejghifkdcbm"
    assert candidate(s = "x(y(z))a(b(c)d)e(f(g(h)i)j)k") == "xzyadcbejghifk"
    assert candidate(s = "x(y(z))w") == "xzyw"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))z(y(x(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "(a(b(c(d(e(fhjlnprtvxzywusqomkigz(y(x(w(v(usqomkigecabdfhjlnprt"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p)q)r)s)t)u)v)w)x)y)z))))") == "(a(bdfyhwjulsnqpormtkvixgzec"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z)))))))))))))))))))))(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))") == "(a(b(c(d(egikmoqsuwyzxvtrpnljhf(a(b(c(d(e(fhjlnprtvxzywusqomkig"
    assert candidate(s = "(abc)(def)((ghi)(jkl))(mno)(pqr)((stu)(vwx))(yz)") == "cbafedjklghionmrqpvwxstuzy"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i))))))))") == "(acegihfdb"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p)q)r)s)t)u)v)w)x)y)z))))z(y(x(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "(a(bdfyhwjulsnqpormtkvixgzecz(y(x(w(v(usqomkigecabdfhjlnprt"
    assert candidate(s = "p(q(r(s)t)u)v(w(x(y(z))w)v)u") == "purstqvvxzywwu"
    assert candidate(s = "a(b(c(d(e(f(g)h)i)j)k)l)m") == "alcjehgfidkbm"
    assert candidate(s = "(a(bc)de)") == "edbca"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x(yz))))))))))") == "(anclejghifkdmboqsuwyzxvtrp"
    assert candidate(s = "a(bc(def(ghi(jkl(mno(pqr(stu(vwx(yz)))))))))b") == "adefjklpqrvwxzyutsonmihgcbb"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v)w)x)y)z)") == "(anclejghifkdmbozqxsvutwryp"
    assert candidate(s = "abcdefgh(ijklmnopqrstuvwxyz)") == "abcdefghzyxwvutsrqponmlkji"
    assert candidate(s = "(abc(def(ghi(jkl(mno)pqr)stu)vwx(yz))(abc(def(ghi(jkl(mno)pqr)stu)vwx(yz))") == "(abcyzxwvghirqpmnolkjstufed(abcyzxwvghirqpmnolkjstufed"
    assert candidate(s = "(abcdefgh)ijklmnopqrstuvwxyz") == "hgfedcbaijklmnopqrstuvwxyz"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(vw)x)y)z)))") == "anclejghifkdmbo(prztxvwuysq"
    assert candidate(s = "a(b(c)d(e(f)g)h)i") == "ahefgdcbi"
    assert candidate(s = "((abc)(def))") == "defabc"
    assert candidate(s = "(a(b(c)d)e(f(g(h)i)j)k)") == "kfihgjebcda"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z)))") == "(acnejghifklmdotqrspuxwvyzb"
    assert candidate(s = "a(b(c)d(e(f(g)h)i)j(k(l(m)n)o)p(q(r)s)t(u(v)w)x(y(z)))") == "ayzxuvwtqrspknmlojehgfidcb"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x(y(z(u(v(w(x)y)z))))))))))))))") == "prtvxzvyxwzuywusqobmdkfihgjelcna"
    assert candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m(n(o)p)q)r)s(t(u(v)w)x)yz") == "adcbejghifkrmponqlsxuvwtyz"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w)x)y(z))") == "zyvwxupsrqtobmdkfihgjelcna"
    assert candidate(s = "(a(b(c)d)e(f(g)h)i)") == "ifghebcda"
    assert candidate(s = "abc(def(ghi)jkl)(mno(pqr)stu)(vw(x(yz)))") == "abclkjghifedutspqronmxzywv"
    assert candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))b)c") == "a(b(c(d(ebgikmoqsuwyzxvtrpnljhfc"
    assert candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r)s)t)u)v)w)x)y)z)))))))))") == "acegizkxmvotqrspunwlyjhfdb"
    assert candidate(s = "(ab)(cd)(ef)(gh)(ij)(kl)(mn)(op)(qr)(st)(uv)(wx)(yz)") == "badcfehgjilknmporqtsvuxwzy"
    assert candidate(s = "(abcdefgh(i(jklm(nopq)rst)uv)wxyz)") == "zyxwitsrnopqmlkjuvhgfedcba"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v(w)x)y)z)))") == "(anclejghifkdmboqzsxwvutyrp"
    assert candidate(s = "(p(q(r)s)t)(u(v(w)x)y)") == "tqrspyvwxu"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u") == "anclejghifkdmbotqrspu"
    assert candidate(s = "(ab(cd(ef(gh(ij)kl)mn)op)qr)st") == "rqcdnmghjiklfeopbast"
    assert candidate(s = "(x(y(z)))") == "yzx"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w)x)y)z)u)v)w)x)y(z))") == "zypwrutyvwxuzsvqxobmdkfihgjelcna"
    assert candidate(s = "(a(b)c(d(e(f(g)h)i)j)k(l(m)n)o(p(q(r)s)t)u)") == "upsrqtolmnkdifghejcba"
    assert candidate(s = "((a(b)c)(d(e(f)g)h)i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))j)") == "(cbahefgdijkmoqsuwyzxvtrpnlj"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u)v)") == "(avcnelghijkfmdotqrspub"
    assert candidate(s = "x(y(z))") == "xzy"
    assert candidate(s = "x(a(y(b(z(c)d)e)f)g)h(i(j(k(l)m)n)o)p") == "xgyezcdbfahojmlknip"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u(v(w(x)y)z)u)v)w)x)y(z))w)x)y(z)") == "xpzyrwtuvyxwzuvsxqwobmdkfihgjelcnayz"
    assert candidate(s = "(ab)(cd)((ef)(gh))(ij(kl(mn(op)qr)st)(uv(w(x(yz))))") == "badcghef(ijtsmnpoqrlkwyzxvu"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))") == "(a(b(c(d(e(fhjlnprtvxzywusqomkig"
    assert candidate(s = "x(y(z)(w))v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "xwzyv(usqomkigecabdfhjlnprt"
    assert candidate(s = "((((((((((((a))))))))))))") == "a"
    assert candidate(s = "((a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r(s(t(u)v)w)x)y)z))") == "(pyrwtuvsxqzobmdkfihgjelcna"
    assert candidate(s = "x(y(z))a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p(q(r)s)t(u(v)w)x(y(z)))") == "xzyadcbejghifknmloyzxuvwtqrsp"
    assert candidate(s = "(a(b(c(d(e(f(g)))))))") == "bdfgeca"
    assert candidate(s = "m(n(o(p(q(r(s(t(u(v(w(x(y(z(abc)def)ghi)jkl)mno)pqr)stu)vwx)yzz)") == "m(n(o(p(q(rzzytutsvonmxihgzcbadefyjklwpqruvwxs"
    assert candidate(s = "(p(q(r(s(t(u(v(w(x(y(z)))))))))))") == "qsuwyzxvtrp"
    assert candidate(s = "a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))b") == "a(b(c(d(e(fhjlnprtvxzywusqomkigb"
    assert candidate(s = "(p(q(r(s(t(u)v)w)x)y)z)") == "zqxsvutwryp"
    assert candidate(s = "(abc(def(ghi(jkl(mno(pqr(stu(vwx(yz)))))))))") == "defjklpqrvwxzyutsonmihgcba"
    assert candidate(s = "a(b(c(d(e(f(g)h)i)j)k)l)") == "alcjehgfidkb"
    assert candidate(s = "(a(b(c(d(e(f(g(h(ij)kl)mno)pqr)stu)vw)xy)z)") == "(azcwverqpglkijhmnofstudxyb"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v)w)x)y(z))") == "zypsrqtwvuxobmdkfihgjelcna"
    assert candidate(s = "(a(bc(def)ghi)jkl)") == "lkjbcfedghia"
    assert candidate(s = "x(y(z)(w(v(u(t(s(r(q(p(o(n(m(l(k(j(i(h(g(f(e(d(c(b(a))))))))))))))))))))") == "x(yz(w(v(usqomkigecabdfhjlnprt"
    assert candidate(s = "((a(b)c)(d(e(f)g)h)i(j(k(l(m)n)o)p)q") == "(cbahefgdipknmlojq"
    assert candidate(s = "abc(def(ghi(jkl(mno(pqr(stu(vwx)y(z)))))))") == "abcghimnostuxwvyzrqplkjfed"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z)))(a(b(c(d(e(f(g(h)i)j)k(l)m)n)o(p(q(r)s)t)u(v(w)x)y(z))))") == "(acnejghifklmdotqrspuxwvyzbbzyvwxupsrqtodmlkfihgjenca"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(j(k(l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))))))l(m(n(o(p(q(r(s(t(u(v(w(x(y(z))))))))))))))))") == "(a(b(c(dfhjlnprtvxzywusqomkiglnprtvxzywusqome"
    assert candidate(s = "(a(b(c(d(e(f)g)h)i)j)") == "(ajchefgdib"
    assert candidate(s = "x(y(z((a)(b))c)d)e") == "xdzbacye"
    assert candidate(s = "(a(b(c(d(e(f(g(h(i(jk)lm)n)o)p)q)r)s)t)u)") == "ubsdqfohmljkingpercta"


