def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAACGGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAACGGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = []) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = []) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['TACCGGTA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['TACCGGTA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "CCCCCCCC",bank = ['AAAAAAAA', 'AAAAAAAC', 'AAAAAACC', 'AAAAACCC', 'AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'ACCCCCCC', 'CCCCCCCC']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "CCCCCCCC",bank = ['AAAAAAAA', 'AAAAAAAC', 'AAAAAACC', 'AAAAACCC', 'AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'ACCCCCCC', 'CCCCCCCC']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCAAAA",bank = ['AACCAAAA', 'AACCAAAT', 'AACCAATA', 'AACCGAAA', 'AACCAATA', 'AACCAATT', 'AACAAATT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCAAAA",bank = ['AACCAAAA', 'AACCAAAT', 'AACCAATA', 'AACCGAAA', 'AACCAATA', 'AACCAATT', 'AACAAATT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCTGCTA",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'ACCGGCTA', 'ACCTGCTA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCTGCTA",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'ACCGGCTA', 'ACCTGCTA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTTTCCCC",bank = ['AAACGGCT', 'AACCGGCA', 'AAACGGTA', 'AAACGGCC', 'TTTTCCCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTTTCCCC",bank = ['AAACGGCT', 'AACCGGCA', 'AAACGGTA', 'AAACGGCC', 'TTTTCCCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTTTCCCC",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCT', 'AACCGGCG', 'TTACGGCG', 'TTACGGCC', 'TTACGGTC', 'TTACGGTT', 'TTAGGGTT', 'TTAGGGTC', 'TTAGGGCC', 'TTAGGGCG', 'TTTTGGCG', 'TTTTGGCC', 'TTTTGGTC', 'TTTTGGTT', 'TTTTGGGA', 'TTTTGGAA', 'TTTTGGAT', 'TTTTGCAA', 'TTTTGCCA', 'TTTTGCTA', 'TTTTGCAC', 'TTTTGCGA', 'TTTTGCAG', 'TTTTGCGT', 'TTTTGCTC', 'TTTTGCCG', 'TTTTGGCG', 'TTTTGCCC', 'TTTTCCCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTTTCCCC",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCT', 'AACCGGCG', 'TTACGGCG', 'TTACGGCC', 'TTACGGTC', 'TTACGGTT', 'TTAGGGTT', 'TTAGGGTC', 'TTAGGGCC', 'TTAGGGCG', 'TTTTGGCG', 'TTTTGGCC', 'TTTTGGTC', 'TTTTGGTT', 'TTTTGGGA', 'TTTTGGAA', 'TTTTGGAT', 'TTTTGCAA', 'TTTTGCCA', 'TTTTGCTA', 'TTTTGCAC', 'TTTTGCGA', 'TTTTGCAG', 'TTTTGCGT', 'TTTTGCTC', 'TTTTGCCG', 'TTTTGGCG', 'TTTTGCCC', 'TTTTCCCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGCCGACT",bank = ['AACCGGCA', 'AACCGGAA', 'AACCGGGA', 'GGCCGGTA', 'GGCCGGCA', 'GGCCGGAA', 'GGCCGGGA', 'GGCCGACT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGCCGACT",bank = ['AACCGGCA', 'AACCGGAA', 'AACCGGGA', 'GGCCGGTA', 'GGCCGGCA', 'GGCCGGAA', 'GGCCGGGA', 'GGCCGACT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAGGG', 'AAAGGGGG', 'AAGGGGGG', 'AGGGGGGG', 'GGGGGGGG', 'GGGGGGGT', 'GGGGGGTT', 'GGGGGTTT', 'GGGGTTTT', 'GGGTTTTT', 'GGTTTTTT', 'GTTTTTTT', 'TTTTTTTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAGGG', 'AAAGGGGG', 'AAGGGGGG', 'AGGGGGGG', 'GGGGGGGG', 'GGGGGGGT', 'GGGGGGTT', 'GGGGGTTT', 'GGGGTTTT', 'GGGTTTTT', 'GGTTTTTT', 'GTTTTTTT', 'TTTTTTTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAACC', 'AAAAACCC', 'AAAAACGG', 'AAAACGGG', 'AAACGGGG', 'AACGGGGG', 'ACGGGGGG', 'CGGGGGGG', 'TTTTTTTA', 'TTTTTTAG', 'TTTTTTCG', 'TTTTTCGG', 'TTTTGCGG', 'TTTTGGGG', 'TTTGCGGG', 'TTTGGGGG', 'TTGCGGGG', 'TTGGGGGG', 'TGCGGGGG', 'TGGGGGGG', 'GCGGGGGG', 'GGGGGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAACC', 'AAAAACCC', 'AAAAACGG', 'AAAACGGG', 'AAACGGGG', 'AACGGGGG', 'ACGGGGGG', 'CGGGGGGG', 'TTTTTTTA', 'TTTTTTAG', 'TTTTTTCG', 'TTTTTCGG', 'TTTTGCGG', 'TTTTGGGG', 'TTTGCGGG', 'TTTGGGGG', 'TTGCGGGG', 'TTGGGGGG', 'TGCGGGGG', 'TGGGGGGG', 'GCGGGGGG', 'GGGGGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "ACAGACGG",endGene = "AACCGGGA",bank = ['AACGACGG', 'AACGACGT', 'AACGGCGT', 'AACGGCGA', 'AACGGGGA', 'AACCGGGA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "ACAGACGG",endGene = "AACCGGGA",bank = ['AACGACGG', 'AACGACGT', 'AACGGCGT', 'AACGGCGA', 'AACGGGGA', 'AACCGGGA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "ACGTACGT",endGene = "TTACGTAC",bank = ['ACGTACGA', 'TTACGTAA', 'TTACGTAC', 'TTACGTCG', 'ACGTACGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "ACGTACGT",endGene = "TTACGTAC",bank = ['ACGTACGA', 'TTACGTAA', 'TTACGTAC', 'TTACGTCG', 'ACGTACGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "CCCCCCCC",bank = ['AAAAAACC', 'AAAAACCC', 'AAAACCCC', 'AAACCCCC', 'AACCACCC', 'AACCCCAC', 'AACCACCC', 'ACCAACCC', 'ACCCACCC', 'CCCCCCCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "CCCCCCCC",bank = ['AAAAAACC', 'AAAAACCC', 'AAAACCCC', 'AAACCCCC', 'AACCACCC', 'AACCCCAC', 'AACCACCC', 'ACCAACCC', 'ACCCACCC', 'CCCCCCCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGCA', 'GACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'GACCGGTT', 'GACCGGTC', 'GACCGGTA', 'GACCGGAC']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGCA', 'GACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'GACCGGTT', 'GACCGGTC', 'GACCGGTA', 'GACCGGAC']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGTAA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTC', 'AACCGTCA', 'AACCGTAA']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGTAA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTC', 'AACCGTCA', 'AACCGTAA']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AAACGGTA', 'AACCGCTA', 'AAACGGTT', 'TTTTGGTT', 'TTTTTGGT', 'TTTTTTGT', 'TTTTTTTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AAACGGTA', 'AACCGCTA', 'AAACGGTT', 'TTTTGGTT', 'TTTTTGGT', 'TTTTTTGT', 'TTTTTTTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGTC', 'TACCGGTT', 'GGACGGTT', 'GGGGGGTA', 'GGGGGGTT', 'GGGGGGGT', 'GGGGGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGTC', 'TACCGGTT', 'GGACGGTT', 'GGGGGGTA', 'GGGGGGTT', 'GGGGGGGT', 'GGGGGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "CGCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'CGCGGGTA', 'CGCGCGCG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "CGCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'CGCGGGTA', 'CGCGCGCG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGAACTTT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'GAACGGTA', 'GGAACTTA', 'GGAACTTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGAACTTT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'GAACGGTA', 'GGAACTTA', 'GGAACTTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'AACCGGTC', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'AACCGGTC', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGCT",bank = ['AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGCT', 'AACCGGCT']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGCT",bank = ['AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGCT', 'AACCGGCT']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAACCCC",endGene = "CCCCAAAA",bank = ['AAAACCCA', 'AAAACCAA', 'AAAACCAA', 'AAAACAAA', 'AAACAAAA', 'AACAAAAA', 'ACAAAAAA', 'CAAAAAAA', 'CAAACCAA', 'CCAACCAA', 'CCCCAAAC', 'CCCCACAA', 'CCCCAACC', 'CCCCAAAC', 'CCCCAACA', 'CCCCAAAA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAACCCC",endGene = "CCCCAAAA",bank = ['AAAACCCA', 'AAAACCAA', 'AAAACCAA', 'AAAACAAA', 'AAACAAAA', 'AACAAAAA', 'ACAAAAAA', 'CAAAAAAA', 'CAAACCAA', 'CCAACCAA', 'CCCCAAAC', 'CCCCACAA', 'CCCCAACC', 'CCCCAAAC', 'CCCCAACA', 'CCCCAAAA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAACCC",endGene = "CCCCCCCC",bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'AACCACCC', 'AACCGCCC', 'AACCGCCC', 'AACCGGCC', 'AACCGGTC', 'AACCGGTA', 'AACCGGTT', 'AACCGGCT', 'AACCGGCG', 'AACCGGCA', 'AACCGGCC', 'AACCGGCG', 'AACCGGCA', 'GGCCCCCC', 'GGCCCACC', 'GGCCCCGC', 'GGCCCCGA', 'GGCCCCTC', 'GGCCCCTG', 'GGCCCCTA', 'GGCCGGCC', 'GGCCGGCG', 'GGCCGGCA', 'GGCCGGTC', 'GGCCGGTA', 'GGCCGGTT', 'GGCCGCCC', 'GGCCGGGG', 'CCCCGGGG', 'CCCCGGGC', 'CCCCGGCG', 'CCCCGGCA', 'CCCCGGTC', 'CCCCGGTA', 'CCCCGGTT', 'CCCCGCCC', 'CCCCGGGG', 'CCCCCCCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAACCC",endGene = "CCCCCCCC",bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'AACCACCC', 'AACCGCCC', 'AACCGCCC', 'AACCGGCC', 'AACCGGTC', 'AACCGGTA', 'AACCGGTT', 'AACCGGCT', 'AACCGGCG', 'AACCGGCA', 'AACCGGCC', 'AACCGGCG', 'AACCGGCA', 'GGCCCCCC', 'GGCCCACC', 'GGCCCCGC', 'GGCCCCGA', 'GGCCCCTC', 'GGCCCCTG', 'GGCCCCTA', 'GGCCGGCC', 'GGCCGGCG', 'GGCCGGCA', 'GGCCGGTC', 'GGCCGGTA', 'GGCCGGTT', 'GGCCGCCC', 'GGCCGGGG', 'CCCCGGGG', 'CCCCGGGC', 'CCCCGGCG', 'CCCCGGCA', 'CCCCGGTC', 'CCCCGGTA', 'CCCCGGTT', 'CCCCGCCC', 'CCCCGGGG', 'CCCCCCCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TTCGCGTA', 'TTCGCGCG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TTCGCGTA', 'TTCGCGCG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAGGCGTT",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAGGCGTT",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAACCC",endGene = "GGGGCCCC",bank = ['AAAACCCC', 'AAAGCCCC', 'AAGGCCCC', 'GGGGCCCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAACCC",endGene = "GGGGCCCC",bank = ['AAAACCCC', 'AAAGCCCC', 'AAGGCCCC', 'GGGGCCCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGGGGGGA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'GGGGGGTT', 'GGGGGGTA', 'GGGGGGGA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGGGGGGA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'GGGGGGTT', 'GGGGGGTA', 'GGGGGGGA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAAAAAAA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAAAAGTA', 'AAAAAAAA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAAAAAAA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAAAAGTA', 'AAAAAAAA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'TTTTTTTA', 'TTTTTTTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'TTTTTTTA', 'TTTTTTTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAACCC",endGene = "CCCCGGGG",bank = ['AACCCCCC', 'ACCCCCCG', 'ACCACCCC', 'ACCACCCC', 'ACCCCACG', 'CCCCGGGA', 'CCCCGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAACCC",endGene = "CCCCGGGG",bank = ['AACCCCCC', 'ACCCCCCG', 'ACCACCCC', 'ACCACCCC', 'ACCCCACG', 'CCCCGGGA', 'CCCCGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "GGGGCCCC",endGene = "AACCGGTT",bank = ['GGGGCCCG', 'GGGGCCCT', 'GGGGCCTT', 'GGGGCCGG', 'GGGGACGG', 'GGGAGCGG', 'GGGAACGG', 'GGAACCGG', 'GAACCGGG', 'AACCGGGG', 'AACCGGTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "GGGGCCCC",endGene = "AACCGGTT",bank = ['GGGGCCCG', 'GGGGCCCT', 'GGGGCCTT', 'GGGGCCGG', 'GGGGACGG', 'GGGAGCGG', 'GGGAACGG', 'GGAACCGG', 'GAACCGGG', 'AACCGGGG', 'AACCGGTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "TTTTTTTT",endGene = "AAAAAAAA",bank = ['ATTTTTTT', 'AATTTTTT', 'AAATTTTT', 'AAAATTTT', 'AAAAATTT', 'AAAAATTA', 'AAAAAATT', 'AAAAAAAT', 'AAAAAAAC', 'AAAACAAA', 'AAACAAAA', 'AACAAAAA', 'ACAAAAAA', 'CAAAAAAA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "TTTTTTTT",endGene = "AAAAAAAA",bank = ['ATTTTTTT', 'AATTTTTT', 'AAATTTTT', 'AAAATTTT', 'AAAAATTT', 'AAAAATTA', 'AAAAAATT', 'AAAAAAAT', 'AAAAAAAC', 'AAAACAAA', 'AAACAAAA', 'AACAAAAA', 'ACAAAAAA', 'CAAAAAAA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AGCTAGCA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AGCTAGCA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AGCTAGCA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AGCTAGCA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGTGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'ACCGTGTA', 'ACCGTGGT', 'ACCGTGTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGTGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'ACCGTGTA', 'ACCGTGGT', 'ACCGTGTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT', 'ACCGCGGA', 'ACCGCGGC', 'ACCGCGCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT', 'ACCGCGGA', 'ACCGCGGC', 'ACCGCGCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AGCGGTTA",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT', 'AGCGGTTA', 'AGCGGCTA', 'AGCGGCTC', 'AGCGGCGT', 'AGCGGCGC', 'AGCGGCCC', 'AGCGGGTA', 'AGCGGGCA', 'AGCGGGCG', 'AGCGGGCT', 'AGCGGGAA', 'AGCGGGAC', 'AGCGGGAG', 'AGCGGCGT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AGCGGTTA",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT', 'AGCGGTTA', 'AGCGGCTA', 'AGCGGCTC', 'AGCGGCGT', 'AGCGGCGC', 'AGCGGCCC', 'AGCGGGTA', 'AGCGGGCA', 'AGCGGGCG', 'AGCGGGCT', 'AGCGGGAA', 'AGCGGGAC', 'AGCGGGAG', 'AGCGGCGT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGGTTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'ACCGGTTA', 'ACCGGGTA', 'ACCGGATA', 'ACCGGTTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGGTTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'ACCGGTTA', 'ACCGGGTA', 'ACCGGATA', 'ACCGGTTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "GACCGGTA",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'GACCGGTT', 'GACCGGTC', 'GACCGGTA', 'GACCGGAC']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "GACCGGTA",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'GACCGGTT', 'GACCGGTC', 'GACCGGTA', 'GACCGGAC']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGTGGT",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAA', 'AACCGCAT', 'AACCGCCT', 'AACCGCGT', 'AACCGCGC', 'AAACGGTA', 'AAACGGCA', 'AAACGGCG', 'AAACGGCT', 'AAACGGAT', 'AAACGGAA', 'AAACGGCA', 'AAACGGCC', 'AAACGCCG', 'AAACGCCT', 'ACCGGGTA', 'ACCGGGCA', 'ACCGGGCG', 'ACCGGGCT', 'ACCGGGAT', 'ACCGGGAA', 'ACCGGGCA', 'ACCGGGCC', 'ACCGGGCG', 'ACCGGGCT', 'ACCGGCTA', 'ACCGGCCA', 'ACCGGCGT', 'ACCGGCGC', 'ACCGGCCT', 'ACCGGCCC', 'ACCGGTAA', 'ACCGGTCG', 'ACCGGTTA', 'ACCGGTCA', 'ACCGGTCC', 'ACCGGTCG', 'ACCGGTCA', 'ACCGGTCC', 'ACCGGTCG', 'ACCGGTCA', 'ACCGGTCC', 'ACCGTGGC', 'ACCGTGGT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGTGGT",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAA', 'AACCGCAT', 'AACCGCCT', 'AACCGCGT', 'AACCGCGC', 'AAACGGTA', 'AAACGGCA', 'AAACGGCG', 'AAACGGCT', 'AAACGGAT', 'AAACGGAA', 'AAACGGCA', 'AAACGGCC', 'AAACGCCG', 'AAACGCCT', 'ACCGGGTA', 'ACCGGGCA', 'ACCGGGCG', 'ACCGGGCT', 'ACCGGGAT', 'ACCGGGAA', 'ACCGGGCA', 'ACCGGGCC', 'ACCGGGCG', 'ACCGGGCT', 'ACCGGCTA', 'ACCGGCCA', 'ACCGGCGT', 'ACCGGCGC', 'ACCGGCCT', 'ACCGGCCC', 'ACCGGTAA', 'ACCGGTCG', 'ACCGGTTA', 'ACCGGTCA', 'ACCGGTCC', 'ACCGGTCG', 'ACCGGTCA', 'ACCGGTCC', 'ACCGGTCG', 'ACCGGTCA', 'ACCGGTCC', 'ACCGTGGC', 'ACCGTGGT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAACGGTA",endGene = "AACCGGTA",bank = ['AAACGGTT', 'AACCGGTT', 'AACCGGTA']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAACGGTA",endGene = "AACCGGTA",bank = ['AAACGGTT', 'AACCGGTT', 'AACCGGTA']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGAA', 'AACCGGTC', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'GACCGGTA']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGAA', 'AACCGGTC', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'GACCGGTA']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGGA",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGGA",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AAACGGTA', 'GGAAAAAA', 'GGGGGGGA', 'GGGGGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AAACGGTA', 'GGAAAAAA', 'GGGGGGGA', 'GGGGGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "GAGGACAA",endGene = "AACCGGTA",bank = ['AACCGGTA', 'GAGGAGAA', 'GAGGAGGA', 'GAGGACGA', 'GAGGACCA', 'GAGGACTA', 'GAGGACAA', 'GAGGACAT', 'GAAGACAA', 'AACGACAA', 'AACGGCAA', 'AACGGGAA', 'AACGGGTA', 'AACCGGTA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "GAGGACAA",endGene = "AACCGGTA",bank = ['AACCGGTA', 'GAGGAGAA', 'GAGGAGGA', 'GAGGACGA', 'GAGGACCA', 'GAGGACTA', 'GAGGACAA', 'GAGGACAT', 'GAAGACAA', 'AACGACAA', 'AACGGCAA', 'AACGGGAA', 'AACGGGTA', 'AACCGGTA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGGCTA",bank = ['AACCGGTA', 'AACCGCTA', 'ACCGGCTA', 'ACCGGCTC', 'ACCGGCCC', 'ACCGGTTA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGGCTA",bank = ['AACCGGTA', 'AACCGCTA', 'ACCGGCTA', 'ACCGGCTC', 'ACCGGCCC', 'ACCGGTTA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAACGGGA",bank = ['AACCGGTA', 'AAACGGTA', 'AAACGGCA', 'AAACGGAA', 'AAACGGGA', 'AAACGGGA']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAACGGGA",bank = ['AACCGGTA', 'AAACGGTA', 'AAACGGCA', 'AAACGGAA', 'AAACGGGA', 'AAACGGGA']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACGGTACC",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'ACGGTACC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACGGTACC",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'ACGGTACC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTCCGGAA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'TTACGGTA', 'TTACGGCA', 'TTCCGGTA', 'TTCCGGCA', 'TTCCGGAA', 'GGCCGGTA', 'GGCCGGCA', 'GGCCGGAA', 'TTCCGGTG', 'TTCCGGTC', 'TTCCGGAU', 'TTCCGGAC', 'TTCCGGAG', 'TTCCGGAT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTCCGGAA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'TTACGGTA', 'TTACGGCA', 'TTCCGGTA', 'TTCCGGCA', 'TTCCGGAA', 'GGCCGGTA', 'GGCCGGCA', 'GGCCGGAA', 'TTCCGGTG', 'TTCCGGTC', 'TTCCGGAU', 'TTCCGGAC', 'TTCCGGAG', 'TTCCGGAT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTC",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'AACCGGTC']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTC",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'AACCGGTC']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAACCC",endGene = "GGGGGGGG",bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'AACCACCC', 'AACCGCCC', 'AACCGGCC', 'AACCGGTC', 'AACCGGTA', 'AACCGGTT', 'AACCGGCT', 'AACCGGCG', 'AACCGGCA', 'GGCCCCCC', 'GGCCCACC', 'GGCCCCGC', 'GGCCCCGA', 'GGCCCCTC', 'GGCCCCTG', 'GGCCCCTA', 'GGCCGGCC', 'GGCCGGCG', 'GGCCGGCA', 'GGCCGGTC', 'GGCCGGTA', 'GGCCGGTT', 'GGCCGCCC', 'GGCCGGGG', 'GGGGGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAACCC",endGene = "GGGGGGGG",bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'AACCACCC', 'AACCGCCC', 'AACCGGCC', 'AACCGGTC', 'AACCGGTA', 'AACCGGTT', 'AACCGGCT', 'AACCGGCG', 'AACCGGCA', 'GGCCCCCC', 'GGCCCACC', 'GGCCCCGC', 'GGCCCCGA', 'GGCCCCTC', 'GGCCCCTG', 'GGCCCCTA', 'GGCCGGCC', 'GGCCGGCG', 'GGCCGGCA', 'GGCCGGTC', 'GGCCGGTA', 'GGCCGGTT', 'GGCCGCCC', 'GGCCGGGG', 'GGGGGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'GGGGGGTA', 'GGGGGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'GGGGGGTA', 'GGGGGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAAAAAGG",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAA', 'AACCGCAC', 'AACCGCCA', 'AACCGCCG', 'AACCGCCT', 'AAACGGTA', 'AAACGGCA', 'AAACGGCG', 'AAACGGCT', 'AAACGGAT', 'AAACGGAA', 'AAACGGCA', 'AAACGGCC', 'AAACGCCG', 'AAACGCCT', 'AAAAGGTA', 'AAAAGGCA', 'AAAAGGCG', 'AAAAGGCT', 'AAAAGGAA', 'AAAAGGAC', 'AAAAGGAG', 'AAAAAGTA', 'AAAAAGCA', 'AAAAAGCG', 'AAAAAGCT', 'AAAAAGAA', 'AAAAAGAC', 'AAAAAGAG', 'AAAAAAGT', 'AAAAAAGC', 'AAAAAAGA', 'AAAAAAGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAAAAAGG",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAA', 'AACCGCAC', 'AACCGCCA', 'AACCGCCG', 'AACCGCCT', 'AAACGGTA', 'AAACGGCA', 'AAACGGCG', 'AAACGGCT', 'AAACGGAT', 'AAACGGAA', 'AAACGGCA', 'AAACGGCC', 'AAACGCCG', 'AAACGCCT', 'AAAAGGTA', 'AAAAGGCA', 'AAAAGGCG', 'AAAAGGCT', 'AAAAGGAA', 'AAAAGGAC', 'AAAAGGAG', 'AAAAAGTA', 'AAAAAGCA', 'AAAAAGCG', 'AAAAAGCT', 'AAAAAGAA', 'AAAAAGAC', 'AAAAAGAG', 'AAAAAAGT', 'AAAAAAGC', 'AAAAAAGA', 'AAAAAAGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAACGGCC",bank = ['AAACGGTA', 'AAACGGCA', 'AAACGGCC', 'AACCGGCA', 'AACCGGTA', 'AACCGGTC']) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAACGGCC",bank = ['AAACGGTA', 'AAACGGCA', 'AAACGGCC', 'AACCGGCA', 'AACCGGTA', 'AACCGGTC']) == 4: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AGCTATAG",endGene = "GACTGTAG",bank = ['AGCTATAC', 'AGCTGTAG', 'AGCTTTAG', 'GACTATAG', 'GACTGTAG', 'GACTTTAG', 'GAATATAG', 'GGCTATAG', 'AGGTATAG']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AGCTATAG",endGene = "GACTGTAG",bank = ['AGCTATAC', 'AGCTGTAG', 'AGCTTTAG', 'GACTATAG', 'GACTGTAG', 'GACTTTAG', 'GAATATAG', 'GGCTATAG', 'AGGTATAG']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAGAACGG",endGene = "GGAACGGT",bank = ['AAGAACGA', 'AAGAACGG', 'AAGAACGT', 'AAGACGGT', 'AAGGACGT', 'AGGAACGT', 'GGAACGGT', 'GGAACGGC', 'GGAACGGA', 'GGGAACGA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAGAACGG",endGene = "GGAACGGT",bank = ['AAGAACGA', 'AAGAACGG', 'AAGAACGT', 'AAGACGGT', 'AAGGACGT', 'AGGAACGT', 'GGAACGGT', 'GGAACGGC', 'GGAACGGA', 'GGGAACGA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "CGGTTTAA",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGTA', 'CCCGGGTT', 'CGGTTTTT', 'CGGTTTAA', 'CGGTTTTG', 'CGGTGGAA', 'CGGACGAA', 'AACCGGAG', 'AACCGGCG', 'AACCGGGA', 'AACCGGTT', 'AACCGGAT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTT', 'AACCGGTA', 'AACCGGTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "CGGTTTAA",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGTA', 'CCCGGGTT', 'CGGTTTTT', 'CGGTTTAA', 'CGGTTTTG', 'CGGTGGAA', 'CGGACGAA', 'AACCGGAG', 'AACCGGCG', 'AACCGGGA', 'AACCGGTT', 'AACCGGAT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTT', 'AACCGGTA', 'AACCGGTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAACGGGA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'AAACGGGA', 'AAACGGGC', 'AACCGGGT', 'AACCGGGG']) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAACGGGA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'AAACGGGA', 'AAACGGGC', 'AACCGGGT', 'AACCGGGG']) == 3: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAAGA', 'AAAACAAA', 'AAACAAAA', 'AAGAAAAA', 'AGAAAAAA', 'GAAAAAAA', 'TAAAAAAA', 'TTAAAAAA', 'TTTAAAAA', 'TTTTAAAA', 'TTTTTAAA', 'TTTTTTAA', 'TTTTTTTA', 'TTTTTTTT']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAAGA', 'AAAACAAA', 'AAACAAAA', 'AAGAAAAA', 'AGAAAAAA', 'GAAAAAAA', 'TAAAAAAA', 'TTAAAAAA', 'TTTAAAAA', 'TTTTAAAA', 'TTTTTAAA', 'TTTTTTAA', 'TTTTTTTA', 'TTTTTTTT']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "ACGTACGT",endGene = "TGCATGCA",bank = ['ACGTACGA', 'ACGTACGC', 'ACGTCAGT', 'TACGACGT', 'TGCATGCA', 'TGCATGCG', 'TGCATGTA', 'TGCAACGT', 'TGCGACGT', 'TGCAACGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "ACGTACGT",endGene = "TGCATGCA",bank = ['ACGTACGA', 'ACGTACGC', 'ACGTCAGT', 'TACGACGT', 'TGCATGCA', 'TGCATGCG', 'TGCATGTA', 'TGCAACGT', 'TGCGACGT', 'TGCAACGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTCCGCCC",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGCA', 'AACCGGCC', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAC', 'AACCGGAG', 'AACCGGAA', 'AACCGCAT', 'AACCGCCT', 'AACCGCGT', 'AACCGCGC', 'AACCGCCT', 'AACCGCCC', 'AACCAGCC', 'AACCAGCA', 'AACCAGCT', 'AACCAGCG', 'AACCGCCA', 'AACCGCCC', 'AACCGCCA', 'AACCGCCC', 'AACCGCCT', 'AACCGCCA', 'AACCGCCG', 'AACCGCCC', 'AACCGCCC', 'AACCGCCC', 'TTACGGCC', 'TTACGGCA', 'TTACGGCT', 'TTACGGCG', 'TTACGGTA', 'TTACGGTC', 'TTACGGAA', 'TTACGGAC', 'TTACGGAG', 'TTACGGCG', 'TTACGGCA', 'TTACGGCT', 'TTACGGCG', 'TTAGGGCC', 'TTAGGGCA', 'TTAGGGCT', 'TTAGGGCG', 'TTAGGGTA', 'TTAGGGTC', 'TTAGGGAA', 'TTAGGGAC', 'TTAGGGAG', 'TTAGGGCG', 'TTAGGGCA', 'TTAGGGCT', 'TTAGGGCG', 'TTTTGGCC', 'TTTTGGCA', 'TTTTGGCT', 'TTTTGGCG', 'TTTTGGTA', 'TTTTGGTC', 'TTTTGGAA', 'TTTTGGAC', 'TTTTGGAG', 'TTTTGGCA', 'TTTTGGCC', 'TTTTGGCT', 'TTTTGGCG', 'TTTTGGAA', 'TTTTGGAC', 'TTTTGGAG', 'TTTTGCAA', 'TTTTGCCA', 'TTTTGCTA', 'TTTTGCAC', 'TTTTGCGA', 'TTTTGCAG', 'TTTTGCGT', 'TTTTGCTC', 'TTTTGCCG', 'TTTTGGCG', 'TTTTGCCC', 'TTTTCCCC']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTCCGCCC",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGCA', 'AACCGGCC', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAC', 'AACCGGAG', 'AACCGGAA', 'AACCGCAT', 'AACCGCCT', 'AACCGCGT', 'AACCGCGC', 'AACCGCCT', 'AACCGCCC', 'AACCAGCC', 'AACCAGCA', 'AACCAGCT', 'AACCAGCG', 'AACCGCCA', 'AACCGCCC', 'AACCGCCA', 'AACCGCCC', 'AACCGCCT', 'AACCGCCA', 'AACCGCCG', 'AACCGCCC', 'AACCGCCC', 'AACCGCCC', 'TTACGGCC', 'TTACGGCA', 'TTACGGCT', 'TTACGGCG', 'TTACGGTA', 'TTACGGTC', 'TTACGGAA', 'TTACGGAC', 'TTACGGAG', 'TTACGGCG', 'TTACGGCA', 'TTACGGCT', 'TTACGGCG', 'TTAGGGCC', 'TTAGGGCA', 'TTAGGGCT', 'TTAGGGCG', 'TTAGGGTA', 'TTAGGGTC', 'TTAGGGAA', 'TTAGGGAC', 'TTAGGGAG', 'TTAGGGCG', 'TTAGGGCA', 'TTAGGGCT', 'TTAGGGCG', 'TTTTGGCC', 'TTTTGGCA', 'TTTTGGCT', 'TTTTGGCG', 'TTTTGGTA', 'TTTTGGTC', 'TTTTGGAA', 'TTTTGGAC', 'TTTTGGAG', 'TTTTGGCA', 'TTTTGGCC', 'TTTTGGCT', 'TTTTGGCG', 'TTTTGGAA', 'TTTTGGAC', 'TTTTGGAG', 'TTTTGCAA', 'TTTTGCCA', 'TTTTGCTA', 'TTTTGCAC', 'TTTTGCGA', 'TTTTGCAG', 'TTTTGCGT', 'TTTTGCTC', 'TTTTGCCG', 'TTTTGGCG', 'TTTTGCCC', 'TTTTCCCC']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "AAAAAAAA",bank = ['AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "AAAAAAAA",bank = ['AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGCT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'AACCGGCA', 'AACCGGCT']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGCT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'AACCGGCA', 'AACCGGCT']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAAAA', 'AAAACCCC', 'AAAAACCC', 'AAAAAACC', 'AAAAAAAC', 'AAAAAAAT', 'AAAAAATT', 'AAAAATTT', 'AAAATTTT', 'AAATTTTT', 'AATTTTTT', 'ATTTTTTT', 'TTTTTTTT']) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAAAA', 'AAAACCCC', 'AAAAACCC', 'AAAAAACC', 'AAAAAAAC', 'AAAAAAAT', 'AAAAAATT', 'AAAAATTT', 'AAAATTTT', 'AAATTTTT', 'AATTTTTT', 'ATTTTTTT', 'TTTTTTTT']) == 8: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGGTTA",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'ACCGGTTA', 'ACCGGGTA', 'ACCGGTCG', 'ACCGGCTA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGGTTA",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'ACCGGTTA', 'ACCGGGTA', 'ACCGGTCG', 'ACCGGCTA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAGCGGTA",bank = ['AACCGGTA', 'AAGCGGTA', 'AACCGCTA', 'AAACGGTA']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAGCGGTA",bank = ['AACCGGTA', 'AAGCGGTA', 'AACCGCTA', 'AAACGGTA']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "CGTACGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'CGTACGTA', 'CGTACGTT', 'CGTACGCA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "CGTACGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'CGTACGTA', 'CGTACGTT', 'CGTACGCA']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTC",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA']) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTC",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA']) == 1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TTTTGGTA', 'TTTTTTTA', 'TTTTTTTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TTTTGGTA', 'TTTTTTTA', 'TTTTTTTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAGCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTA', 'AAGCGGTA']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAGCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTA', 'AAGCGGTA']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AAACGGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'AACCGGCA', 'AACCGGAA', 'AAACGGCA', 'AAACGGAA', 'AACCGGTC', 'AAACGGTC', 'AAACGGCA', 'AAACGGAA', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTT']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AAACGGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'AACCGGCA', 'AACCGGAA', 'AAACGGCA', 'AAACGGAA', 'AACCGGTC', 'AAACGGTC', 'AAACGGCA', 'AAACGGAA', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTT']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "TACCGGTA",bank = ['AACCGGTC', 'TACCGGTA', 'AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TACCGGTA', 'TACCGGTT', 'TACCGGTC']) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "TACCGGTA",bank = ['AACCGGTC', 'TACCGGTA', 'AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TACCGGTA', 'TACCGGTT', 'TACCGGTC']) == 2: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGGA', 'AAGCGGGA', 'AAGCGGTA', 'AAGCGGGA', 'GGGGGGGA', 'GGGGGGGG']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGGA', 'AAGCGGGA', 'AAGCGGTA', 'AAGCGGGA', 'GGGGGGGA', 'GGGGGGGG']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "AACCGGTT",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT']) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "AACCGGTT",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT']) == 0: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGCA', 'GACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGCA', 'GACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == -1: {e}')
    
    total += 1
    try:
        result = candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT', 'ACCGCGGA']) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT', 'ACCGCGGA']) == -1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(startGene = "AACCGGTT",endGene = "AAACGGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = []) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['TACCGGTA']) == -1
    assert candidate(startGene = "AAAAAAAA",endGene = "CCCCCCCC",bank = ['AAAAAAAA', 'AAAAAAAC', 'AAAAAACC', 'AAAAACCC', 'AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'ACCCCCCC', 'CCCCCCCC']) == 8
    assert candidate(startGene = "AACCGGTT",endGene = "AACCAAAA",bank = ['AACCAAAA', 'AACCAAAT', 'AACCAATA', 'AACCGAAA', 'AACCAATA', 'AACCAATT', 'AACAAATT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == 4
    assert candidate(startGene = "AACCGGTT",endGene = "ACCTGCTA",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'ACCGGCTA', 'ACCTGCTA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "TTTTCCCC",bank = ['AAACGGCT', 'AACCGGCA', 'AAACGGTA', 'AAACGGCC', 'TTTTCCCC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "TTTTCCCC",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCT', 'AACCGGCG', 'TTACGGCG', 'TTACGGCC', 'TTACGGTC', 'TTACGGTT', 'TTAGGGTT', 'TTAGGGTC', 'TTAGGGCC', 'TTAGGGCG', 'TTTTGGCG', 'TTTTGGCC', 'TTTTGGTC', 'TTTTGGTT', 'TTTTGGGA', 'TTTTGGAA', 'TTTTGGAT', 'TTTTGCAA', 'TTTTGCCA', 'TTTTGCTA', 'TTTTGCAC', 'TTTTGCGA', 'TTTTGCAG', 'TTTTGCGT', 'TTTTGCTC', 'TTTTGCCG', 'TTTTGGCG', 'TTTTGCCC', 'TTTTCCCC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "GGCCGACT",bank = ['AACCGGCA', 'AACCGGAA', 'AACCGGGA', 'GGCCGGTA', 'GGCCGGCA', 'GGCCGGAA', 'GGCCGGGA', 'GGCCGACT']) == -1
    assert candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAGGG', 'AAAGGGGG', 'AAGGGGGG', 'AGGGGGGG', 'GGGGGGGG', 'GGGGGGGT', 'GGGGGGTT', 'GGGGGTTT', 'GGGGTTTT', 'GGGTTTTT', 'GGTTTTTT', 'GTTTTTTT', 'TTTTTTTT']) == -1
    assert candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAACC', 'AAAAACCC', 'AAAAACGG', 'AAAACGGG', 'AAACGGGG', 'AACGGGGG', 'ACGGGGGG', 'CGGGGGGG', 'TTTTTTTA', 'TTTTTTAG', 'TTTTTTCG', 'TTTTTCGG', 'TTTTGCGG', 'TTTTGGGG', 'TTTGCGGG', 'TTTGGGGG', 'TTGCGGGG', 'TTGGGGGG', 'TGCGGGGG', 'TGGGGGGG', 'GCGGGGGG', 'GGGGGGGG']) == -1
    assert candidate(startGene = "ACAGACGG",endGene = "AACCGGGA",bank = ['AACGACGG', 'AACGACGT', 'AACGGCGT', 'AACGGCGA', 'AACGGGGA', 'AACCGGGA']) == -1
    assert candidate(startGene = "ACGTACGT",endGene = "TTACGTAC",bank = ['ACGTACGA', 'TTACGTAA', 'TTACGTAC', 'TTACGTCG', 'ACGTACGG']) == -1
    assert candidate(startGene = "AAAAAAAA",endGene = "CCCCCCCC",bank = ['AAAAAACC', 'AAAAACCC', 'AAAACCCC', 'AAACCCCC', 'AACCACCC', 'AACCCCAC', 'AACCACCC', 'ACCAACCC', 'ACCCACCC', 'CCCCCCCC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGCA', 'GACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'GACCGGTT', 'GACCGGTC', 'GACCGGTA', 'GACCGGAC']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGTAA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTC', 'AACCGTCA', 'AACCGTAA']) == 4
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AAACGGTA', 'AACCGCTA', 'AAACGGTT', 'TTTTGGTT', 'TTTTTGGT', 'TTTTTTGT', 'TTTTTTTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGTC', 'TACCGGTT', 'GGACGGTT', 'GGGGGGTA', 'GGGGGGTT', 'GGGGGGGT', 'GGGGGGGG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "CGCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'CGCGGGTA', 'CGCGCGCG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "GGAACTTT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'GAACGGTA', 'GGAACTTA', 'GGAACTTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'AACCGGTC', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGCT",bank = ['AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGCT', 'AACCGGCT']) == 1
    assert candidate(startGene = "AAAACCCC",endGene = "CCCCAAAA",bank = ['AAAACCCA', 'AAAACCAA', 'AAAACCAA', 'AAAACAAA', 'AAACAAAA', 'AACAAAAA', 'ACAAAAAA', 'CAAAAAAA', 'CAAACCAA', 'CCAACCAA', 'CCCCAAAC', 'CCCCACAA', 'CCCCAACC', 'CCCCAAAC', 'CCCCAACA', 'CCCCAAAA']) == -1
    assert candidate(startGene = "AAAAACCC",endGene = "CCCCCCCC",bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'AACCACCC', 'AACCGCCC', 'AACCGCCC', 'AACCGGCC', 'AACCGGTC', 'AACCGGTA', 'AACCGGTT', 'AACCGGCT', 'AACCGGCG', 'AACCGGCA', 'AACCGGCC', 'AACCGGCG', 'AACCGGCA', 'GGCCCCCC', 'GGCCCACC', 'GGCCCCGC', 'GGCCCCGA', 'GGCCCCTC', 'GGCCCCTG', 'GGCCCCTA', 'GGCCGGCC', 'GGCCGGCG', 'GGCCGGCA', 'GGCCGGTC', 'GGCCGGTA', 'GGCCGGTT', 'GGCCGCCC', 'GGCCGGGG', 'CCCCGGGG', 'CCCCGGGC', 'CCCCGGCG', 'CCCCGGCA', 'CCCCGGTC', 'CCCCGGTA', 'CCCCGGTT', 'CCCCGCCC', 'CCCCGGGG', 'CCCCCCCC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "TTCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TTCGCGTA', 'TTCGCGCG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAGGCGTT",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT']) == -1
    assert candidate(startGene = "AAAAACCC",endGene = "GGGGCCCC",bank = ['AAAACCCC', 'AAAGCCCC', 'AAGGCCCC', 'GGGGCCCC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "GGGGGGGA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'GGGGGGTT', 'GGGGGGTA', 'GGGGGGGA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTA",bank = ['AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "AAAAAAAA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAAAAGTA', 'AAAAAAAA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'TTTTTTTA', 'TTTTTTTT']) == -1
    assert candidate(startGene = "AAAAACCC",endGene = "CCCCGGGG",bank = ['AACCCCCC', 'ACCCCCCG', 'ACCACCCC', 'ACCACCCC', 'ACCCCACG', 'CCCCGGGA', 'CCCCGGGG']) == -1
    assert candidate(startGene = "GGGGCCCC",endGene = "AACCGGTT",bank = ['GGGGCCCG', 'GGGGCCCT', 'GGGGCCTT', 'GGGGCCGG', 'GGGGACGG', 'GGGAGCGG', 'GGGAACGG', 'GGAACCGG', 'GAACCGGG', 'AACCGGGG', 'AACCGGTT']) == -1
    assert candidate(startGene = "TTTTTTTT",endGene = "AAAAAAAA",bank = ['ATTTTTTT', 'AATTTTTT', 'AAATTTTT', 'AAAATTTT', 'AAAAATTT', 'AAAAATTA', 'AAAAAATT', 'AAAAAAAT', 'AAAAAAAC', 'AAAACAAA', 'AAACAAAA', 'AACAAAAA', 'ACAAAAAA', 'CAAAAAAA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AGCTAGCA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AACCGGTA', 'AGCTAGCA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGTGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'ACCGTGTA', 'ACCGTGGT', 'ACCGTGTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT', 'ACCGCGGA', 'ACCGCGGC', 'ACCGCGCC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AGCGGTTA",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT', 'AGCGGTTA', 'AGCGGCTA', 'AGCGGCTC', 'AGCGGCGT', 'AGCGGCGC', 'AGCGGCCC', 'AGCGGGTA', 'AGCGGGCA', 'AGCGGGCG', 'AGCGGGCT', 'AGCGGGAA', 'AGCGGGAC', 'AGCGGGAG', 'AGCGGCGT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGGTTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'ACCGGTTA', 'ACCGGGTA', 'ACCGGATA', 'ACCGGTTT']) == -1
    assert candidate(startGene = "GACCGGTA",endGene = "AACCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT', 'GACCGGTT', 'GACCGGTC', 'GACCGGTA', 'GACCGGAC']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGTGGT",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAA', 'AACCGCAT', 'AACCGCCT', 'AACCGCGT', 'AACCGCGC', 'AAACGGTA', 'AAACGGCA', 'AAACGGCG', 'AAACGGCT', 'AAACGGAT', 'AAACGGAA', 'AAACGGCA', 'AAACGGCC', 'AAACGCCG', 'AAACGCCT', 'ACCGGGTA', 'ACCGGGCA', 'ACCGGGCG', 'ACCGGGCT', 'ACCGGGAT', 'ACCGGGAA', 'ACCGGGCA', 'ACCGGGCC', 'ACCGGGCG', 'ACCGGGCT', 'ACCGGCTA', 'ACCGGCCA', 'ACCGGCGT', 'ACCGGCGC', 'ACCGGCCT', 'ACCGGCCC', 'ACCGGTAA', 'ACCGGTCG', 'ACCGGTTA', 'ACCGGTCA', 'ACCGGTCC', 'ACCGGTCG', 'ACCGGTCA', 'ACCGGTCC', 'ACCGGTCG', 'ACCGGTCA', 'ACCGGTCC', 'ACCGTGGC', 'ACCGTGGT']) == -1
    assert candidate(startGene = "AAACGGTA",endGene = "AACCGGTA",bank = ['AAACGGTT', 'AACCGGTT', 'AACCGGTA']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGAA', 'AACCGGTC', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'GACCGGTA']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGGA",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AAACGGTA', 'GGAAAAAA', 'GGGGGGGA', 'GGGGGGGG']) == -1
    assert candidate(startGene = "GAGGACAA",endGene = "AACCGGTA",bank = ['AACCGGTA', 'GAGGAGAA', 'GAGGAGGA', 'GAGGACGA', 'GAGGACCA', 'GAGGACTA', 'GAGGACAA', 'GAGGACAT', 'GAAGACAA', 'AACGACAA', 'AACGGCAA', 'AACGGGAA', 'AACGGGTA', 'AACCGGTA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGGCTA",bank = ['AACCGGTA', 'AACCGCTA', 'ACCGGCTA', 'ACCGGCTC', 'ACCGGCCC', 'ACCGGTTA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAACGGGA",bank = ['AACCGGTA', 'AAACGGTA', 'AAACGGCA', 'AAACGGAA', 'AAACGGGA', 'AAACGGGA']) == 3
    assert candidate(startGene = "AACCGGTT",endGene = "ACGGTACC",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'ACGGTACC']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "TTCCGGAA",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'AAACGGCA', 'TTACGGTA', 'TTACGGCA', 'TTCCGGTA', 'TTCCGGCA', 'TTCCGGAA', 'GGCCGGTA', 'GGCCGGCA', 'GGCCGGAA', 'TTCCGGTG', 'TTCCGGTC', 'TTCCGGAU', 'TTCCGGAC', 'TTCCGGAG', 'TTCCGGAT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTC",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'AACCGGTC']) == 1
    assert candidate(startGene = "AAAAACCC",endGene = "GGGGGGGG",bank = ['AAAACCCC', 'AAACCCCC', 'AACCCCCC', 'AACCACCC', 'AACCGCCC', 'AACCGGCC', 'AACCGGTC', 'AACCGGTA', 'AACCGGTT', 'AACCGGCT', 'AACCGGCG', 'AACCGGCA', 'GGCCCCCC', 'GGCCCACC', 'GGCCCCGC', 'GGCCCCGA', 'GGCCCCTC', 'GGCCCCTG', 'GGCCCCTA', 'GGCCGGCC', 'GGCCGGCG', 'GGCCGGCA', 'GGCCGGTC', 'GGCCGGTA', 'GGCCGGTT', 'GGCCGCCC', 'GGCCGGGG', 'GGGGGGGG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'GGGGGGTA', 'GGGGGGGG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAAAAAGG",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAA', 'AACCGCAC', 'AACCGCCA', 'AACCGCCG', 'AACCGCCT', 'AAACGGTA', 'AAACGGCA', 'AAACGGCG', 'AAACGGCT', 'AAACGGAT', 'AAACGGAA', 'AAACGGCA', 'AAACGGCC', 'AAACGCCG', 'AAACGCCT', 'AAAAGGTA', 'AAAAGGCA', 'AAAAGGCG', 'AAAAGGCT', 'AAAAGGAA', 'AAAAGGAC', 'AAAAGGAG', 'AAAAAGTA', 'AAAAAGCA', 'AAAAAGCG', 'AAAAAGCT', 'AAAAAGAA', 'AAAAAGAC', 'AAAAAGAG', 'AAAAAAGT', 'AAAAAAGC', 'AAAAAAGA', 'AAAAAAGG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAACGGCC",bank = ['AAACGGTA', 'AAACGGCA', 'AAACGGCC', 'AACCGGCA', 'AACCGGTA', 'AACCGGTC']) == 4
    assert candidate(startGene = "AGCTATAG",endGene = "GACTGTAG",bank = ['AGCTATAC', 'AGCTGTAG', 'AGCTTTAG', 'GACTATAG', 'GACTGTAG', 'GACTTTAG', 'GAATATAG', 'GGCTATAG', 'AGGTATAG']) == 3
    assert candidate(startGene = "AAGAACGG",endGene = "GGAACGGT",bank = ['AAGAACGA', 'AAGAACGG', 'AAGAACGT', 'AAGACGGT', 'AAGGACGT', 'AGGAACGT', 'GGAACGGT', 'GGAACGGC', 'GGAACGGA', 'GGGAACGA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "CGGTTTAA",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGTA', 'CCCGGGTT', 'CGGTTTTT', 'CGGTTTAA', 'CGGTTTTG', 'CGGTGGAA', 'CGGACGAA', 'AACCGGAG', 'AACCGGCG', 'AACCGGGA', 'AACCGGTT', 'AACCGGAT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTT', 'AACCGGTA', 'AACCGGTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAACGGGA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'AAACGGGA', 'AAACGGGC', 'AACCGGGT', 'AACCGGGG']) == 3
    assert candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAAGA', 'AAAACAAA', 'AAACAAAA', 'AAGAAAAA', 'AGAAAAAA', 'GAAAAAAA', 'TAAAAAAA', 'TTAAAAAA', 'TTTAAAAA', 'TTTTAAAA', 'TTTTTAAA', 'TTTTTTAA', 'TTTTTTTA', 'TTTTTTTT']) == 8
    assert candidate(startGene = "ACGTACGT",endGene = "TGCATGCA",bank = ['ACGTACGA', 'ACGTACGC', 'ACGTCAGT', 'TACGACGT', 'TGCATGCA', 'TGCATGCG', 'TGCATGTA', 'TGCAACGT', 'TGCGACGT', 'TGCAACGG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "TTCCGCCC",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGCA', 'AACCGGCC', 'AACCGGCG', 'AACCGGCT', 'AACCGGAT', 'AACCGGAC', 'AACCGGAG', 'AACCGGAA', 'AACCGCAT', 'AACCGCCT', 'AACCGCGT', 'AACCGCGC', 'AACCGCCT', 'AACCGCCC', 'AACCAGCC', 'AACCAGCA', 'AACCAGCT', 'AACCAGCG', 'AACCGCCA', 'AACCGCCC', 'AACCGCCA', 'AACCGCCC', 'AACCGCCT', 'AACCGCCA', 'AACCGCCG', 'AACCGCCC', 'AACCGCCC', 'AACCGCCC', 'TTACGGCC', 'TTACGGCA', 'TTACGGCT', 'TTACGGCG', 'TTACGGTA', 'TTACGGTC', 'TTACGGAA', 'TTACGGAC', 'TTACGGAG', 'TTACGGCG', 'TTACGGCA', 'TTACGGCT', 'TTACGGCG', 'TTAGGGCC', 'TTAGGGCA', 'TTAGGGCT', 'TTAGGGCG', 'TTAGGGTA', 'TTAGGGTC', 'TTAGGGAA', 'TTAGGGAC', 'TTAGGGAG', 'TTAGGGCG', 'TTAGGGCA', 'TTAGGGCT', 'TTAGGGCG', 'TTTTGGCC', 'TTTTGGCA', 'TTTTGGCT', 'TTTTGGCG', 'TTTTGGTA', 'TTTTGGTC', 'TTTTGGAA', 'TTTTGGAC', 'TTTTGGAG', 'TTTTGGCA', 'TTTTGGCC', 'TTTTGGCT', 'TTTTGGCG', 'TTTTGGAA', 'TTTTGGAC', 'TTTTGGAG', 'TTTTGCAA', 'TTTTGCCA', 'TTTTGCTA', 'TTTTGCAC', 'TTTTGCGA', 'TTTTGCAG', 'TTTTGCGT', 'TTTTGCTC', 'TTTTGCCG', 'TTTTGGCG', 'TTTTGCCC', 'TTTTCCCC']) == -1
    assert candidate(startGene = "AAAAAAAA",endGene = "AAAAAAAA",bank = ['AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AAAAAAAA']) == 0
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGCT",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'AACCGGCA', 'AACCGGCT']) == 1
    assert candidate(startGene = "AAAAAAAA",endGene = "TTTTTTTT",bank = ['AAAAAAAA', 'AAAACCCC', 'AAAAACCC', 'AAAAAACC', 'AAAAAAAC', 'AAAAAAAT', 'AAAAAATT', 'AAAAATTT', 'AAAATTTT', 'AAATTTTT', 'AATTTTTT', 'ATTTTTTT', 'TTTTTTTT']) == 8
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGGTTA",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'ACCGGTTA', 'ACCGGGTA', 'ACCGGTCG', 'ACCGGCTA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAGCGGTA",bank = ['AACCGGTA', 'AAGCGGTA', 'AACCGCTA', 'AAACGGTA']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "CGTACGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AAACGGTA', 'AACCGGAC', 'CGTACGTA', 'CGTACGTT', 'CGTACGCA']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTC",bank = ['AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA', 'AACCGGGA']) == 1
    assert candidate(startGene = "AACCGGTT",endGene = "TTTTTTTT",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TTTTGGTA', 'TTTTTTTA', 'TTTTTTTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AAGCGGTA",bank = ['AACCGGCA', 'AACCGGTA', 'AACCGGTA', 'AAGCGGTA']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "AAACGGTA",bank = ['AACCGGTA', 'AACCGCTA', 'AAACGGTA', 'AACCGGCA', 'AACCGGAA', 'AAACGGCA', 'AAACGGAA', 'AACCGGTC', 'AAACGGTC', 'AAACGGCA', 'AAACGGAA', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTC', 'AACCGGTT', 'AACCGGTA', 'AACCGGTT']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "TACCGGTA",bank = ['AACCGGTC', 'TACCGGTA', 'AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'TACCGGTA', 'TACCGGTT', 'TACCGGTC']) == 2
    assert candidate(startGene = "AACCGGTT",endGene = "GGGGGGGG",bank = ['AACCGGTA', 'AACCGGCA', 'AACCGGGA', 'AAGCGGGA', 'AAGCGGTA', 'AAGCGGGA', 'GGGGGGGA', 'GGGGGGGG']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "AACCGGTT",bank = ['AACCGGTA', 'AACCGGCT', 'AACCGGCA', 'AACCGGCG', 'AACCGGTC', 'AACCGCTA', 'AAACGGTA', 'AACAGGTA', 'AAACGGTC', 'AAACGGCT', 'AAACGGCG', 'AAACGGTT', 'AAGGCGTA', 'AAGGCGTC', 'AAGGCGCA', 'AAGGCGCG', 'AAGGCGCT', 'AAGGCGTT']) == 0
    assert candidate(startGene = "AACCGGTT",endGene = "GACCGGTA",bank = ['AACCGGCA', 'GACCGGTA', 'AACCGGCT', 'AACCGGAA', 'AACCGGAT', 'AACCGGTT']) == -1
    assert candidate(startGene = "AACCGGTT",endGene = "ACCGCGCG",bank = ['AACCGGTA', 'AACCGGCA', 'AAACGGTA', 'ACCGCGTA', 'ACCGCGCG', 'ACCGCGCT', 'ACCGCGTT', 'ACCGCGGA']) == -1


