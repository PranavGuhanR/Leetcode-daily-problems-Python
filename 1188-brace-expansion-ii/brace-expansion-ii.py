class Solution:
    def braceExpansionII(self, expression):

        def merge(groups, words):
            current = groups[-1]

            if not current:
                groups[-1] = words
                return

            combined = []

            for a in current:
                for b in words:
                    combined.append(a + b)

            groups[-1] = combined

        def dfs(start, end):
            groups = [[]]
            depth = 0
            left = 0

            for i in range(start, end + 1):

                if expression[i] == '{':
                    depth += 1

                    if depth == 1:
                        left = i + 1

                elif expression[i] == '}':
                    depth -= 1

                    if depth == 0:
                        merge(groups, dfs(left, i - 1))

                elif expression[i] == ',' and depth == 0:
                    groups.append([])

                elif depth == 0:
                    merge(groups, [expression[i]])

            result = set()

            for group in groups:
                for word in group:
                    result.add(word)

            return list(result)

        return sorted(dfs(0, len(expression) - 1))