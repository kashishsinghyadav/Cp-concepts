import java.util.ArrayDeque;
import java.util.Queue;

public class Lvl {

    static class Node {
        int data;
        Node left, right;

        public Node(int item) {
            data = item;
            left = right = null;
        }
    }

    static class Tree {

        public static void level(Node root) {
            if (root == null) {
                return;
            }

            Queue<Node> q = new ArrayDeque<>();
            q.add(root);

            while (!q.isEmpty()) {
                Node curr = q.poll();
                System.out.print(curr.data + " ");

                if (curr.left != null) {
                    q.add(curr.left);
                }

                if (curr.right != null) {
                    q.add(curr.right);
                }
            }
        }
    }

    public static void main(String args[]) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        Tree.level(root);
    }
}
