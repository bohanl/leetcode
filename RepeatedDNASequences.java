public class Solution {
    private int compressStr(String s) {
        int x = 0;
        for (char c : s.toCharArray()) {
            switch (c) {
            case 'C': // 10
                x |= 2;
                break;
            case 'G': // 01
                x |= 1;
                break;
            case 'T': // 11
                x |= 3;
                break;
            default: // 'A' 00
                break;
            }
            x <<= 2;
        }
        
        return x;
    }
    
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> res = new HashSet<String>();
        Set<Integer> set = new HashSet<Integer>();
        
        for (int i = 0; i <= s.length()-10; i++) {
            String ss = s.substring(i, i+10);
            int v = compressStr(ss);
            if (set.contains(v)) {
                res.add(ss);
            } else {
                set.add(v);
            }
        }
        
        return new ArrayList<String>(res);
    }
}
