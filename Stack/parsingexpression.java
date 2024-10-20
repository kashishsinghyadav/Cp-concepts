

class Solution {
    public String findval(String op, List<String> arr) {
        if (op.equals("&")) {
            if (arr.contains("f")) {
                return "f";
            } else {
                return "t";
            }
        } else if (op.equals("|")) {
            if (arr.contains("t")) {
                return "t";
            } else {
                return "f";
            }
        } else {
            String val = arr.get(0);
            if (val.equals("t")) {
                return "f";
            } else {
                return "t";
            }
        }
    }

    public boolean parseBoolExpr(String exp) {
        Stack<String> stack = new Stack<>();

        for (int i = 0; i < exp.length(); i++) {
            char c = exp.charAt(i);

            if (c == ',') {
                continue;
            }
            if (c != ')') {
                stack.push(String.valueOf(c));
            }
            if (c == ')') {
                List<String> arr = new ArrayList<>();
                while (!stack.isEmpty() && !stack.peek().equals("(")) {
                    arr.add(stack.pop());
                }
                stack.pop();
                String opr = stack.pop();
                stack.push(findval(opr, arr));
            }
        }

        return stack.peek().equals("t");
    }
}
