public class Solution {
    
    private static final Map<Character, Integer> compressMap = new HashMap<>();
    
    static {
        compressMap.put('A', 0);
        compressMap.put('C', 2);
        compressMap.put('G', 1);
        compressMap.put('T', 3);
    }
    
    private int compressStr(String s, int start, int end) {
        int x = 0;
        for (int i = start; i < end; i++) {
            x |= compressMap.get(s.charAt(i));
            x <<= 2;
        }
        
        return x;
    }
    
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i <= s.length()-10; i++) {
            int v = compressStr(s, i, i+10);
            int count = 1;
            if (map.containsKey(v)) {
                count += map.get(v);
            }
            if (count == 2) {
                res.add(s.substring(i, i+10));
            }
            map.put(v, count);
        }
        
        return res;
    }
}
