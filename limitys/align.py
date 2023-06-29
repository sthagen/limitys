from typing import no_type_check

__all__ = ['Alignment', 'Hirschberg', 'Needleman', 'SegmentAlignment']


@no_type_check
class Alignment(object):
    SCORE_UNIFORM = 1
    SCORE_PROPORTION = 2

    @no_type_check
    def __init__(self):
        self.seq_a = None
        self.seq_b = None
        self.len_a = None
        self.len_b = None
        self.score_null = 5
        self.score_sub = -100
        self.score_del = -3
        self.score_ins = -3
        self.separator = '|'
        self.mode = Alignment.SCORE_UNIFORM

    @no_type_check
    def set_score(self, score_null=None, score_sub=None, score_del=None, score_ins=None):
        if score_null is not None:
            self.score_null = score_null
        if score_sub is not None:
            self.score_sub = score_sub
        if score_del is not None:
            self.score_del = score_del
        if score_ins is not None:
            self.score_ins = score_ins

    @no_type_check
    def match(self, a, b):
        if a == b and self.mode == Alignment.SCORE_UNIFORM:
            return self.score_null
        elif self.mode == Alignment.SCORE_UNIFORM:
            return self.score_sub
        elif a == b:
            return self.score_null * len(a)
        else:
            return self.score_sub * len(a)

    @no_type_check
    def delete(self, a):
        """Deleted elements are on seqa."""
        if self.mode == Alignment.SCORE_UNIFORM:
            return self.score_del
        return self.score_del * len(a)

    @no_type_check
    def insert(self, a):
        """Inserted elements are on seqb."""
        if self.mode == Alignment.SCORE_UNIFORM:
            return self.score_ins
        return self.score_ins * len(a)

    @no_type_check
    def score(self, aligned_seq_a, aligned_seq_b):
        score = 0
        for a, b in zip(aligned_seq_a, aligned_seq_b):
            if a == b:
                score += self.score_null
            else:
                if a == self.separator:
                    score += self.score_ins
                elif b == self.separator:
                    score += self.score_del
                else:
                    score += self.score_sub
        return score

    @no_type_check
    def map_alignment(self, aligned_seq_a, aligned_seq_b):
        map_b2a = []
        idx = 0
        for x, y in zip(aligned_seq_a, aligned_seq_b):
            if x == y:
                map_b2a.append(idx)
                idx += 1
            elif x == self.separator:
                map_b2a.append(idx)
            elif y == self.separator:
                idx += 1
                continue
        return map_b2a


@no_type_check
class Needleman(Alignment):
    @no_type_check
    def __init__(self, *args):
        super(Needleman, self).__init__()
        self.semi_global = False
        self.matrix = None

    @no_type_check
    def init_matrix(self):
        rows = self.len_a + 1
        cols = self.len_b + 1
        self.matrix = [[0] * cols for _ in range(rows)]

    @no_type_check
    def compute_matrix(self):
        seq_a = self.seq_a
        seq_b = self.seq_b
        len_a = self.len_a
        len_b = self.len_b

        if not self.semi_global:
            for i in range(1, len_a + 1):
                self.matrix[i][0] = self.delete(seq_a[i - 1]) + self.matrix[i - 1][0]
            for i in range(1, len_b + 1):
                self.matrix[0][i] = self.insert(seq_b[i - 1]) + self.matrix[0][i - 1]

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                """
                Note that rows = len_a+1, cols = len_b+1
                """

                score_sub = self.matrix[i - 1][j - 1] + self.match(seq_a[i - 1], seq_b[j - 1])
                score_del = self.matrix[i - 1][j] + self.delete(seq_a[i - 1])
                score_ins = self.matrix[i][j - 1] + self.insert(seq_b[j - 1])
                self.matrix[i][j] = max(score_sub, score_del, score_ins)

    @no_type_check
    def backtrack(self):
        aligned_seq_a, aligned_seq_b = [], []
        seq_a, seq_b = self.seq_a, self.seq_b

        if self.semi_global:
            last_col_max, _ = max(enumerate([row[-1] for row in self.matrix]), key=lambda a: a[1])
            last_row_max, _ = max(enumerate([col for col in self.matrix[-1]]), key=lambda a: a[1])

            if self.len_a < self.len_b:
                i, j = self.len_a, last_row_max
                aligned_seq_a = [self.separator] * (self.len_b - last_row_max)
                aligned_seq_b = seq_b[last_row_max:]
            else:
                i, j = last_col_max, self.len_b
                aligned_seq_a = seq_a[last_col_max:]
                aligned_seq_b = [self.separator] * (self.len_a - last_col_max)
        else:
            i, j = self.len_a, self.len_b

        mat = self.matrix

        while i > 0 or j > 0:
            if self.semi_global and (i == 0 or j == 0):
                if i == 0 and j > 0:
                    aligned_seq_a = [self.separator] * j + aligned_seq_a
                    aligned_seq_b = seq_b[:j] + aligned_seq_b
                elif i > 0 and j == 0:
                    aligned_seq_a = seq_a[:i] + aligned_seq_a
                    aligned_seq_b = [self.separator] * i + aligned_seq_b
                break

            if j > 0 and mat[i][j] == mat[i][j - 1] + self.insert(seq_b[j - 1]):
                aligned_seq_a.insert(0, self.separator * len(seq_b[j - 1]))
                aligned_seq_b.insert(0, seq_b[j - 1])
                j -= 1

            elif i > 0 and mat[i][j] == mat[i - 1][j] + self.delete(seq_a[i - 1]):
                aligned_seq_a.insert(0, seq_a[i - 1])
                aligned_seq_b.insert(0, self.separator * len(seq_a[i - 1]))
                i -= 1

            elif i > 0 and j > 0 and mat[i][j] == mat[i - 1][j - 1] + self.match(seq_a[i - 1], seq_b[j - 1]):
                aligned_seq_a.insert(0, seq_a[i - 1])
                aligned_seq_b.insert(0, seq_b[j - 1])
                i -= 1
                j -= 1

            else:
                print(seq_a)
                print(seq_b)
                print(aligned_seq_a)
                print(aligned_seq_b)
                raise Exception('backtrack error', i, j, seq_a[i - 2 : i + 1], seq_b[j - 2 : j + 1])

        return aligned_seq_a, aligned_seq_b

    @no_type_check
    def align(self, seq_a, seq_b, semi_global=True, mode=None):
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.len_a = len(self.seq_a)
        self.len_b = len(self.seq_b)

        self.semi_global = semi_global

        if mode is not None:
            self.mode = mode
        self.init_matrix()
        self.compute_matrix()
        return self.backtrack()


@no_type_check
class Hirschberg(Alignment):
    @no_type_check
    def __init__(self):
        super(Hirschberg, self).__init__()
        self.needleman = Needleman()

    @no_type_check
    def last_row(self, seqa, seqb):
        lena = len(seqa)
        lenb = len(seqb)
        pre_row = [0] * (lenb + 1)
        cur_row = [0] * (lenb + 1)

        for j in range(1, lenb + 1):
            pre_row[j] = pre_row[j - 1] + self.insert(seqb[j - 1])

        for i in range(1, lena + 1):
            cur_row[0] = self.delete(seqa[i - 1]) + pre_row[0]
            for j in range(1, lenb + 1):
                score_sub = pre_row[j - 1] + self.match(seqa[i - 1], seqb[j - 1])
                score_del = pre_row[j] + self.delete(seqa[i - 1])
                score_ins = cur_row[j - 1] + self.insert(seqb[j - 1])
                cur_row[j] = max(score_sub, score_del, score_ins)

            pre_row = cur_row
            cur_row = [0] * (lenb + 1)

        return pre_row

    @no_type_check
    def align_rec(self, seq_a, seq_b):
        aligned_a, aligned_b = [], []
        len_a, len_b = len(seq_a), len(seq_b)

        if len_a == 0:
            for i in range(len_b):
                aligned_a.append(self.separator * len(seq_b[i]))
                aligned_b.append(seq_b[i])
        elif len_b == 0:
            for i in range(len_a):
                aligned_a.append(seq_a[i])
                aligned_b.append(self.separator * len(seq_a[i]))

        elif len(seq_a) == 1:
            aligned_a, aligned_b = self.needleman.align(seq_a, seq_b)

        else:
            mid_a = int(len_a / 2)

            rowleft = self.last_row(seq_a[:mid_a], seq_b)
            rowright = self.last_row(seq_a[mid_a:][::-1], seq_b[::-1])

            rowright.reverse()

            row = [left + right for left, right in zip(rowleft, rowright)]
            maxidx, _ = max(enumerate(row), key=lambda a: a[1])

            mid_b = maxidx

            aligned_a_left, aligned_b_left = self.align_rec(seq_a[:mid_a], seq_b[:mid_b])
            aligned_a_right, aligned_b_right = self.align_rec(seq_a[mid_a:], seq_b[mid_b:])
            aligned_a = aligned_a_left + aligned_a_right
            aligned_b = aligned_b_left + aligned_b_right

        return aligned_a, aligned_b

    @no_type_check
    def align(self, seq_a, seq_b, mode=None):
        self.seq_a = seq_a
        self.seq_b = seq_b
        self.len_a = len(self.seq_a)
        self.len_b = len(self.seq_b)
        if mode is not None:
            self.mode = mode
        return self.align_rec(self.seq_a, self.seq_b)


@no_type_check
class SegmentAlignment(Alignment):
    step = 50

    @no_type_check
    def __init__(self):
        super(SegmentAlignment, self).__init__()

    @no_type_check
    @classmethod
    def skip_same(cls, seq_a, seq_b, curr_a, curr_b, aligned_seq_a, aligned_seq_b):
        while True:
            if seq_a[curr_a] == seq_b[curr_b]:
                aligned_seq_a.append(seq_a[curr_a])
                aligned_seq_b.append(seq_b[curr_b])
                curr_a += 1
                curr_b += 1
            else:
                break

            if curr_a >= len(seq_a) or curr_b >= len(seq_b):
                break

        return curr_a, curr_b

    @no_type_check
    @classmethod
    def align(cls, seq_left, seq_right, segment_half=False, base_alignment='Needleman', semi_global=True):
        if len(seq_left) < len(seq_right):
            seq_a, seq_b = seq_left, seq_right
        else:
            seq_b, seq_a = seq_left, seq_right

        len_a = len(seq_a)
        len_b = len(seq_b)

        diff = cls.step

        curr_a = 0
        curr_b = 0
        is_needleman = False

        if base_alignment == 'Hirschberg':
            aligner = Hirschberg()
        elif base_alignment == 'Needleman':
            aligner = Needleman()
            is_needleman = True
        else:
            aligner = None

        align = aligner.align

        aligned_a = []
        aligned_b = []

        insert_length = 0
        while curr_a < len_a and curr_b < len_b:
            if not (is_needleman and semi_global):
                curr_a, curr_b = cls.skip_same(seq_a, seq_b, curr_a, curr_b, aligned_a, aligned_b)

            sub_seq_a = seq_a[curr_a : curr_a + cls.step]
            sub_seq_b = seq_b[curr_b : curr_b + cls.step + diff]

            if is_needleman:
                aligned_sub_a, aligned_sub_b = align(sub_seq_a, sub_seq_b, semi_global=semi_global)
            else:
                aligned_sub_a, aligned_sub_b = align(sub_seq_a, sub_seq_b)

            if segment_half:
                half_aligned_sub_a = []
                char_len = 0

                for char in aligned_sub_a:
                    half_aligned_sub_a.append(char)
                    if char != '|':
                        char_len += 1
                    if char_len >= cls.step / 2:
                        break

                aligned_sub_a = half_aligned_sub_a
                aligned_sub_b = aligned_sub_b[: len(aligned_sub_a)]

                incre_a = int(cls.step / 2)
                incre_b = sum([1 for char in aligned_sub_b if char != '|'])
                aligned_a += aligned_sub_a
                aligned_b += aligned_sub_b
            else:
                insert_length = 0
                for char in aligned_sub_a[::-1]:
                    if char == '|':
                        insert_length += 1
                    else:
                        break

                incre_a = len(sub_seq_a)
                incre_b = len(sub_seq_b) - insert_length
                aligned_a += aligned_sub_a[: len(aligned_sub_a) - insert_length]
                aligned_b += aligned_sub_b[: len(aligned_sub_b) - insert_length]

            curr_a += incre_a
            curr_b += incre_b

            diff = cls.step

        if curr_b < len_b:
            aligned_a += ['|'] * (len_b - curr_b)
            aligned_b += seq_b[curr_b:]
        else:
            aligned_a += seq_a[curr_a:]
            aligned_b += ['|'] * (len_a - curr_a)
        if len(seq_left) < len(seq_right):
            return aligned_a, aligned_b
        else:
            return aligned_b, aligned_a
