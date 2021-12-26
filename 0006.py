class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1:
            return s
        elif numRows == 1:
            return s
        else:
            first_offset =  2 + (numRows-2)*2
            prev = 0
            current = first_offset
            chunks = list()
            while current< len(s):
                chunks.append(s[prev:current])
                prev+=first_offset
                current+=first_offset
            if prev<len(s):
                chunks.append(s[prev:])

            lines = list()
            for i in range(numRows):
                lines.append(list())
            for i in range(len(chunks)):
                if numRows-1 < len(chunks[i]):
                    lines[numRows-1].append(chunks[i][numRows-1])
                lines[0].append(chunks[i][0])
                for j in range(1,numRows-1):
                    if j< len(chunks[i]):
                        lines[j].append(chunks[i][j])
                last = numRows-2
                for j in range(numRows, len(chunks[i])):
                    lines[last].append(chunks[i][j])
                    last-=1
            final = ""
            for i in lines:
                final += "".join(i)
            return final