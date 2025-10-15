def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "(a(b)c)d(e(fg)h") == "(a(b)c)de(fg)h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c)d(e(fg)h") == "(a(b)c)de(fg)h": {e}')
    
    total += 1
    try:
        result = candidate(s = "()") == "()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()") == "()": {e}')
    
    total += 1
    try:
        result = candidate(s = "))(()") == "()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))(()") == "()": {e}')
    
    total += 1
    try:
        result = candidate(s = "ab(c(d)e)f(g(h)i)j(kl)") == "ab(c(d)e)f(g(h)i)j(kl)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "ab(c(d)e)f(g(h)i)j(kl)") == "ab(c(d)e)f(g(h)i)j(kl)": {e}')
    
    total += 1
    try:
        result = candidate(s = "a)b(c)d") == "ab(c)d"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a)b(c)d") == "ab(c)d": {e}')
    
    total += 1
    try:
        result = candidate(s = "()()") == "()()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()") == "()()": {e}')
    
    total += 1
    try:
        result = candidate(s = "") == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == "": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c)d(e(f)g)h(i)") == "(a(b)c)d(e(f)g)h(i)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c)d(e(f)g)h(i)") == "(a(b)c)d(e(f)g)h(i)": {e}')
    
    total += 1
    try:
        result = candidate(s = "))(())") == "(())"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "))(())") == "(())": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c)d(e(f)g)h") == "(a(b)c)d(e(f)g)h"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c)d(e(f)g)h") == "(a(b)c)d(e(f)g)h": {e}')
    
    total += 1
    try:
        result = candidate(s = "lee(t(c)o)de)") == "lee(t(c)o)de"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "lee(t(c)o)de)") == "lee(t(c)o)de": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b)c)d(e(fg)h)i(j(k(l)m)n)o(pq(r)s)t(uv(w)x)y(z)") == "a(b)cd(e(fg)h)i(j(k(l)m)n)o(pq(r)s)t(uv(w)x)y(z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b)c)d(e(fg)h)i(j(k(l)m)n)o(pq(r)s)t(uv(w)x)y(z)") == "a(b)cd(e(fg)h)i(j(k(l)m)n)o(pq(r)s)t(uv(w)x)y(z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)s)t(u)v(w(x)y)z(((())") == "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)st(u)v(w(x)y)z(())"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)s)t(u)v(w(x)y)z(((())") == "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)st(u)v(w(x)y)z(())": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)st(u)v(w(x)y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)st(u)v(w(x)y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a((b)c)d(e(f)g)h(i(j(k(l)m)n)o(p(q(r)s)t(uv(w)x)y(z))))") == "a((b)c)d(e(f)g)h(i(j(k(l)m)n)o(p(q(r)s)t(uv(w)x)y(z)))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a((b)c)d(e(f)g)h(i(j(k(l)m)n)o(p(q(r)s)t(uv(w)x)y(z))))") == "a((b)c)d(e(f)g)h(i(j(k(l)m)n)o(p(q(r)s)t(uv(w)x)y(z)))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z)") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w)xy(z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z)") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w)xy(z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f)g(h)i)j)k") == "a(b(c)d(e(f)g(h)i)j)k"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f)g(h)i)j)k") == "a(b(c)d(e(f)g(h)i)j)k": {e}')
    
    total += 1
    try:
        result = candidate(s = "(())((()())())(()(()))(()(()())())(()(()))(()(()())())") == "(())((()())())(()(()))(()(()())())(()(()))(()(()())())"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())((()())())(()(()))(()(()())())(()(()))(()(()())())") == "(())((()())())(()(()))(()(()())())(()(()))(()(()())())": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)": {e}')
    
    total += 1
    try:
        result = candidate(s = "(x(y(z)))a(b(c)d(e(f)g)h)i)j)k") == "(x(y(z)))a(b(c)d(e(f)g)h)ijk"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(x(y(z)))a(b(c)d(e(f)g)h)i)j)k") == "(x(y(z)))a(b(c)d(e(f)g)h)ijk": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b)c(d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b)c(d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b)c(d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b)c(d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((a))))))))))") == "((((((((((a))))))))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((a))))))))))") == "((((((((((a))))))))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o)p(q(r)s)t(u(v(w)x)y(z))") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)op(q(r)s)t(u(v(w)x)y(z))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o)p(q(r)s)t(u(v(w)x)y(z))") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)op(q(r)s)t(u(v(w)x)y(z))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o)p(q(r)s)t(u(v(w)x)y(z)))") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)op(q(r)s)t(u(v(w)x)y(z))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o)p(q(r)s)t(u(v(w)x)y(z)))") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)op(q(r)s)t(u(v(w)x)y(z))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "abcde(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "abcde(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "((abc)(def))ghi(jkl(mno)pqr)stu(vwx(yz)") == "((abc)(def))ghi(jkl(mno)pqr)stuvwx(yz)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((abc)(def))ghi(jkl(mno)pqr)stu(vwx(yz)") == "((abc)(def))ghi(jkl(mno)pqr)stuvwx(yz)": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a(b)c)d)e(f(g(h)i)j)k(lmno)p(q(rst)uvw)x(y(z))") == "((a(b)c)d)e(f(g(h)i)j)k(lmno)p(q(rst)uvw)x(y(z))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a(b)c)d)e(f(g(h)i)j)k(lmno)p(q(rst)uvw)x(y(z))") == "((a(b)c)d)e(f(g(h)i)j)k(lmno)p(q(rst)uvw)x(y(z))": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((a))))))))") == "((((((((a))))))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((a))))))))") == "((((((((a))))))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "(a(b(c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "(a(b(c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(())((())())(((())))") == "(())((())())(((())))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(())((())())(((())))") == "(())((())())(((())))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a((((((((((b))))))))))") == "a((((((((((b))))))))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a((((((((((b))))))))))") == "a((((((((((b))))))))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((a)bb)ccc)d)eeee(f)ggg(h)iii") == "((((a)bb)ccc)d)eeee(f)ggg(h)iii"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((a)bb)ccc)d)eeee(f)ggg(h)iii") == "((((a)bb)ccc)d)eeee(f)ggg(h)iii": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b)c)d(e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "a(b)cd(e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b)c)d(e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "a(b)cd(e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc(def(ghi)jkl)mno(pqr)stu(vwxyz)") == "abc(def(ghi)jkl)mno(pqr)stu(vwxyz)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc(def(ghi)jkl)mno(pqr)stu(vwxyz)") == "abc(def(ghi)jkl)mno(pqr)stu(vwxyz)": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a(b)c)d(e(f)g)h(i)j)k(l(m)n)o(p)q(r)s)t") == "((a(b)c)d(e(f)g)h(i)j)k(l(m)n)o(p)q(r)st"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a(b)c)d(e(f)g)h(i)j)k(l(m)n)o(p)q(r)s)t") == "((a(b)c)d(e(f)g)h(i)j)k(l(m)n)o(p)q(r)st": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)s)t(u)v(w(x)y)z)()(()") == "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)st(u)v(w(x)y)z()()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)s)t(u)v(w(x)y)z)()(()") == "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)st(u)v(w(x)y)z()()": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "(abc(def(ghi(jkl(mnopqr(stu(vwx(yz)))))))") == "abc(def(ghi(jkl(mnopqr(stu(vwx(yz)))))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(abc(def(ghi(jkl(mnopqr(stu(vwx(yz)))))))") == "abc(def(ghi(jkl(mnopqr(stu(vwx(yz)))))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)))") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)))") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((((((((((((((()))))))))))))))))))))))))") == "((((((((((((((((((((((()))))))))))))))))))))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((((((((((((((()))))))))))))))))))))))))") == "((((((((((((((((((((((()))))))))))))))))))))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((a(b)c)d)e)f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "(((((a(b)c)d)e)f)g)hi(j(k(l)m)n)o(p)q(r)st(u)v(w(x)y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((a(b)c)d)e)f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "(((((a(b)c)d)e)f)g)hi(j(k(l)m)n)o(p)q(r)st(u)v(w(x)y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((a))))))))))b") == "((((((((((a))))))))))b"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((a))))))))))b") == "((((((((((a))))))))))b": {e}')
    
    total += 1
    try:
        result = candidate(s = "()()()((()))(())(((()))(()(()))(())(()))") == "()()()((()))(())(((()))(()(()))(())(()))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "()()()((()))(())(((()))(()(()))(())(()))") == "()()()((()))(())(((()))(()(()))(())(()))": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((()))))))))))") == "((((((((((()))))))))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((()))))))))))") == "((((((((((()))))))))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(((abc)def)ghijklmnopqrst)uv(wxyz)") == "(((abc)def)ghijklmnopqrst)uv(wxyz)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((abc)def)ghijklmnopqrst)uv(wxyz)") == "(((abc)def)ghijklmnopqrst)uv(wxyz)": {e}')
    
    total += 1
    try:
        result = candidate(s = "abc)def(ghi)jkl(mno)pqr(stu)vwx(yz") == "abcdef(ghi)jkl(mno)pqr(stu)vwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abc)def(ghi)jkl(mno)pqr(stu)vwx(yz") == "abcdef(ghi)jkl(mno)pqr(stu)vwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a)(b)(c)(d))") == "((a)(b)(c)(d))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a)(b)(c)(d))") == "((a)(b)(c)(d))": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz(abcdefghijklmnopqrstuvwxyz)") == "abcdefghijklmnopqrstuvwxyz(abcdefghijklmnopqrstuvwxyz)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz(abcdefghijklmnopqrstuvwxyz)") == "abcdefghijklmnopqrstuvwxyz(abcdefghijklmnopqrstuvwxyz)": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((((((((((((()))))))))))))))))))))))))))))()") == "((((((((((((((((((((()))))))))))))))))))))()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((((((((((((()))))))))))))))))))))))))))))()") == "((((((((((((((((((((()))))))))))))))))))))()": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "((((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "((((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v(w)x)y(z)))") == "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v(w)x)y(z))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v(w)x)y(z)))") == "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v(w)x)y(z))": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y(z)u)v)w)x)y)z") == "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y(z)u)v)w)x)yz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y(z)u)v)w)x)y)z") == "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y(z)u)v)w)x)yz": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((a(b)c)d))))))") == "((((((a(b)c)d)))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((a(b)c)d))))))") == "((((((a(b)c)d)))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z))))") == "ab(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z))))") == "ab(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z))))": {e}')
    
    total += 1
    try:
        result = candidate(s = "((((((((((((((((((((((()") == "()"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((((((((((((((((((((()") == "()": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b)c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "a(b)cd(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b)c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "a(b)cd(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v)w)x(y(z)))") == "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v)w)x(y(z))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v)w)x(y(z)))") == "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v)w)x(y(z))": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d)e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "a(b(c)d)e(f(g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w(x)y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d)e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "a(b(c)d)e(f(g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w(x)y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z(abc)") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz(abc)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z(abc)") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz(abc)": {e}')
    
    total += 1
    try:
        result = candidate(s = "((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)") == "((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)") == "((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y)z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y)z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)abc(def)") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyzabc(def)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)abc(def)") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyzabc(def)": {e}')
    
    total += 1
    try:
        result = candidate(s = "abcdefghijklmnopqrstuvwxyz)abcdefghijklmnopqrstuvwxyz(") == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "abcdefghijklmnopqrstuvwxyz)abcdefghijklmnopqrstuvwxyz(") == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v(w)x)y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v(w)x)y)z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v(w)x)y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v(w)x)y)z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)(z)") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)(z)"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)(z)") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)(z)": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)st(u)v(w)x(y)z(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)st(u)v(w)x(y)z(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z": {e}')
    
    total += 1
    try:
        result = candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)abc") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyzabc"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)abc") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyzabc": {e}')
    
    total += 1
    try:
        result = candidate(s = "a(b(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "ab(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "a(b(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "ab(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "(a(b)c)d(e(fg)h") == "(a(b)c)de(fg)h"
    assert candidate(s = "()") == "()"
    assert candidate(s = "))(()") == "()"
    assert candidate(s = "ab(c(d)e)f(g(h)i)j(kl)") == "ab(c(d)e)f(g(h)i)j(kl)"
    assert candidate(s = "a)b(c)d") == "ab(c)d"
    assert candidate(s = "()()") == "()()"
    assert candidate(s = "") == ""
    assert candidate(s = "(a(b)c)d(e(f)g)h(i)") == "(a(b)c)d(e(f)g)h(i)"
    assert candidate(s = "))(())") == "(())"
    assert candidate(s = "(a(b)c)d(e(f)g)h") == "(a(b)c)d(e(f)g)h"
    assert candidate(s = "lee(t(c)o)de)") == "lee(t(c)o)de"
    assert candidate(s = "a(b)c)d(e(fg)h)i(j(k(l)m)n)o(pq(r)s)t(uv(w)x)y(z)") == "a(b)cd(e(fg)h)i(j(k(l)m)n)o(pq(r)s)t(uv(w)x)y(z)"
    assert candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)s)t(u)v(w(x)y)z(((())") == "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)st(u)v(w(x)y)z(())"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)st(u)v(w(x)y)z"
    assert candidate(s = "a((b)c)d(e(f)g)h(i(j(k(l)m)n)o(p(q(r)s)t(uv(w)x)y(z))))") == "a((b)c)d(e(f)g)h(i(j(k(l)m)n)o(p(q(r)s)t(uv(w)x)y(z)))"
    assert candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z)") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w)xy(z)"
    assert candidate(s = "a(b(c)d(e(f)g(h)i)j)k") == "a(b(c)d(e(f)g(h)i)j)k"
    assert candidate(s = "(())((()())())(()(()))(()(()())())(()(()))(()(()())())") == "(())((()())())(()(()))(()(()())())(()(()))(()(()())())"
    assert candidate(s = "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)))"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)"
    assert candidate(s = "(x(y(z)))a(b(c)d(e(f)g)h)i)j)k") == "(x(y(z)))a(b(c)d(e(f)g)h)ijk"
    assert candidate(s = "a(b)c(d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b)c(d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
    assert candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyz"
    assert candidate(s = "((((((((((a))))))))))") == "((((((((((a))))))))))"
    assert candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o)p(q(r)s)t(u(v(w)x)y(z))") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)op(q(r)s)t(u(v(w)x)y(z))"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o)p(q(r)s)t(u(v(w)x)y(z)))") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)op(q(r)s)t(u(v(w)x)y(z))"
    assert candidate(s = "a(b(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "abcde(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
    assert candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz"
    assert candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz"
    assert candidate(s = "((abc)(def))ghi(jkl(mno)pqr)stu(vwx(yz)") == "((abc)(def))ghi(jkl(mno)pqr)stuvwx(yz)"
    assert candidate(s = "((a(b)c)d)e(f(g(h)i)j)k(lmno)p(q(rst)uvw)x(y(z))") == "((a(b)c)d)e(f(g(h)i)j)k(lmno)p(q(rst)uvw)x(y(z))"
    assert candidate(s = "((((((((a))))))))") == "((((((((a))))))))"
    assert candidate(s = "(a(b(c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "(a(b(c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))"
    assert candidate(s = "(())((())())(((())))") == "(())((())())(((())))"
    assert candidate(s = "a((((((((((b))))))))))") == "a((((((((((b))))))))))"
    assert candidate(s = "((((a)bb)ccc)d)eeee(f)ggg(h)iii") == "((((a)bb)ccc)d)eeee(f)ggg(h)iii"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z"
    assert candidate(s = "a(b)c)d(e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "a(b)cd(e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z"
    assert candidate(s = "abc(def(ghi)jkl)mno(pqr)stu(vwxyz)") == "abc(def(ghi)jkl)mno(pqr)stu(vwxyz)"
    assert candidate(s = "((a(b)c)d(e(f)g)h(i)j)k(l(m)n)o(p)q(r)s)t") == "((a(b)c)d(e(f)g)h(i)j)k(l(m)n)o(p)q(r)st"
    assert candidate(s = "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)s)t(u)v(w(x)y)z)()(()") == "a(b(c)d)e(f(g(h)i)j)k(l(m)n)o(p)q(r)st(u)v(w(x)y)z()()"
    assert candidate(s = "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b(c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w)x(y)z"
    assert candidate(s = "(abc(def(ghi(jkl(mnopqr(stu(vwx(yz)))))))") == "abc(def(ghi(jkl(mnopqr(stu(vwx(yz)))))))"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)))") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z"
    assert candidate(s = "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)") == "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
    assert candidate(s = "((((((((((((((((((((((()))))))))))))))))))))))))") == "((((((((((((((((((((((()))))))))))))))))))))))"
    assert candidate(s = "(((((a(b)c)d)e)f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "(((((a(b)c)d)e)f)g)hi(j(k(l)m)n)o(p)q(r)st(u)v(w(x)y)z"
    assert candidate(s = "((((((((((a))))))))))b") == "((((((((((a))))))))))b"
    assert candidate(s = "()()()((()))(())(((()))(()(()))(())(()))") == "()()()((()))(())(((()))(()(()))(())(()))"
    assert candidate(s = "((((((((((()))))))))))") == "((((((((((()))))))))))"
    assert candidate(s = "(((abc)def)ghijklmnopqrst)uv(wxyz)") == "(((abc)def)ghijklmnopqrst)uv(wxyz)"
    assert candidate(s = "abc)def(ghi)jkl(mno)pqr(stu)vwx(yz") == "abcdef(ghi)jkl(mno)pqr(stu)vwxyz"
    assert candidate(s = "((a)(b)(c)(d))") == "((a)(b)(c)(d))"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz(abcdefghijklmnopqrstuvwxyz)") == "abcdefghijklmnopqrstuvwxyz(abcdefghijklmnopqrstuvwxyz)"
    assert candidate(s = "((((((((((((((((((((()))))))))))))))))))))))))))))()") == "((((((((((((((((((((()))))))))))))))))))))()"
    assert candidate(s = "((((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "((((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z)"
    assert candidate(s = "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v(w)x)y(z)))") == "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v(w)x)y(z))"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z"
    assert candidate(s = "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y(z)u)v)w)x)y)z") == "a(b(c(d(e(f(g(h)i(j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y(z)u)v)w)x)yz"
    assert candidate(s = "((((((a(b)c)d))))))") == "((((((a(b)c)d)))))"
    assert candidate(s = "a(b(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z))))") == "ab(c)d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y(z))))"
    assert candidate(s = "((((((((((((((((((((((()") == "()"
    assert candidate(s = "a(b)c)d(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z") == "a(b)cd(e(f)g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z"
    assert candidate(s = "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v)w)x(y(z)))") == "(a(b)c)d(e(f(g)h)i(j(k(l)m)n)o)p(q(r)s)t(u(v)w)x(y(z))"
    assert candidate(s = "a(b(c)d)e(f(g)h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w(x)y)z") == "a(b(c)d)e(f(g)h)i(j(k(l)m)n)o(p)q(r)st(u)v(w(x)y)z"
    assert candidate(s = "a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z(abc)") == "a(b(c)d(e(f(g(h)i)j)k)l)mnopqrstuvwxyz(abc)"
    assert candidate(s = "((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)") == "((a(b)c)d(e(f)g)h)i(j(k(l)m)n)o(p)"
    assert candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyz"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t)u(v(w(x)y)z)"
    assert candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)abc(def)") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyzabc(def)"
    assert candidate(s = "abcdefghijklmnopqrstuvwxyz)abcdefghijklmnopqrstuvwxyz(") == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v(w)x)y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q(r)s)t(u(v(w)x)y)z)"
    assert candidate(s = "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)(z)") == "(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)(z)"
    assert candidate(s = "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z)") == "a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)st(u)v(w)x(y)z(a(b(c(d(e(f(g(h)i)j)k)l)m)n)o(p(q)r)s)t(u)v(w)x(y)z"
    assert candidate(s = "(a(b(c)d(e(f(g(h)i)j)k)l)m)n)o)p)q)r)s)t)u)v)w)x)y)z)abc") == "(a(b(c)d(e(f(g(h)i)j)k)l)m)nopqrstuvwxyzabc"
    assert candidate(s = "a(b(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))") == "ab(c(d(e(f(g(h)i(j(k(l)m)n)o(p)q(r)s)t(u)v(w)x(y)z))))"


