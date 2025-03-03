from inspect import stack


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        folder_name = ''
        for letter in path + '/':
            if letter != '/':
                folder_name += letter
            else:
                if folder_name == '..' and path_stack:
                    path_stack.pop()
                elif folder_name != '..' and folder_name != '' and folder_name != '.':
                    path_stack.append(folder_name)
                folder_name = ''
        while path_stack:
            folder_name = '/' + path_stack.pop() + folder_name
        return folder_name if folder_name != '' else '/'


if __name__ == '__main__':
    print(Solution().simplifyPath(path="/home/"))
