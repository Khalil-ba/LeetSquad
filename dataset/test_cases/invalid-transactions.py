def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,50,1200,mtv']) == ['alice,50,1200,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,50,1200,mtv']) == ['alice,50,1200,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,beijing', 'bob,25,800,mtv', 'bob,100,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,beijing', 'bob,25,800,mtv', 'bob,100,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing']) == ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing']) == ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,1100,mtv', 'bob,50,2000,mtv', 'alice,100,1000,beijing']) == ['alice,20,1100,mtv', 'bob,50,2000,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,1100,mtv', 'bob,50,2000,mtv', 'alice,100,1000,beijing']) == ['alice,20,1100,mtv', 'bob,50,2000,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,mtv', 'alice,61,100,mtv']) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,mtv', 'alice,61,100,mtv']) == []: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,60,100,mtv', 'alice,120,100,beijing']) == ['alice,60,100,mtv', 'alice,120,100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,60,100,mtv', 'alice,120,100,beijing']) == ['alice,60,100,mtv', 'alice,120,100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,21,800,beijing']) == ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,21,800,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,21,800,beijing']) == ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,21,800,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv']) == ['bob,50,1200,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv']) == ['bob,50,1200,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,1500,mtv', 'alice,21,100,beijing', 'alice,22,2000,mtv']) == ['alice,20,1500,mtv', 'alice,21,100,beijing', 'alice,22,2000,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,1500,mtv', 'alice,21,100,beijing', 'alice,22,2000,mtv']) == ['alice,20,1500,mtv', 'alice,21,100,beijing', 'alice,22,2000,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'bob,20,800,mtv', 'alice,50,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'bob,20,800,mtv', 'alice,50,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,1500,mtv', 'alice,25,800,mtv', 'alice,30,1200,beijing']) == ['alice,20,1500,mtv', 'alice,25,800,mtv', 'alice,30,1200,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,1500,mtv', 'alice,25,800,mtv', 'alice,30,1200,beijing']) == ['alice,20,1500,mtv', 'alice,25,800,mtv', 'alice,30,1200,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv', 'alice,60,1200,mtv', 'bob,120,1200,beijing']) == ['bob,50,1200,mtv', 'alice,60,1200,mtv', 'bob,120,1200,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv', 'alice,60,1200,mtv', 'bob,120,1200,beijing']) == ['bob,50,1200,mtv', 'alice,60,1200,mtv', 'bob,120,1200,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,20,1001,mtv']) == ['alice,20,1001,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,20,1001,mtv']) == ['alice,20,1001,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,1500,mtv', 'alice,20,100,beijing', 'alice,50,1200,mtv']) == ['alice,20,1500,mtv', 'alice,20,100,beijing', 'alice,50,1200,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,1500,mtv', 'alice,20,100,beijing', 'alice,50,1200,mtv']) == ['alice,20,1500,mtv', 'alice,20,100,beijing', 'alice,50,1200,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'bob,20,800,mtv', 'alice,80,800,beijing']) == ['alice,20,800,mtv', 'alice,80,800,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'bob,20,800,mtv', 'alice,80,800,beijing']) == ['alice,20,800,mtv', 'alice,80,800,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing', 'dave,5,800,mtv', 'dave,7,900,newyork', 'dave,10,1000,beijing', 'dave,15,1100,mtv']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing', 'dave,5,800,mtv', 'dave,7,900,newyork', 'dave,10,1000,beijing', 'dave,15,1100,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing', 'dave,5,800,mtv', 'dave,7,900,newyork', 'dave,10,1000,beijing', 'dave,15,1100,mtv']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing', 'dave,5,800,mtv', 'dave,7,900,newyork', 'dave,10,1000,beijing', 'dave,15,1100,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,70,500,mtv', 'alice,130,500,newyork', 'alice,190,500,mtv', 'alice,250,500,beijing', 'bob,10,1200,newyork', 'bob,70,1200,beijing', 'bob,130,1200,mtv', 'bob,190,1200,newyork', 'bob,250,1200,beijing']) == ['alice,70,500,mtv', 'alice,130,500,newyork', 'alice,190,500,mtv', 'alice,250,500,beijing', 'bob,10,1200,newyork', 'bob,70,1200,beijing', 'bob,130,1200,mtv', 'bob,190,1200,newyork', 'bob,250,1200,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,70,500,mtv', 'alice,130,500,newyork', 'alice,190,500,mtv', 'alice,250,500,beijing', 'bob,10,1200,newyork', 'bob,70,1200,beijing', 'bob,130,1200,mtv', 'bob,190,1200,newyork', 'bob,250,1200,beijing']) == ['alice,70,500,mtv', 'alice,130,500,newyork', 'alice,190,500,mtv', 'alice,250,500,beijing', 'bob,10,1200,newyork', 'bob,70,1200,beijing', 'bob,130,1200,mtv', 'bob,190,1200,newyork', 'bob,250,1200,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,70,600,mtv', 'alice,120,800,newyork', 'alice,130,1100,newyork']) == ['alice,70,600,mtv', 'alice,120,800,newyork', 'alice,130,1100,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,70,600,mtv', 'alice,120,800,newyork', 'alice,130,1100,newyork']) == ['alice,70,600,mtv', 'alice,120,800,newyork', 'alice,130,1100,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,70,1500,beijing', 'alice,130,1100,mtv', 'alice,190,900,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'bob,140,1100,mtv', 'bob,200,900,beijing']) == ['alice,10,500,mtv', 'alice,70,1500,beijing', 'alice,130,1100,mtv', 'alice,190,900,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'bob,140,1100,mtv', 'bob,200,900,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,70,1500,beijing', 'alice,130,1100,mtv', 'alice,190,900,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'bob,140,1100,mtv', 'bob,200,900,beijing']) == ['alice,10,500,mtv', 'alice,70,1500,beijing', 'alice,130,1100,mtv', 'alice,190,900,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'bob,140,1100,mtv', 'bob,200,900,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['ivan,10,1300,madrid', 'ivan,40,800,madrid', 'ivan,70,1100,barcelona', 'ivan,100,1200,madrid', 'ivan,130,900,valencia', 'ivan,160,1000,madrid', 'ivan,190,800,barcelona', 'ivan,220,1500,madrid', 'ivan,250,600,valencia', 'ivan,280,1200,madrid', 'ivan,310,800,barcelona', 'ivan,340,900,madrid', 'ivan,370,700,valencia', 'ivan,400,1500,madrid']) == ['ivan,10,1300,madrid', 'ivan,40,800,madrid', 'ivan,70,1100,barcelona', 'ivan,100,1200,madrid', 'ivan,130,900,valencia', 'ivan,160,1000,madrid', 'ivan,190,800,barcelona', 'ivan,220,1500,madrid', 'ivan,250,600,valencia', 'ivan,280,1200,madrid', 'ivan,310,800,barcelona', 'ivan,340,900,madrid', 'ivan,370,700,valencia', 'ivan,400,1500,madrid']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['ivan,10,1300,madrid', 'ivan,40,800,madrid', 'ivan,70,1100,barcelona', 'ivan,100,1200,madrid', 'ivan,130,900,valencia', 'ivan,160,1000,madrid', 'ivan,190,800,barcelona', 'ivan,220,1500,madrid', 'ivan,250,600,valencia', 'ivan,280,1200,madrid', 'ivan,310,800,barcelona', 'ivan,340,900,madrid', 'ivan,370,700,valencia', 'ivan,400,1500,madrid']) == ['ivan,10,1300,madrid', 'ivan,40,800,madrid', 'ivan,70,1100,barcelona', 'ivan,100,1200,madrid', 'ivan,130,900,valencia', 'ivan,160,1000,madrid', 'ivan,190,800,barcelona', 'ivan,220,1500,madrid', 'ivan,250,600,valencia', 'ivan,280,1200,madrid', 'ivan,310,800,barcelona', 'ivan,340,900,madrid', 'ivan,370,700,valencia', 'ivan,400,1500,madrid']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,10,1200,mtv', 'frank,20,1000,beijing', 'frank,30,1500,mtv', 'frank,40,900,newyork', 'frank,50,1100,mtv', 'frank,60,800,beijing', 'frank,70,1000,newyork']) == ['frank,10,1200,mtv', 'frank,20,1000,beijing', 'frank,30,1500,mtv', 'frank,40,900,newyork', 'frank,50,1100,mtv', 'frank,60,800,beijing', 'frank,70,1000,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,10,1200,mtv', 'frank,20,1000,beijing', 'frank,30,1500,mtv', 'frank,40,900,newyork', 'frank,50,1100,mtv', 'frank,60,800,beijing', 'frank,70,1000,newyork']) == ['frank,10,1200,mtv', 'frank,20,1000,beijing', 'frank,30,1500,mtv', 'frank,40,900,newyork', 'frank,50,1100,mtv', 'frank,60,800,beijing', 'frank,70,1000,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['eve,5,1000,berlin', 'eve,10,100,berlin', 'eve,70,1100,berlin', 'eve,120,1200,berlin', 'eve,180,1300,berlin']) == ['eve,70,1100,berlin', 'eve,120,1200,berlin', 'eve,180,1300,berlin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['eve,5,1000,berlin', 'eve,10,100,berlin', 'eve,70,1100,berlin', 'eve,120,1200,berlin', 'eve,180,1300,berlin']) == ['eve,70,1100,berlin', 'eve,120,1200,berlin', 'eve,180,1300,berlin']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['jane,10,900,sanfrancisco', 'jane,20,1100,sanfrancisco', 'jane,30,800,sanfrancisco', 'jane,40,1200,losangeles', 'jane,50,1000,losangeles', 'jane,60,950,sanfrancisco', 'jane,70,1050,sanfrancisco', 'jane,80,850,losangeles', 'jane,90,1150,sanfrancisco']) == ['jane,10,900,sanfrancisco', 'jane,20,1100,sanfrancisco', 'jane,30,800,sanfrancisco', 'jane,40,1200,losangeles', 'jane,50,1000,losangeles', 'jane,60,950,sanfrancisco', 'jane,70,1050,sanfrancisco', 'jane,80,850,losangeles', 'jane,90,1150,sanfrancisco']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['jane,10,900,sanfrancisco', 'jane,20,1100,sanfrancisco', 'jane,30,800,sanfrancisco', 'jane,40,1200,losangeles', 'jane,50,1000,losangeles', 'jane,60,950,sanfrancisco', 'jane,70,1050,sanfrancisco', 'jane,80,850,losangeles', 'jane,90,1150,sanfrancisco']) == ['jane,10,900,sanfrancisco', 'jane,20,1100,sanfrancisco', 'jane,30,800,sanfrancisco', 'jane,40,1200,losangeles', 'jane,50,1000,losangeles', 'jane,60,950,sanfrancisco', 'jane,70,1050,sanfrancisco', 'jane,80,850,losangeles', 'jane,90,1150,sanfrancisco']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['ivan,10,900,moscow', 'ivan,20,1100,moscow', 'ivan,30,800,moscow', 'ivan,40,1200,stuttgart', 'ivan,50,1000,stuttgart', 'ivan,60,950,moscow', 'ivan,70,1050,moscow', 'ivan,80,850,stuttgart']) == ['ivan,10,900,moscow', 'ivan,20,1100,moscow', 'ivan,30,800,moscow', 'ivan,40,1200,stuttgart', 'ivan,50,1000,stuttgart', 'ivan,60,950,moscow', 'ivan,70,1050,moscow', 'ivan,80,850,stuttgart']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['ivan,10,900,moscow', 'ivan,20,1100,moscow', 'ivan,30,800,moscow', 'ivan,40,1200,stuttgart', 'ivan,50,1000,stuttgart', 'ivan,60,950,moscow', 'ivan,70,1050,moscow', 'ivan,80,850,stuttgart']) == ['ivan,10,900,moscow', 'ivan,20,1100,moscow', 'ivan,30,800,moscow', 'ivan,40,1200,stuttgart', 'ivan,50,1000,stuttgart', 'ivan,60,950,moscow', 'ivan,70,1050,moscow', 'ivan,80,850,stuttgart']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['eve,5,1500,mtv', 'eve,65,1100,beijing', 'eve,70,500,mtv', 'eve,130,1000,newyork', 'eve,135,800,mtv', 'eve,190,1100,beijing']) == ['eve,5,1500,mtv', 'eve,65,1100,beijing', 'eve,70,500,mtv', 'eve,130,1000,newyork', 'eve,135,800,mtv', 'eve,190,1100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['eve,5,1500,mtv', 'eve,65,1100,beijing', 'eve,70,500,mtv', 'eve,130,1000,newyork', 'eve,135,800,mtv', 'eve,190,1100,beijing']) == ['eve,5,1500,mtv', 'eve,65,1100,beijing', 'eve,70,500,mtv', 'eve,130,1000,newyork', 'eve,135,800,mtv', 'eve,190,1100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['dave,5,500,boston', 'dave,30,1100,boston', 'dave,35,600,ny', 'dave,45,900,boston', 'dave,70,1500,ny']) == ['dave,5,500,boston', 'dave,30,1100,boston', 'dave,35,600,ny', 'dave,45,900,boston', 'dave,70,1500,ny']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['dave,5,500,boston', 'dave,30,1100,boston', 'dave,35,600,ny', 'dave,45,900,boston', 'dave,70,1500,ny']) == ['dave,5,500,boston', 'dave,30,1100,boston', 'dave,35,600,ny', 'dave,45,900,boston', 'dave,70,1500,ny']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['ian,10,500,tokyo', 'ian,20,600,tokyo', 'ian,30,700,tokyo', 'ian,40,800,tokyo', 'ian,50,900,tokyo', 'ian,60,1000,tokyo', 'ian,70,1100,tokyo', 'ian,80,1200,tokyo', 'ian,90,1300,tokyo', 'ian,100,1400,tokyo', 'ian,110,1500,tokyo', 'ian,120,1600,tokyo', 'ian,130,1700,tokyo', 'ian,140,1800,tokyo', 'ian,150,1900,tokyo', 'ian,160,1500,osaka', 'ian,170,1600,osaka', 'ian,180,1700,osaka', 'ian,190,1800,osaka', 'ian,200,1900,osaka']) == ['ian,70,1100,tokyo', 'ian,80,1200,tokyo', 'ian,90,1300,tokyo', 'ian,100,1400,tokyo', 'ian,110,1500,tokyo', 'ian,120,1600,tokyo', 'ian,130,1700,tokyo', 'ian,140,1800,tokyo', 'ian,150,1900,tokyo', 'ian,160,1500,osaka', 'ian,170,1600,osaka', 'ian,180,1700,osaka', 'ian,190,1800,osaka', 'ian,200,1900,osaka']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['ian,10,500,tokyo', 'ian,20,600,tokyo', 'ian,30,700,tokyo', 'ian,40,800,tokyo', 'ian,50,900,tokyo', 'ian,60,1000,tokyo', 'ian,70,1100,tokyo', 'ian,80,1200,tokyo', 'ian,90,1300,tokyo', 'ian,100,1400,tokyo', 'ian,110,1500,tokyo', 'ian,120,1600,tokyo', 'ian,130,1700,tokyo', 'ian,140,1800,tokyo', 'ian,150,1900,tokyo', 'ian,160,1500,osaka', 'ian,170,1600,osaka', 'ian,180,1700,osaka', 'ian,190,1800,osaka', 'ian,200,1900,osaka']) == ['ian,70,1100,tokyo', 'ian,80,1200,tokyo', 'ian,90,1300,tokyo', 'ian,100,1400,tokyo', 'ian,110,1500,tokyo', 'ian,120,1600,tokyo', 'ian,130,1700,tokyo', 'ian,140,1800,tokyo', 'ian,150,1900,tokyo', 'ian,160,1500,osaka', 'ian,170,1600,osaka', 'ian,180,1700,osaka', 'ian,190,1800,osaka', 'ian,200,1900,osaka']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,10,800,toronto', 'grace,30,700,toronto', 'grace,60,1200,vancouver', 'grace,90,600,toronto', 'grace,120,800,toronto', 'grace,150,900,montreal', 'grace,180,1500,toronto', 'grace,210,700,vancouver', 'grace,240,600,montreal', 'grace,270,1100,toronto', 'grace,300,900,vancouver', 'grace,330,800,montreal']) == ['grace,10,800,toronto', 'grace,30,700,toronto', 'grace,60,1200,vancouver', 'grace,90,600,toronto', 'grace,120,800,toronto', 'grace,150,900,montreal', 'grace,180,1500,toronto', 'grace,210,700,vancouver', 'grace,240,600,montreal', 'grace,270,1100,toronto', 'grace,300,900,vancouver', 'grace,330,800,montreal']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,10,800,toronto', 'grace,30,700,toronto', 'grace,60,1200,vancouver', 'grace,90,600,toronto', 'grace,120,800,toronto', 'grace,150,900,montreal', 'grace,180,1500,toronto', 'grace,210,700,vancouver', 'grace,240,600,montreal', 'grace,270,1100,toronto', 'grace,300,900,vancouver', 'grace,330,800,montreal']) == ['grace,10,800,toronto', 'grace,30,700,toronto', 'grace,60,1200,vancouver', 'grace,90,600,toronto', 'grace,120,800,toronto', 'grace,150,900,montreal', 'grace,180,1500,toronto', 'grace,210,700,vancouver', 'grace,240,600,montreal', 'grace,270,1100,toronto', 'grace,300,900,vancouver', 'grace,330,800,montreal']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,10,1200,beijing', 'alice,20,500,newyork', 'bob,10,300,mtv', 'bob,11,1500,beijing']) == ['alice,10,500,mtv', 'alice,10,1200,beijing', 'alice,20,500,newyork', 'bob,10,300,mtv', 'bob,11,1500,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,10,1200,beijing', 'alice,20,500,newyork', 'bob,10,300,mtv', 'bob,11,1500,beijing']) == ['alice,10,500,mtv', 'alice,10,1200,beijing', 'alice,20,500,newyork', 'bob,10,300,mtv', 'bob,11,1500,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['charlie,10,1000,paris', 'charlie,50,2000,london', 'charlie,60,1500,paris', 'charlie,120,800,london']) == ['charlie,10,1000,paris', 'charlie,50,2000,london', 'charlie,60,1500,paris', 'charlie,120,800,london']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['charlie,10,1000,paris', 'charlie,50,2000,london', 'charlie,60,1500,paris', 'charlie,120,800,london']) == ['charlie,10,1000,paris', 'charlie,50,2000,london', 'charlie,60,1500,paris', 'charlie,120,800,london']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,10,500,seattle', 'frank,20,500,sanfrancisco', 'frank,30,1500,seattle', 'frank,90,700,sanfrancisco', 'frank,150,1200,seattle']) == ['frank,10,500,seattle', 'frank,20,500,sanfrancisco', 'frank,30,1500,seattle', 'frank,90,700,sanfrancisco', 'frank,150,1200,seattle']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,10,500,seattle', 'frank,20,500,sanfrancisco', 'frank,30,1500,seattle', 'frank,90,700,sanfrancisco', 'frank,150,1200,seattle']) == ['frank,10,500,seattle', 'frank,20,500,sanfrancisco', 'frank,30,1500,seattle', 'frank,90,700,sanfrancisco', 'frank,150,1200,seattle']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,10,1500,chicago', 'grace,20,1600,chicago', 'grace,30,1700,chicago', 'grace,40,1800,chicago', 'grace,50,1900,chicago', 'grace,60,1500,paris', 'grace,70,1600,paris', 'grace,80,1700,paris', 'grace,90,1800,paris', 'grace,100,1900,paris']) == ['grace,10,1500,chicago', 'grace,20,1600,chicago', 'grace,30,1700,chicago', 'grace,40,1800,chicago', 'grace,50,1900,chicago', 'grace,60,1500,paris', 'grace,70,1600,paris', 'grace,80,1700,paris', 'grace,90,1800,paris', 'grace,100,1900,paris']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,10,1500,chicago', 'grace,20,1600,chicago', 'grace,30,1700,chicago', 'grace,40,1800,chicago', 'grace,50,1900,chicago', 'grace,60,1500,paris', 'grace,70,1600,paris', 'grace,80,1700,paris', 'grace,90,1800,paris', 'grace,100,1900,paris']) == ['grace,10,1500,chicago', 'grace,20,1600,chicago', 'grace,30,1700,chicago', 'grace,40,1800,chicago', 'grace,50,1900,chicago', 'grace,60,1500,paris', 'grace,70,1600,paris', 'grace,80,1700,paris', 'grace,90,1800,paris', 'grace,100,1900,paris']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,10,1000,mtv', 'grace,20,1100,newyork', 'grace,30,900,beijing', 'grace,90,1100,newyork', 'grace,150,1000,beijing', 'grace,210,1500,mtv', 'grace,220,800,newyork', 'grace,300,1200,beijing', 'grace,350,1100,mtv']) == ['grace,10,1000,mtv', 'grace,20,1100,newyork', 'grace,30,900,beijing', 'grace,90,1100,newyork', 'grace,150,1000,beijing', 'grace,210,1500,mtv', 'grace,220,800,newyork', 'grace,300,1200,beijing', 'grace,350,1100,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,10,1000,mtv', 'grace,20,1100,newyork', 'grace,30,900,beijing', 'grace,90,1100,newyork', 'grace,150,1000,beijing', 'grace,210,1500,mtv', 'grace,220,800,newyork', 'grace,300,1200,beijing', 'grace,350,1100,mtv']) == ['grace,10,1000,mtv', 'grace,20,1100,newyork', 'grace,30,900,beijing', 'grace,90,1100,newyork', 'grace,150,1000,beijing', 'grace,210,1500,mtv', 'grace,220,800,newyork', 'grace,300,1200,beijing', 'grace,350,1100,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,50,1000,newyork', 'alice,70,900,beijing', 'bob,40,1000,mtv', 'bob,120,1500,newyork']) == ['alice,20,800,mtv', 'alice,50,1000,newyork', 'alice,70,900,beijing', 'bob,120,1500,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,50,1000,newyork', 'alice,70,900,beijing', 'bob,40,1000,mtv', 'bob,120,1500,newyork']) == ['alice,20,800,mtv', 'alice,50,1000,newyork', 'alice,70,900,beijing', 'bob,120,1500,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['charlie,10,1500,paris', 'charlie,20,1000,boston', 'charlie,30,500,paris', 'charlie,40,1200,newyork', 'charlie,50,800,boston']) == ['charlie,10,1500,paris', 'charlie,20,1000,boston', 'charlie,30,500,paris', 'charlie,40,1200,newyork', 'charlie,50,800,boston']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['charlie,10,1500,paris', 'charlie,20,1000,boston', 'charlie,30,500,paris', 'charlie,40,1200,newyork', 'charlie,50,800,boston']) == ['charlie,10,1500,paris', 'charlie,20,1000,boston', 'charlie,30,500,paris', 'charlie,40,1200,newyork', 'charlie,50,800,boston']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,70,1000,mtv', 'alice,130,1100,newyork', 'alice,190,900,mtv', 'alice,250,100,beijing']) == ['alice,70,1000,mtv', 'alice,130,1100,newyork', 'alice,190,900,mtv', 'alice,250,100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,70,1000,mtv', 'alice,130,1100,newyork', 'alice,190,900,mtv', 'alice,250,100,beijing']) == ['alice,70,1000,mtv', 'alice,130,1100,newyork', 'alice,190,900,mtv', 'alice,250,100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['charlie,10,900,paris', 'david,15,1100,london', 'charlie,20,700,paris', 'david,60,800,paris']) == ['david,15,1100,london', 'david,60,800,paris']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['charlie,10,900,paris', 'david,15,1100,london', 'charlie,20,700,paris', 'david,60,800,paris']) == ['david,15,1100,london', 'david,60,800,paris']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['ivan,1,1000,boston', 'ivan,10,500,boston', 'ivan,60,1500,newyork', 'ivan,65,2000,chicago', 'ivan,120,800,newyork', 'ivan,125,1200,lasvegas', 'ivan,180,600,newyork']) == ['ivan,1,1000,boston', 'ivan,10,500,boston', 'ivan,60,1500,newyork', 'ivan,65,2000,chicago', 'ivan,120,800,newyork', 'ivan,125,1200,lasvegas', 'ivan,180,600,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['ivan,1,1000,boston', 'ivan,10,500,boston', 'ivan,60,1500,newyork', 'ivan,65,2000,chicago', 'ivan,120,800,newyork', 'ivan,125,1200,lasvegas', 'ivan,180,600,newyork']) == ['ivan,1,1000,boston', 'ivan,10,500,boston', 'ivan,60,1500,newyork', 'ivan,65,2000,chicago', 'ivan,120,800,newyork', 'ivan,125,1200,lasvegas', 'ivan,180,600,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,1,1100,chicago', 'frank,10,600,chicago', 'frank,11,2000,newyork', 'frank,20,500,chicago', 'frank,30,3000,newyork', 'frank,40,1500,chicago']) == ['frank,1,1100,chicago', 'frank,10,600,chicago', 'frank,11,2000,newyork', 'frank,20,500,chicago', 'frank,30,3000,newyork', 'frank,40,1500,chicago']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,1,1100,chicago', 'frank,10,600,chicago', 'frank,11,2000,newyork', 'frank,20,500,chicago', 'frank,30,3000,newyork', 'frank,40,1500,chicago']) == ['frank,1,1100,chicago', 'frank,10,600,chicago', 'frank,11,2000,newyork', 'frank,20,500,chicago', 'frank,30,3000,newyork', 'frank,40,1500,chicago']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['charlie,10,1500,nyc', 'david,20,1100,paris', 'charlie,30,1200,nyc', 'david,40,900,london', 'charlie,60,1000,paris']) == ['charlie,10,1500,nyc', 'david,20,1100,paris', 'charlie,30,1200,nyc', 'david,40,900,london', 'charlie,60,1000,paris']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['charlie,10,1500,nyc', 'david,20,1100,paris', 'charlie,30,1200,nyc', 'david,40,900,london', 'charlie,60,1000,paris']) == ['charlie,10,1500,nyc', 'david,20,1100,paris', 'charlie,30,1200,nyc', 'david,40,900,london', 'charlie,60,1000,paris']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['dave,5,2500,london', 'eve,10,1100,london', 'dave,15,600,birmingham', 'eve,20,400,london', 'dave,25,900,glasgow', 'eve,30,1000,birmingham']) == ['dave,5,2500,london', 'eve,10,1100,london', 'dave,15,600,birmingham', 'eve,20,400,london', 'dave,25,900,glasgow', 'eve,30,1000,birmingham']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['dave,5,2500,london', 'eve,10,1100,london', 'dave,15,600,birmingham', 'eve,20,400,london', 'dave,25,900,glasgow', 'eve,30,1000,birmingham']) == ['dave,5,2500,london', 'eve,10,1100,london', 'dave,15,600,birmingham', 'eve,20,400,london', 'dave,25,900,glasgow', 'eve,30,1000,birmingham']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['hank,5,900,chicago', 'hank,35,800,chicago', 'hank,65,700,losangeles', 'hank,95,1500,chicago', 'hank,125,600,losangeles', 'hank,155,1200,chicago', 'hank,185,800,losangeles', 'hank,215,900,chicago', 'hank,245,700,losangeles', 'hank,275,1500,chicago', 'hank,305,600,losangeles', 'hank,335,1200,chicago', 'hank,365,800,losangeles', 'hank,395,900,chicago']) == ['hank,5,900,chicago', 'hank,35,800,chicago', 'hank,65,700,losangeles', 'hank,95,1500,chicago', 'hank,125,600,losangeles', 'hank,155,1200,chicago', 'hank,185,800,losangeles', 'hank,215,900,chicago', 'hank,245,700,losangeles', 'hank,275,1500,chicago', 'hank,305,600,losangeles', 'hank,335,1200,chicago', 'hank,365,800,losangeles', 'hank,395,900,chicago']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['hank,5,900,chicago', 'hank,35,800,chicago', 'hank,65,700,losangeles', 'hank,95,1500,chicago', 'hank,125,600,losangeles', 'hank,155,1200,chicago', 'hank,185,800,losangeles', 'hank,215,900,chicago', 'hank,245,700,losangeles', 'hank,275,1500,chicago', 'hank,305,600,losangeles', 'hank,335,1200,chicago', 'hank,365,800,losangeles', 'hank,395,900,chicago']) == ['hank,5,900,chicago', 'hank,35,800,chicago', 'hank,65,700,losangeles', 'hank,95,1500,chicago', 'hank,125,600,losangeles', 'hank,155,1200,chicago', 'hank,185,800,losangeles', 'hank,215,900,chicago', 'hank,245,700,losangeles', 'hank,275,1500,chicago', 'hank,305,600,losangeles', 'hank,335,1200,chicago', 'hank,365,800,losangeles', 'hank,395,900,chicago']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['heidi,1,1000,boston', 'heidi,60,1000,newyork', 'heidi,120,1000,boston', 'heidi,180,1000,newyork', 'heidi,240,1000,boston', 'heidi,300,1000,newyork']) == ['heidi,1,1000,boston', 'heidi,60,1000,newyork', 'heidi,120,1000,boston', 'heidi,180,1000,newyork', 'heidi,240,1000,boston', 'heidi,300,1000,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['heidi,1,1000,boston', 'heidi,60,1000,newyork', 'heidi,120,1000,boston', 'heidi,180,1000,newyork', 'heidi,240,1000,boston', 'heidi,300,1000,newyork']) == ['heidi,1,1000,boston', 'heidi,60,1000,newyork', 'heidi,120,1000,boston', 'heidi,180,1000,newyork', 'heidi,240,1000,boston', 'heidi,300,1000,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['heidi,10,900,berlin', 'heidi,20,1100,berlin', 'heidi,30,800,berlin', 'heidi,40,1200,munich', 'heidi,50,1000,munich', 'heidi,60,950,berlin', 'heidi,70,1050,berlin']) == ['heidi,10,900,berlin', 'heidi,20,1100,berlin', 'heidi,30,800,berlin', 'heidi,40,1200,munich', 'heidi,50,1000,munich', 'heidi,60,950,berlin', 'heidi,70,1050,berlin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['heidi,10,900,berlin', 'heidi,20,1100,berlin', 'heidi,30,800,berlin', 'heidi,40,1200,munich', 'heidi,50,1000,munich', 'heidi,60,950,berlin', 'heidi,70,1050,berlin']) == ['heidi,10,900,berlin', 'heidi,20,1100,berlin', 'heidi,30,800,berlin', 'heidi,40,1200,munich', 'heidi,50,1000,munich', 'heidi,60,950,berlin', 'heidi,70,1050,berlin']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,10,900,rome', 'grace,20,1100,rome', 'grace,30,800,rome', 'grace,40,1200,paris', 'grace,50,1000,paris', 'grace,60,950,rome']) == ['grace,10,900,rome', 'grace,20,1100,rome', 'grace,30,800,rome', 'grace,40,1200,paris', 'grace,50,1000,paris', 'grace,60,950,rome']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,10,900,rome', 'grace,20,1100,rome', 'grace,30,800,rome', 'grace,40,1200,paris', 'grace,50,1000,paris', 'grace,60,950,rome']) == ['grace,10,900,rome', 'grace,20,1100,rome', 'grace,30,800,rome', 'grace,40,1200,paris', 'grace,50,1000,paris', 'grace,60,950,rome']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,10,500,mtv', 'grace,110,600,mtv', 'grace,210,1100,newyork', 'grace,310,100,beijing', 'grace,410,1300,mtv', 'grace,510,1000,beijing']) == ['grace,210,1100,newyork', 'grace,410,1300,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,10,500,mtv', 'grace,110,600,mtv', 'grace,210,1100,newyork', 'grace,310,100,beijing', 'grace,410,1300,mtv', 'grace,510,1000,beijing']) == ['grace,210,1100,newyork', 'grace,410,1300,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['ivan,10,500,chicago', 'ivan,20,500,chicago', 'ivan,25,1000,boston', 'ivan,30,600,boston', 'ivan,85,700,chicago', 'ivan,90,2000,boston', 'ivan,140,1200,chicago', 'ivan,180,800,boston']) == ['ivan,10,500,chicago', 'ivan,20,500,chicago', 'ivan,25,1000,boston', 'ivan,30,600,boston', 'ivan,85,700,chicago', 'ivan,90,2000,boston', 'ivan,140,1200,chicago', 'ivan,180,800,boston']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['ivan,10,500,chicago', 'ivan,20,500,chicago', 'ivan,25,1000,boston', 'ivan,30,600,boston', 'ivan,85,700,chicago', 'ivan,90,2000,boston', 'ivan,140,1200,chicago', 'ivan,180,800,boston']) == ['ivan,10,500,chicago', 'ivan,20,500,chicago', 'ivan,25,1000,boston', 'ivan,30,600,boston', 'ivan,85,700,chicago', 'ivan,90,2000,boston', 'ivan,140,1200,chicago', 'ivan,180,800,boston']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,10,500,sf', 'frank,20,600,sf', 'frank,30,700,sf', 'frank,40,800,sf', 'frank,50,900,sf', 'frank,60,1000,sf', 'frank,70,1100,sf', 'frank,80,1200,sf', 'frank,90,1300,sf', 'frank,100,1400,sf']) == ['frank,90,1300,sf', 'frank,100,1400,sf', 'frank,70,1100,sf', 'frank,80,1200,sf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,10,500,sf', 'frank,20,600,sf', 'frank,30,700,sf', 'frank,40,800,sf', 'frank,50,900,sf', 'frank,60,1000,sf', 'frank,70,1100,sf', 'frank,80,1200,sf', 'frank,90,1300,sf', 'frank,100,1400,sf']) == ['frank,90,1300,sf', 'frank,100,1400,sf', 'frank,70,1100,sf', 'frank,80,1200,sf']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'alice,50,1200,beijing', 'alice,120,1000,mtv', 'bob,20,600,mtv', 'bob,80,600,newyork', 'bob,150,600,mtv']) == ['alice,20,800,mtv', 'alice,50,1200,beijing', 'bob,20,600,mtv', 'bob,80,600,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'alice,50,1200,beijing', 'alice,120,1000,mtv', 'bob,20,600,mtv', 'bob,80,600,newyork', 'bob,150,600,mtv']) == ['alice,20,800,mtv', 'alice,50,1200,beijing', 'bob,20,600,mtv', 'bob,80,600,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv', 'charlie,30,1500,newyork', 'dave,40,100,beijing', 'eve,60,900,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing']) == ['bob,50,1200,mtv', 'charlie,30,1500,newyork', 'frank,80,2000,newyork', 'grace,100,1100,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv', 'charlie,30,1500,newyork', 'dave,40,100,beijing', 'eve,60,900,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing']) == ['bob,50,1200,mtv', 'charlie,30,1500,newyork', 'frank,80,2000,newyork', 'grace,100,1100,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,1000,mtv', 'bob,20,1100,mtv', 'charlie,30,900,newyork', 'dave,40,100,beijing', 'eve,60,900,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing', 'heidi,120,1000,mtv', 'ivan,140,1200,newyork', 'juliet,160,1300,beijing', 'karen,180,1400,mtv', 'leo,200,1500,newyork', 'mike,220,1600,beijing']) == ['bob,20,1100,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing', 'ivan,140,1200,newyork', 'juliet,160,1300,beijing', 'karen,180,1400,mtv', 'leo,200,1500,newyork', 'mike,220,1600,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,1000,mtv', 'bob,20,1100,mtv', 'charlie,30,900,newyork', 'dave,40,100,beijing', 'eve,60,900,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing', 'heidi,120,1000,mtv', 'ivan,140,1200,newyork', 'juliet,160,1300,beijing', 'karen,180,1400,mtv', 'leo,200,1500,newyork', 'mike,220,1600,beijing']) == ['bob,20,1100,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing', 'ivan,140,1200,newyork', 'juliet,160,1300,beijing', 'karen,180,1400,mtv', 'leo,200,1500,newyork', 'mike,220,1600,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'charlie,30,1100,newyork', 'dave,40,100,beijing', 'eve,50,900,mtv', 'frank,60,500,newyork', 'grace,70,1500,mtv', 'heidi,80,600,beijing']) == ['charlie,30,1100,newyork', 'grace,70,1500,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'charlie,30,1100,newyork', 'dave,40,100,beijing', 'eve,50,900,mtv', 'frank,60,500,newyork', 'grace,70,1500,mtv', 'heidi,80,600,beijing']) == ['charlie,30,1100,newyork', 'grace,70,1500,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,5,300,losangeles', 'grace,10,1500,lasvegas', 'grace,15,800,lasvegas', 'grace,75,1000,losangeles', 'grace,80,600,lasvegas', 'grace,130,900,losangeles']) == ['grace,5,300,losangeles', 'grace,10,1500,lasvegas', 'grace,15,800,lasvegas', 'grace,75,1000,losangeles', 'grace,80,600,lasvegas', 'grace,130,900,losangeles']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,5,300,losangeles', 'grace,10,1500,lasvegas', 'grace,15,800,lasvegas', 'grace,75,1000,losangeles', 'grace,80,600,lasvegas', 'grace,130,900,losangeles']) == ['grace,5,300,losangeles', 'grace,10,1500,lasvegas', 'grace,15,800,lasvegas', 'grace,75,1000,losangeles', 'grace,80,600,lasvegas', 'grace,130,900,losangeles']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,5,500,mtv', 'frank,20,1500,mtv', 'frank,30,1000,newyork', 'frank,70,900,newyork', 'frank,90,800,beijing', 'frank,120,700,beijing', 'frank,150,1200,mtv', 'frank,170,1100,newyork']) == ['frank,5,500,mtv', 'frank,20,1500,mtv', 'frank,30,1000,newyork', 'frank,70,900,newyork', 'frank,90,800,beijing', 'frank,120,700,beijing', 'frank,150,1200,mtv', 'frank,170,1100,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,5,500,mtv', 'frank,20,1500,mtv', 'frank,30,1000,newyork', 'frank,70,900,newyork', 'frank,90,800,beijing', 'frank,120,700,beijing', 'frank,150,1200,mtv', 'frank,170,1100,newyork']) == ['frank,5,500,mtv', 'frank,20,1500,mtv', 'frank,30,1000,newyork', 'frank,70,900,newyork', 'frank,90,800,beijing', 'frank,120,700,beijing', 'frank,150,1200,mtv', 'frank,170,1100,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['grace,5,900,sanfrancisco', 'grace,10,1200,sanfrancisco', 'grace,20,800,sanfrancisco', 'grace,25,1000,sanfrancisco', 'grace,30,600,sanfrancisco', 'grace,40,1200,sanfrancisco']) == ['grace,10,1200,sanfrancisco', 'grace,40,1200,sanfrancisco']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['grace,5,900,sanfrancisco', 'grace,10,1200,sanfrancisco', 'grace,20,800,sanfrancisco', 'grace,25,1000,sanfrancisco', 'grace,30,600,sanfrancisco', 'grace,40,1200,sanfrancisco']) == ['grace,10,1200,sanfrancisco', 'grace,40,1200,sanfrancisco']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['eve,10,1500,mtv', 'eve,10,900,newyork', 'eve,60,1000,beijing', 'eve,110,1100,newyork', 'eve,150,1200,mtv', 'eve,200,1300,beijing']) == ['eve,10,1500,mtv', 'eve,10,900,newyork', 'eve,60,1000,beijing', 'eve,110,1100,newyork', 'eve,150,1200,mtv', 'eve,200,1300,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['eve,10,1500,mtv', 'eve,10,900,newyork', 'eve,60,1000,beijing', 'eve,110,1100,newyork', 'eve,150,1200,mtv', 'eve,200,1300,beijing']) == ['eve,10,1500,mtv', 'eve,10,900,newyork', 'eve,60,1000,beijing', 'eve,110,1100,newyork', 'eve,150,1200,mtv', 'eve,200,1300,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['eve,10,500,boston', 'eve,40,600,boston', 'eve,70,550,boston', 'eve,100,900,boston', 'eve,130,1100,boston']) == ['eve,130,1100,boston']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['eve,10,500,boston', 'eve,40,600,boston', 'eve,70,550,boston', 'eve,100,900,boston', 'eve,130,1100,boston']) == ['eve,130,1100,boston']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing', 'alice,50,900,mtv', 'alice,60,500,newyork']) == ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing', 'alice,50,900,mtv', 'alice,60,500,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing', 'alice,50,900,mtv', 'alice,60,500,newyork']) == ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing', 'alice,50,900,mtv', 'alice,60,500,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,10,1200,newyork', 'frank,40,800,chicago', 'frank,60,1500,boston', 'frank,100,1100,boston', 'frank,140,1000,chicago']) == ['frank,10,1200,newyork', 'frank,40,800,chicago', 'frank,60,1500,boston', 'frank,100,1100,boston', 'frank,140,1000,chicago']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,10,1200,newyork', 'frank,40,800,chicago', 'frank,60,1500,boston', 'frank,100,1100,boston', 'frank,140,1000,chicago']) == ['frank,10,1200,newyork', 'frank,40,800,chicago', 'frank,60,1500,boston', 'frank,100,1100,boston', 'frank,140,1000,chicago']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['charlie,10,1000,mtv', 'charlie,15,900,newyork', 'dave,30,1100,beijing', 'dave,60,1200,newyork', 'dave,80,1300,mtv']) == ['charlie,10,1000,mtv', 'charlie,15,900,newyork', 'dave,30,1100,beijing', 'dave,60,1200,newyork', 'dave,80,1300,mtv']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['charlie,10,1000,mtv', 'charlie,15,900,newyork', 'dave,30,1100,beijing', 'dave,60,1200,newyork', 'dave,80,1300,mtv']) == ['charlie,10,1000,mtv', 'charlie,15,900,newyork', 'dave,30,1100,beijing', 'dave,60,1200,newyork', 'dave,80,1300,mtv']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['hannah,10,1500,mtv', 'hannah,20,1000,beijing', 'hannah,30,1200,mtv', 'hannah,40,800,newyork', 'hannah,50,1100,mtv', 'hannah,60,900,beijing', 'hannah,70,1000,newyork', 'hannah,80,1300,mtv', 'hannah,90,1000,beijing']) == ['hannah,10,1500,mtv', 'hannah,20,1000,beijing', 'hannah,30,1200,mtv', 'hannah,40,800,newyork', 'hannah,50,1100,mtv', 'hannah,60,900,beijing', 'hannah,70,1000,newyork', 'hannah,80,1300,mtv', 'hannah,90,1000,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['hannah,10,1500,mtv', 'hannah,20,1000,beijing', 'hannah,30,1200,mtv', 'hannah,40,800,newyork', 'hannah,50,1100,mtv', 'hannah,60,900,beijing', 'hannah,70,1000,newyork', 'hannah,80,1300,mtv', 'hannah,90,1000,beijing']) == ['hannah,10,1500,mtv', 'hannah,20,1000,beijing', 'hannah,30,1200,mtv', 'hannah,40,800,newyork', 'hannah,50,1100,mtv', 'hannah,60,900,beijing', 'hannah,70,1000,newyork', 'hannah,80,1300,mtv', 'hannah,90,1000,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,1500,mtv', 'bob,20,1200,beijing', 'alice,30,1300,newyork', 'bob,40,1400,mtv', 'alice,50,1600,newyork', 'bob,60,1100,newyork']) == ['alice,10,1500,mtv', 'bob,20,1200,beijing', 'alice,30,1300,newyork', 'bob,40,1400,mtv', 'alice,50,1600,newyork', 'bob,60,1100,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,1500,mtv', 'bob,20,1200,beijing', 'alice,30,1300,newyork', 'bob,40,1400,mtv', 'alice,50,1600,newyork', 'bob,60,1100,newyork']) == ['alice,10,1500,mtv', 'bob,20,1200,beijing', 'alice,30,1300,newyork', 'bob,40,1400,mtv', 'alice,50,1600,newyork', 'bob,60,1100,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,500,mtv', 'bob,20,800,beijing', 'bob,30,1100,mtv', 'charlie,10,500,newyork', 'charlie,20,800,newyork', 'charlie,30,1100,newyork']) == ['alice,10,500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,500,mtv', 'bob,20,800,beijing', 'bob,30,1100,mtv', 'charlie,30,1100,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,500,mtv', 'bob,20,800,beijing', 'bob,30,1100,mtv', 'charlie,10,500,newyork', 'charlie,20,800,newyork', 'charlie,30,1100,newyork']) == ['alice,10,500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,500,mtv', 'bob,20,800,beijing', 'bob,30,1100,mtv', 'charlie,30,1100,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,1500,mtv', 'alice,70,900,beijing', 'bob,30,600,mtv', 'bob,100,1200,newyork', 'charlie,50,1300,mtv', 'charlie,110,1000,beijing']) == ['alice,10,1500,mtv', 'alice,70,900,beijing', 'bob,100,1200,newyork', 'charlie,50,1300,mtv', 'charlie,110,1000,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,1500,mtv', 'alice,70,900,beijing', 'bob,30,600,mtv', 'bob,100,1200,newyork', 'charlie,50,1300,mtv', 'charlie,110,1000,beijing']) == ['alice,10,1500,mtv', 'alice,70,900,beijing', 'bob,100,1200,newyork', 'charlie,50,1300,mtv', 'charlie,110,1000,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'alice,70,1500,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'charlie,30,1100,newyork', 'charlie,90,1500,newyork', 'dave,40,100,beijing', 'dave,100,1500,beijing']) == ['alice,10,500,mtv', 'alice,70,1500,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'charlie,30,1100,newyork', 'charlie,90,1500,newyork', 'dave,100,1500,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'alice,70,1500,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'charlie,30,1100,newyork', 'charlie,90,1500,newyork', 'dave,40,100,beijing', 'dave,100,1500,beijing']) == ['alice,10,500,mtv', 'alice,70,1500,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'charlie,30,1100,newyork', 'charlie,90,1500,newyork', 'dave,100,1500,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['eve,15,1200,chicago', 'eve,20,900,chicago', 'eve,75,1000,boston', 'eve,80,600,boston', 'eve,130,800,chicago']) == ['eve,15,1200,chicago', 'eve,20,900,chicago', 'eve,75,1000,boston', 'eve,80,600,boston', 'eve,130,800,chicago']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['eve,15,1200,chicago', 'eve,20,900,chicago', 'eve,75,1000,boston', 'eve,80,600,boston', 'eve,130,800,chicago']) == ['eve,15,1200,chicago', 'eve,20,900,chicago', 'eve,75,1000,boston', 'eve,80,600,boston', 'eve,130,800,chicago']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['charlie,10,1500,london', 'charlie,40,900,paris', 'charlie,90,1100,london', 'dave,20,800,berlin', 'dave,70,800,berlin', 'dave,110,800,moscow', 'eve,30,500,rome', 'eve,90,2000,venice', 'eve,150,400,london']) == ['charlie,10,1500,london', 'charlie,40,900,paris', 'charlie,90,1100,london', 'dave,70,800,berlin', 'dave,110,800,moscow', 'eve,30,500,rome', 'eve,90,2000,venice', 'eve,150,400,london']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['charlie,10,1500,london', 'charlie,40,900,paris', 'charlie,90,1100,london', 'dave,20,800,berlin', 'dave,70,800,berlin', 'dave,110,800,moscow', 'eve,30,500,rome', 'eve,90,2000,venice', 'eve,150,400,london']) == ['charlie,10,1500,london', 'charlie,40,900,paris', 'charlie,90,1100,london', 'dave,70,800,berlin', 'dave,110,800,moscow', 'eve,30,500,rome', 'eve,90,2000,venice', 'eve,150,400,london']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['heidi,1,2000,newyork', 'heidi,5,500,newyork', 'heidi,10,1000,boston', 'heidi,15,600,boston', 'heidi,30,700,newyork', 'heidi,65,2000,boston', 'heidi,120,800,newyork']) == ['heidi,1,2000,newyork', 'heidi,5,500,newyork', 'heidi,10,1000,boston', 'heidi,15,600,boston', 'heidi,30,700,newyork', 'heidi,65,2000,boston', 'heidi,120,800,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['heidi,1,2000,newyork', 'heidi,5,500,newyork', 'heidi,10,1000,boston', 'heidi,15,600,boston', 'heidi,30,700,newyork', 'heidi,65,2000,boston', 'heidi,120,800,newyork']) == ['heidi,1,2000,newyork', 'heidi,5,500,newyork', 'heidi,10,1000,boston', 'heidi,15,600,boston', 'heidi,30,700,newyork', 'heidi,65,2000,boston', 'heidi,120,800,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,1500,mtv', 'alice,15,1600,newyork', 'alice,20,1700,beijing', 'alice,25,1800,mtv', 'alice,30,1900,newyork', 'alice,35,2000,beijing']) == ['alice,10,1500,mtv', 'alice,15,1600,newyork', 'alice,20,1700,beijing', 'alice,25,1800,mtv', 'alice,30,1900,newyork', 'alice,35,2000,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,1500,mtv', 'alice,15,1600,newyork', 'alice,20,1700,beijing', 'alice,25,1800,mtv', 'alice,30,1900,newyork', 'alice,35,2000,beijing']) == ['alice,10,1500,mtv', 'alice,15,1600,newyork', 'alice,20,1700,beijing', 'alice,25,1800,mtv', 'alice,30,1900,newyork', 'alice,35,2000,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,1500,mtv', 'bob,20,800,newyork', 'alice,30,900,beijing', 'alice,60,1000,mtv', 'bob,80,1100,newyork', 'alice,120,800,mtv', 'bob,140,900,beijing']) == ['alice,10,1500,mtv', 'alice,30,900,beijing', 'alice,60,1000,mtv', 'bob,80,1100,newyork', 'bob,140,900,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,1500,mtv', 'bob,20,800,newyork', 'alice,30,900,beijing', 'alice,60,1000,mtv', 'bob,80,1100,newyork', 'alice,120,800,mtv', 'bob,140,900,beijing']) == ['alice,10,1500,mtv', 'alice,30,900,beijing', 'alice,60,1000,mtv', 'bob,80,1100,newyork', 'bob,140,900,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['frank,10,700,boston', 'frank,30,1500,boston', 'frank,60,900,boston', 'frank,90,1200,newyork', 'frank,120,1100,paris', 'frank,150,800,boston', 'frank,180,1200,boston', 'frank,210,1100,paris', 'frank,240,800,boston', 'frank,270,1500,newyork']) == ['frank,30,1500,boston', 'frank,60,900,boston', 'frank,90,1200,newyork', 'frank,120,1100,paris', 'frank,150,800,boston', 'frank,180,1200,boston', 'frank,210,1100,paris', 'frank,240,800,boston', 'frank,270,1500,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['frank,10,700,boston', 'frank,30,1500,boston', 'frank,60,900,boston', 'frank,90,1200,newyork', 'frank,120,1100,paris', 'frank,150,800,boston', 'frank,180,1200,boston', 'frank,210,1100,paris', 'frank,240,800,boston', 'frank,270,1500,newyork']) == ['frank,30,1500,boston', 'frank,60,900,boston', 'frank,90,1200,newyork', 'frank,120,1100,paris', 'frank,150,800,boston', 'frank,180,1200,boston', 'frank,210,1100,paris', 'frank,240,800,boston', 'frank,270,1500,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,5,500,mtv', 'bob,10,1500,beijing', 'alice,15,500,mtv', 'bob,20,1000,beijing', 'alice,25,500,beijing', 'bob,30,1000,newyork']) == ['alice,5,500,mtv', 'bob,10,1500,beijing', 'alice,15,500,mtv', 'bob,20,1000,beijing', 'alice,25,500,beijing', 'bob,30,1000,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,5,500,mtv', 'bob,10,1500,beijing', 'alice,15,500,mtv', 'bob,20,1000,beijing', 'alice,25,500,beijing', 'bob,30,1000,newyork']) == ['alice,5,500,mtv', 'bob,10,1500,beijing', 'alice,15,500,mtv', 'bob,20,1000,beijing', 'alice,25,500,beijing', 'bob,30,1000,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,500,mtv', 'bob,10,500,beijing', 'alice,70,1500,newyork', 'bob,70,1500,mtv', 'alice,120,2000,newyork', 'bob,120,2000,beijing']) == ['alice,10,500,mtv', 'bob,10,500,beijing', 'alice,70,1500,newyork', 'bob,70,1500,mtv', 'alice,120,2000,newyork', 'bob,120,2000,beijing']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,500,mtv', 'bob,10,500,beijing', 'alice,70,1500,newyork', 'bob,70,1500,mtv', 'alice,120,2000,newyork', 'bob,120,2000,beijing']) == ['alice,10,500,mtv', 'bob,10,500,beijing', 'alice,70,1500,newyork', 'bob,70,1500,mtv', 'alice,120,2000,newyork', 'bob,120,2000,beijing']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['alice,10,1500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,1500,newyork', 'bob,20,700,beijing', 'bob,30,900,newyork']) == ['alice,10,1500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,1500,newyork', 'bob,20,700,beijing', 'bob,30,900,newyork']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['alice,10,1500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,1500,newyork', 'bob,20,700,beijing', 'bob,30,900,newyork']) == ['alice,10,1500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,1500,newyork', 'bob,20,700,beijing', 'bob,30,900,newyork']: {e}')
    
    total += 1
    try:
        result = candidate(transactions = ['hannah,10,1000,moscow', 'hannah,20,900,moscow', 'hannah,30,800,moscow', 'hannah,40,700,moscow', 'hannah,50,600,moscow', 'hannah,60,1000,moscow', 'hannah,70,900,moscow', 'hannah,80,800,moscow', 'hannah,90,700,moscow', 'hannah,100,600,moscow', 'hannah,110,1500,paris', 'hannah,120,1600,paris', 'hannah,130,1700,paris', 'hannah,140,1800,paris', 'hannah,150,1900,paris']) == ['hannah,50,600,moscow', 'hannah,60,1000,moscow', 'hannah,70,900,moscow', 'hannah,80,800,moscow', 'hannah,90,700,moscow', 'hannah,100,600,moscow', 'hannah,110,1500,paris', 'hannah,120,1600,paris', 'hannah,130,1700,paris', 'hannah,140,1800,paris', 'hannah,150,1900,paris']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(transactions = ['hannah,10,1000,moscow', 'hannah,20,900,moscow', 'hannah,30,800,moscow', 'hannah,40,700,moscow', 'hannah,50,600,moscow', 'hannah,60,1000,moscow', 'hannah,70,900,moscow', 'hannah,80,800,moscow', 'hannah,90,700,moscow', 'hannah,100,600,moscow', 'hannah,110,1500,paris', 'hannah,120,1600,paris', 'hannah,130,1700,paris', 'hannah,140,1800,paris', 'hannah,150,1900,paris']) == ['hannah,50,600,moscow', 'hannah,60,1000,moscow', 'hannah,70,900,moscow', 'hannah,80,800,moscow', 'hannah,90,700,moscow', 'hannah,100,600,moscow', 'hannah,110,1500,paris', 'hannah,120,1600,paris', 'hannah,130,1700,paris', 'hannah,140,1800,paris', 'hannah,150,1900,paris']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,50,1200,mtv']) == ['alice,50,1200,mtv']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,beijing', 'bob,25,800,mtv', 'bob,100,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing']) == ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing']
    assert candidate(transactions = ['alice,20,1100,mtv', 'bob,50,2000,mtv', 'alice,100,1000,beijing']) == ['alice,20,1100,mtv', 'bob,50,2000,mtv']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,mtv', 'alice,61,100,mtv']) == []
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,60,100,mtv', 'alice,120,100,beijing']) == ['alice,60,100,mtv', 'alice,120,100,beijing']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,21,800,beijing']) == ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,21,800,beijing']
    assert candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv']) == ['bob,50,1200,mtv']
    assert candidate(transactions = ['alice,20,1500,mtv', 'alice,21,100,beijing', 'alice,22,2000,mtv']) == ['alice,20,1500,mtv', 'alice,21,100,beijing', 'alice,22,2000,mtv']
    assert candidate(transactions = ['alice,20,800,mtv', 'bob,20,800,mtv', 'alice,50,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']
    assert candidate(transactions = ['alice,20,1500,mtv', 'alice,25,800,mtv', 'alice,30,1200,beijing']) == ['alice,20,1500,mtv', 'alice,25,800,mtv', 'alice,30,1200,beijing']
    assert candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv', 'alice,60,1200,mtv', 'bob,120,1200,beijing']) == ['bob,50,1200,mtv', 'alice,60,1200,mtv', 'bob,120,1200,beijing']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,20,1000,mtv', 'alice,20,1001,mtv']) == ['alice,20,1001,mtv']
    assert candidate(transactions = ['alice,20,1500,mtv', 'alice,20,100,beijing', 'alice,50,1200,mtv']) == ['alice,20,1500,mtv', 'alice,20,100,beijing', 'alice,50,1200,mtv']
    assert candidate(transactions = ['alice,20,800,mtv', 'bob,20,800,mtv', 'alice,80,800,beijing']) == ['alice,20,800,mtv', 'alice,80,800,beijing']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,50,100,beijing']) == ['alice,20,800,mtv', 'alice,50,100,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing', 'dave,5,800,mtv', 'dave,7,900,newyork', 'dave,10,1000,beijing', 'dave,15,1100,mtv']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing', 'dave,5,800,mtv', 'dave,7,900,newyork', 'dave,10,1000,beijing', 'dave,15,1100,mtv']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,70,500,mtv', 'alice,130,500,newyork', 'alice,190,500,mtv', 'alice,250,500,beijing', 'bob,10,1200,newyork', 'bob,70,1200,beijing', 'bob,130,1200,mtv', 'bob,190,1200,newyork', 'bob,250,1200,beijing']) == ['alice,70,500,mtv', 'alice,130,500,newyork', 'alice,190,500,mtv', 'alice,250,500,beijing', 'bob,10,1200,newyork', 'bob,70,1200,beijing', 'bob,130,1200,mtv', 'bob,190,1200,newyork', 'bob,250,1200,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,70,600,mtv', 'alice,120,800,newyork', 'alice,130,1100,newyork']) == ['alice,70,600,mtv', 'alice,120,800,newyork', 'alice,130,1100,newyork']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,70,1500,beijing', 'alice,130,1100,mtv', 'alice,190,900,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'bob,140,1100,mtv', 'bob,200,900,beijing']) == ['alice,10,500,mtv', 'alice,70,1500,beijing', 'alice,130,1100,mtv', 'alice,190,900,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'bob,140,1100,mtv', 'bob,200,900,beijing']
    assert candidate(transactions = ['ivan,10,1300,madrid', 'ivan,40,800,madrid', 'ivan,70,1100,barcelona', 'ivan,100,1200,madrid', 'ivan,130,900,valencia', 'ivan,160,1000,madrid', 'ivan,190,800,barcelona', 'ivan,220,1500,madrid', 'ivan,250,600,valencia', 'ivan,280,1200,madrid', 'ivan,310,800,barcelona', 'ivan,340,900,madrid', 'ivan,370,700,valencia', 'ivan,400,1500,madrid']) == ['ivan,10,1300,madrid', 'ivan,40,800,madrid', 'ivan,70,1100,barcelona', 'ivan,100,1200,madrid', 'ivan,130,900,valencia', 'ivan,160,1000,madrid', 'ivan,190,800,barcelona', 'ivan,220,1500,madrid', 'ivan,250,600,valencia', 'ivan,280,1200,madrid', 'ivan,310,800,barcelona', 'ivan,340,900,madrid', 'ivan,370,700,valencia', 'ivan,400,1500,madrid']
    assert candidate(transactions = ['frank,10,1200,mtv', 'frank,20,1000,beijing', 'frank,30,1500,mtv', 'frank,40,900,newyork', 'frank,50,1100,mtv', 'frank,60,800,beijing', 'frank,70,1000,newyork']) == ['frank,10,1200,mtv', 'frank,20,1000,beijing', 'frank,30,1500,mtv', 'frank,40,900,newyork', 'frank,50,1100,mtv', 'frank,60,800,beijing', 'frank,70,1000,newyork']
    assert candidate(transactions = ['eve,5,1000,berlin', 'eve,10,100,berlin', 'eve,70,1100,berlin', 'eve,120,1200,berlin', 'eve,180,1300,berlin']) == ['eve,70,1100,berlin', 'eve,120,1200,berlin', 'eve,180,1300,berlin']
    assert candidate(transactions = ['jane,10,900,sanfrancisco', 'jane,20,1100,sanfrancisco', 'jane,30,800,sanfrancisco', 'jane,40,1200,losangeles', 'jane,50,1000,losangeles', 'jane,60,950,sanfrancisco', 'jane,70,1050,sanfrancisco', 'jane,80,850,losangeles', 'jane,90,1150,sanfrancisco']) == ['jane,10,900,sanfrancisco', 'jane,20,1100,sanfrancisco', 'jane,30,800,sanfrancisco', 'jane,40,1200,losangeles', 'jane,50,1000,losangeles', 'jane,60,950,sanfrancisco', 'jane,70,1050,sanfrancisco', 'jane,80,850,losangeles', 'jane,90,1150,sanfrancisco']
    assert candidate(transactions = ['ivan,10,900,moscow', 'ivan,20,1100,moscow', 'ivan,30,800,moscow', 'ivan,40,1200,stuttgart', 'ivan,50,1000,stuttgart', 'ivan,60,950,moscow', 'ivan,70,1050,moscow', 'ivan,80,850,stuttgart']) == ['ivan,10,900,moscow', 'ivan,20,1100,moscow', 'ivan,30,800,moscow', 'ivan,40,1200,stuttgart', 'ivan,50,1000,stuttgart', 'ivan,60,950,moscow', 'ivan,70,1050,moscow', 'ivan,80,850,stuttgart']
    assert candidate(transactions = ['eve,5,1500,mtv', 'eve,65,1100,beijing', 'eve,70,500,mtv', 'eve,130,1000,newyork', 'eve,135,800,mtv', 'eve,190,1100,beijing']) == ['eve,5,1500,mtv', 'eve,65,1100,beijing', 'eve,70,500,mtv', 'eve,130,1000,newyork', 'eve,135,800,mtv', 'eve,190,1100,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing', 'charlie,50,700,mtv', 'charlie,55,700,newyork', 'charlie,60,700,beijing']
    assert candidate(transactions = ['dave,5,500,boston', 'dave,30,1100,boston', 'dave,35,600,ny', 'dave,45,900,boston', 'dave,70,1500,ny']) == ['dave,5,500,boston', 'dave,30,1100,boston', 'dave,35,600,ny', 'dave,45,900,boston', 'dave,70,1500,ny']
    assert candidate(transactions = ['ian,10,500,tokyo', 'ian,20,600,tokyo', 'ian,30,700,tokyo', 'ian,40,800,tokyo', 'ian,50,900,tokyo', 'ian,60,1000,tokyo', 'ian,70,1100,tokyo', 'ian,80,1200,tokyo', 'ian,90,1300,tokyo', 'ian,100,1400,tokyo', 'ian,110,1500,tokyo', 'ian,120,1600,tokyo', 'ian,130,1700,tokyo', 'ian,140,1800,tokyo', 'ian,150,1900,tokyo', 'ian,160,1500,osaka', 'ian,170,1600,osaka', 'ian,180,1700,osaka', 'ian,190,1800,osaka', 'ian,200,1900,osaka']) == ['ian,70,1100,tokyo', 'ian,80,1200,tokyo', 'ian,90,1300,tokyo', 'ian,100,1400,tokyo', 'ian,110,1500,tokyo', 'ian,120,1600,tokyo', 'ian,130,1700,tokyo', 'ian,140,1800,tokyo', 'ian,150,1900,tokyo', 'ian,160,1500,osaka', 'ian,170,1600,osaka', 'ian,180,1700,osaka', 'ian,190,1800,osaka', 'ian,200,1900,osaka']
    assert candidate(transactions = ['grace,10,800,toronto', 'grace,30,700,toronto', 'grace,60,1200,vancouver', 'grace,90,600,toronto', 'grace,120,800,toronto', 'grace,150,900,montreal', 'grace,180,1500,toronto', 'grace,210,700,vancouver', 'grace,240,600,montreal', 'grace,270,1100,toronto', 'grace,300,900,vancouver', 'grace,330,800,montreal']) == ['grace,10,800,toronto', 'grace,30,700,toronto', 'grace,60,1200,vancouver', 'grace,90,600,toronto', 'grace,120,800,toronto', 'grace,150,900,montreal', 'grace,180,1500,toronto', 'grace,210,700,vancouver', 'grace,240,600,montreal', 'grace,270,1100,toronto', 'grace,300,900,vancouver', 'grace,330,800,montreal']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,10,1200,beijing', 'alice,20,500,newyork', 'bob,10,300,mtv', 'bob,11,1500,beijing']) == ['alice,10,500,mtv', 'alice,10,1200,beijing', 'alice,20,500,newyork', 'bob,10,300,mtv', 'bob,11,1500,beijing']
    assert candidate(transactions = ['charlie,10,1000,paris', 'charlie,50,2000,london', 'charlie,60,1500,paris', 'charlie,120,800,london']) == ['charlie,10,1000,paris', 'charlie,50,2000,london', 'charlie,60,1500,paris', 'charlie,120,800,london']
    assert candidate(transactions = ['frank,10,500,seattle', 'frank,20,500,sanfrancisco', 'frank,30,1500,seattle', 'frank,90,700,sanfrancisco', 'frank,150,1200,seattle']) == ['frank,10,500,seattle', 'frank,20,500,sanfrancisco', 'frank,30,1500,seattle', 'frank,90,700,sanfrancisco', 'frank,150,1200,seattle']
    assert candidate(transactions = ['grace,10,1500,chicago', 'grace,20,1600,chicago', 'grace,30,1700,chicago', 'grace,40,1800,chicago', 'grace,50,1900,chicago', 'grace,60,1500,paris', 'grace,70,1600,paris', 'grace,80,1700,paris', 'grace,90,1800,paris', 'grace,100,1900,paris']) == ['grace,10,1500,chicago', 'grace,20,1600,chicago', 'grace,30,1700,chicago', 'grace,40,1800,chicago', 'grace,50,1900,chicago', 'grace,60,1500,paris', 'grace,70,1600,paris', 'grace,80,1700,paris', 'grace,90,1800,paris', 'grace,100,1900,paris']
    assert candidate(transactions = ['grace,10,1000,mtv', 'grace,20,1100,newyork', 'grace,30,900,beijing', 'grace,90,1100,newyork', 'grace,150,1000,beijing', 'grace,210,1500,mtv', 'grace,220,800,newyork', 'grace,300,1200,beijing', 'grace,350,1100,mtv']) == ['grace,10,1000,mtv', 'grace,20,1100,newyork', 'grace,30,900,beijing', 'grace,90,1100,newyork', 'grace,150,1000,beijing', 'grace,210,1500,mtv', 'grace,220,800,newyork', 'grace,300,1200,beijing', 'grace,350,1100,mtv']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,50,1000,newyork', 'alice,70,900,beijing', 'bob,40,1000,mtv', 'bob,120,1500,newyork']) == ['alice,20,800,mtv', 'alice,50,1000,newyork', 'alice,70,900,beijing', 'bob,120,1500,newyork']
    assert candidate(transactions = ['charlie,10,1500,paris', 'charlie,20,1000,boston', 'charlie,30,500,paris', 'charlie,40,1200,newyork', 'charlie,50,800,boston']) == ['charlie,10,1500,paris', 'charlie,20,1000,boston', 'charlie,30,500,paris', 'charlie,40,1200,newyork', 'charlie,50,800,boston']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,70,1000,mtv', 'alice,130,1100,newyork', 'alice,190,900,mtv', 'alice,250,100,beijing']) == ['alice,70,1000,mtv', 'alice,130,1100,newyork', 'alice,190,900,mtv', 'alice,250,100,beijing']
    assert candidate(transactions = ['charlie,10,900,paris', 'david,15,1100,london', 'charlie,20,700,paris', 'david,60,800,paris']) == ['david,15,1100,london', 'david,60,800,paris']
    assert candidate(transactions = ['ivan,1,1000,boston', 'ivan,10,500,boston', 'ivan,60,1500,newyork', 'ivan,65,2000,chicago', 'ivan,120,800,newyork', 'ivan,125,1200,lasvegas', 'ivan,180,600,newyork']) == ['ivan,1,1000,boston', 'ivan,10,500,boston', 'ivan,60,1500,newyork', 'ivan,65,2000,chicago', 'ivan,120,800,newyork', 'ivan,125,1200,lasvegas', 'ivan,180,600,newyork']
    assert candidate(transactions = ['frank,1,1100,chicago', 'frank,10,600,chicago', 'frank,11,2000,newyork', 'frank,20,500,chicago', 'frank,30,3000,newyork', 'frank,40,1500,chicago']) == ['frank,1,1100,chicago', 'frank,10,600,chicago', 'frank,11,2000,newyork', 'frank,20,500,chicago', 'frank,30,3000,newyork', 'frank,40,1500,chicago']
    assert candidate(transactions = ['charlie,10,1500,nyc', 'david,20,1100,paris', 'charlie,30,1200,nyc', 'david,40,900,london', 'charlie,60,1000,paris']) == ['charlie,10,1500,nyc', 'david,20,1100,paris', 'charlie,30,1200,nyc', 'david,40,900,london', 'charlie,60,1000,paris']
    assert candidate(transactions = ['dave,5,2500,london', 'eve,10,1100,london', 'dave,15,600,birmingham', 'eve,20,400,london', 'dave,25,900,glasgow', 'eve,30,1000,birmingham']) == ['dave,5,2500,london', 'eve,10,1100,london', 'dave,15,600,birmingham', 'eve,20,400,london', 'dave,25,900,glasgow', 'eve,30,1000,birmingham']
    assert candidate(transactions = ['hank,5,900,chicago', 'hank,35,800,chicago', 'hank,65,700,losangeles', 'hank,95,1500,chicago', 'hank,125,600,losangeles', 'hank,155,1200,chicago', 'hank,185,800,losangeles', 'hank,215,900,chicago', 'hank,245,700,losangeles', 'hank,275,1500,chicago', 'hank,305,600,losangeles', 'hank,335,1200,chicago', 'hank,365,800,losangeles', 'hank,395,900,chicago']) == ['hank,5,900,chicago', 'hank,35,800,chicago', 'hank,65,700,losangeles', 'hank,95,1500,chicago', 'hank,125,600,losangeles', 'hank,155,1200,chicago', 'hank,185,800,losangeles', 'hank,215,900,chicago', 'hank,245,700,losangeles', 'hank,275,1500,chicago', 'hank,305,600,losangeles', 'hank,335,1200,chicago', 'hank,365,800,losangeles', 'hank,395,900,chicago']
    assert candidate(transactions = ['heidi,1,1000,boston', 'heidi,60,1000,newyork', 'heidi,120,1000,boston', 'heidi,180,1000,newyork', 'heidi,240,1000,boston', 'heidi,300,1000,newyork']) == ['heidi,1,1000,boston', 'heidi,60,1000,newyork', 'heidi,120,1000,boston', 'heidi,180,1000,newyork', 'heidi,240,1000,boston', 'heidi,300,1000,newyork']
    assert candidate(transactions = ['heidi,10,900,berlin', 'heidi,20,1100,berlin', 'heidi,30,800,berlin', 'heidi,40,1200,munich', 'heidi,50,1000,munich', 'heidi,60,950,berlin', 'heidi,70,1050,berlin']) == ['heidi,10,900,berlin', 'heidi,20,1100,berlin', 'heidi,30,800,berlin', 'heidi,40,1200,munich', 'heidi,50,1000,munich', 'heidi,60,950,berlin', 'heidi,70,1050,berlin']
    assert candidate(transactions = ['grace,10,900,rome', 'grace,20,1100,rome', 'grace,30,800,rome', 'grace,40,1200,paris', 'grace,50,1000,paris', 'grace,60,950,rome']) == ['grace,10,900,rome', 'grace,20,1100,rome', 'grace,30,800,rome', 'grace,40,1200,paris', 'grace,50,1000,paris', 'grace,60,950,rome']
    assert candidate(transactions = ['grace,10,500,mtv', 'grace,110,600,mtv', 'grace,210,1100,newyork', 'grace,310,100,beijing', 'grace,410,1300,mtv', 'grace,510,1000,beijing']) == ['grace,210,1100,newyork', 'grace,410,1300,mtv']
    assert candidate(transactions = ['ivan,10,500,chicago', 'ivan,20,500,chicago', 'ivan,25,1000,boston', 'ivan,30,600,boston', 'ivan,85,700,chicago', 'ivan,90,2000,boston', 'ivan,140,1200,chicago', 'ivan,180,800,boston']) == ['ivan,10,500,chicago', 'ivan,20,500,chicago', 'ivan,25,1000,boston', 'ivan,30,600,boston', 'ivan,85,700,chicago', 'ivan,90,2000,boston', 'ivan,140,1200,chicago', 'ivan,180,800,boston']
    assert candidate(transactions = ['frank,10,500,sf', 'frank,20,600,sf', 'frank,30,700,sf', 'frank,40,800,sf', 'frank,50,900,sf', 'frank,60,1000,sf', 'frank,70,1100,sf', 'frank,80,1200,sf', 'frank,90,1300,sf', 'frank,100,1400,sf']) == ['frank,90,1300,sf', 'frank,100,1400,sf', 'frank,70,1100,sf', 'frank,80,1200,sf']
    assert candidate(transactions = ['alice,20,800,mtv', 'alice,50,1200,beijing', 'alice,120,1000,mtv', 'bob,20,600,mtv', 'bob,80,600,newyork', 'bob,150,600,mtv']) == ['alice,20,800,mtv', 'alice,50,1200,beijing', 'bob,20,600,mtv', 'bob,80,600,newyork']
    assert candidate(transactions = ['alice,20,800,mtv', 'bob,50,1200,mtv', 'charlie,30,1500,newyork', 'dave,40,100,beijing', 'eve,60,900,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing']) == ['bob,50,1200,mtv', 'charlie,30,1500,newyork', 'frank,80,2000,newyork', 'grace,100,1100,beijing']
    assert candidate(transactions = ['alice,10,1000,mtv', 'bob,20,1100,mtv', 'charlie,30,900,newyork', 'dave,40,100,beijing', 'eve,60,900,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing', 'heidi,120,1000,mtv', 'ivan,140,1200,newyork', 'juliet,160,1300,beijing', 'karen,180,1400,mtv', 'leo,200,1500,newyork', 'mike,220,1600,beijing']) == ['bob,20,1100,mtv', 'frank,80,2000,newyork', 'grace,100,1100,beijing', 'ivan,140,1200,newyork', 'juliet,160,1300,beijing', 'karen,180,1400,mtv', 'leo,200,1500,newyork', 'mike,220,1600,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'charlie,30,1100,newyork', 'dave,40,100,beijing', 'eve,50,900,mtv', 'frank,60,500,newyork', 'grace,70,1500,mtv', 'heidi,80,600,beijing']) == ['charlie,30,1100,newyork', 'grace,70,1500,mtv']
    assert candidate(transactions = ['grace,5,300,losangeles', 'grace,10,1500,lasvegas', 'grace,15,800,lasvegas', 'grace,75,1000,losangeles', 'grace,80,600,lasvegas', 'grace,130,900,losangeles']) == ['grace,5,300,losangeles', 'grace,10,1500,lasvegas', 'grace,15,800,lasvegas', 'grace,75,1000,losangeles', 'grace,80,600,lasvegas', 'grace,130,900,losangeles']
    assert candidate(transactions = ['frank,5,500,mtv', 'frank,20,1500,mtv', 'frank,30,1000,newyork', 'frank,70,900,newyork', 'frank,90,800,beijing', 'frank,120,700,beijing', 'frank,150,1200,mtv', 'frank,170,1100,newyork']) == ['frank,5,500,mtv', 'frank,20,1500,mtv', 'frank,30,1000,newyork', 'frank,70,900,newyork', 'frank,90,800,beijing', 'frank,120,700,beijing', 'frank,150,1200,mtv', 'frank,170,1100,newyork']
    assert candidate(transactions = ['grace,5,900,sanfrancisco', 'grace,10,1200,sanfrancisco', 'grace,20,800,sanfrancisco', 'grace,25,1000,sanfrancisco', 'grace,30,600,sanfrancisco', 'grace,40,1200,sanfrancisco']) == ['grace,10,1200,sanfrancisco', 'grace,40,1200,sanfrancisco']
    assert candidate(transactions = ['eve,10,1500,mtv', 'eve,10,900,newyork', 'eve,60,1000,beijing', 'eve,110,1100,newyork', 'eve,150,1200,mtv', 'eve,200,1300,beijing']) == ['eve,10,1500,mtv', 'eve,10,900,newyork', 'eve,60,1000,beijing', 'eve,110,1100,newyork', 'eve,150,1200,mtv', 'eve,200,1300,beijing']
    assert candidate(transactions = ['eve,10,500,boston', 'eve,40,600,boston', 'eve,70,550,boston', 'eve,100,900,boston', 'eve,130,1100,boston']) == ['eve,130,1100,boston']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing', 'alice,50,900,mtv', 'alice,60,500,newyork']) == ['alice,10,500,mtv', 'bob,20,600,mtv', 'alice,30,1100,newyork', 'bob,40,100,beijing', 'alice,50,900,mtv', 'alice,60,500,newyork']
    assert candidate(transactions = ['frank,10,1200,newyork', 'frank,40,800,chicago', 'frank,60,1500,boston', 'frank,100,1100,boston', 'frank,140,1000,chicago']) == ['frank,10,1200,newyork', 'frank,40,800,chicago', 'frank,60,1500,boston', 'frank,100,1100,boston', 'frank,140,1000,chicago']
    assert candidate(transactions = ['charlie,10,1000,mtv', 'charlie,15,900,newyork', 'dave,30,1100,beijing', 'dave,60,1200,newyork', 'dave,80,1300,mtv']) == ['charlie,10,1000,mtv', 'charlie,15,900,newyork', 'dave,30,1100,beijing', 'dave,60,1200,newyork', 'dave,80,1300,mtv']
    assert candidate(transactions = ['hannah,10,1500,mtv', 'hannah,20,1000,beijing', 'hannah,30,1200,mtv', 'hannah,40,800,newyork', 'hannah,50,1100,mtv', 'hannah,60,900,beijing', 'hannah,70,1000,newyork', 'hannah,80,1300,mtv', 'hannah,90,1000,beijing']) == ['hannah,10,1500,mtv', 'hannah,20,1000,beijing', 'hannah,30,1200,mtv', 'hannah,40,800,newyork', 'hannah,50,1100,mtv', 'hannah,60,900,beijing', 'hannah,70,1000,newyork', 'hannah,80,1300,mtv', 'hannah,90,1000,beijing']
    assert candidate(transactions = ['alice,10,1500,mtv', 'bob,20,1200,beijing', 'alice,30,1300,newyork', 'bob,40,1400,mtv', 'alice,50,1600,newyork', 'bob,60,1100,newyork']) == ['alice,10,1500,mtv', 'bob,20,1200,beijing', 'alice,30,1300,newyork', 'bob,40,1400,mtv', 'alice,50,1600,newyork', 'bob,60,1100,newyork']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,500,mtv', 'bob,20,800,beijing', 'bob,30,1100,mtv', 'charlie,10,500,newyork', 'charlie,20,800,newyork', 'charlie,30,1100,newyork']) == ['alice,10,500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,500,mtv', 'bob,20,800,beijing', 'bob,30,1100,mtv', 'charlie,30,1100,newyork']
    assert candidate(transactions = ['alice,10,1500,mtv', 'alice,70,900,beijing', 'bob,30,600,mtv', 'bob,100,1200,newyork', 'charlie,50,1300,mtv', 'charlie,110,1000,beijing']) == ['alice,10,1500,mtv', 'alice,70,900,beijing', 'bob,100,1200,newyork', 'charlie,50,1300,mtv', 'charlie,110,1000,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'alice,70,1500,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'charlie,30,1100,newyork', 'charlie,90,1500,newyork', 'dave,40,100,beijing', 'dave,100,1500,beijing']) == ['alice,10,500,mtv', 'alice,70,1500,beijing', 'bob,20,600,mtv', 'bob,80,1500,beijing', 'charlie,30,1100,newyork', 'charlie,90,1500,newyork', 'dave,100,1500,beijing']
    assert candidate(transactions = ['eve,15,1200,chicago', 'eve,20,900,chicago', 'eve,75,1000,boston', 'eve,80,600,boston', 'eve,130,800,chicago']) == ['eve,15,1200,chicago', 'eve,20,900,chicago', 'eve,75,1000,boston', 'eve,80,600,boston', 'eve,130,800,chicago']
    assert candidate(transactions = ['charlie,10,1500,london', 'charlie,40,900,paris', 'charlie,90,1100,london', 'dave,20,800,berlin', 'dave,70,800,berlin', 'dave,110,800,moscow', 'eve,30,500,rome', 'eve,90,2000,venice', 'eve,150,400,london']) == ['charlie,10,1500,london', 'charlie,40,900,paris', 'charlie,90,1100,london', 'dave,70,800,berlin', 'dave,110,800,moscow', 'eve,30,500,rome', 'eve,90,2000,venice', 'eve,150,400,london']
    assert candidate(transactions = ['heidi,1,2000,newyork', 'heidi,5,500,newyork', 'heidi,10,1000,boston', 'heidi,15,600,boston', 'heidi,30,700,newyork', 'heidi,65,2000,boston', 'heidi,120,800,newyork']) == ['heidi,1,2000,newyork', 'heidi,5,500,newyork', 'heidi,10,1000,boston', 'heidi,15,600,boston', 'heidi,30,700,newyork', 'heidi,65,2000,boston', 'heidi,120,800,newyork']
    assert candidate(transactions = ['alice,10,1500,mtv', 'alice,15,1600,newyork', 'alice,20,1700,beijing', 'alice,25,1800,mtv', 'alice,30,1900,newyork', 'alice,35,2000,beijing']) == ['alice,10,1500,mtv', 'alice,15,1600,newyork', 'alice,20,1700,beijing', 'alice,25,1800,mtv', 'alice,30,1900,newyork', 'alice,35,2000,beijing']
    assert candidate(transactions = ['alice,10,1500,mtv', 'bob,20,800,newyork', 'alice,30,900,beijing', 'alice,60,1000,mtv', 'bob,80,1100,newyork', 'alice,120,800,mtv', 'bob,140,900,beijing']) == ['alice,10,1500,mtv', 'alice,30,900,beijing', 'alice,60,1000,mtv', 'bob,80,1100,newyork', 'bob,140,900,beijing']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing']) == ['alice,10,500,mtv', 'bob,10,600,mtv', 'alice,20,1200,newyork', 'bob,20,600,newyork', 'alice,30,600,beijing', 'bob,30,600,mtv', 'alice,40,600,newyork', 'bob,40,600,beijing']
    assert candidate(transactions = ['frank,10,700,boston', 'frank,30,1500,boston', 'frank,60,900,boston', 'frank,90,1200,newyork', 'frank,120,1100,paris', 'frank,150,800,boston', 'frank,180,1200,boston', 'frank,210,1100,paris', 'frank,240,800,boston', 'frank,270,1500,newyork']) == ['frank,30,1500,boston', 'frank,60,900,boston', 'frank,90,1200,newyork', 'frank,120,1100,paris', 'frank,150,800,boston', 'frank,180,1200,boston', 'frank,210,1100,paris', 'frank,240,800,boston', 'frank,270,1500,newyork']
    assert candidate(transactions = ['alice,5,500,mtv', 'bob,10,1500,beijing', 'alice,15,500,mtv', 'bob,20,1000,beijing', 'alice,25,500,beijing', 'bob,30,1000,newyork']) == ['alice,5,500,mtv', 'bob,10,1500,beijing', 'alice,15,500,mtv', 'bob,20,1000,beijing', 'alice,25,500,beijing', 'bob,30,1000,newyork']
    assert candidate(transactions = ['alice,10,500,mtv', 'bob,10,500,beijing', 'alice,70,1500,newyork', 'bob,70,1500,mtv', 'alice,120,2000,newyork', 'bob,120,2000,beijing']) == ['alice,10,500,mtv', 'bob,10,500,beijing', 'alice,70,1500,newyork', 'bob,70,1500,mtv', 'alice,120,2000,newyork', 'bob,120,2000,beijing']
    assert candidate(transactions = ['alice,10,1500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,1500,newyork', 'bob,20,700,beijing', 'bob,30,900,newyork']) == ['alice,10,1500,mtv', 'alice,20,800,beijing', 'alice,30,1100,mtv', 'bob,10,1500,newyork', 'bob,20,700,beijing', 'bob,30,900,newyork']
    assert candidate(transactions = ['hannah,10,1000,moscow', 'hannah,20,900,moscow', 'hannah,30,800,moscow', 'hannah,40,700,moscow', 'hannah,50,600,moscow', 'hannah,60,1000,moscow', 'hannah,70,900,moscow', 'hannah,80,800,moscow', 'hannah,90,700,moscow', 'hannah,100,600,moscow', 'hannah,110,1500,paris', 'hannah,120,1600,paris', 'hannah,130,1700,paris', 'hannah,140,1800,paris', 'hannah,150,1900,paris']) == ['hannah,50,600,moscow', 'hannah,60,1000,moscow', 'hannah,70,900,moscow', 'hannah,80,800,moscow', 'hannah,90,700,moscow', 'hannah,100,600,moscow', 'hannah,110,1500,paris', 'hannah,120,1600,paris', 'hannah,130,1700,paris', 'hannah,140,1800,paris', 'hannah,150,1900,paris']


