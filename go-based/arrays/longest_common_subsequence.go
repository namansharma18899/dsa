package main

func longestConsecutive(nums []int) int {
	seqs := make(map[int]int, len(nums))

	for _, num := range nums {
		if _, exists := seqs[num]; exists {
			continue
		}

		prevSeq, nextSeq := seqs[num-1], seqs[num+1]
		currSeq := prevSeq + nextSeq + 1
		seqs[num] = currSeq
		if prevSeq > 0 {
			seqs[num-prevSeq] = currSeq
		}
		if nextSeq > 0 {
			seqs[num+nextSeq] = currSeq
		}
	}

	maxSeq := 0
	for _, seq := range seqs {
		maxSeq = max(seq, maxSeq)
	}

	return maxSeq
}
