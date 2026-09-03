class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(' ||
                c == '{' ||
                c == '[') {
                    stk.push(c);
            } else {
                if (stk.isEmpty()) {
                    return false;
                }

                char ch = stk.pop();
                if (ch == '{' && c != '}' ||
                    ch == '(' && c != ')' || 
                    ch == '[' && c != ']'){
                        return false;
                }
            }
        }

        return stk.isEmpty();
        
    }
}
