class Solution_with_Trie {

    class TrieNode {
        TrieNode[] children = new TrieNode[26];
        boolean isEnd = false;
        int childCount = 0;
    }

    TrieNode root = new TrieNode();

    // Insert word into trie
    private void insert(String word) {

        TrieNode node = root;

        for (char ch : word.toCharArray()) {

            int idx = ch - 'a';

            if (node.children[idx] == null) {
                node.children[idx] = new TrieNode();
                node.childCount++;
            }

            node = node.children[idx];
        }

        node.isEnd = true;
    }

    public String longestCommonPrefix(String[] strs) {

        if (strs == null || strs.length == 0)
            return "";

        // Build Trie
        for (String word : strs) {
            insert(word);
        }

        // Find LCP
        StringBuilder prefix = new StringBuilder();

        TrieNode node = root;

        while (node.childCount == 1 && !node.isEnd) {

            for (int i = 0; i < 26; i++) {

                if (node.children[i] != null) {

                    prefix.append((char) (i + 'a'));
                    node = node.children[i];
                    break;
                }
            }
        }

        return prefix.toString();
    }
}
