class Solution:
    # split path by '/'
    # skip on '.' and ''
    # pop nonempty stack on '..' 
    # push path on everything else
    def simplifyPath(self, path: str) -> str:
        st = []
        dirs = path.split('/')
        for di in dirs:
            if di == '..' and st:
                st.pop()
            elif di != '.' and di != '' and di != '..':
                st.append(di)
        return '/' + '/'.join(st)