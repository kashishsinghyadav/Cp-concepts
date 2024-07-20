import java.util.ArrayList;

class StackA {
    class Stack {
        ArrayList<Integer> list = new ArrayList<>();

        public boolean isempty() {
            return list.isEmpty();
        }

        public void push(int data) {
            list.add(data);
        }

        public int pop() {
            if (isempty()) {
                throw new RuntimeException("Stack is empty");
            }
            return list.remove(list.size() - 1);
        }

        public int peek() {
            if (isempty()) {
                throw new RuntimeException("Stack is empty");
            }
            return list.get(list.size() - 1);
        }
    }

    public static void main(String[] args) {
        StackA.Stack stack = new StackA().new Stack();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        while (!stack.isempty()) {
            System.out.println(stack.peek());
            stack.pop();
        }
    }
}
