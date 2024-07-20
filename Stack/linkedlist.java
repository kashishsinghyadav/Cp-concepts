class Stack{
 static class Node{

 	int data;
	Node next;
	public Node(int data){
	this.data=data;
	next=null;
}
}

static class St{

public static Node head;
public static Boolean isempty(){
return head==null;
}
public static void push(int data){
	Node newnode=new Node(data);
	if(isempty()){
	head=newnode;
	return;
}
	
	newnode.next=head;
	head=newnode;
	


}
public static int pop(){
	if(isempty()){
	return -1;
	
}
	int pp=head.data;
	head=head.next;
	return pp;

}

public static int peek(){
	if(isempty()){
return -1;
}
return head.data;
}
}


public static void main(String args[]){

St s=new St();
s.push(1);
s.push(2);
s.push(3);
while(!s.isempty()){
System.out.println(s.peek());
s.pop();
}

}
}
