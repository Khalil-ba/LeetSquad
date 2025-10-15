def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Lily', 'Rose'],heights = [150, 145, 155]) == ['Rose', 'Zoe', 'Lily']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Lily', 'Rose'],heights = [150, 145, 155]) == ['Rose', 'Zoe', 'Lily']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Qwen', 'Alibaba', 'Cloud'],heights = [200, 190, 180]) == ['Qwen', 'Alibaba', 'Cloud']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Qwen', 'Alibaba', 'Cloud'],heights = [200, 190, 180]) == ['Qwen', 'Alibaba', 'Cloud']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ava', 'Sophia', 'Isabella'],heights = [160, 165, 170]) == ['Isabella', 'Sophia', 'Ava']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ava', 'Sophia', 'Isabella'],heights = [160, 165, 170]) == ['Isabella', 'Sophia', 'Ava']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Mary', 'John', 'Emma'],heights = [180, 165, 170]) == ['Mary', 'Emma', 'John']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Mary', 'John', 'Emma'],heights = [180, 165, 170]) == ['Mary', 'Emma', 'John']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['A', 'B', 'C', 'D'],heights = [150, 160, 170, 180]) == ['D', 'C', 'B', 'A']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['A', 'B', 'C', 'D'],heights = [150, 160, 170, 180]) == ['D', 'C', 'B', 'A']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ava', 'Ella', 'Olivia'],heights = [168, 162, 170]) == ['Olivia', 'Ava', 'Ella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ava', 'Ella', 'Olivia'],heights = [168, 162, 170]) == ['Olivia', 'Ava', 'Ella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alice', 'Bob', 'Bob'],heights = [155, 185, 150]) == ['Bob', 'Alice', 'Bob']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alice', 'Bob', 'Bob'],heights = [155, 185, 150]) == ['Bob', 'Alice', 'Bob']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Liam', 'Noah'],heights = [165, 175, 185]) == ['Noah', 'Liam', 'Zoe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Liam', 'Noah'],heights = [165, 175, 185]) == ['Noah', 'Liam', 'Zoe']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Noah', 'Liam', 'Mason'],heights = [185, 180, 175]) == ['Noah', 'Liam', 'Mason']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Noah', 'Liam', 'Mason'],heights = [185, 180, 175]) == ['Noah', 'Liam', 'Mason']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Mia', 'Ella', 'Olivia'],heights = [168, 162, 170]) == ['Olivia', 'Mia', 'Ella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Mia', 'Ella', 'Olivia'],heights = [168, 162, 170]) == ['Olivia', 'Mia', 'Ella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Tom', 'Jerry', 'Spike'],heights = [190, 160, 175]) == ['Tom', 'Spike', 'Jerry']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Tom', 'Jerry', 'Spike'],heights = [190, 160, 175]) == ['Tom', 'Spike', 'Jerry']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Liam', 'Noah'],heights = [175, 180, 165]) == ['Liam', 'Zoe', 'Noah']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Liam', 'Noah'],heights = [175, 180, 165]) == ['Liam', 'Zoe', 'Noah']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Z', 'Y', 'X'],heights = [165, 175, 185]) == ['X', 'Y', 'Z']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Z', 'Y', 'X'],heights = [165, 175, 185]) == ['X', 'Y', 'Z']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Anna', 'Elsa', 'Olaf'],heights = [170, 180, 160]) == ['Elsa', 'Anna', 'Olaf']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Anna', 'Elsa', 'Olaf'],heights = [170, 180, 160]) == ['Elsa', 'Anna', 'Olaf']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin'],heights = [179, 178, 177, 176, 175, 174, 173]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin'],heights = [179, 178, 177, 176, 175, 174, 173]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['William', 'James', 'Benjamin', 'Henry'],heights = [190, 170, 180, 160]) == ['William', 'Benjamin', 'James', 'Henry']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['William', 'James', 'Benjamin', 'Henry'],heights = [190, 170, 180, 160]) == ['William', 'Benjamin', 'James', 'Henry']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Jackson', 'Aiden', 'Mason', 'Lucas'],heights = [182, 188, 178, 180]) == ['Aiden', 'Jackson', 'Lucas', 'Mason']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Jackson', 'Aiden', 'Mason', 'Lucas'],heights = [182, 188, 178, 180]) == ['Aiden', 'Jackson', 'Lucas', 'Mason']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Dominic', 'Penelope', 'Victor', 'Emilia', 'Mason'],heights = [178, 173, 189, 169, 174]) == ['Victor', 'Dominic', 'Mason', 'Penelope', 'Emilia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Dominic', 'Penelope', 'Victor', 'Emilia', 'Mason'],heights = [178, 173, 189, 169, 174]) == ['Victor', 'Dominic', 'Mason', 'Penelope', 'Emilia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ezra', 'Isabella', 'Oliver', 'Sophia', 'Noah', 'Emma', 'James', 'Amelia', 'Benjamin', 'Ava', 'Elijah', 'Liam'],heights = [177, 165, 183, 170, 185, 171, 179, 172, 180, 167, 182, 184]) == ['Noah', 'Liam', 'Oliver', 'Elijah', 'Benjamin', 'James', 'Ezra', 'Amelia', 'Emma', 'Sophia', 'Ava', 'Isabella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ezra', 'Isabella', 'Oliver', 'Sophia', 'Noah', 'Emma', 'James', 'Amelia', 'Benjamin', 'Ava', 'Elijah', 'Liam'],heights = [177, 165, 183, 170, 185, 171, 179, 172, 180, 167, 182, 184]) == ['Noah', 'Liam', 'Oliver', 'Elijah', 'Benjamin', 'James', 'Ezra', 'Amelia', 'Emma', 'Sophia', 'Ava', 'Isabella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Daniel', 'Matthew', 'Ethan', 'Logan', 'Jackson'],heights = [175, 170, 165, 160, 155]) == ['Daniel', 'Matthew', 'Ethan', 'Logan', 'Jackson']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Daniel', 'Matthew', 'Ethan', 'Logan', 'Jackson'],heights = [175, 170, 165, 160, 155]) == ['Daniel', 'Matthew', 'Ethan', 'Logan', 'Jackson']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['William', 'James', 'George', 'Charles'],heights = [188, 192, 178, 180]) == ['James', 'William', 'Charles', 'George']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['William', 'James', 'George', 'Charles'],heights = [188, 192, 178, 180]) == ['James', 'William', 'Charles', 'George']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William'],heights = [180, 178, 175, 173, 170]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'William']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William'],heights = [180, 178, 175, 173, 170]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'William']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Jackson', 'Mia', 'Logan'],heights = [160, 200, 180, 170]) == ['Jackson', 'Mia', 'Logan', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Jackson', 'Mia', 'Logan'],heights = [160, 200, 180, 170]) == ['Jackson', 'Mia', 'Logan', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Amelia', 'Olivia', 'Emma', 'Sophia'],heights = [155, 165, 175, 185]) == ['Sophia', 'Emma', 'Olivia', 'Amelia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Amelia', 'Olivia', 'Emma', 'Sophia'],heights = [155, 165, 175, 185]) == ['Sophia', 'Emma', 'Olivia', 'Amelia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Emma', 'Noah', 'Olivia', 'Elijah', 'Ava', 'Sophia'],heights = [173, 186, 168, 183, 170, 165]) == ['Noah', 'Elijah', 'Emma', 'Ava', 'Olivia', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Emma', 'Noah', 'Olivia', 'Elijah', 'Ava', 'Sophia'],heights = [173, 186, 168, 183, 170, 165]) == ['Noah', 'Elijah', 'Emma', 'Ava', 'Olivia', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Levi', 'Carter', 'Aria', 'Sebastian', 'Avery'],heights = [175, 184, 168, 189, 176]) == ['Sebastian', 'Carter', 'Avery', 'Levi', 'Aria']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Levi', 'Carter', 'Aria', 'Sebastian', 'Avery'],heights = [175, 184, 168, 189, 176]) == ['Sebastian', 'Carter', 'Avery', 'Levi', 'Aria']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Olivia', 'Isabella', 'Ava', 'Emma'],heights = [162, 178, 168, 173, 175]) == ['Olivia', 'Emma', 'Ava', 'Isabella', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Olivia', 'Isabella', 'Ava', 'Emma'],heights = [162, 178, 168, 173, 175]) == ['Olivia', 'Emma', 'Ava', 'Isabella', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['William', 'James', 'Oliver', 'Noah', 'Elijah', 'Lucas'],heights = [195, 194, 193, 192, 191, 190]) == ['William', 'James', 'Oliver', 'Noah', 'Elijah', 'Lucas']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['William', 'James', 'Oliver', 'Noah', 'Elijah', 'Lucas'],heights = [195, 194, 193, 192, 191, 190]) == ['William', 'James', 'Oliver', 'Noah', 'Elijah', 'Lucas']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zachary', 'Christopher', 'Jonathan', 'Matthew'],heights = [195, 190, 180, 185]) == ['Zachary', 'Christopher', 'Matthew', 'Jonathan']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zachary', 'Christopher', 'Jonathan', 'Matthew'],heights = [195, 190, 180, 185]) == ['Zachary', 'Christopher', 'Matthew', 'Jonathan']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf'],heights = [160, 165, 170, 175, 180]) == ['Golf', 'Foxtrot', 'Echo', 'Delta', 'Charlie']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf'],heights = [160, 165, 170, 175, 180]) == ['Golf', 'Foxtrot', 'Echo', 'Delta', 'Charlie']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ava', 'Isabella', 'Sophia', 'Emma', 'Olivia', 'Mia'],heights = [155, 157, 158, 160, 159, 156]) == ['Emma', 'Olivia', 'Sophia', 'Isabella', 'Mia', 'Ava']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ava', 'Isabella', 'Sophia', 'Emma', 'Olivia', 'Mia'],heights = [155, 157, 158, 160, 159, 156]) == ['Emma', 'Olivia', 'Sophia', 'Isabella', 'Mia', 'Ava']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Grace', 'Heidi', 'Ivy', 'Judy', 'Kara'],heights = [158, 168, 178, 188, 198]) == ['Kara', 'Judy', 'Ivy', 'Heidi', 'Grace']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Grace', 'Heidi', 'Ivy', 'Judy', 'Kara'],heights = [158, 168, 178, 188, 198]) == ['Kara', 'Judy', 'Ivy', 'Heidi', 'Grace']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Mila', 'Aaron', 'Jasper', 'Sophie'],heights = [170, 160, 200, 180]) == ['Jasper', 'Sophie', 'Mila', 'Aaron']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Mila', 'Aaron', 'Jasper', 'Sophie'],heights = [170, 160, 200, 180]) == ['Jasper', 'Sophie', 'Mila', 'Aaron']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Finn', 'Jake', 'BMO', 'Marceline', 'LSP'],heights = [160, 170, 155, 180, 150]) == ['Marceline', 'Jake', 'Finn', 'BMO', 'LSP']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Finn', 'Jake', 'BMO', 'Marceline', 'LSP'],heights = [160, 170, 155, 180, 150]) == ['Marceline', 'Jake', 'Finn', 'BMO', 'LSP']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Chris', 'Ava', 'Ian'],heights = [165, 190, 175, 180]) == ['Chris', 'Ian', 'Ava', 'Zoe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Chris', 'Ava', 'Ian'],heights = [165, 190, 175, 180]) == ['Chris', 'Ian', 'Ava', 'Zoe']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Grace', 'Katherine', 'Ava', 'Sophie', 'Liam'],heights = [165, 172, 160, 170, 180]) == ['Liam', 'Katherine', 'Sophie', 'Grace', 'Ava']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Grace', 'Katherine', 'Ava', 'Sophie', 'Liam'],heights = [165, 172, 160, 170, 180]) == ['Liam', 'Katherine', 'Sophie', 'Grace', 'Ava']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Olivia', 'Emma', 'Ava', 'Sophia'],heights = [158, 159, 160, 157]) == ['Ava', 'Emma', 'Olivia', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Olivia', 'Emma', 'Ava', 'Sophia'],heights = [158, 159, 160, 157]) == ['Ava', 'Emma', 'Olivia', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Evelyn', 'Arthur', 'Sophie', 'Miles'],heights = [160, 190, 180, 175]) == ['Arthur', 'Sophie', 'Miles', 'Evelyn']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Evelyn', 'Arthur', 'Sophie', 'Miles'],heights = [160, 190, 180, 175]) == ['Arthur', 'Sophie', 'Miles', 'Evelyn']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ethan', 'Abigail', 'Daniel', 'Ella'],heights = [185, 168, 195, 175]) == ['Daniel', 'Ethan', 'Ella', 'Abigail']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ethan', 'Abigail', 'Daniel', 'Ella'],heights = [185, 168, 195, 175]) == ['Daniel', 'Ethan', 'Ella', 'Abigail']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ava', 'Ella', 'Scarlett', 'Grace'],heights = [185, 175, 165, 155]) == ['Ava', 'Ella', 'Scarlett', 'Grace']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ava', 'Ella', 'Scarlett', 'Grace'],heights = [185, 175, 165, 155]) == ['Ava', 'Ella', 'Scarlett', 'Grace']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Amelia', 'Olivia', 'Ava', 'Isla'],heights = [168, 169, 170, 171]) == ['Isla', 'Ava', 'Olivia', 'Amelia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Amelia', 'Olivia', 'Ava', 'Isla'],heights = [168, 169, 170, 171]) == ['Isla', 'Ava', 'Olivia', 'Amelia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Noah', 'Sophia', 'Mia', 'Ethan'],heights = [195, 180, 175, 170]) == ['Noah', 'Sophia', 'Mia', 'Ethan']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Noah', 'Sophia', 'Mia', 'Ethan'],heights = [195, 180, 175, 170]) == ['Noah', 'Sophia', 'Mia', 'Ethan']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Michael', 'Jordan', 'LeBron', 'Stephen', 'Kobe'],heights = [198, 206, 203, 191, 198]) == ['Jordan', 'LeBron', 'Michael', 'Kobe', 'Stephen']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Michael', 'Jordan', 'LeBron', 'Stephen', 'Kobe'],heights = [198, 206, 203, 191, 198]) == ['Jordan', 'LeBron', 'Michael', 'Kobe', 'Stephen']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alex', 'Brian', 'Carter', 'David', 'Ethan'],heights = [155, 165, 175, 185, 195]) == ['Ethan', 'David', 'Carter', 'Brian', 'Alex']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alex', 'Brian', 'Carter', 'David', 'Ethan'],heights = [155, 165, 175, 185, 195]) == ['Ethan', 'David', 'Carter', 'Brian', 'Alex']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Jonathan', 'Katherine', 'Lucas', 'Mia', 'Nina'],heights = [175, 165, 180, 170, 160]) == ['Lucas', 'Jonathan', 'Mia', 'Katherine', 'Nina']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Jonathan', 'Katherine', 'Lucas', 'Mia', 'Nina'],heights = [175, 165, 180, 170, 160]) == ['Lucas', 'Jonathan', 'Mia', 'Katherine', 'Nina']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Lucas', 'Hannah', 'Olivia', 'Avery'],heights = [185, 168, 190, 175]) == ['Olivia', 'Lucas', 'Avery', 'Hannah']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Lucas', 'Hannah', 'Olivia', 'Avery'],heights = [185, 168, 190, 175]) == ['Olivia', 'Lucas', 'Avery', 'Hannah']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Nina', 'Nora', 'Nina', 'Nora'],heights = [160, 162, 158, 159]) == ['Nora', 'Nina', 'Nora', 'Nina']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Nina', 'Nora', 'Nina', 'Nora'],heights = [160, 162, 158, 159]) == ['Nora', 'Nina', 'Nora', 'Nina']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Daniel', 'Matilda', 'Samuel', 'Lucas', 'Mia', 'Emily', 'Oliver', 'Ava'],heights = [182, 165, 178, 184, 170, 167, 190, 173]) == ['Oliver', 'Lucas', 'Daniel', 'Samuel', 'Ava', 'Mia', 'Emily', 'Matilda']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Daniel', 'Matilda', 'Samuel', 'Lucas', 'Mia', 'Emily', 'Oliver', 'Ava'],heights = [182, 165, 178, 184, 170, 167, 190, 173]) == ['Oliver', 'Lucas', 'Daniel', 'Samuel', 'Ava', 'Mia', 'Emily', 'Matilda']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Olivia', 'Ava', 'Isabella', 'Mia'],heights = [160, 165, 170, 175, 180]) == ['Mia', 'Isabella', 'Ava', 'Olivia', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Olivia', 'Ava', 'Isabella', 'Mia'],heights = [160, 165, 170, 175, 180]) == ['Mia', 'Isabella', 'Ava', 'Olivia', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Oliver', 'Isabella', 'Noah'],heights = [172, 180, 168, 182]) == ['Noah', 'Oliver', 'Sophia', 'Isabella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Oliver', 'Isabella', 'Noah'],heights = [172, 180, 168, 182]) == ['Noah', 'Oliver', 'Sophia', 'Isabella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Sophia', 'Ava', 'Isabella'],heights = [163, 164, 165, 162]) == ['Ava', 'Sophia', 'Zoe', 'Isabella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Sophia', 'Ava', 'Isabella'],heights = [163, 164, 165, 162]) == ['Ava', 'Sophia', 'Zoe', 'Isabella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Oliver', 'Amelia', 'Evelyn', 'Jasper'],heights = [185, 170, 180, 190]) == ['Jasper', 'Oliver', 'Evelyn', 'Amelia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Oliver', 'Amelia', 'Evelyn', 'Jasper'],heights = [185, 170, 180, 190]) == ['Jasper', 'Oliver', 'Evelyn', 'Amelia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Emily', 'Emma', 'Mia', 'Sophia', 'Isabella', 'Ava', 'Olivia'],heights = [163, 164, 162, 165, 166, 161, 160]) == ['Isabella', 'Sophia', 'Emma', 'Emily', 'Mia', 'Ava', 'Olivia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Emily', 'Emma', 'Mia', 'Sophia', 'Isabella', 'Ava', 'Olivia'],heights = [163, 164, 162, 165, 166, 161, 160]) == ['Isabella', 'Sophia', 'Emma', 'Emily', 'Mia', 'Ava', 'Olivia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Isabella', 'Sophia', 'Olivia', 'Ava', 'Emma'],heights = [162, 172, 182, 192, 202]) == ['Emma', 'Ava', 'Olivia', 'Sophia', 'Isabella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Isabella', 'Sophia', 'Olivia', 'Ava', 'Emma'],heights = [162, 172, 182, 192, 202]) == ['Emma', 'Ava', 'Olivia', 'Sophia', 'Isabella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Noah', 'Oliver', 'Lucas', 'Ethan'],heights = [200, 199, 198, 197, 196]) == ['Liam', 'Noah', 'Oliver', 'Lucas', 'Ethan']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Noah', 'Oliver', 'Lucas', 'Ethan'],heights = [200, 199, 198, 197, 196]) == ['Liam', 'Noah', 'Oliver', 'Lucas', 'Ethan']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Scarlett', 'Ava', 'Emma', 'Olivia', 'Sophia'],heights = [175, 180, 170, 165, 185]) == ['Sophia', 'Ava', 'Scarlett', 'Emma', 'Olivia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Scarlett', 'Ava', 'Emma', 'Olivia', 'Sophia'],heights = [175, 180, 170, 165, 185]) == ['Sophia', 'Ava', 'Scarlett', 'Emma', 'Olivia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Emma', 'Ava', 'Olivia', 'Isabella', 'Mia'],heights = [169, 168, 167, 166, 165, 164]) == ['Sophia', 'Emma', 'Ava', 'Olivia', 'Isabella', 'Mia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Emma', 'Ava', 'Olivia', 'Isabella', 'Mia'],heights = [169, 168, 167, 166, 165, 164]) == ['Sophia', 'Emma', 'Ava', 'Olivia', 'Isabella', 'Mia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Benjamin', 'Logan', 'Jackson', 'David', 'Aiden'],heights = [150, 160, 170, 180, 190]) == ['Aiden', 'David', 'Jackson', 'Logan', 'Benjamin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Benjamin', 'Logan', 'Jackson', 'David', 'Aiden'],heights = [150, 160, 170, 180, 190]) == ['Aiden', 'David', 'Jackson', 'Logan', 'Benjamin']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Mia', 'Evelyn', 'Abigail', 'Scarlett', 'Amelia'],heights = [180, 175, 170, 165, 160]) == ['Mia', 'Evelyn', 'Abigail', 'Scarlett', 'Amelia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Mia', 'Evelyn', 'Abigail', 'Scarlett', 'Amelia'],heights = [180, 175, 170, 165, 160]) == ['Mia', 'Evelyn', 'Abigail', 'Scarlett', 'Amelia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Camila', 'Lincoln', 'Madison', 'Isaac', 'Scarlett'],heights = [167, 187, 170, 182, 163]) == ['Lincoln', 'Isaac', 'Madison', 'Camila', 'Scarlett']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Camila', 'Lincoln', 'Madison', 'Isaac', 'Scarlett'],heights = [167, 187, 170, 182, 163]) == ['Lincoln', 'Isaac', 'Madison', 'Camila', 'Scarlett']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava', 'Mia'],heights = [162, 171, 168, 165, 169]) == ['Isabella', 'Mia', 'Olivia', 'Ava', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava', 'Mia'],heights = [162, 171, 168, 165, 169]) == ['Isabella', 'Mia', 'Olivia', 'Ava', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Theodore', 'George', 'Thomas', 'James'],heights = [175, 185, 180, 170]) == ['George', 'Thomas', 'Theodore', 'James']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Theodore', 'George', 'Thomas', 'James'],heights = [175, 185, 180, 170]) == ['George', 'Thomas', 'Theodore', 'James']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sam', 'Max', 'Leo', 'Sam'],heights = [185, 182, 179, 184]) == ['Sam', 'Sam', 'Max', 'Leo']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sam', 'Max', 'Leo', 'Sam'],heights = [185, 182, 179, 184]) == ['Sam', 'Sam', 'Max', 'Leo']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Charlotte', 'Sophia', 'Ava', 'Isabella'],heights = [165, 170, 175, 180]) == ['Isabella', 'Ava', 'Sophia', 'Charlotte']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Charlotte', 'Sophia', 'Ava', 'Isabella'],heights = [165, 170, 175, 180]) == ['Isabella', 'Ava', 'Sophia', 'Charlotte']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Charlotte', 'Amelia', 'Evelyn', 'Abigail', 'Sofia'],heights = [150, 155, 160, 165, 170]) == ['Sofia', 'Abigail', 'Evelyn', 'Amelia', 'Charlotte']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Charlotte', 'Amelia', 'Evelyn', 'Abigail', 'Sofia'],heights = [150, 155, 160, 165, 170]) == ['Sofia', 'Abigail', 'Evelyn', 'Amelia', 'Charlotte']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Lily', 'Aaron', 'Emma', 'Nolan'],heights = [165, 185, 175, 195]) == ['Nolan', 'Aaron', 'Emma', 'Lily']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Lily', 'Aaron', 'Emma', 'Nolan'],heights = [165, 185, 175, 195]) == ['Nolan', 'Aaron', 'Emma', 'Lily']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava'],heights = [165, 172, 168, 170]) == ['Isabella', 'Ava', 'Olivia', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava'],heights = [165, 172, 168, 170]) == ['Isabella', 'Ava', 'Olivia', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ethan', 'Noah', 'Liam', 'Mason'],heights = [180, 185, 170, 175]) == ['Noah', 'Ethan', 'Mason', 'Liam']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ethan', 'Noah', 'Liam', 'Mason'],heights = [180, 185, 170, 175]) == ['Noah', 'Ethan', 'Mason', 'Liam']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alexander', 'Sophia', 'Benjamin', 'Charlotte', 'Elijah', 'Mia', 'James', 'Amelia'],heights = [180, 166, 175, 168, 183, 172, 178, 171]) == ['Elijah', 'Alexander', 'James', 'Benjamin', 'Mia', 'Amelia', 'Charlotte', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alexander', 'Sophia', 'Benjamin', 'Charlotte', 'Elijah', 'Mia', 'James', 'Amelia'],heights = [180, 166, 175, 168, 183, 172, 178, 171]) == ['Elijah', 'Alexander', 'James', 'Benjamin', 'Mia', 'Amelia', 'Charlotte', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas'],heights = [187, 186, 185, 184, 183, 182]) == ['William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas'],heights = [187, 186, 185, 184, 183, 182]) == ['William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Eva', 'Nathan', 'Ella', 'Samuel', 'Sophia'],heights = [169, 179, 171, 186, 174]) == ['Samuel', 'Nathan', 'Sophia', 'Ella', 'Eva']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Eva', 'Nathan', 'Ella', 'Samuel', 'Sophia'],heights = [169, 179, 171, 186, 174]) == ['Samuel', 'Nathan', 'Sophia', 'Ella', 'Eva']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Addison', 'Mia', 'Hannah', 'Abigail'],heights = [168, 167, 166, 165, 164]) == ['Zoe', 'Addison', 'Mia', 'Hannah', 'Abigail']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Addison', 'Mia', 'Hannah', 'Abigail'],heights = [168, 167, 166, 165, 164]) == ['Zoe', 'Addison', 'Mia', 'Hannah', 'Abigail']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Benjamin', 'Olivia', 'Daniel', 'Zachary'],heights = [170, 180, 160, 190]) == ['Zachary', 'Olivia', 'Benjamin', 'Daniel']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Benjamin', 'Olivia', 'Daniel', 'Zachary'],heights = [170, 180, 160, 190]) == ['Zachary', 'Olivia', 'Benjamin', 'Daniel']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Carter', 'Jackson', 'Lucas', 'Logan', 'Benjamin'],heights = [190, 185, 180, 175, 170]) == ['Carter', 'Jackson', 'Lucas', 'Logan', 'Benjamin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Carter', 'Jackson', 'Lucas', 'Logan', 'Benjamin'],heights = [190, 185, 180, 175, 170]) == ['Carter', 'Jackson', 'Lucas', 'Logan', 'Benjamin']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Amelia', 'Oliver', 'Ava', 'Noah', 'Sophia', 'Ethan', 'Isabella', 'Elijah'],heights = [172, 188, 169, 185, 171, 182, 168, 184]) == ['Oliver', 'Noah', 'Elijah', 'Ethan', 'Amelia', 'Sophia', 'Ava', 'Isabella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Amelia', 'Oliver', 'Ava', 'Noah', 'Sophia', 'Ethan', 'Isabella', 'Elijah'],heights = [172, 188, 169, 185, 171, 182, 168, 184]) == ['Oliver', 'Noah', 'Elijah', 'Ethan', 'Amelia', 'Sophia', 'Ava', 'Isabella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley'],heights = [182, 178, 165, 180, 170]) == ['Michael', 'Matthew', 'Christopher', 'Ashley', 'Jessica']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley'],heights = [182, 178, 165, 180, 170]) == ['Michael', 'Matthew', 'Christopher', 'Ashley', 'Jessica']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Amelia', 'Sophia', 'Isabella', 'Olivia', 'Ava', 'Emma'],heights = [150, 151, 152, 153, 154, 155]) == ['Emma', 'Ava', 'Olivia', 'Isabella', 'Sophia', 'Amelia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Amelia', 'Sophia', 'Isabella', 'Olivia', 'Ava', 'Emma'],heights = [150, 151, 152, 153, 154, 155]) == ['Emma', 'Ava', 'Olivia', 'Isabella', 'Sophia', 'Amelia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Catherine', 'Margaret', 'Joan', 'Eleanor'],heights = [167, 173, 170, 169]) == ['Margaret', 'Joan', 'Eleanor', 'Catherine']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Catherine', 'Margaret', 'Joan', 'Eleanor'],heights = [167, 173, 170, 169]) == ['Margaret', 'Joan', 'Eleanor', 'Catherine']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Mason', 'Jacob', 'William', 'Ethan', 'Alexander'],heights = [155, 165, 175, 185, 195]) == ['Alexander', 'Ethan', 'William', 'Jacob', 'Mason']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Mason', 'Jacob', 'William', 'Ethan', 'Alexander'],heights = [155, 165, 175, 185, 195]) == ['Alexander', 'Ethan', 'William', 'Jacob', 'Mason']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Ava', 'Emma', 'Isabella', 'Olivia', 'Mia', 'Charlotte'],heights = [169, 168, 167, 166, 165, 164, 163]) == ['Sophia', 'Ava', 'Emma', 'Isabella', 'Olivia', 'Mia', 'Charlotte']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Ava', 'Emma', 'Isabella', 'Olivia', 'Mia', 'Charlotte'],heights = [169, 168, 167, 166, 165, 164, 163]) == ['Sophia', 'Ava', 'Emma', 'Isabella', 'Olivia', 'Mia', 'Charlotte']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Scarlett', 'Avery', 'James', 'Michael', 'Evelyn'],heights = [162, 177, 181, 180, 166]) == ['James', 'Michael', 'Avery', 'Evelyn', 'Scarlett']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Scarlett', 'Avery', 'James', 'Michael', 'Evelyn'],heights = [162, 177, 181, 180, 166]) == ['James', 'Michael', 'Avery', 'Evelyn', 'Scarlett']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Jackson', 'Ava', 'Lucas', 'Mia', 'Ethan'],heights = [160, 195, 168, 180, 170, 185]) == ['Jackson', 'Ethan', 'Lucas', 'Mia', 'Ava', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Jackson', 'Ava', 'Lucas', 'Mia', 'Ethan'],heights = [160, 195, 168, 180, 170, 185]) == ['Jackson', 'Ethan', 'Lucas', 'Mia', 'Ava', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava', 'Emma'],heights = [160, 165, 170, 175, 180]) == ['Emma', 'Ava', 'Olivia', 'Isabella', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava', 'Emma'],heights = [160, 165, 170, 175, 180]) == ['Emma', 'Ava', 'Olivia', 'Isabella', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alexander', 'Michael', 'Benjamin', 'Daniel'],heights = [190, 188, 185, 187]) == ['Alexander', 'Michael', 'Daniel', 'Benjamin']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alexander', 'Michael', 'Benjamin', 'Daniel'],heights = [190, 188, 185, 187]) == ['Alexander', 'Michael', 'Daniel', 'Benjamin']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Mia', 'Ethan', 'Amelia', 'Liam', 'Olivia'],heights = [168, 180, 169, 182, 165]) == ['Liam', 'Ethan', 'Amelia', 'Mia', 'Olivia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Mia', 'Ethan', 'Amelia', 'Liam', 'Olivia'],heights = [168, 180, 169, 182, 165]) == ['Liam', 'Ethan', 'Amelia', 'Mia', 'Olivia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Olivia', 'Ava', 'Isabella'],heights = [165, 170, 175, 180]) == ['Isabella', 'Ava', 'Olivia', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Olivia', 'Ava', 'Isabella'],heights = [165, 170, 175, 180]) == ['Isabella', 'Ava', 'Olivia', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alexander', 'Michael', 'William', 'James', 'Benjamin'],heights = [155, 190, 165, 185, 170]) == ['Michael', 'James', 'Benjamin', 'William', 'Alexander']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alexander', 'Michael', 'William', 'James', 'Benjamin'],heights = [155, 190, 165, 185, 170]) == ['Michael', 'James', 'Benjamin', 'William', 'Alexander']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Emily', 'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava'],heights = [161, 160, 159, 158, 157, 156]) == ['Emily', 'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Emily', 'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava'],heights = [161, 160, 159, 158, 157, 156]) == ['Emily', 'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Lily', 'Rosie', 'Lena'],heights = [160, 162, 158, 159]) == ['Lily', 'Zoe', 'Lena', 'Rosie']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Lily', 'Rosie', 'Lena'],heights = [160, 162, 158, 159]) == ['Lily', 'Zoe', 'Lena', 'Rosie']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Abigail', 'Daniel', 'Jackson', 'Harper'],heights = [165, 172, 179, 183, 170]) == ['Jackson', 'Daniel', 'Abigail', 'Harper', 'Zoe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Abigail', 'Daniel', 'Jackson', 'Harper'],heights = [165, 172, 179, 183, 170]) == ['Jackson', 'Daniel', 'Abigail', 'Harper', 'Zoe']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Jackson', 'Aiden', 'Lucas', 'Caleb', 'Noah'],heights = [151, 161, 171, 181, 191]) == ['Noah', 'Caleb', 'Lucas', 'Aiden', 'Jackson']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Jackson', 'Aiden', 'Lucas', 'Caleb', 'Noah'],heights = [151, 161, 171, 181, 191]) == ['Noah', 'Caleb', 'Lucas', 'Aiden', 'Jackson']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alexander', 'Noah', 'Daniel', 'Matthew', 'Logan'],heights = [182, 181, 183, 180, 179]) == ['Daniel', 'Alexander', 'Noah', 'Matthew', 'Logan']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alexander', 'Noah', 'Daniel', 'Matthew', 'Logan'],heights = [182, 181, 183, 180, 179]) == ['Daniel', 'Alexander', 'Noah', 'Matthew', 'Logan']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James'],heights = [170, 180, 190, 200, 210]) == ['James', 'Elijah', 'Oliver', 'Noah', 'Liam']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James'],heights = [170, 180, 190, 200, 210]) == ['James', 'Elijah', 'Oliver', 'Noah', 'Liam']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Lucas', 'Mason', 'Logan', 'Ethan'],heights = [178, 177, 179, 176]) == ['Logan', 'Lucas', 'Mason', 'Ethan']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Lucas', 'Mason', 'Logan', 'Ethan'],heights = [178, 177, 179, 176]) == ['Logan', 'Lucas', 'Mason', 'Ethan']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Peter', 'Paul', 'Mary', 'John', 'Jane'],heights = [175, 180, 165, 170, 160]) == ['Paul', 'Peter', 'John', 'Mary', 'Jane']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Peter', 'Paul', 'Mary', 'John', 'Jane'],heights = [175, 180, 165, 170, 160]) == ['Paul', 'Peter', 'John', 'Mary', 'Jane']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['William', 'James', 'Benjamin', 'Henry', 'Noah', 'Liam'],heights = [185, 180, 175, 170, 190, 195]) == ['Liam', 'Noah', 'William', 'James', 'Benjamin', 'Henry']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['William', 'James', 'Benjamin', 'Henry', 'Noah', 'Liam'],heights = [185, 180, 175, 170, 190, 195]) == ['Liam', 'Noah', 'William', 'James', 'Benjamin', 'Henry']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Lily', 'Ella', 'Amelia'],heights = [160, 165, 170, 175]) == ['Amelia', 'Ella', 'Lily', 'Zoe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Lily', 'Ella', 'Amelia'],heights = [160, 165, 170, 175]) == ['Amelia', 'Ella', 'Lily', 'Zoe']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Amelia', 'Connor', 'Sophia', 'Ethan'],heights = [175, 195, 180, 185]) == ['Connor', 'Ethan', 'Sophia', 'Amelia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Amelia', 'Connor', 'Sophia', 'Ethan'],heights = [175, 195, 180, 185]) == ['Connor', 'Ethan', 'Sophia', 'Amelia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['William', 'James', 'Oliver', 'Benjamin', 'Elijah'],heights = [190, 185, 180, 175, 170]) == ['William', 'James', 'Oliver', 'Benjamin', 'Elijah']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['William', 'James', 'Oliver', 'Benjamin', 'Elijah'],heights = [190, 185, 180, 175, 170]) == ['William', 'James', 'Oliver', 'Benjamin', 'Elijah']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Emily', 'Ava', 'Sophia', 'Charlotte', 'Isabella'],heights = [160, 170, 165, 155, 175]) == ['Isabella', 'Ava', 'Sophia', 'Emily', 'Charlotte']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Emily', 'Ava', 'Sophia', 'Charlotte', 'Isabella'],heights = [160, 170, 165, 155, 175]) == ['Isabella', 'Ava', 'Sophia', 'Emily', 'Charlotte']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James'],heights = [179, 178, 177, 176, 175, 174]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James'],heights = [179, 178, 177, 176, 175, 174]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Jonathan', 'Jordan', 'Jack', 'Jared', 'James', 'Jackson'],heights = [198, 197, 196, 195, 194, 193]) == ['Jonathan', 'Jordan', 'Jack', 'Jared', 'James', 'Jackson']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Jonathan', 'Jordan', 'Jack', 'Jared', 'James', 'Jackson'],heights = [198, 197, 196, 195, 194, 193]) == ['Jonathan', 'Jordan', 'Jack', 'Jared', 'James', 'Jackson']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zoe', 'Yasmin', 'Xander', 'Will', 'Vera'],heights = [150, 160, 170, 180, 190]) == ['Vera', 'Will', 'Xander', 'Yasmin', 'Zoe']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zoe', 'Yasmin', 'Xander', 'Will', 'Vera'],heights = [150, 160, 170, 180, 190]) == ['Vera', 'Will', 'Xander', 'Yasmin', 'Zoe']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Ava', 'Isabella', 'Sophia', 'Mia'],heights = [165, 175, 185, 155]) == ['Sophia', 'Isabella', 'Ava', 'Mia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Ava', 'Isabella', 'Sophia', 'Mia'],heights = [165, 175, 185, 155]) == ['Sophia', 'Isabella', 'Ava', 'Mia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zara', 'Oliver', 'Isabella', 'Charlie'],heights = [175, 190, 165, 180]) == ['Oliver', 'Charlie', 'Zara', 'Isabella']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zara', 'Oliver', 'Isabella', 'Charlie'],heights = [175, 190, 165, 180]) == ['Oliver', 'Charlie', 'Zara', 'Isabella']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alex', 'Brian', 'Craig', 'David', 'Evan'],heights = [173, 171, 175, 169, 172]) == ['Craig', 'Alex', 'Evan', 'Brian', 'David']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alex', 'Brian', 'Craig', 'David', 'Evan'],heights = [173, 171, 175, 169, 172]) == ['Craig', 'Alex', 'Evan', 'Brian', 'David']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Alexander', 'Michael', 'James', 'John', 'Daniel', 'David'],heights = [172, 171, 173, 174, 175, 176]) == ['David', 'Daniel', 'John', 'James', 'Alexander', 'Michael']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Alexander', 'Michael', 'James', 'John', 'Daniel', 'David'],heights = [172, 171, 173, 174, 175, 176]) == ['David', 'Daniel', 'John', 'James', 'Alexander', 'Michael']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Scarlett', 'William', 'Lily', 'James', 'Ava', 'Thomas', 'Ella', 'Noah', 'Ethan', 'Mia', 'Olivia'],heights = [174, 185, 167, 180, 168, 182, 170, 183, 181, 169, 165]) == ['William', 'Noah', 'Thomas', 'Ethan', 'James', 'Scarlett', 'Ella', 'Mia', 'Ava', 'Lily', 'Olivia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Scarlett', 'William', 'Lily', 'James', 'Ava', 'Thomas', 'Ella', 'Noah', 'Ethan', 'Mia', 'Olivia'],heights = [174, 185, 167, 180, 168, 182, 170, 183, 181, 169, 165]) == ['William', 'Noah', 'Thomas', 'Ethan', 'James', 'Scarlett', 'Ella', 'Mia', 'Ava', 'Lily', 'Olivia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Emma', 'Charlotte', 'Ava', 'Logan', 'Benjamin'],heights = [163, 170, 167, 178, 185]) == ['Benjamin', 'Logan', 'Charlotte', 'Ava', 'Emma']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Emma', 'Charlotte', 'Ava', 'Logan', 'Benjamin'],heights = [163, 170, 167, 178, 185]) == ['Benjamin', 'Logan', 'Charlotte', 'Ava', 'Emma']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophie', 'Grayson', 'Hannah', 'Isaac', 'Layla'],heights = [170, 185, 165, 188, 172]) == ['Isaac', 'Grayson', 'Layla', 'Sophie', 'Hannah']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophie', 'Grayson', 'Hannah', 'Isaac', 'Layla'],heights = [170, 185, 165, 188, 172]) == ['Isaac', 'Grayson', 'Layla', 'Sophie', 'Hannah']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Evelyn', 'Sophie', 'Isabella', 'Mia', 'Emma'],heights = [168, 170, 166, 165, 172]) == ['Emma', 'Sophie', 'Evelyn', 'Isabella', 'Mia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Evelyn', 'Sophie', 'Isabella', 'Mia', 'Emma'],heights = [168, 170, 166, 165, 172]) == ['Emma', 'Sophie', 'Evelyn', 'Isabella', 'Mia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Zara', 'Xander', 'Yasmin', 'Will'],heights = [160, 175, 170, 165]) == ['Xander', 'Yasmin', 'Will', 'Zara']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Zara', 'Xander', 'Yasmin', 'Will'],heights = [160, 175, 170, 165]) == ['Xander', 'Yasmin', 'Will', 'Zara']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Hannah', 'Sophie', 'Lucas'],heights = [195, 170, 180, 175]) == ['Liam', 'Sophie', 'Lucas', 'Hannah']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Hannah', 'Sophie', 'Lucas'],heights = [195, 170, 180, 175]) == ['Liam', 'Sophie', 'Lucas', 'Hannah']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Sophia', 'Elijah', 'Amelia'],heights = [181, 168, 185, 171, 183, 167, 170, 182, 173]) == ['Noah', 'Oliver', 'Elijah', 'Liam', 'Amelia', 'Emma', 'Sophia', 'Olivia', 'Ava']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Sophia', 'Elijah', 'Amelia'],heights = [181, 168, 185, 171, 183, 167, 170, 182, 173]) == ['Noah', 'Oliver', 'Elijah', 'Liam', 'Amelia', 'Emma', 'Sophia', 'Olivia', 'Ava']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Sophia', 'Ava', 'Isabella', 'Mia'],heights = [160, 170, 175, 180]) == ['Mia', 'Isabella', 'Ava', 'Sophia']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Sophia', 'Ava', 'Isabella', 'Mia'],heights = [160, 170, 175, 180]) == ['Mia', 'Isabella', 'Ava', 'Sophia']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Avery', 'Grayson', 'Evan', 'Nathan'],heights = [172, 182, 175, 180]) == ['Grayson', 'Nathan', 'Evan', 'Avery']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Avery', 'Grayson', 'Evan', 'Nathan'],heights = [172, 182, 175, 180]) == ['Grayson', 'Nathan', 'Evan', 'Avery']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Willow', 'Tara', 'Xander', 'Alyson', 'Reese'],heights = [175, 160, 170, 165, 180]) == ['Reese', 'Willow', 'Xander', 'Alyson', 'Tara']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Willow', 'Tara', 'Xander', 'Alyson', 'Reese'],heights = [175, 160, 170, 165, 180]) == ['Reese', 'Willow', 'Xander', 'Alyson', 'Tara']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Eli', 'Ella', 'Ezra', 'Emilia', 'Evan'],heights = [170, 175, 160, 180, 165]) == ['Emilia', 'Ella', 'Eli', 'Evan', 'Ezra']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Eli', 'Ella', 'Ezra', 'Emilia', 'Evan'],heights = [170, 175, 160, 180, 165]) == ['Emilia', 'Ella', 'Eli', 'Evan', 'Ezra']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['James', 'Benjamin', 'Mason', 'Noah', 'Lucas'],heights = [170, 175, 180, 185, 190]) == ['Lucas', 'Noah', 'Mason', 'Benjamin', 'James']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['James', 'Benjamin', 'Mason', 'Noah', 'Lucas'],heights = [170, 175, 180, 185, 190]) == ['Lucas', 'Noah', 'Mason', 'Benjamin', 'James']: {e}')
    
    total += 1
    try:
        result = candidate(names = ['Jack', 'Rose', 'Cal', 'Fabian', 'Molly'],heights = [170, 175, 165, 180, 160]) == ['Fabian', 'Rose', 'Jack', 'Cal', 'Molly']
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(names = ['Jack', 'Rose', 'Cal', 'Fabian', 'Molly'],heights = [170, 175, 165, 180, 160]) == ['Fabian', 'Rose', 'Jack', 'Cal', 'Molly']: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(names = ['Zoe', 'Lily', 'Rose'],heights = [150, 145, 155]) == ['Rose', 'Zoe', 'Lily']
    assert candidate(names = ['Qwen', 'Alibaba', 'Cloud'],heights = [200, 190, 180]) == ['Qwen', 'Alibaba', 'Cloud']
    assert candidate(names = ['Ava', 'Sophia', 'Isabella'],heights = [160, 165, 170]) == ['Isabella', 'Sophia', 'Ava']
    assert candidate(names = ['Mary', 'John', 'Emma'],heights = [180, 165, 170]) == ['Mary', 'Emma', 'John']
    assert candidate(names = ['A', 'B', 'C', 'D'],heights = [150, 160, 170, 180]) == ['D', 'C', 'B', 'A']
    assert candidate(names = ['Ava', 'Ella', 'Olivia'],heights = [168, 162, 170]) == ['Olivia', 'Ava', 'Ella']
    assert candidate(names = ['Alice', 'Bob', 'Bob'],heights = [155, 185, 150]) == ['Bob', 'Alice', 'Bob']
    assert candidate(names = ['Zoe', 'Liam', 'Noah'],heights = [165, 175, 185]) == ['Noah', 'Liam', 'Zoe']
    assert candidate(names = ['Noah', 'Liam', 'Mason'],heights = [185, 180, 175]) == ['Noah', 'Liam', 'Mason']
    assert candidate(names = ['Mia', 'Ella', 'Olivia'],heights = [168, 162, 170]) == ['Olivia', 'Mia', 'Ella']
    assert candidate(names = ['Tom', 'Jerry', 'Spike'],heights = [190, 160, 175]) == ['Tom', 'Spike', 'Jerry']
    assert candidate(names = ['Zoe', 'Liam', 'Noah'],heights = [175, 180, 165]) == ['Liam', 'Zoe', 'Noah']
    assert candidate(names = ['Z', 'Y', 'X'],heights = [165, 175, 185]) == ['X', 'Y', 'Z']
    assert candidate(names = ['Anna', 'Elsa', 'Olaf'],heights = [170, 180, 160]) == ['Elsa', 'Anna', 'Olaf']
    assert candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin'],heights = [179, 178, 177, 176, 175, 174, 173]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin']
    assert candidate(names = ['William', 'James', 'Benjamin', 'Henry'],heights = [190, 170, 180, 160]) == ['William', 'Benjamin', 'James', 'Henry']
    assert candidate(names = ['Jackson', 'Aiden', 'Mason', 'Lucas'],heights = [182, 188, 178, 180]) == ['Aiden', 'Jackson', 'Lucas', 'Mason']
    assert candidate(names = ['Dominic', 'Penelope', 'Victor', 'Emilia', 'Mason'],heights = [178, 173, 189, 169, 174]) == ['Victor', 'Dominic', 'Mason', 'Penelope', 'Emilia']
    assert candidate(names = ['Ezra', 'Isabella', 'Oliver', 'Sophia', 'Noah', 'Emma', 'James', 'Amelia', 'Benjamin', 'Ava', 'Elijah', 'Liam'],heights = [177, 165, 183, 170, 185, 171, 179, 172, 180, 167, 182, 184]) == ['Noah', 'Liam', 'Oliver', 'Elijah', 'Benjamin', 'James', 'Ezra', 'Amelia', 'Emma', 'Sophia', 'Ava', 'Isabella']
    assert candidate(names = ['Daniel', 'Matthew', 'Ethan', 'Logan', 'Jackson'],heights = [175, 170, 165, 160, 155]) == ['Daniel', 'Matthew', 'Ethan', 'Logan', 'Jackson']
    assert candidate(names = ['William', 'James', 'George', 'Charles'],heights = [188, 192, 178, 180]) == ['James', 'William', 'Charles', 'George']
    assert candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William'],heights = [180, 178, 175, 173, 170]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'William']
    assert candidate(names = ['Sophia', 'Jackson', 'Mia', 'Logan'],heights = [160, 200, 180, 170]) == ['Jackson', 'Mia', 'Logan', 'Sophia']
    assert candidate(names = ['Amelia', 'Olivia', 'Emma', 'Sophia'],heights = [155, 165, 175, 185]) == ['Sophia', 'Emma', 'Olivia', 'Amelia']
    assert candidate(names = ['Emma', 'Noah', 'Olivia', 'Elijah', 'Ava', 'Sophia'],heights = [173, 186, 168, 183, 170, 165]) == ['Noah', 'Elijah', 'Emma', 'Ava', 'Olivia', 'Sophia']
    assert candidate(names = ['Levi', 'Carter', 'Aria', 'Sebastian', 'Avery'],heights = [175, 184, 168, 189, 176]) == ['Sebastian', 'Carter', 'Avery', 'Levi', 'Aria']
    assert candidate(names = ['Sophia', 'Olivia', 'Isabella', 'Ava', 'Emma'],heights = [162, 178, 168, 173, 175]) == ['Olivia', 'Emma', 'Ava', 'Isabella', 'Sophia']
    assert candidate(names = ['William', 'James', 'Oliver', 'Noah', 'Elijah', 'Lucas'],heights = [195, 194, 193, 192, 191, 190]) == ['William', 'James', 'Oliver', 'Noah', 'Elijah', 'Lucas']
    assert candidate(names = ['Zachary', 'Christopher', 'Jonathan', 'Matthew'],heights = [195, 190, 180, 185]) == ['Zachary', 'Christopher', 'Matthew', 'Jonathan']
    assert candidate(names = ['Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf'],heights = [160, 165, 170, 175, 180]) == ['Golf', 'Foxtrot', 'Echo', 'Delta', 'Charlie']
    assert candidate(names = ['Ava', 'Isabella', 'Sophia', 'Emma', 'Olivia', 'Mia'],heights = [155, 157, 158, 160, 159, 156]) == ['Emma', 'Olivia', 'Sophia', 'Isabella', 'Mia', 'Ava']
    assert candidate(names = ['Grace', 'Heidi', 'Ivy', 'Judy', 'Kara'],heights = [158, 168, 178, 188, 198]) == ['Kara', 'Judy', 'Ivy', 'Heidi', 'Grace']
    assert candidate(names = ['Mila', 'Aaron', 'Jasper', 'Sophie'],heights = [170, 160, 200, 180]) == ['Jasper', 'Sophie', 'Mila', 'Aaron']
    assert candidate(names = ['Finn', 'Jake', 'BMO', 'Marceline', 'LSP'],heights = [160, 170, 155, 180, 150]) == ['Marceline', 'Jake', 'Finn', 'BMO', 'LSP']
    assert candidate(names = ['Zoe', 'Chris', 'Ava', 'Ian'],heights = [165, 190, 175, 180]) == ['Chris', 'Ian', 'Ava', 'Zoe']
    assert candidate(names = ['Grace', 'Katherine', 'Ava', 'Sophie', 'Liam'],heights = [165, 172, 160, 170, 180]) == ['Liam', 'Katherine', 'Sophie', 'Grace', 'Ava']
    assert candidate(names = ['Olivia', 'Emma', 'Ava', 'Sophia'],heights = [158, 159, 160, 157]) == ['Ava', 'Emma', 'Olivia', 'Sophia']
    assert candidate(names = ['Evelyn', 'Arthur', 'Sophie', 'Miles'],heights = [160, 190, 180, 175]) == ['Arthur', 'Sophie', 'Miles', 'Evelyn']
    assert candidate(names = ['Ethan', 'Abigail', 'Daniel', 'Ella'],heights = [185, 168, 195, 175]) == ['Daniel', 'Ethan', 'Ella', 'Abigail']
    assert candidate(names = ['Ava', 'Ella', 'Scarlett', 'Grace'],heights = [185, 175, 165, 155]) == ['Ava', 'Ella', 'Scarlett', 'Grace']
    assert candidate(names = ['Amelia', 'Olivia', 'Ava', 'Isla'],heights = [168, 169, 170, 171]) == ['Isla', 'Ava', 'Olivia', 'Amelia']
    assert candidate(names = ['Noah', 'Sophia', 'Mia', 'Ethan'],heights = [195, 180, 175, 170]) == ['Noah', 'Sophia', 'Mia', 'Ethan']
    assert candidate(names = ['Michael', 'Jordan', 'LeBron', 'Stephen', 'Kobe'],heights = [198, 206, 203, 191, 198]) == ['Jordan', 'LeBron', 'Michael', 'Kobe', 'Stephen']
    assert candidate(names = ['Alex', 'Brian', 'Carter', 'David', 'Ethan'],heights = [155, 165, 175, 185, 195]) == ['Ethan', 'David', 'Carter', 'Brian', 'Alex']
    assert candidate(names = ['Jonathan', 'Katherine', 'Lucas', 'Mia', 'Nina'],heights = [175, 165, 180, 170, 160]) == ['Lucas', 'Jonathan', 'Mia', 'Katherine', 'Nina']
    assert candidate(names = ['Lucas', 'Hannah', 'Olivia', 'Avery'],heights = [185, 168, 190, 175]) == ['Olivia', 'Lucas', 'Avery', 'Hannah']
    assert candidate(names = ['Nina', 'Nora', 'Nina', 'Nora'],heights = [160, 162, 158, 159]) == ['Nora', 'Nina', 'Nora', 'Nina']
    assert candidate(names = ['Daniel', 'Matilda', 'Samuel', 'Lucas', 'Mia', 'Emily', 'Oliver', 'Ava'],heights = [182, 165, 178, 184, 170, 167, 190, 173]) == ['Oliver', 'Lucas', 'Daniel', 'Samuel', 'Ava', 'Mia', 'Emily', 'Matilda']
    assert candidate(names = ['Sophia', 'Olivia', 'Ava', 'Isabella', 'Mia'],heights = [160, 165, 170, 175, 180]) == ['Mia', 'Isabella', 'Ava', 'Olivia', 'Sophia']
    assert candidate(names = ['Sophia', 'Oliver', 'Isabella', 'Noah'],heights = [172, 180, 168, 182]) == ['Noah', 'Oliver', 'Sophia', 'Isabella']
    assert candidate(names = ['Zoe', 'Sophia', 'Ava', 'Isabella'],heights = [163, 164, 165, 162]) == ['Ava', 'Sophia', 'Zoe', 'Isabella']
    assert candidate(names = ['Oliver', 'Amelia', 'Evelyn', 'Jasper'],heights = [185, 170, 180, 190]) == ['Jasper', 'Oliver', 'Evelyn', 'Amelia']
    assert candidate(names = ['Emily', 'Emma', 'Mia', 'Sophia', 'Isabella', 'Ava', 'Olivia'],heights = [163, 164, 162, 165, 166, 161, 160]) == ['Isabella', 'Sophia', 'Emma', 'Emily', 'Mia', 'Ava', 'Olivia']
    assert candidate(names = ['Isabella', 'Sophia', 'Olivia', 'Ava', 'Emma'],heights = [162, 172, 182, 192, 202]) == ['Emma', 'Ava', 'Olivia', 'Sophia', 'Isabella']
    assert candidate(names = ['Liam', 'Noah', 'Oliver', 'Lucas', 'Ethan'],heights = [200, 199, 198, 197, 196]) == ['Liam', 'Noah', 'Oliver', 'Lucas', 'Ethan']
    assert candidate(names = ['Scarlett', 'Ava', 'Emma', 'Olivia', 'Sophia'],heights = [175, 180, 170, 165, 185]) == ['Sophia', 'Ava', 'Scarlett', 'Emma', 'Olivia']
    assert candidate(names = ['Sophia', 'Emma', 'Ava', 'Olivia', 'Isabella', 'Mia'],heights = [169, 168, 167, 166, 165, 164]) == ['Sophia', 'Emma', 'Ava', 'Olivia', 'Isabella', 'Mia']
    assert candidate(names = ['Benjamin', 'Logan', 'Jackson', 'David', 'Aiden'],heights = [150, 160, 170, 180, 190]) == ['Aiden', 'David', 'Jackson', 'Logan', 'Benjamin']
    assert candidate(names = ['Mia', 'Evelyn', 'Abigail', 'Scarlett', 'Amelia'],heights = [180, 175, 170, 165, 160]) == ['Mia', 'Evelyn', 'Abigail', 'Scarlett', 'Amelia']
    assert candidate(names = ['Camila', 'Lincoln', 'Madison', 'Isaac', 'Scarlett'],heights = [167, 187, 170, 182, 163]) == ['Lincoln', 'Isaac', 'Madison', 'Camila', 'Scarlett']
    assert candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava', 'Mia'],heights = [162, 171, 168, 165, 169]) == ['Isabella', 'Mia', 'Olivia', 'Ava', 'Sophia']
    assert candidate(names = ['Theodore', 'George', 'Thomas', 'James'],heights = [175, 185, 180, 170]) == ['George', 'Thomas', 'Theodore', 'James']
    assert candidate(names = ['Sam', 'Max', 'Leo', 'Sam'],heights = [185, 182, 179, 184]) == ['Sam', 'Sam', 'Max', 'Leo']
    assert candidate(names = ['Charlotte', 'Sophia', 'Ava', 'Isabella'],heights = [165, 170, 175, 180]) == ['Isabella', 'Ava', 'Sophia', 'Charlotte']
    assert candidate(names = ['Charlotte', 'Amelia', 'Evelyn', 'Abigail', 'Sofia'],heights = [150, 155, 160, 165, 170]) == ['Sofia', 'Abigail', 'Evelyn', 'Amelia', 'Charlotte']
    assert candidate(names = ['Lily', 'Aaron', 'Emma', 'Nolan'],heights = [165, 185, 175, 195]) == ['Nolan', 'Aaron', 'Emma', 'Lily']
    assert candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava'],heights = [165, 172, 168, 170]) == ['Isabella', 'Ava', 'Olivia', 'Sophia']
    assert candidate(names = ['Ethan', 'Noah', 'Liam', 'Mason'],heights = [180, 185, 170, 175]) == ['Noah', 'Ethan', 'Mason', 'Liam']
    assert candidate(names = ['Alexander', 'Sophia', 'Benjamin', 'Charlotte', 'Elijah', 'Mia', 'James', 'Amelia'],heights = [180, 166, 175, 168, 183, 172, 178, 171]) == ['Elijah', 'Alexander', 'James', 'Benjamin', 'Mia', 'Amelia', 'Charlotte', 'Sophia']
    assert candidate(names = ['William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas'],heights = [187, 186, 185, 184, 183, 182]) == ['William', 'James', 'Oliver', 'Benjamin', 'Elijah', 'Lucas']
    assert candidate(names = ['Eva', 'Nathan', 'Ella', 'Samuel', 'Sophia'],heights = [169, 179, 171, 186, 174]) == ['Samuel', 'Nathan', 'Sophia', 'Ella', 'Eva']
    assert candidate(names = ['Zoe', 'Addison', 'Mia', 'Hannah', 'Abigail'],heights = [168, 167, 166, 165, 164]) == ['Zoe', 'Addison', 'Mia', 'Hannah', 'Abigail']
    assert candidate(names = ['Benjamin', 'Olivia', 'Daniel', 'Zachary'],heights = [170, 180, 160, 190]) == ['Zachary', 'Olivia', 'Benjamin', 'Daniel']
    assert candidate(names = ['Carter', 'Jackson', 'Lucas', 'Logan', 'Benjamin'],heights = [190, 185, 180, 175, 170]) == ['Carter', 'Jackson', 'Lucas', 'Logan', 'Benjamin']
    assert candidate(names = ['Amelia', 'Oliver', 'Ava', 'Noah', 'Sophia', 'Ethan', 'Isabella', 'Elijah'],heights = [172, 188, 169, 185, 171, 182, 168, 184]) == ['Oliver', 'Noah', 'Elijah', 'Ethan', 'Amelia', 'Sophia', 'Ava', 'Isabella']
    assert candidate(names = ['Michael', 'Christopher', 'Jessica', 'Matthew', 'Ashley'],heights = [182, 178, 165, 180, 170]) == ['Michael', 'Matthew', 'Christopher', 'Ashley', 'Jessica']
    assert candidate(names = ['Amelia', 'Sophia', 'Isabella', 'Olivia', 'Ava', 'Emma'],heights = [150, 151, 152, 153, 154, 155]) == ['Emma', 'Ava', 'Olivia', 'Isabella', 'Sophia', 'Amelia']
    assert candidate(names = ['Catherine', 'Margaret', 'Joan', 'Eleanor'],heights = [167, 173, 170, 169]) == ['Margaret', 'Joan', 'Eleanor', 'Catherine']
    assert candidate(names = ['Mason', 'Jacob', 'William', 'Ethan', 'Alexander'],heights = [155, 165, 175, 185, 195]) == ['Alexander', 'Ethan', 'William', 'Jacob', 'Mason']
    assert candidate(names = ['Sophia', 'Ava', 'Emma', 'Isabella', 'Olivia', 'Mia', 'Charlotte'],heights = [169, 168, 167, 166, 165, 164, 163]) == ['Sophia', 'Ava', 'Emma', 'Isabella', 'Olivia', 'Mia', 'Charlotte']
    assert candidate(names = ['Scarlett', 'Avery', 'James', 'Michael', 'Evelyn'],heights = [162, 177, 181, 180, 166]) == ['James', 'Michael', 'Avery', 'Evelyn', 'Scarlett']
    assert candidate(names = ['Sophia', 'Jackson', 'Ava', 'Lucas', 'Mia', 'Ethan'],heights = [160, 195, 168, 180, 170, 185]) == ['Jackson', 'Ethan', 'Lucas', 'Mia', 'Ava', 'Sophia']
    assert candidate(names = ['Sophia', 'Isabella', 'Olivia', 'Ava', 'Emma'],heights = [160, 165, 170, 175, 180]) == ['Emma', 'Ava', 'Olivia', 'Isabella', 'Sophia']
    assert candidate(names = ['Alexander', 'Michael', 'Benjamin', 'Daniel'],heights = [190, 188, 185, 187]) == ['Alexander', 'Michael', 'Daniel', 'Benjamin']
    assert candidate(names = ['Mia', 'Ethan', 'Amelia', 'Liam', 'Olivia'],heights = [168, 180, 169, 182, 165]) == ['Liam', 'Ethan', 'Amelia', 'Mia', 'Olivia']
    assert candidate(names = ['Sophia', 'Olivia', 'Ava', 'Isabella'],heights = [165, 170, 175, 180]) == ['Isabella', 'Ava', 'Olivia', 'Sophia']
    assert candidate(names = ['Alexander', 'Michael', 'William', 'James', 'Benjamin'],heights = [155, 190, 165, 185, 170]) == ['Michael', 'James', 'Benjamin', 'William', 'Alexander']
    assert candidate(names = ['Emily', 'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava'],heights = [161, 160, 159, 158, 157, 156]) == ['Emily', 'Emma', 'Sophia', 'Olivia', 'Isabella', 'Ava']
    assert candidate(names = ['Zoe', 'Lily', 'Rosie', 'Lena'],heights = [160, 162, 158, 159]) == ['Lily', 'Zoe', 'Lena', 'Rosie']
    assert candidate(names = ['Zoe', 'Abigail', 'Daniel', 'Jackson', 'Harper'],heights = [165, 172, 179, 183, 170]) == ['Jackson', 'Daniel', 'Abigail', 'Harper', 'Zoe']
    assert candidate(names = ['Jackson', 'Aiden', 'Lucas', 'Caleb', 'Noah'],heights = [151, 161, 171, 181, 191]) == ['Noah', 'Caleb', 'Lucas', 'Aiden', 'Jackson']
    assert candidate(names = ['Alexander', 'Noah', 'Daniel', 'Matthew', 'Logan'],heights = [182, 181, 183, 180, 179]) == ['Daniel', 'Alexander', 'Noah', 'Matthew', 'Logan']
    assert candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'James'],heights = [170, 180, 190, 200, 210]) == ['James', 'Elijah', 'Oliver', 'Noah', 'Liam']
    assert candidate(names = ['Lucas', 'Mason', 'Logan', 'Ethan'],heights = [178, 177, 179, 176]) == ['Logan', 'Lucas', 'Mason', 'Ethan']
    assert candidate(names = ['Peter', 'Paul', 'Mary', 'John', 'Jane'],heights = [175, 180, 165, 170, 160]) == ['Paul', 'Peter', 'John', 'Mary', 'Jane']
    assert candidate(names = ['William', 'James', 'Benjamin', 'Henry', 'Noah', 'Liam'],heights = [185, 180, 175, 170, 190, 195]) == ['Liam', 'Noah', 'William', 'James', 'Benjamin', 'Henry']
    assert candidate(names = ['Zoe', 'Lily', 'Ella', 'Amelia'],heights = [160, 165, 170, 175]) == ['Amelia', 'Ella', 'Lily', 'Zoe']
    assert candidate(names = ['Amelia', 'Connor', 'Sophia', 'Ethan'],heights = [175, 195, 180, 185]) == ['Connor', 'Ethan', 'Sophia', 'Amelia']
    assert candidate(names = ['William', 'James', 'Oliver', 'Benjamin', 'Elijah'],heights = [190, 185, 180, 175, 170]) == ['William', 'James', 'Oliver', 'Benjamin', 'Elijah']
    assert candidate(names = ['Emily', 'Ava', 'Sophia', 'Charlotte', 'Isabella'],heights = [160, 170, 165, 155, 175]) == ['Isabella', 'Ava', 'Sophia', 'Emily', 'Charlotte']
    assert candidate(names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James'],heights = [179, 178, 177, 176, 175, 174]) == ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James']
    assert candidate(names = ['Jonathan', 'Jordan', 'Jack', 'Jared', 'James', 'Jackson'],heights = [198, 197, 196, 195, 194, 193]) == ['Jonathan', 'Jordan', 'Jack', 'Jared', 'James', 'Jackson']
    assert candidate(names = ['Zoe', 'Yasmin', 'Xander', 'Will', 'Vera'],heights = [150, 160, 170, 180, 190]) == ['Vera', 'Will', 'Xander', 'Yasmin', 'Zoe']
    assert candidate(names = ['Ava', 'Isabella', 'Sophia', 'Mia'],heights = [165, 175, 185, 155]) == ['Sophia', 'Isabella', 'Ava', 'Mia']
    assert candidate(names = ['Zara', 'Oliver', 'Isabella', 'Charlie'],heights = [175, 190, 165, 180]) == ['Oliver', 'Charlie', 'Zara', 'Isabella']
    assert candidate(names = ['Alex', 'Brian', 'Craig', 'David', 'Evan'],heights = [173, 171, 175, 169, 172]) == ['Craig', 'Alex', 'Evan', 'Brian', 'David']
    assert candidate(names = ['Alexander', 'Michael', 'James', 'John', 'Daniel', 'David'],heights = [172, 171, 173, 174, 175, 176]) == ['David', 'Daniel', 'John', 'James', 'Alexander', 'Michael']
    assert candidate(names = ['Scarlett', 'William', 'Lily', 'James', 'Ava', 'Thomas', 'Ella', 'Noah', 'Ethan', 'Mia', 'Olivia'],heights = [174, 185, 167, 180, 168, 182, 170, 183, 181, 169, 165]) == ['William', 'Noah', 'Thomas', 'Ethan', 'James', 'Scarlett', 'Ella', 'Mia', 'Ava', 'Lily', 'Olivia']
    assert candidate(names = ['Emma', 'Charlotte', 'Ava', 'Logan', 'Benjamin'],heights = [163, 170, 167, 178, 185]) == ['Benjamin', 'Logan', 'Charlotte', 'Ava', 'Emma']
    assert candidate(names = ['Sophie', 'Grayson', 'Hannah', 'Isaac', 'Layla'],heights = [170, 185, 165, 188, 172]) == ['Isaac', 'Grayson', 'Layla', 'Sophie', 'Hannah']
    assert candidate(names = ['Evelyn', 'Sophie', 'Isabella', 'Mia', 'Emma'],heights = [168, 170, 166, 165, 172]) == ['Emma', 'Sophie', 'Evelyn', 'Isabella', 'Mia']
    assert candidate(names = ['Zara', 'Xander', 'Yasmin', 'Will'],heights = [160, 175, 170, 165]) == ['Xander', 'Yasmin', 'Will', 'Zara']
    assert candidate(names = ['Liam', 'Hannah', 'Sophie', 'Lucas'],heights = [195, 170, 180, 175]) == ['Liam', 'Sophie', 'Lucas', 'Hannah']
    assert candidate(names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Sophia', 'Elijah', 'Amelia'],heights = [181, 168, 185, 171, 183, 167, 170, 182, 173]) == ['Noah', 'Oliver', 'Elijah', 'Liam', 'Amelia', 'Emma', 'Sophia', 'Olivia', 'Ava']
    assert candidate(names = ['Sophia', 'Ava', 'Isabella', 'Mia'],heights = [160, 170, 175, 180]) == ['Mia', 'Isabella', 'Ava', 'Sophia']
    assert candidate(names = ['Avery', 'Grayson', 'Evan', 'Nathan'],heights = [172, 182, 175, 180]) == ['Grayson', 'Nathan', 'Evan', 'Avery']
    assert candidate(names = ['Willow', 'Tara', 'Xander', 'Alyson', 'Reese'],heights = [175, 160, 170, 165, 180]) == ['Reese', 'Willow', 'Xander', 'Alyson', 'Tara']
    assert candidate(names = ['Eli', 'Ella', 'Ezra', 'Emilia', 'Evan'],heights = [170, 175, 160, 180, 165]) == ['Emilia', 'Ella', 'Eli', 'Evan', 'Ezra']
    assert candidate(names = ['James', 'Benjamin', 'Mason', 'Noah', 'Lucas'],heights = [170, 175, 180, 185, 190]) == ['Lucas', 'Noah', 'Mason', 'Benjamin', 'James']
    assert candidate(names = ['Jack', 'Rose', 'Cal', 'Fabian', 'Molly'],heights = [170, 175, 165, 180, 160]) == ['Fabian', 'Rose', 'Jack', 'Cal', 'Molly']


