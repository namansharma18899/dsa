class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        def make_mirror(m_root):
            if not m_root:
                return None
            temp = m_root.left
            m_root.left = m_root.right
            m_root.right = temp
            make_mirror(m_root.left)
            make_mirror(m_root.right)
        mr = root
        make_mirror(root)
        return mr
        # Code here