def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1"), tree_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1"), tree_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4---5"), tree_node([1, 2, None, 3, 4, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4---5"), tree_node([1, 2, None, 3, 4, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---5----6"), tree_node([1, 2, None, 3, None, 5, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---5----6"), tree_node([1, 2, None, 3, None, 5, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8-9-10"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8-9-10"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8--9"), tree_node([1, 2, 4, 3, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8--9"), tree_node([1, 2, 4, 3, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2-3----4-----5"), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2-3----4-----5"), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2-3--4--5"), tree_node([1, 2, 3, None, None, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2-3--4--5"), tree_node([1, 2, 3, None, None, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2---3----4-----5"), tree_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2---3----4-----5"), tree_node([1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2-3-4-5"), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2-3-4-5"), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2-3"), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2-3"), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2"), tree_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2"), tree_node([1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4-5--6---7"), tree_node([1, 2, 5, 3, None, 6, None, 4, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4-5--6---7"), tree_node([1, 2, 5, 3, None, 6, None, 4, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4-5"), tree_node([1, 2, 4, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4-5"), tree_node([1, 2, 4, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2-3--4-5--6-7"), tree_node([1, 2, 3, None, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2-3--4-5--6-7"), tree_node([1, 2, 3, None, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-401--349---90--88"), tree_node([1, 401, None, 349, 88, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-401--349---90--88"), tree_node([1, 401, None, 349, 88, 90])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5"), tree_node([1, 2, 4, 3, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5"), tree_node([1, 2, 4, 3, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9-10--11"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9-10--11"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8-9-10-11-12-13-14-15-16-17-18-19"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8-9-10-11-12-13-14-15-16-17-18-19"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11------------12-------------13"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11------------12-------------13"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7----------8-9-10-11-12-13"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7----------8-9-10-11-12-13"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7--8--9--10--11--12-13"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7--8--9--10--11--12-13"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4----5-6------7--8---9"), tree_node([1, 2, 4, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4----5-6------7--8---9"), tree_node([1, 2, 4, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9--10--11--12--13--14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9--10--11--12--13--14"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5--6--7---8----9-10--11--12-13"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5--6--7---8----9-10--11--12-13"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4------5--------6"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4------5--------6"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13-------------14"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13-------------14"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5---6------7"), tree_node([1, 2, 4, 3, None, 5, None, None, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5---6------7"), tree_node([1, 2, 4, 3, None, 5, None, None, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11------------12"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11------------12"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25--26--27--28--29--30--31--32--33--34--35--36--37--38--39--40--41--42--43--44--45--46--47--48--49--50"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25--26--27--28--29--30--31--32--33--34--35--36--37--38--39--40--41--42--43--44--45--46--47--48--49--50"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5-----6----7---8-9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5-----6----7---8-9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4---5----6-----7"), tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4---5----6-----7"), tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2-3-4-5-6-7-8-9"), tree_node([1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2-3-4-5-6-7-8-9"), tree_node([1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4-5--6--7---8-9-10-11-12"), tree_node([1, 2, 5, 3, None, 6, 7, 4, None, None, None, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4-5--6--7---8-9-10-11-12"), tree_node([1, 2, 5, 3, None, 6, 7, 4, None, None, None, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12-13-14"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12-13-14"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6--------7"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6--------7"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9--10--11--12--13--14--15--16"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9--10--11--12--13--14--15--16"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9-10-11-12-13-14"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9-10-11-12-13-14"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5-6------7---8-9--10----11"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5-6------7---8-9--10----11"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9--10--11-12--13--14--15--16--17--18--19--20"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9--10--11-12--13--14--15--16--17--18--19--20"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5-6--7---8--9-10----11--12"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5-6--7---8--9-10----11--12"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5--6-7---8-9--10-11--12-13--14"), tree_node([1, 2, 7, 3, 6, None, None, 4, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5--6-7---8-9--10-11--12-13--14"), tree_node([1, 2, 7, 3, 6, None, None, 4, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5---6--7"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5---6--7"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5----6-----7------8-------9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5----6-----7------8-------9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8-9-10-11-12-13-14-15-16-17-18"), tree_node([1, 2, 4, 3, None, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8-9-10-11-12-13-14-15-16-17-18"), tree_node([1, 2, 4, 3, None, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5---6---7---8---9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5---6---7---8---9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6--------7-8--9---10----11"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6--------7-8--9---10----11"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11--12--13--14--15"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11--12--13--14--15"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9-10--11--12-13--14--15--16--17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9-10--11--12-13--14--15--16--17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "10-20--30---40----50-60--70---80----90"), tree_node([10, 20, 60, 30, None, 70, None, 40, None, 80, None, 50, None, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "10-20--30---40----50-60--70---80----90"), tree_node([10, 20, 60, 30, None, 70, None, 40, None, 80, None, 50, None, 90])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5------6--------7--------8------9----10--11-12--13"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5------6--------7--------8------9----10--11-12--13"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8--9-10-11-12-13-14-15"), tree_node([1, 2, 4, 3, None, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8--9-10-11-12-13-14-15"), tree_node([1, 2, 4, 3, None, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5--6-7---8----9"), tree_node([1, 2, 4, 3, None, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5--6-7---8----9"), tree_node([1, 2, 4, 3, None, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5-6----7-8--9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5-6----7-8--9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9--10-11-12--13--14-15-16--17-18--19-20"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9--10-11-12--13--14-15-16--17-18--19-20"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6-7-8--9-10--11--12-13--14"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6-7-8--9-10--11--12-13--14"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-5-6--7----8-9----10--11----12"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-5-6--7----8-9----10--11----12"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8-9--10--11--12"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8-9--10--11--12"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6----7------8"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6----7------8"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "10-20--30---40----50-60--70-80"), tree_node([10, 20, 60, 30, None, 70, None, 40, None, None, None, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "10-20--30---40----50-60--70-80"), tree_node([10, 20, 60, 30, None, 70, None, 40, None, None, None, 50])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5--6-7---8-9--10-11--12-13--14-15--16-17--18--19--20--21--22"), tree_node([1, 2, 7, 3, 6, None, None, 4, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5--6-7---8-9--10-11--12-13--14-15--16-17--18--19--20--21--22"), tree_node([1, 2, 7, 3, 6, None, None, 4, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8-9--10-11--12-13"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8-9--10-11--12-13"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6-7--8---9"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6-7--8---9"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6-7-8-9-10-11-12"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6-7-8-9-10-11-12"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5---6----7--8--9--10--11--12"), tree_node([1, 2, 4, 3, None, 5, 8, None, None, 6, None, None, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5---6----7--8--9--10--11--12"), tree_node([1, 2, 4, 3, None, 5, 8, None, None, 6, None, None, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5---6----7"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5---6----7"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20-21"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20-21"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8-9-10-11-12"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8-9-10-11-12"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4---5----6-----7------8"), tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4---5----6-----7------8"), tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4-5--6----7-8"), tree_node([1, 2, 5, 3, None, 6, None, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4-5--6----7-8"), tree_node([1, 2, 5, 3, None, 6, None, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8--9-10"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8--9-10"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6--7---8----9-10--11--12--13"), tree_node([1, 2, 10, 3, 7, 11, 12, 4, None, 8, None, None, None, None, None, 5, None, 9, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6--7---8----9-10--11--12--13"), tree_node([1, 2, 10, 3, 7, 11, 12, 4, None, 8, None, None, None, None, None, 5, None, 9, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4---5-6--7---8----9-10--11"), tree_node([1, 2, 6, 3, 4, 7, None, None, None, 5, None, 8, None, None, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4---5-6--7---8----9-10--11"), tree_node([1, 2, 6, 3, 4, 7, None, None, None, 5, None, 8, None, None, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12--13--14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12--13--14"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10-11--12-13--14-15--16-17--18--19--20"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10-11--12-13--14-15--16-17--18--19--20"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6-7--8-9--10"), tree_node([1, 2, 5, 3, 4, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6-7--8-9--10"), tree_node([1, 2, 5, 3, 4, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20-21--22----23"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20-21--22----23"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8--9---10"), tree_node([1, 2, 4, 3, None, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8--9---10"), tree_node([1, 2, 4, 3, None, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19--20--21"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19--20--21"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9-10-11-12-13-14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9-10-11-12-13-14"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5---6----7-8--9----10-11"), tree_node([1, 2, 4, 3, None, 5, None, None, None, 6, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5---6----7-8--9----10-11"), tree_node([1, 2, 4, 3, None, 5, None, None, None, 6, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5-----6------7-------8"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5-----6------7-------8"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6-7--8--9-10-11--12--13"), tree_node([1, 2, 5, 3, 4, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6-7--8--9-10-11--12--13"), tree_node([1, 2, 5, 3, 4, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6-------7"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6-------7"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8-9-10-11"), tree_node([1, 2, 4, 3, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8-9-10-11"), tree_node([1, 2, 4, 3, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13-14--15"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13-14--15"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13-------------14--------------15"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13-------------14--------------15"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8--9--10-11"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8--9--10-11"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5--6--7----8-9----10"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5--6--7----8-9----10"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8-9--10--11"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8-9--10--11"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8-9-10--11"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8-9-10--11"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5------6--------7--------8------9----10--11"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5------6--------7--------8------9----10--11"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6---7----8-9-10-11-12-13"), tree_node([1, 2, 5, 3, 4, 6, None, None, None, None, None, 7, None, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6---7----8-9-10-11-12-13"), tree_node([1, 2, 5, 3, 4, 6, None, None, None, None, None, 7, None, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12-13--14--15"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12-13--14--15"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10-11--12-13--14"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10-11--12-13--14"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5--6--7---8----9"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5--6--7---8----9"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12--13--14--15--16"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12--13--14--15--16"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12-13-14-15"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12-13-14-15"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6-7--8----9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6-7--8----9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6-7"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6-7"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19--20--21--22--23"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19--20--21--22--23"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7----8----9"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7----8----9"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12--13--14--15--16--17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12--13--14--15--16--17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5----6--7"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5----6--7"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4----5----6----7----8----9"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4----5----6----7----8----9"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8----9----10"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8----9----10"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8--9-10-11-12-13-14-15-16"), tree_node([1, 2, 4, 3, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8--9-10-11-12-13-14-15-16"), tree_node([1, 2, 4, 3, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5----6--7----8"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5----6--7----8"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5--6--7--8-9--10--11--12--13--14--15--16--17--18--19--20--21"), tree_node([1, 2, 4, 3, None, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5--6--7--8-9--10--11--12--13--14--15--16--17--18--19--20--21"), tree_node([1, 2, 4, 3, None, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6----7---8-9----10--11"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6----7---8-9----10--11"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5----6------7------8----9"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5----6------7------8----9"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9--10-11-12-13-14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9--10-11-12-13-14"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14-15"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14-15"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9-10-11-12-13-14-15-16"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9-10-11-12-13-14-15-16"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7----------8"), tree_node([1, 2, None, 3, None, 4, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7----------8"), tree_node([1, 2, None, 3, None, 4, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5--6---7----8"), tree_node([1, 2, None, 3, 6, 4, None, 7, None, 5, None, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5--6---7----8"), tree_node([1, 2, None, 3, 6, 4, None, 7, None, 5, None, 8])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4---5----6-7--8-9-10-11-12"), tree_node([1, 2, 7, 3, 4, 8, None, None, None, 5, None, None, None, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4---5----6-7--8-9-10-11-12"), tree_node([1, 2, 7, 3, 4, 8, None, None, None, 5, None, None, None, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5-6--7---8----9"), tree_node([1, 2, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5-6--7---8----9"), tree_node([1, 2, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4-----5------6"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4-----5------6"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9--10-11-12-13-14-15-16-17"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9--10-11-12-13-14-15-16-17"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3----4------5--------6----------7"), tree_node([1, 2, None, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3----4------5--------6----------7"), tree_node([1, 2, None, 3])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8-9-10-11"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8-9-10-11"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3-4--5--6--7--8-9--10-11-12-13-14-15-16-17-18-19-20"), tree_node([1, 2, 4, 3, None, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3-4--5--6--7--8-9--10-11-12-13-14-15-16-17-18-19-20"), tree_node([1, 2, 4, 3, None, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16--17--18--19"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16--17--18--19"), tree_node([1, 2, None, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24"), tree_node([1, 2, None, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24"), tree_node([1, 2, None, 3, 4])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_tree(candidate(traversal = "1"), tree_node([1]))
    assert is_same_tree(candidate(traversal = "1-2--3--4---5"), tree_node([1, 2, None, 3, 4, None, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3---5----6"), tree_node([1, 2, None, 3, None, 5, None, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8-9-10"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8--9"), tree_node([1, 2, 4, 3, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2-3----4-----5"), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(traversal = "1-2-3--4--5"), tree_node([1, 2, 3, None, None, 4, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2---3----4-----5"), tree_node([1, 2]))
    assert is_same_tree(candidate(traversal = "1-2-3-4-5"), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(traversal = "1-2-3"), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(traversal = "1-2"), tree_node([1, 2]))
    assert is_same_tree(candidate(traversal = "1-2--3---4-5--6---7"), tree_node([1, 2, 5, 3, None, 6, None, 4, None, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4-5"), tree_node([1, 2, 4, 3]))
    assert is_same_tree(candidate(traversal = "1-2-3--4-5--6-7"), tree_node([1, 2, 3, None, None, 4]))
    assert is_same_tree(candidate(traversal = "1-401--349---90--88"), tree_node([1, 401, None, 349, 88, 90]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5"), tree_node([1, 2, 4, 3, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9-10--11"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8-9-10-11-12-13-14-15-16-17-18-19"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11------------12-------------13"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7----------8-9-10-11-12-13"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7--8--9--10--11--12-13"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4----5-6------7--8---9"), tree_node([1, 2, 4, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9--10--11--12--13--14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5--6--7---8----9-10--11--12-13"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3----4------5--------6"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13-------------14"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5---6------7"), tree_node([1, 2, 4, 3, None, 5, None, None, None, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11------------12"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25--26--27--28--29--30--31--32--33--34--35--36--37--38--39--40--41--42--43--44--45--46--47--48--49--50"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5-----6----7---8-9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4---5----6-----7"), tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2-3-4-5-6-7-8-9"), tree_node([1, 2, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3---4-5--6--7---8-9-10-11-12"), tree_node([1, 2, 5, 3, None, 6, 7, 4, None, None, None, 8]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12-13-14"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6--------7"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10-----------11"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9--10--11--12--13--14--15--16"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9-10-11-12-13-14"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5-6------7---8-9--10----11"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9--10--11-12--13--14--15--16--17--18--19--20"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5-6--7---8--9-10----11--12"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5--6-7---8-9--10-11--12-13--14"), tree_node([1, 2, 7, 3, 6, None, None, 4, None, None, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5---6--7"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5----6-----7------8-------9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8-9-10-11-12-13-14-15-16-17-18"), tree_node([1, 2, 4, 3, None, 5, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5---6---7---8---9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6--------7-8--9---10----11"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11--12--13--14--15"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9-10--11--12-13--14--15--16--17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "10-20--30---40----50-60--70---80----90"), tree_node([10, 20, 60, 30, None, 70, None, 40, None, 80, None, 50, None, 90]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5------6--------7--------8------9----10--11-12--13"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8--9-10-11-12-13-14-15"), tree_node([1, 2, 4, 3, None, 5, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5--6-7---8----9"), tree_node([1, 2, 4, 3, None, 5, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5-6----7-8--9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8--9--10-11-12--13--14-15-16--17-18--19-20"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6-7-8--9-10--11--12-13--14"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-5-6--7----8-9----10--11----12"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8-9--10--11--12"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6----7------8"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "10-20--30---40----50-60--70-80"), tree_node([10, 20, 60, 30, None, 70, None, 40, None, None, None, 50]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5--6-7---8-9--10-11--12-13--14-15--16-17--18--19--20--21--22"), tree_node([1, 2, 7, 3, 6, None, None, 4, None, None, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8-9--10-11--12-13"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8--9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6-7--8---9"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6-7-8-9-10-11-12"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10-11-12--13--14-15-16--17-18--19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5---6----7--8--9--10--11--12"), tree_node([1, 2, 4, 3, None, 5, 8, None, None, 6, None, None, None, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5---6----7"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20-21"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8-9-10-11-12"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4---5----6-----7------8"), tree_node([1, 2, None, 3, 4, None, None, 5, None, 6, None, 7, None, 8]))
    assert is_same_tree(candidate(traversal = "1-2--3---4-5--6----7-8"), tree_node([1, 2, 5, 3, None, 6, None, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8--9-10"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6--7---8----9-10--11--12--13"), tree_node([1, 2, 10, 3, 7, 11, 12, 4, None, 8, None, None, None, None, None, 5, None, 9, None, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4---5-6--7---8----9-10--11"), tree_node([1, 2, 6, 3, 4, 7, None, None, None, 5, None, 8, None, None, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12--13--14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6-------7--------8---------9----------10"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10-11--12-13--14-15--16-17--18--19--20"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6-7--8-9--10"), tree_node([1, 2, 5, 3, 4, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20-21--22----23"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5--6-7-8--9---10"), tree_node([1, 2, 4, 3, None, 5, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19--20--21"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9-10-11-12-13-14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5---6----7-8--9----10-11"), tree_node([1, 2, 4, 3, None, 5, None, None, None, 6, None, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5-----6------7-------8"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6-7--8--9-10-11--12--13"), tree_node([1, 2, 5, 3, 4, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6-------7"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8-9-10-11"), tree_node([1, 2, 4, 3, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13-14--15"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13--14----15--16-17--18----19--20"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12------------13-------------14--------------15"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8--9--10-11"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5--6--7----8-9----10"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7--8-9--10--11"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5--6--7-8-9-10-11-12-13"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7-8-9-10--11"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5------6--------7--------8------9----10--11"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6---7----8-9-10-11-12-13"), tree_node([1, 2, 5, 3, 4, 6, None, None, None, None, None, 7, None, 8]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12-13--14--15"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8-9--10-11--12-13--14"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5--6--7---8----9"), tree_node([1, 2, None, 3, 6, 4, None, None, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12--13--14--15--16"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8----9-10--11--12-13-14-15"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5, None, 9]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6-7--8----9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6-7"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7-------8--------9---------10----------11-----------12"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19--20--21--22--23"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7----8----9"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8--9--10--11--12--13--14--15--16--17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5----6--7"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3----4----5----6----7----8----9"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8----9----10"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5-6--7-8--9-10-11-12-13-14-15-16"), tree_node([1, 2, 4, 3, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-----6------7"), tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5----6--7----8"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5--6--7--8-9--10--11--12--13--14--15--16--17--18--19--20--21"), tree_node([1, 2, 4, 3, None, 5, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6----7---8-9----10--11"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5-6--7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5----6------7------8----9"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9--10-11-12-13-14"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14-15"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9-10-11-12-13-14-15-16"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5------6---------7----------8"), tree_node([1, 2, None, 3, None, 4, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5--6---7----8"), tree_node([1, 2, None, 3, 6, 4, None, 7, None, 5, None, 8]))
    assert is_same_tree(candidate(traversal = "1-2--3--4---5----6-7--8-9-10-11-12"), tree_node([1, 2, 7, 3, 4, 8, None, None, None, 5, None, None, None, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5-6--7---8----9"), tree_node([1, 2, 5, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3----4-----5------6"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7--8-9--10-11-12-13-14-15-16-17"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3----4------5--------6----------7"), tree_node([1, 2, None, 3]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8-9-10-11"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4----5------6---------7----------8-9-10-11-12-13-14"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3---4----5-6--7---8"), tree_node([1, 2, 6, 3, None, 7, None, 4, None, 8, None, 5]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3-4--5--6--7--8-9--10-11-12-13-14-15-16-17-18-19-20"), tree_node([1, 2, 4, 3, None, 5, 6]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7-8--9--10--11--12--13--14--15--16--17--18--19"), tree_node([1, 2, None, 3, 4]))
    assert is_same_tree(candidate(traversal = "1-2--3--4-5--6--7-8--9-10--11--12-13--14-15--16-17--18--19"), tree_node([1, 2, 5, 3, 4, 6, 7]))
    assert is_same_tree(candidate(traversal = "1-2--3--4--5--6--7--8--9--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24"), tree_node([1, 2, None, 3, 4]))


